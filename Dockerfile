FROM golang:1.8

MAINTAINER otiai10 <otiai10@gmail.com>

RUN apt-get -qq update

# For OCR
RUN apt-get install -y \
  libleptonica-dev \
  libtesseract-dev \
  tesseract-ocr

# For AVCodec
RUN apt-get install -y \
  libav-tools

ADD . $GOPATH/src/github.com/otiai10/api-kcwidget
WORKDIR $GOPATH/src/github.com/otiai10/api-kcwidget
RUN go get ./...

CMD api-kcwidget
