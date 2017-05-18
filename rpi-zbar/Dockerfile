FROM resin/rpi-raspbian:latest

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y \
  wget unzip \
  build-essential cmake pkg-config \
  libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev \
  libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
  libxvidcore-dev libx264-dev \
  libgtk2.0-dev \
  libatlas-base-dev gfortran \
  python2.7-dev python3-dev \
  python3-pip \
  python3-picamera

RUN apt-get clean

RUN pip3 install numpy

RUN cd /tmp && \ 
    wget -q -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip && \
    unzip -q opencv.zip && \
    wget -q -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip && \
    unzip -q opencv_contrib.zip

ADD *.sh /tmp/
RUN chmod +x /tmp/*.sh
RUN /tmp/run-cmake.sh
RUN /tmp/run-make.sh
    
RUN pip3 install zbar-py Image

CMD ["/bin/bash"]
