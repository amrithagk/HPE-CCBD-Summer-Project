from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I visit amazon website')
def step_impl(context):
    context.driver.get("https://www.amazon.in/")


@then('Amazon homepage is opened successfully')
def step_impl(context):
    text = context.driver.title
    assert text == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"



@when('I log in with valid phone number or email "{mobileno}" and password "{password}"')
def step_impl(context, user, pwd):
    signin = context.driver.find_element(By.ID, "nav-link-accountList")
    signin.click()
    signin_input = context.driver.find_element(By.ID, "ap_email")
    signin_input.send_keys(user)
    context.driver.find_element(By.ID, "continue").click()
    pwd_input = context.driver.find_element(By.ID, "ap_password")
    pwd_input.send_keys(pwd)
    context.driver.find_element(By.ID, "signInSubmit").click()

@then('I should login successfully')
def step_impl(context):
    name = context.driver.find_element(By.ID, "nav-link-accountList-nav-line-1").text
    assert name == "Hello, Nisarga"
    context.driver.close()
    

