from selenium import webdriver
from time import sleep
def login(firefox):
    firefox.get("http://automationpractice.com/index.php") # go to home page
    firefox.find_element_by_css_selector(".login").click() # click on login

    firefox.find_element_by_css_selector("#email").send_keys("email@address.org")
    firefox.find_element_by_id("passwd").send_keys("password")
    firefox.find_element_by_css_selector("#SubmitLogin").click()
    sleep(3)
def successful_login(firefox):
    return firefox.current_url == "http://automationpractice.com/index.php?controller=my-account"

if __name__ == "__main__":
    firefox = webdriver.Firefox()
    login(firefox)

    if successful_login:
        print("Successful login")
    else:
        print("Error somewhere.")