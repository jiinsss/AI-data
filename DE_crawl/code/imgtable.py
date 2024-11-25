from transimg import convertToBinaryData
from testsql import insert_data1,insert_data2,create_connection


import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import ssl
import time

ssl._create_default_https_context=ssl._create_unverified_context
from selenium.webdriver.support.ui import WebDriverWait

import urllib.request
from urllib.request import Request,urlopen



img_blob_list=[]
#이미지 파일 넣을 폴더 
import os
img_folder_path='.//imgs'
if not os.path.isdir(img_folder_path):
    os.mkdir(img_folder_path)


#실행경로
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-ssl-errors=yes")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chrome_options)


url = ""
driver.get(url)

src_list=[]
title=[]
imgs=driver.find_elements(By.CLASS_NAME,'TjRVLb')
#imgs=driver.find_elements(By.CSS_SELECTOR,'img')
driver.implicitly_wait(20)
src_index=0
for img in imgs:
    src_index+=1
    driver.implicitly_wait(20)
    src_list.append(img.get_attribute('src'))
    driver.implicitly_wait(10)
    title.append(img.get_attribute('alt'))

print(src_list)
print(title)
#이미지 다운
for index,image_url in enumerate(src_list):
    savename=f'{img_folder_path}/{index}.jpg'
    #https://www.useragentstring.com/
    usragent=''
    request_site=Request(image_url,headers={"User-Agent":usragent})
    mem=urlopen(request_site).read()
    with open(savename, mode='wb') as f:
        f.write(mem)
#blob 저장
for indx in range(len(src_list)):
    img_blob_list.append(convertToBinaryData(f'.//imgs//{indx}.jpg'))
    driver.implicitly_wait(120)

#insert
insert_data1(title[i],img_blob_list[i])