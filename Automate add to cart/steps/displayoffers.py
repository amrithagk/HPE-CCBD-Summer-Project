from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException
import time


@then(u'Displays the offers')
def step_impl(context):

    try:
        context.driver.find_element(By.ID, "attach-close_sideSheet-link").click()
        context.driver.implicitly_wait(10)

        #returns all 3 cards in carousel, hence access the bank offers by indexing the array
        offers = context.driver.find_element(By.XPATH, "//a[@class='a-size-base a-link-emphasis vsx-offers-count']")
        context.driver.execute_script("arguments[0].click();", offers)
        time.sleep(5)
        context.driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-close-white a-icon-medium twister-plus-close-button']").click()
        
    except NoSuchAttributeException or NoSuchElementException:

        print("Exception occurred")
        context.driver.close()
