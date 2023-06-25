from behave import *
from selenium import webdriver

#continue with webdriver implementation

@given(u'User opens www.amazon.in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User opens www.amazon.in')


@given(u'user logs in to their account successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given user logs in to their account successfully')


@when(u'User searches for required item')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User searches for required item')


@when(u'Clicks on the desired item')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Clicks on the desired item')


@then(u'Add the item to the shopping cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Add the item to the shopping cart')