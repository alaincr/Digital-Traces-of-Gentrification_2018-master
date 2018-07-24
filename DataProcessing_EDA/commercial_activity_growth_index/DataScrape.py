import pandas as pd
import numpy as np
import time
import json
from selenium import webdriver
import urllib.request
import os
import geopandas as gpd

browser = webdriver.Chrome("/usr/local/bin/chromedriver")
url = "https://rliapp.mastercardadvisors.com/login/?next=https%3A//rliapp.mastercardadvisors.com/"
browser.get(url) 

username = browser.find_element_by_id("id_username")
password = browser.find_element_by_id("id_password")

username.send_keys("email)
password.send_keys("password")

browser.find_element_by_xpath("//button[@type='submit']").click()

urllib.request.urlretrieve('https://data.cityofnewyork.us/download/i8iw-xf4u/application%2Fzip', "file.gz")
os.system("mv " + "file.gz " + os.getenv("PUIDATA"))
os.system("unzip " + os.getenv("PUIDATA") + "/file.gz -d " + os.getenv("PUIDATA") + "/zipcode")
nyc = gpd.read_file(os.getenv("PUIDATA") + "/zipcode" + "/ZIP_CODE_040114.shp")
nyc.drop(['BLDGZIP', 'PO_NAME', 'STATE', 'COUNTY', 'ST_FIPS', 'CTY_FIPS', 'URL', 'SHAPE_AREA', 'SHAPE_LEN'], axis=1, inplace=True)
ziplist = nyc['ZIPCODE'].values.tolist()

#Growth Score – Ranking of sales revenue growth rate year over year, updated monthly
# 2018.01
value_dict = {}
unsuccessful = []
for i,zipcode in enumerate (ziplist):
    my_url = 'https://rliapp.mastercardadvisors.com/map/2018/01/11/40.7062/-73.9831?' +         'to_placeid=ChIJOwg_06VPwokRYv534QaPC8g' +         '&id=usz' + zipcode + '&metric=growth'

    browser.get(my_url)
    time.sleep(6)
    ranking = browser.find_element_by_id('lt-details-score')
    result = ranking.text
    value_dict[zipcode] = result
    print("{}--{}:{}".format(i,zipcode,result))
    if len(result)==0:
        unsuccessful.append(zipcode)
    randtime = np.random.random(270) + np.random.randint(2,8,270)
    time.sleep(randtime[i])


df = pd.DataFrame.from_dict(value_dict, orient='index')
df.reset_index(inplace=True)
df.columns = ['zipcode', 'growth201801']
df.to_csv('growth201801')
