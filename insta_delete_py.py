from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

username = 'insta_delete_py'
password = 'delete01'

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" )
# Using Chrome to access web
driver = webdriver.Firefox(profile)
# Open the website
driver.get('https://www.instagram.com/')
time.sleep(2)

# Find login button
login_button = driver.find_element_by_xpath("//button[contains(.,'Log In')]")
# Login
login_button.click()
time.sleep(3)

# Select the id box
uid_box = driver.find_element_by_name('username')

# Select the id box
pwd_box = driver.find_element_by_name('password')

uid_box.send_keys(username)
pwd_box.send_keys(password)

# Find login button
login_button = driver.find_element_by_xpath("//button[contains(.,'Log In')]")
# Login
login_button.click()
time.sleep(7)

#Click not now
not_now = driver.find_element_by_xpath("//button[contains(.,'Not Now')]")
time.sleep(1)
not_now.click()
time.sleep(1)

# Click Profile
driver.get('https://www.instagram.com/' + username + '/')
time.sleep(2)

photos = driver.find_element_by_xpath('.//a[contains(text(),"/p/")]')
print(photos)