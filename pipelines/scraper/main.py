import click
import requests
import json

import sys; sys.path.append('/app/')
from pipelines.scraper.scraper import Scraper
from storages.elastic import ElasticStorage


@click.command()
@click.option("--tweet-host", required=True, type=str)
@click.option("--elastic-hosts", required=True, type=str)
@click.option("--tags", required=True, type=(str))
@click.option("--count", type=str, default=1)
@click.option("--times", type=str, default=1)
def run(tweet_host: str, elastic_hosts: int, tags: [str], count: int, times: int):
    elastic_storage = ElasticStorage(hosts=elastic_hosts.split(','))

    url = f"http://{tweet_host}/api/v1/post"
    data = {'names': tags.split(","), 'count': count, 'times': times}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    try:
        result = Scraper(r.json()["data"])
    except KeyError:
        print("Non data fild in request")

    elastic_storage.insert_doc_bunks(result.get_data(), 'demo_run')


if __name__ == "__main__":
    run()
