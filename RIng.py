import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import urllib3

class AddCart(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def test_AddCart(self):
        try:
            driver_chrome = webdriver.Chrome(r'C:\Users\raon\Desktop\NaraStudies\Python\chromedriver_win32\chromedriver.exe')
            self.driver = driver_chrome
            driver_chrome.maximize_window()
            driver_chrome.get('https://www.saucedemo.com/')
            print(driver_chrome.title)
            driver_chrome.find_element_by_id('user-name').send_keys('standard_user')
            driver_chrome.find_element_by_xpath("//*[@id='password']").send_keys('secret_sauce')
            driver_chrome.find_element_by_id('login-button').click()
            time.sleep(5)
            page2 = driver_chrome.find_element_by_xpath('//*[@id="header_container"]/div[2]/span')
            print(page2.text)
            high = Select(driver_chrome.find_element_by_xpath('//*[@id="header_container"]/div[2]/div[2]/span/select'))
            high.select_by_visible_text('Price (low to high)')
            driver_chrome.find_element_by_id("add-to-cart-sauce-labs-onesie").click()
            time.sleep(5)
            low = Select(driver_chrome.find_element_by_xpath('//*[@id="header_container"]/div[2]/div[2]/span/select'))
            low.select_by_visible_text('Price (high to low)')
            driver_chrome.find_element_by_id('add-to-cart-sauce-labs-fleece-jacket').click()
            time.sleep(5)
            driver_chrome.find_element_by_xpath('//*[@id="shopping_cart_container"]/a').click()
            page3 = driver_chrome.find_element_by_xpath('//*[@id="header_container"]/div[2]/span')
            print(page3.text)
        except:
            raise('Saucelabs pages are incorrectly opened')

    def tearDown(self):
        # Close the browser.
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
