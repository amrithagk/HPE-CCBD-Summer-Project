from behave import given, when, then
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user is on the Amazon homepage')
def step_user_on_homepage(context):
    context.driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser
    context.driver.get('https://www.amazon.com')

@when('the user searches for "{search_query}"')
def step_user_searches(context, search_query):
    search_box = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_box.clear()  # Clear the search box
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

@when('the user clicks on the 3rd search result')
def step_user_clicks_third_result(context):
    search_results = context.driver.find_elements(By.CSS_SELECTOR, '.s-result-list .s-result-item')
    if len(search_results) > 3:
        third_result = search_results[3]
        third_result_link = third_result.find_element(By.CSS_SELECTOR, 'a')
        third_result_link.click()
    else:
        context.driver.quit()


@when('the user navigates to the reviews section')
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
