import requests
import json
import click
from cleaner import Clean


@click.command()
@click.option("--host", required=True, type=str)
@click.option("--port", required=True, type=int)
@click.option("--tags", required=True, type=(str))
@click.option("--count", type=str, default=1)
@click.option("--times", type=str, default=1)
def make(host: str, port: int, tags: [str], count: int, times: int):
    url = f"http://{host}:{port}/api/v1/post"
    data = {'names': tags.split(","), 'count': count, 'times': times}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    try:
        result = Clean(r.json()["data"])
        print("ok")
    except KeyError:
        print("Non data fild in request")
    print(result.get_data(json_format=True))


if __name__ == "__main__":
    make()
