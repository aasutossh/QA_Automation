from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

firefox = webdriver.Firefox()

firefox.get("http://automationpractice.com/index.php") # go to home page
firefox.find_element_by_css_selector(".login").click() # click on login
firefox.find_element_by_css_selector("#email_create").send_keys("email@address.org") # enter email address
firefox.find_element_by_css_selector("#SubmitCreate").click() # click on submit button
sleep(3)
firefox.find_element_by_css_selector("#uniform-id_gender1").click() # select Mr.
firefox.find_element_by_css_selector("#customer_firstname").send_keys("Aasutosh") # first name
firefox.find_element_by_css_selector("#customer_lastname").send_keys("Jha") # last name
firefox.find_element_by_css_selector("#passwd").send_keys("password") # enter password
Select(firefox.find_element_by_css_selector("#days")).select_by_value("24")
Select(firefox.find_element_by_css_selector("#months")).select_by_value("11")
Select(firefox.find_element_by_css_selector("#years")).select_by_value("1996")
firefox.find_element_by_css_selector("#address1").send_keys("Dhapakhel, Lalitpur")
firefox.find_element_by_css_selector("#city").send_keys("Satdobato")
Select(firefox.find_element_by_css_selector("#id_state")).select_by_value("5")
firefox.find_element_by_css_selector("#postcode").send_keys("65018")
firefox.find_element_by_css_selector("#phone_mobile").send_keys("9848065866")
firefox.find_element_by_css_selector("#submitAccount").click()

sleep(3)

if firefox.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/p").text == "Welcome to your account. Here you can manage all of your personal information and orders.":
    print("You are registered.")
else:
    print("Some error")