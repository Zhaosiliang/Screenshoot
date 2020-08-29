import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import shutil


def del_file(filepath):
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

img='img15'
num = 54
#需要先在cmd中输入chrome.exe --remote-debugging-port=9222 --user-data-dir="F:\selenum\AutomationProfile"
#user-data-dir为单独的浏览器配置文件目录，以免污染正常浏览器的配置文件
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
print(driver.title)
if os.path.exists(img+'/pic1.png'):
    del_file(img+'/')


for i in range(1, num, 1):
    # driver.find_element_by_css_selector(
    #     "#app > div > div.container > div.conleft > div.section.examHead > div > div.toolBar > div.moulde_p > ul > li:nth-child(2)").click()
    elejiexi = driver.find_element_by_css_selector("#exambt > div.answerAnaly > div > dl:nth-child(3) > dd")
    if elejiexi.text=='无':
        eleimg = driver.find_element_by_id('exam')
    else:
        eleimg = driver.find_element_by_id('exambt')
    images_name = img+'\pic' + str(i) + '.png'
    eleimg.screenshot(images_name)
    # driver.find_element_by_css_selector(
    #     '# app > div > div.container > div.conleft > div.section.examHead > div > div.toolBar > div.moulde_p > ul > li:nth-child(1)').click()
    # driver.find_element_by_id("radio_moveNextDiv").click()
    driver.find_element_by_id("checkbox_moveNextDiv").click()
    # cssSelector("div.ant-menu-submenu-title>span>span")
    time.sleep(0.5)
