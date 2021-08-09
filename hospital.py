# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:31:22 2021

@author: clair
"""

import pandas as pd 

tables = pd.read_html("https://www.nhi.gov.tw/SysService/SevereAcuteHospital.aspx")[1]
tables.to_csv("hospital.csv" , encoding = "utf-8-sig")


