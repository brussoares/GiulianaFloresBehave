import time
from behave import given, when, then
from selenium.webdriver.common.by import By

@when(u'preencho campos de login')
def step_impl(context):
    context.driver.find_element(By.ID, "perfil-hidden").click()
    context.driver.find_element(By.ID, "UrlLogin").click()
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("bruna.costa@mailinator.com")
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("teste@123")
    
@when(u'preencho campos login com dados invalidos')
def step_impl(context):
    context.driver.find_element(By.ID, "perfil-hidden").click()
    context.driver.find_element(By.ID, "UrlLogin").click()
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("bruna.costa@mailinator.com")
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("teste")
    
@when(u'clico no botao continuar')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("teste@123")
    #sleep por conta do captcha
    time.sleep(5)
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
    
@when(u'clico no botao continuar apos preencher dados invalidos')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("teste")
    #sleep por conta do captcha
    time.sleep(5)
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
    
@then(u'visualizo mensagem de erro')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".aviso-erro").text == "ATENÇÃO - e-mail ou senha inválidos!"
    
    context.driver.quit()