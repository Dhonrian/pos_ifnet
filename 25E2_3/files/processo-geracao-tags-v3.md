---
title: Processo de geração de tags na V3
description: Este tutorial ensina qual é o processo de geração de tags na V3
published: true
date: 2025-01-15T12:04:26.066Z
tags: v3, processo, n3, tags, geracao, processo de geração de tags, gerar tags na v3, tags v3
editor: markdown
dateCreated: 2025-01-15T10:49:22.092Z
---

# Processo de geração de tags na V3
Este tutorial tem por objetivo ensinar o processo de geração de tags na V3.

## 1. Aceite e mesclagem do Merge Request
O processo inicia-se ainda no gitlab, após o code review de determinado Merge Request, direcionado à master. Apois o aceite deste, realiza-se a mesclagem junto a master, como no exemplo abaixo:

![aceite-merge-request.png](/aceite-merge-request.png)

## 2. Geração da tag
Localmente, dentro do escopo do projeto, certifique-se que você está na branch `master`.

![master.png](/master.png)

Após certificar-se que está na branch `master`, o primeiro passo é dar um `git fetch origin` para sincronizar quaisquer novas informações do repositório. Isto é necessário para trazer também as tags que foram geradas por outras pessoas.

![git-fetch-origin.png](/git-fetch-origin.png)

Após o `git fetch origin`, é necessário realizar o comando `git pull origin master`, que trará as alterações recém mescladas do merge request, do item 1.

![git-pull-master.png](/git-pull-master.png)

Em seguida, é importante listar as tags para verificar qual número será a próxima. Para isto, utilize o comando `git tag -l`. No exemplo abaixo, a próxima tag a ser gerada seria a `3.9.30`. Importante lembrar que para merge requests de resolução de tickets, atualizamos a versão minor da tag, que é o último número após o ponto, como por exemplo: `3.9.XX`. Já para merge requests que venham de outras branches, como `develop`, atualizamos a versão intermediária, como por exemplo: `3.X.00`.

![git-tag-0.png](/git-tag-0.png) ![git-tag-1.png](/git-tag-1.png)

Na sequência, geramos a tag, com alguma mensagem descritiva que indique as alterações que estão entrando através daquela tag. O comando a ser utilizado é: `git tag -a v3.<versão da rc>.<versão da tag> -m '<comentário da tag>'`. No nosso exemplo, geraríamos a tag dessa forma: `git tag -a v3.9.30 -m 'Ajuste no escopo do autosave para somente o contexto de edição'`. Segue abaixo um exemplo de uma tag gerada anteriormente:

![creating-tag.png](/creating-tag.png)

Após criada a tag, agora é necessário "empurrá-la" para a master. Para isso utilizamos o comando: `git push origin --tags`

![git-push-tags-1.png](/git-push-tags-1.png)
![git-push-tags-2.png](/git-push-tags-2.png)

## 3. Disparo do job de atualização da cidade
Agora de volta ao gitlab, dentro do repositório https://gitlab.geopixel.com.br/platform-gpx/gpx-server, clicamos no menu `Build -> Pipelines`

![build-pipelines.png](/build-pipelines.png)

Clicar agora sobre a pipeline da tag desejada. O clique deve ser na zona grifada de vermelho:

![pipeline.png](/pipeline.png)

Nesta tela, esperar os jobs finalizarem, e por fim escolher a cidade que deseja atualizar. Para isso, basta clicar no ícone de play no nome da cidade e aguardar:

![update-city.png](/update-city.png)

Após a cidade ser atualizada, necessário atualizar a planilha de controle que fica [aqui](https://geopx-my.sharepoint.com/:x:/g/personal/gabriel_baltazar_geopixel_com_br/EQ-mR_sqBRZEqYJlgn18zRIBJAe9lCeYKdZWzII4TuFXbw?e=ThXtRw). Também, após a geração da tag, é importante ir até a VM da cidade atualizada e copiar a pasta `opt/tomcat/webapps/geopixelcidades3` e o artefato `opt/tomcat/webapps/geopixelcidades3_server.war`, compactá-los dentro de uma pasta e enviá-los ao time de implantação, para que utilizem os artefatos mais atualizados nas implantações das cidades. Isto evita que bugs que já foram resolvidos sejam abertos pelos novos clientes, pela versão do SIG na cidade estar desatualizada.

Qualquer dúvida, estou à disposição!

## 4. Cheatseet

Puxando as alterações mais recentes da main
`git fetch origin`
 
Pull da versão mais atualizada da master
`git pull origin master`
 
Listar as tags
`git tag -l`
 
Criar nova tag
`git tag -a v3.<versão da rc>.<versão da tag> -m '<comentário da tag>'`
 
Push das tags para master
`git push origin --tags`
