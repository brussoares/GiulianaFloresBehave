Feature: Fluxo de compra

     @teste_especifico
    Scenario: Fluxo de compra a partir de um banner da home
        Given que acesso o site Giuliana Flores
        When preencho campos de login
        And clico no botao continuar
        Then clico no banner da home
        And realizo o fluxo de compra