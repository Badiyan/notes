How to install chromedriver (Linux)

```
apt-get update &&  apt-get upgrade -y 
apt install -y unzip python3-pip chromium-browser chromium-chromedriver libglib2.0-0 libnss3 libgconf-2-4  libfontconfig1
pip3 install -U selenium
wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip
unzip chromedriver_linux64.zip 
mv chromedriver /usr/bin/
chmod +x /usr/bin/chromedriver
```
### Testing: 

```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
#options.add_argument('--disable-gpu')  # applicable to windows os only
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/bin/chromedriver')
```


