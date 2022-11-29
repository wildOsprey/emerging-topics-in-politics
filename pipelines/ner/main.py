import click

import sys; sys.path.append('/app/')

from algorithms.ner import NERExtractor
from storages.elastic import ElasticStorage


LIMIT = 500


@click.command()
@click.option("--elastic-hosts", required=True, type=str)
@click.option("--index", required=True, type=str)
def run(elastic_hosts, index):
    ner_predictor = NERExtractor()

    elastic_storage = ElasticStorage(hosts=elastic_hosts.split(','))

    data = elastic_storage.get_all_data(index=index)

    update_actions = []

    for sample in data:
        text = sample['_source']['text']
        NER = ner_predictor.extract_ner_words(text)

        update_actions.append(
        (
            sample['_id'],
            {'enteties': NER}
        ))

    elastic_storage.update_doc_bunks(update_actions, index)


if __name__ == "__main__":
    run()
