import click

import sys; sys.path.append('/app')

from algorithms.topic_modelling import LDATopicModeller
from storages.elastic import ElasticStorage
from utils.cleaning import clean_tweet

LIMIT = 500


@click.command()
@click.option("--elastic-hosts", required=True, type=str)
@click.option("--index", required=True, type=str)
def run(elastic_hosts, index):
    elastic_storage = ElasticStorage(hosts=elastic_hosts.split(','))

    data = elastic_storage.get_all_data(index=index)

    topic_model = LDATopicModeller(num_topics=10, minimum_probability=0.5)
    topic_model.create_topic_model([clean_tweet(item['_source']['text']) for item in data])

    update_actions = []

    for sample in data:
        text = sample['_source']['text']
        topic = topic_model.get_topic_from_model(text)

        if topic:
            update_actions.append(
            (
                sample['_id'],
                {'topic': topic}
            ))

    if update_actions:
        elastic_storage.update_doc_bunks(update_actions, index)


if __name__ == "__main__":
    run()
