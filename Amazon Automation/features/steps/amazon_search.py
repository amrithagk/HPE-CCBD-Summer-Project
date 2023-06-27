import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome()


@when('open amazon home page')
def step_impl(context):
    context.driver.get("https://www.amazon.in/")


@when('search for the "{product}"')
def step_impl(context,product):
    context.driver.find_element(By.ID,"twotabsearchtextbox").send_keys(product)


@when('click on search button')
def step_impl(context):
    context.driver.find_element(By.ID,"nav-search-submit-button").click()


@when('find the third product')
def step_impl(context):
    #text = context.driver.find_element("xpath","//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]/a[1]/span[1]").text
    #assert text == "Sony Bravia 139 cm (55 inches) 4K Ultra HD Smart LED Google TV KD-55X74K (Black)"
    window_before=context.driver.window_handles[0]
    context.driver.find_element("xpath","//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]/a[1]/span[1]").click()
    time.sleep(10)
    window_after=context.driver.window_handles[1]
    context.driver.switch_to.window(window_after)


@when('click add to cart button')
def step_impl(context):
    #context.driver.get("https://www.amazon.in/Sony-Bravia-inches-Google-KD-55X74K/dp/B09WN26DG5/ref=sr_1_3?crid=NFEQG485MSTR&keywords=sony%2B55%2Binch%2Btv&qid=1687885969&sprefix=sony%2B55%2B%2Caps%2C775&sr=8-3&th=1")
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    time.sleep(10)


@when('close browser')
def step_impl(context):
    context.driver.close()















