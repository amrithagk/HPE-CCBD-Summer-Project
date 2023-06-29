import time
from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('fetch price of the product')
def step_impl(context):
    price = context.driver.find_element("xpath", " //body/div[@id='a-page']/div[@id='dp']/div[@id='dp-container']/div[@id='ppd']/div[@id='centerCol']/div[@id='apex_desktop']/div[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[2]/span[2]")
    context.driver.execute_script("arguments[0].scrollIntoView();", price)
    time.sleep(10)
    product_price=price.text
    print(product_price)


@when('fetch the description of product')
def step_impl(context):
    element=context.driver.find_element("xpath"," //h1[contains(text(),'About this item')]")
    context.driver.execute_script("arguments[0].scrollIntoView();",element)
    time.sleep(10)
    product_description=[]
    description_element = context.driver.find_elements(By.CLASS_NAME, 'a-unordered-list a-vertical a-spacing-mini')
    for description in description_element:
        product_description.append(description.text)
    for text in product_description:
        print(text)
