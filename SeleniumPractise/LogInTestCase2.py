# TestCase2

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_object = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
call_driver = webdriver.Chrome(service=driver_object)

call_driver.get("https://admin-demo.nopcommerce.com/login")

call_driver.implicitly_wait(20)

call_driver.find_element(By.XPATH, '//input[@type="email"]').clear()
call_driver.find_element(By.XPATH, '//input[@type="email"]').send_keys('admin@yourstore.com')
call_driver.find_element(By.XPATH, '//input[@id="Password"]').clear()
call_driver.find_element(By.XPATH, '//input[@id="Password"]').send_keys('admin')
call_driver.find_element(By.XPATH, '//button[@type="submit"]').click()

actual_title = call_driver.title
expected_title = "Dashboard / nopCommerce administration"

if actual_title == expected_title:
    print("LogIn TestCase Passed")
else:
    print("Login TestCase Failed")
