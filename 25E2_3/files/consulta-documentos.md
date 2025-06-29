---
title: Consulta Documentos - Dados Legados
description: 
published: true
date: 2025-02-12T14:29:31.818Z
tags: 
editor: markdown
dateCreated: 2025-02-12T14:29:30.098Z
---

# Consulta Documentos - Dados Legados

<br>

Nos sistemas de alvará, temos recebido algumas solicitações de clientes para consultar dados legados de suas cidades. Um exemplo específico dessa consulta é a Ficha Rosa para Hortolândia. No entanto, a proposta é desenvolver uma tela genérica que possibilite a consulta de diferentes dados legados.
Para isso, decidimos criar um modal genérico, que ofereça opções de consulta e, após a seleção do tipo de dado, permita a pesquisa dos dados legados por meio de um input que represente a chave necessária para a consulta.Essa abordagem visa atender a diferentes necessidades de consulta de maneira mais flexível.

Nos próximos tópicos será mostrado:

1. Como funciona;
2. Como implantar.

<br>

### Funcionamento

<br>

Para acessar a ferramenta, basta o usuário clicar no menu, posicionado no canto superior esquerdo da aplicação e escolher a opção: **Consultar dados legados**.

![menu-dados-legados.png](/fluxo/menu-dados-legados.png){.align-center}

Com isso, o modal da ferramenta será aberto e assim, podendo fazer o uso.

![modal-dados-legados.png](/fluxo/modal-dados-legados.png){.align-center}

O funcionamento da ferramenta é bem simples, sendo necessário selecionar o tipo de documento que se deseja visualizar, inserir o nome do documento no input indicado e, para realizara pesquisa, clicar no ícone da lupa ao lado direito do input. Após realizar esses passos, a busca será feita e retornado então os documentos:

![modal-dados-legados-pesquisa.png](/fluxo/modal-dados-legados-pesquisa.png){.align-center}

Na coluna **Documento** é mostrado o nome do documento, na **Tipo** o tipo do documento pesquisado e na **Ações** os ícones para visualização e download respectivamente.

<br>

### Implantação

<br>

O funcionamento o Consulta Documentos se baseia em 3 tabelas sendo 2 delas, tabelas que serão criadas com a versão que a ferramenta será disponibilizada. São elas:

- *doctypes*
- legacy_data_type
- legacy_document_type

A tabela **legacy_data_type** irá armazenar o tipo de documento legado que será disponibilizado no selectlist da ferramenta:

![legacy-data-type.png](/fluxo/legacy-data-type.png){.align-center}

A tabela **legacy_documents_type** irá armazenar o id do data_type da tabela *legacy_data_type* e o id do documento da *doctypes*.

![legacy_documents_type.png](/fluxo/legacy_documents_type.png){.align-center}

Abaixo, a visualização do id 317 da *doctypes*.

![doctypes.png](/fluxo/doctypes.png){.align-center}

Ou seja, a **legacy_documents_type** é a tabela que relaciona a categoria de documento legado que será selecionado pelo usuário e que consta na **legacy_data_type** com o tipo do documento que será retornado e que consta na tabela **doctypes**.
O tipo do documento na tabela **doctypes** será configurado de acordo com o pedido do requerente para cada documento legado, assim como o *data_type* da **legacy_data_type**.

Os arquivos dos documentos legado serão armazenados na VM, na pasta do *id* correspondente da **doctypes**.

> Importante ressaltar: se for criado um novo doctype para o documento legado na **doctypes**, será necessária a criação do diretório na VM para inserção dos arquivos e funcionamento correto da ferramenta.
O diretório criado deverá estar na pasta **anexos** da cidade correspondente.
{.is-warning}

