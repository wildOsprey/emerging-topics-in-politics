## Use elastic
```shell
kubectl port-forward svc/elasticsearch-master 9200 -n demo
curl -k -u elastic:changeme https://localhost:9200/_cat/indices
```
## Use kibane
```shell
# Get elastic user password:
kubectl get secrets --namespace=demo elasticsearch-master-credentials -ojsonpath='{.data.password}' | base64 -d
# Setup port forward
kubectl port-forward --namespace=demo svc/helm-kibana-default-kibana 5601
```