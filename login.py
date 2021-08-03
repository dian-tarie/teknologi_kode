from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Windows\System32\chromedriver.exe")
driver.get("https://accounts.tokopedia.com/login")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='google-button']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys("vkook.noona957@gmail.com")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='login-step-one-form']/button").click()
