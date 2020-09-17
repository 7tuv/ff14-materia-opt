FROM ubuntu:latest

# cmakeインストール時にタイムゾーンを聞いてきて自動インストールが止まるので、その対策
ENV DEBIAN_FRONTEND=noninteractive

# scipoptsuite-6.0.2.tgzをコピー
COPY scipoptsuite-6.0.2.tgz /var/tmp/scipoptsuite-6.0.2.tgz

# パッケージのインストール
RUN apt-get update && apt-get install -y \
	cmake \
	build-essential \
	zlib1g-dev \
	libgmp3-dev \
	python3-dev \
	python3-pip

# build SCIP
RUN cd /var/tmp && \
	tar xzf scipoptsuite-6.0.2.tgz && \
	cd scipoptsuite-6.0.2 && \
	mkdir build && \
	cd build && \
	cmake .. && \
	make && \
	make install path='/usr/local'

# export SCIPOPTDIR='/usr/local'
ENV SCIPOPTDIR /usr/local

# install pip modules
RUN pip3 install cython pyscipopt==2.2.3
