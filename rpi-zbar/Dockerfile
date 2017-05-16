FROM resin/rpi-raspbian:latest

RUN apt-get update && \
    apt-get install -y \
    	wget \
	unzip \
	cmake \
	build-essential \
	pkg-config \
	clang \
	libjpeg-dev \
	libtiff5-dev \
	libjasper-dev \
	libpng12-dev \
	libavcodec-dev \
	libavformat-dev \
    libxvidcore-dev \
    libx264-dev \
    libgtk2.0-dev \
    libatlas-base-dev \
    gfortran \
	libeigen3-dev \
	python3-dev \
	libpython3-dev \
	libunicap2-dev \
	libv4l-0 \
	libv4l-dev \
	v4l-utils \
	python3-pip \
	python3-picamera \
	&& \
  apt-get clean

RUN pip3 install numpy

RUN cd /tmp && \ 
    wget -q -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip && \
    unzip -q opencv.zip && \
    wget -q -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip && \
    unzip -q opencv_contrib.zip

ADD run-make.sh /tmp
RUN chmod +x /tmp/run-make.sh
RUN #!/tmp/run-make.sh
    
RUN pip3 install zbar-py Image

CMD ["/bin/bash"]
