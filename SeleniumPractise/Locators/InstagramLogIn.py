from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_driver = Service('C:\\Drivers\\chromedriver-win64\\chromedriver.exe')
callDriver = webdriver.Chrome(service=serv_driver)

callDriver.get('https://www.instagram.com/')
callDriver.maximize_window()
callDriver.implicitly_wait(60)

# callDriver.find_element(By.NAME, "username").send_keys('nandu__sana')

# CSS LOCATOR
# callDriver.find_element(By.CSS_SELECTOR, "input._aa4b._add6._ac4d._ap35").send_keys('nandu__sana') --> Tag class
# callDriver.find_element(By.CSS_SELECTOR, "input[type=text]").send_keys('nandu__sana') --> Tag attribute
# callDriver.find_element(By.CSS_SELECTOR, "input._aa4b._add6._ac4d._ap35[type=text]").send_keys('nandu__sana') --> Tag class $ attribute

# callDriver.find_element(By.NAME, "password").send_keys('deepunandu181')
# callDriver.find_element(By.XPATH, "//button[@type='submit']").click()
# print("TestCasePassed")