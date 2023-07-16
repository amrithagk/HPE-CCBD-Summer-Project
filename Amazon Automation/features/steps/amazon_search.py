import time
from telnetlib import EC

from behave import *
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'launch chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()


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
    window_before=context.driver.window_handles[0]
    context.driver.find_element("xpath","//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]/a[1]/span[1]").click()
    time.sleep(5)
    window_after=context.driver.window_handles[1]
    context.driver.switch_to.window(window_after)


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



@when('click add to cart button')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    time.sleep(10)


@when('close browser')
def step_impl(context):
    context.driver.close()

@then('send email notification')
def step_impl(context):
    print("Task completed")
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        sender="hellojaned123@gmail.com"
        sender_password="rzlzacazmtdkoqoj"
        receiver="hellojaned123@gmail.com"
        smtp.login(sender,sender_password)
        subject="The program was executed successfully"
        body="Congratulations!Your program was successful"
        message=f'Subject: {subject}\n\n{body}'
        smtp.sendmail(sender,receiver,message)
        print("Email sent!")















