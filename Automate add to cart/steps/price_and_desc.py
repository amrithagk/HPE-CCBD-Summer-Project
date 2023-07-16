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


@then('fetch price of the product')
def step_impl(context):
    try:
        price = context.driver.find_element("xpath", " //body/div[@id='a-page']/div[@id='dp']/div[@id='dp-container']/div[@id='ppd']/div[@id='centerCol']/div[@id='apex_desktop']/div[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[2]/span[2]")
        context.driver.execute_script("arguments[0].scrollIntoView();", price)
        time.sleep(10)
        product_price=price.text
        logging.info("Located price.")
    except NoSuchElementException:
        try:
            availability = context.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[3]/div[11]/div[31]/div[1]/span")
            assert availability.text == "Currently unavailable."    
        except AssertionError:
            logging.info("Product is unavailable")
            allure.attach("Product is unavailable", attachment_type=AttachmentType.TEXT)
        except NoSuchElementException:
            logging.info("Couldn't get availability details")


@then('fetch the description of product')
def step_impl(context):
    try:
        element=context.driver.find_element("xpath"," //h1[contains(text(),'About this item')]")
        context.driver.execute_script("arguments[0].scrollIntoView();",element)
        logging.info("Fetched product description")
        time.sleep(10)
        product_description=[]
        description_element = context.driver.find_elements(By.CLASS_NAME, 'a-unordered-list a-vertical a-spacing-mini')
        for description in description_element:
            product_description.append(description.text)
        for text in product_description:
            print(text)
    except:
        logging.info("Couldn't fetch product description")
        allure.attach("Couldn't fetch product description", attachment_type=AttachmentType.TEXT)
