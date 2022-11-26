from fastapi import FastAPI
from pydantic import BaseModel
import json
import twitter

app = FastAPI()
api = twitter.tweets("key.ini")


class Tags(BaseModel):
    names: list
    count: int
    times: int


@app.get("/health")
def health():
    return {"message": 200}


@app.get("/api/v1/get")
async def get_item():
    if api.raw:
        return {"data": api.raw[0].text}
    else:
        return {"message": "empty list"}


@app.post("/api/v1/post")
async def items(tags: Tags):
    return {"data": api.search(hashtags=tags.names, count=tags.count, items=tags.times)}
