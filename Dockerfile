FROM alpine:3.7
RUN apk update && apk add build-base libzmq musl-dev python3 python3-dev zeromq-dev py-pip
RUN pip install boto3
COPY downloadfileS3.py .
COPY .boto /root/
RUN python downloadfileS3.py



