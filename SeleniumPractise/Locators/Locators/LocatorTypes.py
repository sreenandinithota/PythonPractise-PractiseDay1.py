from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
drivers = webdriver.Chrome(service=serv_obj)

drivers.get("https://www.flipkart.com/")
drivers.maximize_window()
drivers.implicitly_wait(20)

# drivers.find_element(By.NAME, "q").send_keys("Laptop")
links = drivers.find_elements(By.TAG_NAME, "a")
print(len(links))

sliders = drivers.find_elements(By.CLASS_NAME, '_8S67Ib')
print(len(sliders))