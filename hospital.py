# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:31:22 2021

@author: clair
"""
#還不會弄那些顏色標籤，先做個最陽春的
import pandas as pd 
#pd.read_html會企圖解析被<table>包含的表格式資料
#讀取結果會是dataframe物件的list
tables = pd.read_html("https://www.nhi.gov.tw/SysService/SevereAcuteHospital.aspx")[1]  #只要list中的第二個dataframe
tables.to_csv("hospital.csv" , encoding = "utf-8-sig")


