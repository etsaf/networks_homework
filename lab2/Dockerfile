FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3 iputils-ping

WORKDIR /find_mtu

COPY find_mtu.py ./

ENTRYPOINT ["python3", "./find_mtu.py"]