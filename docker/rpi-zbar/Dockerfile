FROM jsurf/rpi-raspbian:latest

RUN ["cross-build-start"]

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
	python-numpy \
	libunicap2-dev \
	libv4l-0 \
	libv4l-dev \
	v4l-utils \
	&& \
  apt-get clean

# defining compilers
ENV CC /usr/bin/clang
ENV CXX /usr/bin/clang++

RUN cd /tmp && \ 
    wget -q -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip && \
    unzip -q opencv.zip && \
    wget -q -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip && \
    unzip -q opencv_contrib.zip && \
    mkdir opencv-3.1.0/build && \
    cd opencv-3.1.0/build && \
    cmake \
        -D CMAKE_BUILD_TYPE=RELEASE \
	-D BUILD_opencv_python2=YES \
	-D BUILD_JPEG=YES \
	-D WITH_WEBP=NO \
        -D WITH_OPENEXR=NO \ 
        -D BUILD_TESTS=NO \
	-D BUILD_PERF_TESTS=NO \
	.. && \
    make VERBOSE=1 && \
    make && \
    make install 

RUN ["cross-build-end"]

CMD ["/bin/bash"]
