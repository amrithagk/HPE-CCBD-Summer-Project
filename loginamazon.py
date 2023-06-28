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
    # print(text)
    # assert 'Amazon' in text
    assert text == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"


@given('I am on the Amazon e-commerce site')
def step_impl(context):
    pass


@when('I log in with valid phone number or email "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    # signin = context.driver.find_element_by_xpath("//*[@id='nav-link-accountList'']")
    # signin.click()

    signin = context.driver.find_element(By.ID, "nav-link-accountList")
    signin.click()
    # context.driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    # signin_input = context.driver.find_element_by_id("ap_email")
    # signin_input.send_keys(user)
    signin_input = context.driver.find_element(By.ID, "ap_email")
    signin_input.send_keys(user)
    context.driver.find_element(By.ID, "continue").click()
    pwd_input = context.driver.find_element(By.ID, "ap_password")
    pwd_input.send_keys(pwd)
    context.driver.find_element(By.ID, "signInSubmit").click()
    name = context.driver.find_element(By.ID, "nav-link-accountList-nav-line-1").text
    assert name == "Hello, SUMA"


@when('I search for "{product}"')
def step_impl(context, product):
    search_bar = context.driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys(product)
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@then('I should see the "SONY 55inch TV" listed in the 3rd position')
def step_impl(context):
    # flag = context.driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[
    # 5]/div/div/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
    flag = context.driver.find_element(By.XPATH, "//img[contains(@class, 's-image')]")
    context.driver.execute_script("arguments[0].scrollIntoView();", flag)


@when(u'I click on the "SONY 55inch TV"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the "SONY 55inch TV"')


@then(u'I should be redirected to the product page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be redirected to the product page')


@when(u'I add the item to the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I add the item to the cart')


@then(u'the item should be added successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the item should be added successfully')


@when(u'I view the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I view the cart')


@then(u'I should see the "SONY 55inch TV" in the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the "SONY 55inch TV" in the cart')


@when(u'I check for offers on the "SONY 55inch TV"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I check for offers on the "SONY 55inch TV"')


@then(u'I should see the current available offer(s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the current available offer(s)')


@when(u'I check the latest 5 reviews for the "SONY 55inch TV"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I check the latest 5 reviews for the "SONY 55inch TV"')


@then(u'I should see the reviews displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the reviews displayed')
