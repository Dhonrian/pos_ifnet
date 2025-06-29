---
title: Requerimento no banco de dados
description: Documentação do Requerimento no banco de dados
published: true
date: 2024-10-16T17:54:41.030Z
tags: json, formulário, requerimento
editor: markdown
dateCreated: 2024-10-16T17:54:39.311Z
---

![](https://wiki.flow.geopixel.com.br/template_geo/geopixel_logo_2022.png)

# Introdução

Desde o surgimento do sistema de alvará em Itapira os requerimentos eram salvos na própria aplicação. Entretanto com o aumento do número de clientes essa prática tornou difícil a manutenção e atualização dos requerimentos, fazendo com que muitos se percam ou voltem versões.

Para tratar este problema os requerimentos foram movidos da aplicação para o banco de dados e abaixo será melhor descrito como o modelo se encontra hoje.

## Requerimento

Para adequar este novo comportamento criou-se a nova tabela **flow_form**.

Cada entrada nesta tabela representa um formulário para ser utilizada num determinado fluxo.

![flowform.png](/flow-form/flowform.png)

- **id**: id do formulário.
- **type**: a coluna type faz referência a coluna *type_workflow* da *tab_process_flow*.
- **version**: a versão do formulário que está corrente.
- **type_description**: descrição do type (apenas para visualização e ser melhor identificação).
- **content**: o json que representa o formulário.
- **observation**: observação que é utilizada quando existem novas versões de formulário, explicitando o que foi removido ou adicionado.
- **insert_date**: data que a entrada foi inserida.

> A coluna **type**, **type_description** e **version** juntas formam uma chave primária, ou seja, os valores devem ser únicos pra quando um formulário é adicionado. Não é possível que um fluxo possua uma versão repetida.
{.is-warning}

A coluna **observation** é utilizada quando se é adicionada uma nova versão de um formulário fazendo com que também seja possível ter um histórico de versões dos formulários. 

![Observação no formulário que possuí uma versão 2](/flow-form/observacao.png)

## Outras tabelas

O ID da **flow_form** é utilizadas em outras tabelas pra finalizar o processo de ligação.:

- Na **tab_process** quando um processo é criado a coluna **flow_form_id** recebe o id que foi usado no momento de criação

	![tabproces.png](/flow-form/tabproces.png)

- Na **tab_process_flow** é indicado qual json deve ser utilizado na hora de criar um processo. 
	 
   ![tabprocesflow.png](/flow-form/tabprocesflow.png)
   
> Caso uma nova versão seja criada é necessária atualizar o **flow_form_id** nesta tabela, do contrário todos os novos processos serão criados utilizando o formulário antigo.
{.is-warning}


## No sistema

Em geral não há alteração na aplicação mas quando é criado uma nova versão de requerimento para um fluxo, os processos que seguem a versão antiga terão uma mensagem exibida indicando que há uma nova versão:

![novaversao.jpg](/flow-form/novaversao.jpg)


> No ínicio era possível escolher manter a versão antiga do formulário entretanto quando uma correção era feita a pessoa poderia optar por não alterar a versão. Portanto essa opção foi removida.
{.is-info}
