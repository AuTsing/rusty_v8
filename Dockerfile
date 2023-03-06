FROM rustembedded/cross:aarch64-linux-android

RUN apt update && \
	apt install -y python3 libglib2.0-dev xz-utils

RUN mv /usr/bin/python /usr/bin/python2 && \
	ln -s /usr/bin/python3 /usr/bin/python
