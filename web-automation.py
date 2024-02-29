from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox('./firefoxdriver')
driver.get("https://www.google.com")
