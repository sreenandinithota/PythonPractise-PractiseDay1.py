
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

callDrivers = Service('C:\\Drivers\\chromedriver-win64\\chromedriver.exe')
drivers = webdriver.Chrome(service=callDrivers)

drivers.get('https://www.flipkart.com/')
drivers.maximize_window()
drivers.implicitly_wait(30)

drivers.find_element(By.CSS_SELECTOR, "a[title=Login]").click()
drivers.find_element(By.CSS_SELECTOR, "input._2IX_2-[type=text]").send_keys('nandusana181@gmail.com')
drivers.find_element(By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()

print("LoginTestPassed")