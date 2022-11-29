## Use
```shell
docker build -t screper:1 .
docker run -it --rm --net host screper:1 --host 172.25.0.97 --port 8000 --tags ilon,ua,Ukraine --count 1 --times 3
```