# We will be using daraz for this. password issue?>?> we will be using our http://automationpractice.com/index.php for this task
# we will login then click on cart icon and see in the page if there are items in the cart or not
# if there are items in the cart then we simply return the number and exit
from login_auto import login, successful_login
from selenium import webdriver
from time import sleep

firefox = webdriver.Firefox()
login(firefox)

if successful_login:
    print("Successful login")
else:
    print("Error somewhere.")

sleep(25)
# add no. of items here
# automating addition of items to cart seems hard
# add items manually
print(f'number of items in cart now is {firefox.find_element_by_css_selector("span.ajax_cart_quantity:nth-child(2)").text}.')