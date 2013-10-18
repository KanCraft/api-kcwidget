# Server Side kanColleWidget

python

# Set Up
https://gist.github.com/otiai10/6619523
```sh
#
# usage:
#    sh setup_server.sh
#

## START

# cat /etc/debian_version
#=> 6.0.7
# apt-cache search tesseract-ocr
#=> tesseract-ocr - Command line OCR tool
sudo apt-get update
sudo apt-get install -y tesseract-ocr
sudo apt-get install -y gcc
sudo apt-get install -y python-dev
sudo apt-get install -y python-imaging
sudo apt-get install -y git


# python --version
#=> Python 2.6.6
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python
sudo /usr/local/bin/easy_install pip
# pip search Flask
#=> Flask - A microframework based on Werkzeug, Jinja2 and good intentions 0.10.0
sudo pip install Flask
sudo pip install pyocr

rm -f .ssh/config
echo "Host *" >> .ssh/config
echo "        StrictHostKeyChecking no" >> .ssh/config

rm -rf ocrServer
git clone git@github.com:otiai10/ocrServer.git
cd ocrServer
echo "host = 'kcwidgetocrserver001'" >> conf.py
echo "port = 5000" >> conf.py
# sh cli/app.sh start debug
sh cli/app.sh start

## END
```
# Run Test
```sh
python ./tdriver.py
```
or test spefic base64
```sh
python ./tdriver.py --file ./sample/b64sample001.txt
```
