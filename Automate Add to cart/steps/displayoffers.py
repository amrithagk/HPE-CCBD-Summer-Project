from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@then(u'Displays the offers')
def step_impl(context):

    context.driver.find_element(By.ID, "attach-close_sideSheet-link").click()
    context.driver.implicitly_wait(10)

    #returns all 3 cards in carousel, hence access the bank offers by indexing the array
    offers = context.driver.find_element(By.XPATH, "//a[@class='a-size-base a-link-emphasis vsx-offers-count']")
    context.driver.execute_script("arguments[0].click();", offers)
    
    time.sleep(10)
    context.driver.close()