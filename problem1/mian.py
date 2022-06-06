import csv

from selenium import webdriver
import time
import pandas as pd

browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
browser.get('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="foreignTable"]/div/span').click()
time.sleep(2)
dfs = []
time.sleep(2)
data = browser.page_source
df = pd.read_html(data)[0]

df.to_csv('result.csv', sep=',', header=True, index=True,encoding='utf-8-sig')
print(df)
