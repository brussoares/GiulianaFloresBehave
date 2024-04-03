import time
from behave import given, when, then
from selenium.webdriver.common.by import By

@then(u'clico no banner da home')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "img[alt='Orquideas']").click()


@then(u'realizo o fluxo de compra')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "input[name='addressButton']").click()
    context.driver.find_element(By.CSS_SELECTOR, "div[class='apply-button']").click()
    context.driver.find_element(By.CSS_SELECTOR, ".product-item").click()
    context.driver.find_element(By.ID, "ContentSite_divBtBuy").click()
    context.driver.find_element(By.ID, "btConfirmShippingData").click()
    time.sleep(3)
    context.driver.find_element(By.ID, "ContentSite_divBtBuy").click()
    context.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_imbFinalize_0").click()
    context.driver.find_element(By.ID, "txtDsDestinationName").click()
    context.driver.find_element(By.ID, "txtDsDestinationName").send_keys("Bruna Costa")
    context.driver.find_element(By.ID, "txtPhone").click()
    context.driver.find_element(By.ID, "txtPhone").send_keys("11111111111")
    context.driver.find_element(By.ID, "ContentSite_rptDeliveryAddress_rbtFgPersonalAddress_0_0_0").click()
    context.driver.find_element(By.ID, "txtDsNumber").click()
    context.driver.find_element(By.ID, "txtDsNumber").send_keys("123")
    context.driver.find_element(By.ID, "btnContinue").click()
    
    context.driver.quit()