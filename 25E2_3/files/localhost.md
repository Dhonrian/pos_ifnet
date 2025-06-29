---
title: Multi Tenant no Ambiente de Desenvolvimento
description: Acessando a aplicação no ambiente multi tenant.
published: true
date: 2024-04-25T16:01:47.124Z
tags: ambiente v3, desenvolvimento, v3, ambiente, multi-tenant, tenant, multitenant, multi tenant, localhost
editor: markdown
dateCreated: 2024-04-23T13:45:33.952Z
---

# Multi Tenant no Ambiente de Desenvolvimento
Acessando a aplicação no ambiente multi tenant.

## Rodando o Cliente e Servidor
Rodar a aplicação no ambiente local não mudou com a transição para a arquitetura multi tenant.

> Se você busca informações sobre como configurar os ambientes, acesse esta página: [configuracao-ambiente-geocidades](/v3/ambiente/configuracao-ambiente-geocidades).
{.is-warning}


### Cliente
Uma vez configurado o ambiente, para iniciá-lo, executamos o comando abaixo no terminal dentro do diretório raíz do projeto do client:

```bash
npm run dev
```

> Será aberta automaticamente uma página cuja origem é **localhost:4000**, no entanto, a partir de agora, devemos adicionar à URL o subdomínio referente ao tenant. Para o ambiente de Caçapava, acessamos **cacapava.localhost:4000**.
{.is-info}

### Server
Uma vez configurado o ambiente, basta iniciá-lo de acordo com o método indicado para sua IDE apresentado na documentação [configuracao-ambiente-geocidades](/v3/ambiente/configuracao-ambiente-geocidades).

> Após configurado seu ambiente de desenvolvimento de acordo com sua IDE favorita, é importante exportarmos algumas variáveis de ambiente apontando os caminhos para nossos arquivos de configurações, de dados e temporários. Portanto, defina a variável de ambiente **GPX_HOME** apontando para o caminho absoluto da pasta **resources** encontrada na codebase do server; defina também a variável de ambiente **GPX_TEMP** apontando para o caminho absoluto da pasta **temp** também encontrada na codebase do server; por fim defina a variável de ambiente **GPX_DATA** apontando para o caminho absoluto da pasta **data** disponível em sua máquina.
{.is-warning}
