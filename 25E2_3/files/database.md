---
title: Configurações de Banco de Dados
description: 
published: true
date: 2024-04-23T17:12:02.068Z
tags: ambiente v3, configuração v3, manual v3, configuração, geocidades, v3, cidades, banco, dados, banco de dados
editor: markdown
dateCreated: 2024-04-23T17:12:00.242Z
---

# Configurações de Banco de Dados
Definições de variáveis necessárias à conexão com o banco de dados.

## Variáveis
**databaseHost**: Endereço da máquina na qual o banco está hospedado.
**databasePort**: Porta de acesso ao banco de dados.
**databaseUserName**: Usuário de acesso ao banco de dados.
**databasePassword**: Senha de acesso ao banco de dados.
**databaseName**: Nome do banco de dados a ser acessado.
**databaseDriverName**: Driver do SGDB que está provendo o banco de dados.
**databaseConnectionString**: Template do protocolo de acesso ao banco de dados.
**databaseDialect**: Interpretador das queries realizadas no banco de dados.

## Exemplo de Configuração
Configurações de banco de dados de Caçapava no ambiente localhost.

```json
// database.json
{
    "databaseHost": "localhost",
    "databasePort": 5432,
    "databaseUserName": "postgres",
    "databasePassword": "postgres",
    "databaseName": "cacapava",
    "databaseDriverName": "org.postgresql.Driver",
    "databaseConnectionString": "jdbc:postgresql://<DATABASE_HOST>:<DATABASE_PORT>/<DATABASE_NAME>",
    "databaseDialect": "org.hibernate.spatial.dialect.postgis.PostgisDialect"
}
```
