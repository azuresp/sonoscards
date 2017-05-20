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

RUN mkdir /tmp/opencv-3.1.0/build && \
    cd /tmp/opencv-3.1.0/build && \
    cmake \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=/tmp/opencv_contrib-3.1.0/modules \
    -D BUILD_EXAMPLES=ON ..

RUN cd /tmp/opencv-3.1.0/build && \
    make && \
    make install && \
    ldconfig

RUN pip3 install zbar-py Image

CMD ["/bin/bash"]
