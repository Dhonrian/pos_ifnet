---
title: Como usar o port-forwarding (encaminhamento de porta)
description: Este documento tem por objetivo ensinar como utilizar o port-forwarding na V3
published: true
date: 2024-11-26T11:31:07.249Z
tags: v3, port-forwarding, encaminhamento de porta, n3, suporte, depuração, debug
editor: markdown
dateCreated: 2024-11-26T11:31:05.460Z
---

# Como usar o port-forwarding
## 1. Invocar o método do port-forwarding na execução do projeto
No método principal do projeto (`run` em `PlatformApplication.java`) ivocar o método que estabelece o encaminhamento de porta:
![set-port-forwarding.png](/v3/set-port-forwarding.png)

## 2. Configurar o encaminhamento de porta
No método `setPortForwarding()` realizar as configurações conforme print abaixo (atente-se aos comentários do print):
![port-forwarding-tutorial.png](/v3/port-forwarding-tutorial.png)

Segue abaixo um exemplo do método preenchido com base numa integração em Bertioga (atente-se aos comentários do print):
![port-forwarding-filled.png](/v3/port-forwarding-filled.png)

## 3. Alterar a URL de conexão
Por estarmos utilizando o encaminhamento de porta, estamos simulando a porta externa em nosso próprio computador. Deste modo, se faz necessário alterar a URL de conexão para que consigamos acessar com sucesso a integração. Sem isso, continuaremos sendo bloqueados, pois o Java vai continuar batendo lá no IP externo.

Para alterar a URL de conexão eu utilizei um algoritmo conhecido da V2, na classe `RunApp.java`. Para mais informações procurar Alexandre Penteado ou Gabriel Baltazar:

`ecp` - a string de conexão original que fica na `app_tabela`
`ecp1` - a string decriptada e alterada para `localhost`

Observe também os logs:
![changing-url-conn-string.png](/v3/changing-url-conn-string.png)

## 4. Alterar a string de conexão em tempo de execução
Para se conectar, basta alterar a string de conexão em tempo de execução, na classe `ThemeAccess.java`, conforme print abaixo:
![setting-new-url-conn-string.png](/v3/setting-new-url-conn-string.png)

Desta maneira não precisamos mexer no banco de dados e nenhum problema é gerado devido à falta de atenção.

Com isso o encaminhamento de porta funcionará sem problemas. Para demais dúvidas, favor entrar em contato comigo (leandro.sa@geopixel.com.br)