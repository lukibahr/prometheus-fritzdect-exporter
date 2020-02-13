FROM hypriot/rpi-alpine:3.6

RUN apk add --no-cache python3 gcc python3-dev libc-dev

WORKDIR "/exporter"
ADD src .
RUN pip3 install prometheus_client==0.7.1 fritzconnection==1.2.1

ENTRYPOINT ["python3", "exporter.py"]