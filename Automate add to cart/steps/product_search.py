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