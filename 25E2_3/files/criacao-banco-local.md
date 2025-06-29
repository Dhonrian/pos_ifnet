---
title: Criação de banco de dados local
description: Criação de banco de dados local a partir de um DUMP pré-existente.
published: true
date: 2023-12-05T17:31:56.255Z
tags: 
editor: markdown
dateCreated: 2023-12-05T14:10:20.562Z
---

# Criação de Banco de Dados Local

Este tutorial pressupõe que você tenha um banco de dados PostgreSQL instalado com a extensão PostGIS já configurada, caso isso não seja uma verdade para você, antes de seguir com esse passo a passo, visite a documentação de instalação e configuração do PostgreSQL e PostGIS em: https://gitlab.geopixel.com.br/geopixel/documentation/-/wikis/manual/conf_workspace#instala%C3%A7%C3%A3o-postgres-e-postgis.

## Criar conexão com banco de dados
Clique no botão indicado:
![001-criar-conexao.png](/001-criar-conexao.png)

Selecione a opção `PostgreSQL` e clique no botão `Avançar`:
![002-selecionar-banco-postgresql.png](/002-selecionar-banco-postgresql.png)

Preencha as informações de sua instância local do PostgreSQL:
![003-infos-conexao.png](/003-infos-conexao.png)

Descrição das informações:
`Host: localhost` 
- Indica que o banco de dados está instalado localmente na sua máquina, essa config também serve para banco de dados containerizados.

`Porta: 5432`
- Config padrão que pode ter sido alterado por você na instalação (ou mesmo depois dela).

`Banco de dados: -`
- Se nenhum nome de schema for informado, a conexão habilitará todos os esquemas disponíveis. É útil para ter conexões mais específicas.

`Nome do usuário: postgres`
- Config padrão que pode ter sido alterado por você na instalação (ou mesmo depois dela).

`Senha: postgres`
- Config padrão que pode ter sido alterado por você na instalação (ou mesmo depois dela). 
*Lembrete: é fortemente recomendado não utilizar senhas padrões.*

Teste a conexão com seu banco clicando no botão `Testar conexão...`, confira o resultado e se estiver tudo certo, confirme no botão `Ok` e conclua a criação no botão `Concluir`:
![004-teste-conexao.png](/004-teste-conexao.png)

## Criar novo schema de banco de dados
Basta expandir a conexão recém criada e clicar com o botão direito em `Bancos de dados` e em seguida na opção `Criar nova Banco de dados` do menu que surgiu:
![01-criar-banco-dbeaver.png](/01-criar-banco-dbeaver.png)

Escolha um `Nome do banco de dados` para seu banco local (será apontado pela aplicação) e em `Banco de dados modelo`, escolha a opção `template_postgis`.
![02-criar-banco-postgis.png](/02-criar-banco-postgis.png)
> Esta etapa é fundamental para que o novo schema utilize a extensão do PostGIS!
{.is-warning}

## Restaurar banco de dados via DUMP
Para restaurar basta clicar com o botão direito sobre o schema recém criado e navegar até `Ferramentas > Restaurar`:
![03-criar-restore.png](/03-criar-restore.png)

Informe o caminho do seu arquivo de DUMP e clique no botão `Iniciar`:
![03-restore.png](/03-restore.png)

Confirme a mensagem clicando no botão `Sim`:
![04-restore-confirmacao.png](/04-restore-confirmacao.png)

## Configurar apontamento do GeoPixel Cidades 3
Altere o arquivo `gpx-server/resources/server/config/database.json` com as informações do seu novo schema:
![05-alteracao-database-json.png](/05-alteracao-database-json.png)

Informe:
- databaseHost;
- databasePort;
- databaseUserName;
- databasePassword;
- databaseName.

Teste o apontamento do GeoPixel Cidades 3 com o novo banco de dados iniciando o server:
![06-app-em-execucao.png](/06-app-em-execucao.png)