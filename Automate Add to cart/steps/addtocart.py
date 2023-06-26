from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'User launches Google Chrome web browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@given('User opens www.amazon.in')
def step_impl(context):
    context.driver.get("https://www.amazon.in")
    context.driver.get(r"https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

@when('user enters mobile number "{mobileno}"')
def step_impl(context, mobileno):
    context.driver.find_element(By.ID, "ap_email").send_keys(mobileno)
    continue_button = context.driver.find_element(By.ID, "continue")
    continue_button.click()


@when('user enters password "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.ID, "ap_password").send_keys(password)
    continue_button = context.driver.find_element(By.ID, "continue")
    continue_button.click()


"""
@when(u'user logs in successfully')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "//*[@id='nav-link-accountList-nav-line-1']").text()
    print(text)
    assert text == "Hello, Amritha"
"""


@then(u'User searches for required item')
def step_impl(context):
    search_box = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.send_keys("SONY 55inch TV")
    context.driver.find_element(By.ID, 'nav-search-submit-button').click() #click on the search icon

"""
@then(u'Clicks on the desired item')
def step_impl(context):
    assert True

"""


@then(u'Adds the item to the shopping cart')
def step_impl(context):
    assert True