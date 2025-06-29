---
title: Nova Pipeline do Gitlab
description: Esta doc visa orientar sobre o novo fluxo de integração do gitlab.
published: true
date: 2024-02-06T17:57:38.744Z
tags: 
editor: markdown
dateCreated: 2023-08-11T18:01:08.756Z
---

# Novo fluxo de integração do Gitlab

## Ação manual por parte dos devs
1. Em todo MR, durante a execução da pipeline, será solicitado a inserção manual da branch do (server/client) da qual depende a aplicação na versão do MR. Então devemos seguir como indicado a imagem abaixo.

![solicitação_de_inserção_da_branch_dependente.png](/gitlab-ci/solicitação_de_inserção_da_branch_dependente.png)

2. Clique na engrenagem para abrir a página na qual indicaremos a branch dependente.

![acesso_à_etapa_manual_para_inserção_de_branch_dependente.png](/gitlab-ci/acesso_à_etapa_manual_para_inserção_de_branch_dependente.png)

3. Inserimos então no campo esquerdo (key) o texto "**mr**" e no campo direito (value) o id do merge request dependente.

![ref-mr.png](/ref-mr.png)

Para encontrar o id merge request basta navegar até o MR que será referenciado e observar como no exemplo:

![id-mr.png](/id-mr.png)

Caso não tenha sido criado branch dependente para a tarefa do MR, nenhum valor precisa ser preenchido, e por default a branch referenciada será a "**develop**", basca clicar no ícode de *play*.

![playzinho.png](/playzinho.png)

## Ação manual por parte dos QAs

1. Na página do MR terá disponível um botão para deploy da aplicação, no qual o QA deverá clicar quando for iniciar seus testes. Após clicado será aberto um popup de confirmação, no qual deverá ser clicado no botão de deploy novamente.
![botão_para_iniciar_o_ambiente_de_testes.png](/gitlab-ci/botão_para_iniciar_o_ambiente_de_testes.png)

2. Após o primeiro passo, é preciso aguardar pela finalização do job que subirá o ambiente de teste. Ao atualizar a página após a finalização do job, um botão de acesso à aplicação se tornará disponível para que os QAs acessem e realizem seus testes.
![botão_para_acesso_à_aplicação.png](/gitlab-ci/botão_para_acesso_à_aplicação.png)

3. Após a finaliação dos testes é importante que o ambiente de testes seja removido seguindo os passos abaixo para que não se consuma recursos da máquina que hospeda o ambiente de testes. Clicamos no último job e no botão indicado por um quadrado preenchido.
![botão_para_remoção_do_ambiente_de_testes.png](/gitlab-ci/botão_para_remoção_do_ambiente_de_testes.png)
