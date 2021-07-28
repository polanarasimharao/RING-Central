from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(r'C:\Users\raon\Desktop\NaraStudies\Python\chromedriver_win32\chromedriver.exe')
driver.get('https://www.saucedemo.com/')
print(driver.title)
driver.maximize_window()
driver.find_element_by_id('user-name').send_keys('standard_user')
time.sleep(5)
driver.find_element_by_xpath("//*[@id='password']").send_keys('secret_sauce')
time.sleep(5)
driver.find_element_by_id('login-button').click()
time.sleep(5)
page2=driver.find_element_by_xpath('//*[@id="header_container"]/div[2]/span')
print(page2.text)
high = Select(driver.find_element_by_xpath('//*[@id="header_container"]/div[2]/div[2]/span/select'))
high.select_by_visible_text('Price (low to high)')
time.sleep(5)
driver.find_element_by_id("add-to-cart-sauce-labs-onesie").click()
time.sleep(5)
low = Select(driver.find_element_by_xpath('//*[@id="header_container"]/div[2]/div[2]/span/select'))
low.select_by_visible_text('Price (high to low)')
time.sleep(5)
driver.find_element_by_id('add-to-cart-sauce-labs-fleece-jacket').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="shopping_cart_container"]/a').click()
time.sleep(5)
page3=driver.find_element_by_xpath('//*[@id="header_container"]/div[2]/span')
print(page3.text)
driver.close()



