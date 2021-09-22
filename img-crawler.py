import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import random
from datetime import time
import time
from selenium.webdriver.common.by import By
import json
import sys
import base64
#模擬使用者行為
headers = {
        "Accept":"application/json",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        }
url = 'https://www.google.com/search?q=%E8%B2%93%E5%92%AA&rlz=1C5GCEA_enTW944TW944&sxsrf=AOaemvIGU9-5AY7qJchfEraseoT_YQMN0A:1632157844068&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj16ozkhY7zAhVNCN4KHZLAAcAQ_AUoAXoECAIQAw'

driver = webdriver.Chrome('./chromedriver')
driver.set_page_load_timeout(30)
time.sleep(3)
html = driver.get(url)
i=0
dir_name = "google_images"
for page in range(10):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(random.uniform(7.0, 10.0))
    
html = driver.page_source
soup = BeautifulSoup(html,'lxml')
selector = 'img'
poster_src = [i.get("src") for i in soup.select(selector)]
print(len(poster_src))

for li in range(1,len(poster_src)):
    print(poster_src[li])
    try:
        if(poster_src[li].startswith('https')):
            imgRead = requests.get(poster_src[li],headers=headers)
            with open(dir_name+'/'+"catimageToSave"+str(i)+".jpg", "wb") as f1:
                f1.write(imgRead.content)
                f1.close()
                i+=1
                print(i)
        else:
            img_64=base64.urlsafe_b64decode(poster_src[li][23:] + '=' * (4 - len(poster_src[li][23:]) % 4))
            with open(dir_name+'/'+"catimageToSave"+str(i)+".jpg", "wb") as fh:
                fh.write(img_64)
                fh.close()
                i+=1
                print(i)
    except AttributeError:
        print('AE')
    except TypeError:
        print('N')
print()
i+=1
print(i)