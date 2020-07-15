FROM python:alpine

RUN pip3 install pytest \
                 requests \
                 pytest-html

RUN mkdir -p /pyimgur
ADD . /pyimgur
WORKDIR /pyimgur

RUN chmod +x /pyimgur/run.sh
ENTRYPOINT ["sh","/pyimgur/run.sh"]
