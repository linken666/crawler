# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:46:56 2021

@author: clair
"""

#會有漏部分標題的問題

import time , re 
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
rows = []
driver = webdriver.Chrome("C:/Users/clair/Downloads/chromedriver_win32/chromedriver")  #記得改成driver裝的地址
driver.implicitly_wait(3)  #開啟瀏覽器等三秒讓網頁載入
driver.get('https://www.dcard.tw/f/cpu?latest=true')
for i in range(3):  #要執行幾次
    soup = BeautifulSoup(driver.page_source , 'html.parser')
    for title in soup.select("h2"):
        print (title.text.strip())
        rows.append(title.text.strip())  #把抓到的標題寫到row裡
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") #讓driver執行括號內指令，相當於自己在開發者工具輸入這段字，此指令為滾到網頁最下層
    time.sleep(10)  #停幾秒讓讓訊息跑好
driver.close()
data = {'標題' : rows}
df = pd.DataFrame(data)
df.to_csv( 'decardoutput.csv' , encoding = 'utf-8-sig')
