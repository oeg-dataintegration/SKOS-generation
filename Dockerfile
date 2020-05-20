FROM alpine
RUN apk add nodejs npm python3 py3-pip
RUN npm i -g @rmlio/yarrrml-parser
RUN mkdir /code && mkdir /result && mkdir /data && mkdir /input
COPY code /code
RUN pip3 install -r /code/requirements.txt
CMD ["tail", "-f", "/dev/null"]
