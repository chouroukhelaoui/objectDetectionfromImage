FROM python:3.8

WORKDIR /input

COPY . /input/

RUN pip install --upgrade pip && \
    pip install requests && \
    python -m pip install requests && \
    pip install matplotlib && \
    pip install opencv-python && \
    mkdir /output
RUN chmod +x script.sh
CMD /bin/bash
RUN apt update && apt install -yq ffmpeg