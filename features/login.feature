Feature: Login

    Scenario: Login de usuário autenticado com sucesso
        Given que acesso o site Giuliana Flores
        When preencho campos de login
        And clico no botao continuar
        Then sou direcionado para pagina home

    Scenario: Usuário não existe e/ou a senha está incorreta
        Given que acesso o site Giuliana Flores
        When preencho campos login com dados invalidos
        And clico no botao continuar apos preencher dados invalidos
        Then visualizo mensagem de erro