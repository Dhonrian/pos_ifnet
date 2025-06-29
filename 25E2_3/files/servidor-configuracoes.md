---
title: Servidor de Configurações
description: 
published: true
date: 2024-01-16T14:40:38.146Z
tags: 
editor: markdown
dateCreated: 2024-01-16T14:40:04.100Z
---

# Servidor de Configurações
Temos um servidor responsável por enviar ao mobile os parâmetros necessários para que o aplicativo saiba se comunicar com uma cidade desejada.

## Modelo de Dados
O modelo de dados pode ser visualizado abaixo:

![gpx-config_-_public.png](/gpx-config_-_public.png)

## Acesso
O acesso ocorre no seguinte link: https://services.geopixel.com.br/admin/, você pode solicitar para que o Daniel Araújo crie o seu usuário staff para acessar a interface de administrador.
![gpx-config-server-admin.png](/gpx-config-server-admin.png)
Na interface de administrador você será capaz de consultar, inserir, editar, deletar os parâmetros de determinada cidade.

## Alterações no Modelo de Dados
O modelo de dados é gerado a partir dos modelos Django descritos no código, e só podem ser alterado através de migrações. Portanto, os desenvolvedores serão os responsáveis por alterar o modelo. Para entender como funciona e como realizar uma migração no Django, consulte a [documentação do framework](https://docs.djangoproject.com/en/5.0/topics/migrations/)