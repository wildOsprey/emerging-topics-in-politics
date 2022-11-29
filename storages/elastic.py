import warnings

import elasticsearch
from elasticsearch.helpers import streaming_bulk, reindex

from logging import getLogger
from storages.queries import DEFAULT_QUERY

DEFAULT_ITERATION_SIZE = 500
logger = getLogger()


class ElasticStorage:
    def __init__(self, hosts):
        if not hosts:
            raise ConnectionError(
                f'Hosts: {hosts} are not passed. Unable to create connection for elastic.'
            )

        self.hosts = hosts
        self.es_connection = elasticsearch.Elasticsearch(
            hosts=hosts,
            retry_on_timeout=True,
            timeout=240,
            verify_certs=False
        )

    def reconnect(self):
        self.es_connection = elasticsearch.Elasticsearch(
            hosts=self.hosts,
            retry_on_timeout=True,
            timeout=240
        )

    def is_exist(self, index):
        return self.es_connection.indices.exists(index=index)

    def get_indicies(self, pattern='*'):
        return self.es_connection.indices.get_alias(pattern).keys()

    def get_count(self, index, query=DEFAULT_QUERY):
        count_request = self.es_connection.count(
            index=index,
            body=query
            )
        return int(count_request['count'])

    def get_all_data(self, index:str, query=DEFAULT_QUERY, source_includes=['*'], return_source=True):
        if not self.is_exist(index):
            warnings.warn(f'{index} does not exists')
            return []

        count = self.get_count(index=index, query=query)

        n_iterations = int(count // DEFAULT_ITERATION_SIZE) if count != DEFAULT_ITERATION_SIZE else 0

        args = {
            "body": query,
            "index": index,
            "_source_includes": source_includes,
            "size": DEFAULT_ITERATION_SIZE,
        }

        if n_iterations > 0:
            args['scroll'] = '120s'

        data = self.es_connection.search(**args)

        scroll = data['_scroll_id'] if '_scroll_id' in data else None

        data = data['hits']['hits']

        for _ in range(n_iterations):
            res = self.es_connection.scroll(scroll_id=scroll, scroll='20s')
            scroll = res['_scroll_id']
            data += res['hits']['hits']

        if not return_source:
            return [d['_source'] for d in data]

        return data

    def insert_doc_bunks(self, data, index:str):
        insert_actions = [
            self._get_insert_action(index, sample) for sample in data
            ]

        self.bulk(insert_actions)

    def update_doc_bunks(self, data, index:str):
        update_actions = [
            self._get_update_action(index, elastic_id, sample) for elastic_id, sample in data
            ]

        self.bulk(update_actions)

    def bulk(self, actions):
        try:
            for ok, item in streaming_bulk(
                                    client=self.es_connection,
                                    actions=actions,
                                    chunk_size=100,
                                    max_retries=10,
                                    initial_backoff=5,
                                    raise_on_exception=False
                                ):
                if not ok:
                    warnings.warn(
                        f'Item from bulk coud not be processed: {item}'
                    )

        except Exception as e:
            warnings.warn(f'Error erased in bulk : {str(e)}')

    def get_limited_data(self, index, limit, query=DEFAULT_QUERY, last_item_id=None, return_source=True):
        query['size'] = limit
        query['sort'] = [
            {"id.keyword": "asc", "ignore_unmapped" : True}
        ]

        if last_item_id:
            query["search_after"] = [last_item_id]

        data = self.es_connection.search(
                    index=index,
                    body=query
                )

        data = data['hits']['hits']

        if not data:
            return None, None

        last_item_id = data[-1]['_source']['id']

        if not return_source:
            return (last_item_id, [d['_source'] for d in data])

        return (last_item_id, data)

    def _get_insert_action(self, index, sample):
        return {"_index": index, **sample}

    def _get_update_action(self, index, elastic_id, doc):
        return {
            "_id": elastic_id,
            "_index": index,
            "doc": doc,
            "_op_type": "update",
        }
