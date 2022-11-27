## Use
```shell
docker build -t twapi:1 
docker run -it -p 8000:8000 --env-file .env --rm twapi:1
```
## Api Dock
### [api-doc](http://127.0.0.1:8000/dock)

## Test
```shell
# Post
curl -X 'POST' \
  'http://localhost:8000/api/v1/post' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "names": [
    "UA"
  ],
  "count": 1,
  "times": 1
}'

# Get
curl -X 'GET' \
  'http://localhost:8000/api/v1/get' \
  -H 'accept: application/json'
```