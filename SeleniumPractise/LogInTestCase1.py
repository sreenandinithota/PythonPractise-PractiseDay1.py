
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_vobj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_vobj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window() # For maximizing window
driver.implicitly_wait(20)

driver.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')
# driver.implicitly_wait(60)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys('admin123')
# driver.implicitly_wait(60)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# driver.implicitly_wait(60)

act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
 print("LoginTestPassed")
else:
 print("LoginTestFailed")
driver.close()

