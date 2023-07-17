from behave import given, when, then
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import allure
from allure_commons.types import AttachmentType

logging.basicConfig(filename="amazonlog.log", format="%(asctime)s  %(levelname)s:%(message)s", level=logging.INFO)

@then('the user navigates to the reviews section')
def navigates_to_reviews(context):
    context.driver.switch_to.window(context.driver.window_handles[-1])
    logging.info("Navigated to review section")
    try:
        read_all_reviews_link = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-hook="see-all-reviews-link-foot"]'))
        )
        read_all_reviews_link.click()
        time.sleep(5)
    except:
        logging.info("Couldn't locate reviews")
        allure.attach("Couldn't locate reviews", attachment_type=AttachmentType.TEXT)
        context.driver.quit()

@then('the user should be able to view the reviews')
def views_reviews(context):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.a-section.review.aok-relative'))
        )
        reviews = context.driver.find_elements(By.CSS_SELECTOR, '.a-section.review.aok-relative')
        logging.info("Opened reviews page")
        time.sleep(5)
        for review in reviews:
            print(review.text)
    except:
        logging.info("Couldn't open reviews page")
        allure.attach("Couldn't open reviews page", attachment_type=AttachmentType.TEXT)
    finally:
        context.driver.quit()
