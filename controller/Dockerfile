FROM resin/rpi-raspbian:latest
RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y python3-dev && \
apt-get clean

RUN apt-get install python3-pip

RUN pip3 install flask
RUN pip3 install soco

ADD *.py /
CMD ["python3", "./web.py"]