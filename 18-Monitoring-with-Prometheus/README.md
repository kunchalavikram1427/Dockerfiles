https://docs.docker.com/config/daemon/prometheus/
https://github.com/docker/awesome-compose/tree/master/prometheus-
https://opensource.com/article/19/11/introduction-monitoring-prometheus


cat /etc/docker/daemon.json

{
  "metrics-addr": "0.0.0.0:9323"
}



docker run --name my-prometheus \
    --mount type=bind,source=/tmp/prometheus.yml,destination=/etc/prometheus/prometheus.yml \
    -p 9090:9090 \
    prom/prometheus