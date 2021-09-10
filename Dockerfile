FROM alpine:3.10

MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

LABEL name="karmab/contrail-allow-vips" \
      maintainer="karimboumedhel@gmail.com" \
      vendor="Karmalabs" \
      version="latest" \
      release="0" \
      summary="Node labeller based on rules" \
      description="Node labeller based on rules stored in a config map"

RUN apk add python3 python3-dev
RUN pip3 install requests
ADD contrail-allow-vips.py /

CMD [ "python3", "-u", "/contrail-allow-vips.py" ]
