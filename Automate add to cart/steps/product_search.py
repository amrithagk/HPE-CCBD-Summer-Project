import time
from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
current_dir = os.path.dirname(os.path.realpath(__file__))


screenshot_dir = os.path.join(current_dir, "screenshots")


@when('search for the "{product}"')
    def step_impl(context,product):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(product)
    context.driver.find_element(By.ID, "nav-search-submit-button").click()
    try:
        pass
    except:
        assert "No results for" in context.driver.page_source
        time.sleep(10)
        screenshot_path3 = os.path.join(screenshot_dir, "unsuccessful_search.png")
        context.driver.save_screenshot(screenshot_path3)
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    


@when('click on search button')
def step_impl(context):
    context.driver.find_element(By.ID,"nav-search-submit-button").click()


@then('find the third product')
def step_impl(context):
    window_before=context.driver.window_handles[0]
    context.driver.find_element("xpath","//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]/a[1]/span[1]").click()
    time.sleep(5)
    window_after=context.driver.window_handles[1]
    context.driver.switch_to.window(window_after)
