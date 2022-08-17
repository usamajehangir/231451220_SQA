from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\Windows\chromedriver.exe")
driver.get("https://www.python.org")
print(driver.title)
driver.close()





