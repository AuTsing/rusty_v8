FROM rustembedded/cross:aarch64-linux-android

RUN apt update && apt install -y python3 libglib2.0-dev
