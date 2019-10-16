from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

firefox = webdriver.Firefox()

firefox.get("http://automationpractice.com/index.php") # go to home page
firefox.find_element_by_css_selector(".login").click() # click on login

firefox.find_element_by_css_selector("#email").send_keys("email@address.org")
firefox.find_element_by_id("passwd").send_keys("password")