Feature: Criar Usuario

    Scenario: Criar usuario no site "Giuliana Flores"
        Given que acesso o site Giuliana Flores
        When preencho campos de cadastro 
        And clico no botao finalizar cadastro
        Then sou direcionado para pagina home
    