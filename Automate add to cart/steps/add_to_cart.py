import time
from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import logging
import allure
from allure_commons.types import AttachmentType

logging.basicConfig(filename="amazonlog.log", format="%(asctime)s  %(levelname)s:%(message)s", level=logging.INFO)

@then('click add to cart button')
def step_impl(context):
    try:
        context.driver.find_element(By.ID, "add-to-cart-button").click()
        logging.info("Added product to cart")
        time.sleep(10)
    except NoSuchElementException:
        logging.info("Couldn't add product to cart")
        allure.attach("Couldn't add product to cart", attachment_type=AttachmentType.TEXT)
