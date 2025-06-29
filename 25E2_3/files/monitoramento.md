---
title: Componentes e comportamentos de formulário - Monitoramento
description: Esta página contém a descrição dos componentes e comportamentos de formulário que precisam ser implementados no módulo de monitoramento
published: true
date: 2023-11-24T10:54:29.802Z
tags: formulario, monitoramento, componentes
editor: markdown
dateCreated: 2023-11-24T10:53:53.109Z
---

# Detalhamento dos componentes e comportamentos de formulário - Módulo de Monitoramento

## Componentes

1. Componente de `checkbox`:
Responsável por: Realizar a seleção de um ou mais itens listados dentro de um formulário. Já mapeado no levantamento de Cadastro Imobiliário [GP-3695](https://geopixel.atlassian.net/browse/GP-3695)
Exemplo:
```
{
	"checkbox": "Acordo",
  "id": "acordo_habitacao",
  "attributes": [
  "style=margin-top:5px;margin-right:10px;"
  ],
  "width": 10
 }
```

## Comportamentos

1. Comportamento de `associar usuário`:
Responsável por: Associar um usuário a determinado formulário. Já mapeado no levantamento de Cadastro Imobiliário [GP-3652](https://geopixel.atlassian.net/browse/GP-3652)
Exemplo:
```
{
	"button": "Associar Usuário",
  "id": "btn-user",
  "attributes": [
  "style=margin-top:24px;",
  "onclick=landmark.getAllUsersByPrfId(getProfileIDInSession());"
 ],
 "width": 20
}
```