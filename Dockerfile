FROM alpine:3.19.1

RUN apk update \
    && apk upgrade \
    && apk add python3 \
    && apk add py3-setuptools-pyc\
    && apk add py3-pip-pyc\
    && apk add py3-parsing\
    && apk add py3-parsing-pyc\
    && apk add py3-packaging-pyc\
    && apk add py3-packaging\
    && apk add py3-setuptools\
    && apk add py3-pip

RUN ln -sf python3 /usr/bin/python

RUN apk add tesseract-ocr tesseract-ocr-data-eng

COPY . /myapp
COPY ccu.traineddata /usr/share/tessdata
WORKDIR /myapp
RUN pip3 install --break-system-packages -r requirements.txt

CMD ["python", "main.py"]
