import time
from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('click add to cart button')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    time.sleep(10)
