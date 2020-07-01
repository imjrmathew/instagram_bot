from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Specify your driver location
chrome_path = r"CHROME DRIVER PATH" 
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.instagram.com/")
time.sleep(2)
# Enter Your credentials
uname = "your username"
passwd = "your password"
usernamefield = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
usernamefield.clear()
usernamefield.send_keys(uname)
passwordfield = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
passwordfield.clear()
passwordfield.send_keys(passwd)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
time.sleep(3)
if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section'):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)
if driver.find_element_by_xpath('/html/body/div[4]/div'):
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
time.sleep(3)

for i in range(1,11):
    for j in range(1,4):
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/div[{0}]/div[{1}]'.format(i,j)).click()
        time.sleep(4)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
        time.sleep(4)
        if driver.find_element_by_xpath('/html/body/div[5]/div'):
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
        else:
            driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a').click()
time.sleep(2)
driver.close()
