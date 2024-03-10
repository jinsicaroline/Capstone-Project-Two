from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize ChromeDriver
driver = webdriver.Chrome()

# maximizing the Chrome window
driver.maximize_window()


# Navigate to the OrangeHRM login page
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(1)

# Find and enter the Username
driver.find_element(By.XPATH, "//div[@class='orangehrm-login-forgot']").click()
time.sleep(1)

driver.find_element(By.NAME, 'username').send_keys('Jack')
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(4)


# Close the browser
driver.quit()
