import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'que acesso o site Giuliana Flores')
def step_impl(context):
    # Setup de inicialização
    context.driver = webdriver.Chrome()     # instanciar o objeto do Selenium WebDriver especializado para o chrome
    context.driver.maximize_window          # maximizar a janela do navegador
    context.driver.implicitly_wait(10)      # esperar 10 segundos por qualquer elemento
    # Passo do teste
    context.driver.get("https://www.giulianaflores.com.br/") # abrir o navegador no site
    
@when(u'preencho campos de cadastro')
def step_impl(context):
    context.driver.find_element(By.ID, "perfil-hidden").click()
    context.driver.find_element(By.ID, "UrlLogin").click()
    context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
    context.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Bruna Costa")
    context.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("552.916.810-80")
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("bruna.costa2@mailinator.com")
    context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("teste@123")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("14783-114")
    time.sleep(2)
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("541")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("17986826945")
    
@when(u'clico no botao finalizar cadastro')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").click()
    
@then(u'sou direcionado para pagina home')
def step_impl(context):
    context.driver.find_element(By.ID, "perfil-hidden").click()
    assert context.driver.find_element(By.ID, "lblWelcome").text == "Boa Noite, Bruna!"
    
    context.driver.quit()