from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path="C:\Windows\System32\chromedriver.exe")
driver.get("https://accounts.tokopedia.com/register")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='google-button']/span").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys("vkook.noona957@gmail.com")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys('T@ekook199597')
time.sleep(3)
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/span").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='new_pass']").send_keys("T@ekook199597")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='confirm_pass']").send_keys("T@ekook199597")
time.sleep(3)

#tanggal lahir
tgl_lhr=driver.find_element_by_xpath("//*[@id='form-create']/div[5]/div/select[1]")
drp=Select(tgl_lhr)
drp.select_by_visible_text("30")
time.sleep(3)

#bulan lahir
bln_lhr=driver.find_element_by_xpath("//*[@id='form-create']/div[5]/div/select[2]")
drp=Select(bln_lhr)
drp.select_by_visible_text("Desember")
time.sleep(3)

#tahun lahir
thn_lhr=driver.find_element_by_xpath("//*[@id='form-create']/div[5]/div/select[3]")
drp=Select(bln_lhr)
drp.select_by_visible_text("1995")
time.sleep(3)

driver.find_element_by_xpath("//*[@id='msisdn']").send_keys("08156522247")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='form-create']/div[7]/label/input").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='form-create']/div[8]/div/button").click()
