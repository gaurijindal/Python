from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from login import LoginPage
import time

#chrome_driver_path = "C:\development\chromedriver.exe"  # Ensure double backslashes
# service=Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)'

driver = webdriver.Chrome()


# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager().install())

# chrome_driver_path="C:\development\chromedriver.exe"
#
# driver=webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

login_page = LoginPage(driver)
login_page.enter_username("rahulshettyacademy")
login_page.enter_password("learning")
login_page.click_login()
time.sleep(8)
