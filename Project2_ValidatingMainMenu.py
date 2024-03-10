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
driver.find_element(By.NAME, 'username').send_keys('Admin')
time.sleep(1)

# Find and enter the Password
driver.find_element(By.NAME, 'password').send_keys('admin123')
time.sleep(1)

# Click the Login button
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)

driver.implicitly_wait(10)

if "dashboard/index" in driver.current_url:
    driver.find_element(By.LINK_TEXT, 'Admin').click()
    time.sleep(1)

    menudata = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
    time.sleep(1)

    menulist = driver.find_elements(By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]')

    for e in menulist:
        for a in menudata:
            if e.text == a.title():
               print(e.text)
               time.sleep(1)

# Close the browser
driver.quit()
