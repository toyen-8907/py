# ch7_12.py
from selenium import webdriver
import time

url = 'https://data.epa.gov.tw/dataset/aqx_p_432/resource/8ff027dc-2da2-42e8-85de-78ac3faf470e'

driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
browser.get(url)                    # 網頁下載至瀏覽器

browser.find_element_by_link_text('JSON').click()      # 按JSON鈕
time.sleep(3)

browser.find_element_by_link_text('CSV').click()        # 按CSV鈕
time.sleep(3)

browser.find_element_by_link_text('XML').click()        # 按XML鈕
time.sleep(3)


















