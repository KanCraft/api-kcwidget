# Server Side kanColleWidget

python

# Set Up

### install tesseract-ocr
https://code.google.com/p/tesseract-ocr/
```
sudo apt-get install tesseract-ocr
```

### install python 2.6.6 :pensive:
```
sudo apt-get install python2.6
```

### OPTIONAL : install pyenv
http://qiita.com/la_luna_azul/items/3f64016feaad1722805c
```
cd ~
git clone git://github.com/yyuu/pyenv.git .pyenv

echo 'export PYENV_ROOT="${HOME}/.pyenv"' >> ~/.bashrc
echo 'if [ -d "${PYENV_ROOT}" ]; then' >> ~/.bashrc
echo '    export PATH=${PYENV_ROOT}/bin:$PATH' >> ~/.bashrc
echo '    eval "$(pyenv init -)"' >> ~/.bashrc
echo 'fi' >> ~/.bashrc

exec $SHELL -l

cd $PYENV_ROOT/plugins
git clone git://github.com/yyuu/pyenv-virtualenv.git
```
### install pip
```
sudo easy_install pip
```
### install pyocr
```
pip install pyocr
```
### install Flask
```
pip install Flask
```
### prepare conf.py
```python
host = 'myhost.com'
port = 9999
```
### Start Server
```
python minimum.py
```
