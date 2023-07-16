import os
import allure
from allure_commons.types import AttachmentType
from behave import *
from exceptiongroup import catch
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from telnetlib import EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('I visit amazon website')
def step_impl(context):
    context.driver.get("https://www.amazon.in/")


@when('Amazon homepage is opened successfully')
def step_impl(context):
    text = context.driver.title
    assert text == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"


@when('I am on the Amazon e-commerce site')
def step_impl(context):
    pass


@when('I log in with valid phone number or email "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    signin = context.driver.find_element(By.ID, "nav-link-accountList")
    signin.click()
    signin_input = context.driver.find_element(By.ID, "ap_email")
    signin_input.send_keys(user)
    try:
        context.driver.find_element(By.ID, "continue").click()
        pwd_input = context.driver.find_element(By.ID, "ap_password")
        pwd_input.send_keys(pwd)
        context.driver.find_element(By.ID, "signInSubmit").click()
        try:

            error_message = context.driver.find_element(By.CLASS_NAME, "a-alert-heading").text
            if error_message == "There was a problem":
                screenshot_name2 = "Incorrect_password.png"
                screenshot_path2 = os.path.join(os.getcwd(), screenshot_name2)
                context.driver.save_screenshot(screenshot_path2)
                print(f"Screenshot saved: {screenshot_path2}")
                allure.attach(context.driver.get_screenshot_as_png(), name="IncorrectPasswordSS", attachment_type=AttachmentType.PNG)
                context.driver.close()
            elif error_message == "Important Message!":
                time.sleep(20)
                allure.attach(context.driver.get_screenshot_as_png(), name="IncorrectPasswordSS",
                              attachment_type=AttachmentType.PNG)
                context.driver.close()
        except:
            pass
    except NoSuchElementException as e:
        screenshot_name3 = "incorrect_phoneno.png"
        screenshot_path3 = os.path.join(os.getcwd(), screenshot_name3)
        context.driver.save_screenshot(screenshot_path3)
        print(f"Screenshot saved: {screenshot_path3}")
        allure.attach(context.driver.get_screenshot_as_png(), name="incorrect_phonenoSS", attachment_type=AttachmentType.PNG)
        context.driver.close()


@when('I should login successfully with "{username}"')
def step_impl(context, username):
    try:
        name1 = context.driver.find_element(By.ID, "nav-link-accountList-nav-line-1").text
        assert name1 == "Hello, {0}".format(username)

    except AssertionError:
        # Test case failed, capture screenshot to allure report
        screenshot_name1 = "assertion_error.png"
        screenshot_path1 = os.path.join(os.getcwd(), screenshot_name1)
        context.driver.save_screenshot(screenshot_path1)
        print(f"Screenshot saved: {screenshot_path1}")
        allure.attach(context.driver.get_screenshot_as_png(), name="AssertionErrorSS",
                      attachment_type=AttachmentType.PNG)
        raise AssertionError("Login unsuccessful")


@when('search for the "{product}"')
def step_impl(context, product):
    context.driver.find_element(By.ID, "twotabsearchtextbox").send_keys(product)


@when('click on search button')
def step_impl(context):
    context.driver.find_element(By.ID, "nav-search-submit-button").click()


@then('find the third product')
def step_impl(context):
    window_before = context.driver.window_handles[0]
    context.driver.find_element("xpath",
                                "//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]/a[1]/span[1]").click()
    time.sleep(5)
    window_after = context.driver.window_handles[1]
    context.driver.switch_to.window(window_after)


@then('click add to cart button')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()
    time.sleep(10)


@then('fetch price of the product')
def step_impl(context):
    price = context.driver.find_element("xpath",
                                        " //body/div[@id='a-page']/div[@id='dp']/div[@id='dp-container']/div[@id='ppd']/div[@id='centerCol']/div[@id='apex_desktop']/div[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]/span[2]/span[2]")
    context.driver.execute_script("arguments[0].scrollIntoView();", price)
    time.sleep(10)
    product_price = price.text
    print(product_price)


@then('fetch the description of product')
def step_impl(context):
    element = context.driver.find_element("xpath", " //h1[contains(text(),'About this item')]")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(10)
    product_description = []
    description_element = context.driver.find_elements(By.CLASS_NAME, 'a-unordered-list a-vertical a-spacing-mini')
    for description in description_element:
        product_description.append(description.text)
    for text in product_description:
        print(text)


@then(u'Displays the offers')
def step_impl(context):
    try:
        context.driver.find_element(By.ID, "attach-close_sideSheet-link").click()
        context.driver.implicitly_wait(10)

        # returns all 3 cards in carousel, hence access the bank offers by indexing the array
        offers = context.driver.find_element(By.XPATH, "//a[@class='a-size-base a-link-emphasis vsx-offers-count']")
        context.driver.execute_script("arguments[0].click();", offers)
        time.sleep(5)
        context.driver.find_element(By.XPATH,
                                    "//i[@class='a-icon a-icon-close-white a-icon-medium twister-plus-close-button']").click()

    except NoSuchAttributeException or NoSuchElementException:

        print("Exception occurred")
        context.driver.close()


@then('the user navigates to the reviews section')
def navigates_to_reviews(context):
    context.driver.switch_to.window(context.driver.window_handles[-1])
    try:
        read_all_reviews_link = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-hook="see-all-reviews-link-foot"]'))
        )
        read_all_reviews_link.click()
        time.sleep(10)
    except:
        context.driver.quit()


@then('the user should be able to view the reviews')
def views_reviews(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.a-section.review.aok-relative'))
        )
        reviews = context.driver.find_elements(By.CSS_SELECTOR, '.a-section.review.aok-relative')
        time.sleep(10)
        for review in reviews:
            print(review.text)

    finally:
        context.driver.quit()
