---
title: Guia da Pipeline do Gitlab
description: 
published: true
date: 2024-04-29T19:15:57.500Z
tags: 
editor: markdown
dateCreated: 2024-04-29T18:23:26.386Z
---

# Guia do Ambiente de Testes Multitenant
Como subir o ambiente e acessar as aplicações no novo ambiente multitenant.

## Subindo Ambiente de Testes

Há 3 variações de ambientes de teste, diferindo apenas na conexão entre cliente e servidor:

### {.tabset}
#### Alterações Somente no Cliente

Podemos construir um ambiente no qual houve alteração apenas no lado do cliente e assim utilizaremos a branch de develop do lado do servidor para testarmos nossas modificações.

Neste caso, quando alcançarmos na pipeline o passo manual `server_branch_name`, podemos apenas clicar no botão de **Play**, como indicado na imagem abaixo.

---

![client_dependency_request.png](/v3/client_dependency_request.png)

#### Alterações Somente no Servidor

Podemos construir um ambiente no qual apenas o servidor foi alterado, assim utilizaremos a branch de develop do lado do client para consumir nosso servidor modificado e assim validarmos as alterações.

Neste caso, quando alcançarmos na pipeline o passo manual `client_branch_name`, podemos apenas clicar no botão de **Play**, como indicado na imagem abaixo.

---

![client_dependency_request.png](/v3/server_dependency_request.png)

#### Alterações Cliente e Servidor

Podemos construir um ambiente no qual houve modificações tanto no cliente quanto no servidor, assim cada branch apontará para sua complementar, isto é, a branch que implementa as modificações feitas no cliente apontará para a branch do servidor que implementa as modificações necessárias para validar a tarefa; de igual modo, a branch que implementa as modificações feitas no servidor apontará para a branch do cliente que implementa as modificações necessárias para validar a tarefa.

Neste caso, quando alcançarmos na pipeline o passo manual no cliente `server_branch_name` ou no sevidor `client_branch_name`, em ambos os casos clicamos na engrenagem como indicado na imagem abaixo.

---

![job-manual-action.png](/v3/job-manual-action.png)

---

> Para o cliente, devemos inserir uma variável de nome **branch** e como valor o nome da branch criada em par com a modificação do cliente, como indicado abaixo. Em seguida clicamos em **Run Job** no botão logo abaixo.
{.is-info}

---

![client_indicate_server_branch.png](/v3/client_indicate_server_branch.png)

---

> Para o servidor, devemos inserir uma variável de nome **branch** e como valor o nome da branch criada em par com a modificação do servidor, como indicado abaixo. Em seguida clicamos em **Run Job** no botão logo abaixo.
{.is-info}

---

![server_indicate_client_branch.png](/v3/server_indicate_client_branch.png)

### Deployando o Ambiente de Testes

Uma vez definida a branch dependente e a pipeline executou até a próxima etapa manual, basta clicarmos no botão `Play` para realizar o deploy, como indicado na imagem abaixo.

![deploy_test_environment.png](/v3/deploy_test_environment.png)


Realizado o deploy, irá aparecer um botão para acessar a aplicação, como indicado abaixo. Basta clicar para acessar sua aplicação sob teste.

![view_app_under_test.png](/v3/view_app_under_test.png)


### Alternando entre os Tenants

Ao acessar a aplicação, o tenant padrão é caçapava, como mostra a imagem abaixo, porém podemos mudar o tenant colocando os nomes de outras cidades em minúsculo, sem acento e saparado por underline `_`.

![default_tenant_application.png](/v3/default_tenant_application.png)

