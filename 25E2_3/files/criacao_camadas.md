---
title: Criação de Camadas
description: Artefato para solicitação de criação de novas camadas
published: true
date: 2023-12-08T16:36:00.205Z
tags: 
editor: markdown
dateCreated: 2023-12-07T11:37:44.043Z
---

# Criação de camadas
Seja um mobile ou uma camada vetorial, existem algumas informações básicas que precisam estar na solicitação para garantir que o dado seja implantado corretamente.

Em casos de camadas do tipo forms (formulário), o json com os atributos deve ser anexado como artefato, informando também em um texto sobre as especificidades da camada no Formulário de Implantação, conforme modelo a ser descrito abaixo.

Já em casos em que a camada não se trata necessariamente de um forms, como camadas de linhas e polígonos, deve-se usar o modelo de solicitação abaixo, indicando os atributos da camada e seus tipos (combobox, checkbox, texto, data ou hora) em **arquivo txt**.

Segue exemplo de **modelo para solicitação** de uma nova camada no Geopixel Cidades:

> **Nome da tabela:**
**Nome:** informar nome da camada;
**Tipo:** mobile/ponto/linha/polígono;
**Pasta:** pasta ou subpasta em que ela estará disponível;
**Perfis de edição:** perfis em que a camada estará disponível para edição;
**Perfis de visualização:** perfis em que a camada estará disponível para visualização;
**Simbologia:** descrever como será a simbologia (cores de preenchimento e borda, símbolo, variações de acordo com atributo etc.);
**Incluir na inicialização do(s) perfil(s):** perfis em que a camada irá aparecer assim que o perfil é aberto (indicar se a camada irá estar ligada ou desligada ao logar, ficando apenas na lista de inicialização);
**Atributos:** informar em caso de camadas que não são do tipo forms (formulário json). Tente ser o mais descritivo possível para evitarmos retrabalho. Abaixo deixamos um exemplo de como os atributos podem ser especificados:
	•Atributo 1: nome | tipo | especificações | tamanho da caixa
	•Atributo 2: Invasão | combobox | Opções: Sim;Não | pequena
	•Atributo 3: Observações | caixa de texto | 4 linhas | grande
**Botões perfis edição:**
	• Visualizar/anexar/deletar documentos;
	• Mover;
	• Fotos etc.
**Botões perfis visualização:**
	• Visualizar documentos;
{.is-success}