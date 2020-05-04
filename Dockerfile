FROM ubuntu:18.04
RUN apt-get update && apt-get install -y nodejs npm wget unzip python3 bc vim build-essential python3-pip
RUN npm i -g @rmlio/yarrrml-parser
RUN mkdir /code && mkdir /result && mkdir /data && mkdir /input
COPY input /input
COPY code /code
RUN pip3 install -r /code/requirements.txt
CMD ["tail", "-f", "/dev/null"]