---
title: Configuração do ambiente mobile de campo
description: 
published: true
date: 2023-09-29T12:13:37.151Z
tags: mobile de campo, ambiente v3, configuração v3, manual v3
editor: markdown
dateCreated: 2023-08-17T14:26:08.576Z
---

# Configuração inicial
Passo-a-passo detalhado para a configuração do ambiente do mobile de campo. 
Embora o [readme](https://gitlab.geopixel.com.br/mobile/geopx-android/-/blob/dev/README.md) do projeto esteja completo, alguns detalhes fazem a diferença na configuração do mesmo, por isso a criação desse manual.

# Instalação do Node
Para esse projeto, é necessária a instalação do Node.js na versão 13.xx (Outras versões foram testadas, porém sem sucesso, por isso essa versão em específico).

Para isso, utiliza-se o NVM para download. 
Instale o NVM seguindo esse [tutorial](https://www.freecodecamp.org/news/node-version-manager-nvm-install-guide/) ou faça o download nesse link (https://github.com/coreybutler/nvm-windows/releases).

Após instalação do NVM, a execução do comando pelo CMD deve ser possível:
![mobile-instalacao-nvm.png](/mobile-instalacao-nvm.png)

Após a instalação do NVM, execute os comandos:
`nvm install 13.10.0`
![mobile-instalacao-node-13.png](/mobile-instalacao-node-13.png)

`nvm use 13.10.0`
![mobile-instalacao-use-node-13.png](/mobile-instalacao-use-node-13.png)

# Instalação do quasar
https://quasar.dev/start/quick-start

Após set da versão corrente como 13, faça a instalação dos pacotes do quasar/cli. (É importante esse passo ser seguido após o set da versão)
Para esse passo, a versão do quasar é indiferente.

Novamente no cmd, execute
`npm install -g @quasar/cli`
![mobile-instalacao-quasar.png](/mobile-instalacao-quasar.png)

# Instalação do cordova

Após set da versão corrente como 13, faça a instalação dos pacotes do cordova. (É importante esse passo ser seguido após o set da versão)
Para esse passo, a versão do cordova precisa ser 11.1.0. Testamos outra versão, porém sem sucesso

No cmd, execute
`npm install -g cordova@11.1.0`
![mobile-instalacao-cordova.png](/mobile-instalacao-cordova.png)

# Download do Gradle
Faça o download do gradle na versão 4.10.3. O link abaixo está redirecionando diretamente ao arquivo.
https://gradle.org/next-steps/?version=4.10.3&format=all

Esse arquivo não precisa ser instalado, apenas extraído do zip e armazenado.
Adicione ao Path do sistema o caminho da basta do gradle\bin
![mobile-variaveis-de-ambiente.png](/mobile-variaveis-de-ambiente.png)

# Preparação do ambiente do cordova
https://quasar.dev/quasar-cli-webpack/developing-cordova-apps/preparation

Para isso, precisaremos do android studio e dos SDKs do android inicialmente.
https://developer.android.com/studio
![mobile-develop-studio.png](/mobile-develop-studio.png)

Faça o download e instale-lo.

Adicione as variáveis de ambiente o caminho da pasta do Android 

Após downloads, é necessário a configuração das variáveis de ambiente com os valores.

`ANDROID_HOME "%USERPROFILE%\AppData\Local\Android\Sdk"`
`ANDROID_SDK_ROOT "%USERPROFILE%\AppData\Local\Android\Sdk"`
`path "%path%;%ANDROID_SDK_ROOT%\tools;%ANDROID_SDK_ROOT%\platform-tools;<gradle_path>\bin;"`

Após, abra o Android Studio e faça os downloads dos SDKs. 

![mobile-download-sdks.png](/mobile-download-sdks.png)

Para funcionamento do cordova, baixe pelo menos as versões listadas abaixo. Aguarde alguns instantes.

![mobile-sdks-versions.png](/mobile-sdks-versions.png)

# Configuração do ambiente 

Algumas ações precisam ser tomadas para executar o ambiente:

## Arquivo env

Inicialmente, a aplicação irá conter apenas um arquivo .env.example. Faça a duplicação do mesmo, renomeando apenas para .env e altere o valor do seu conteúdo para local.

![mobile-env.png](/mobile-env.png)

![mobile-env-local.png](/mobile-env-local.png)

## Arquivo de configurações

Para injetar o caminho do servidor que a aplicação irá consumir, ou configurar outros pontos, o arquivo local.js possui os campos para configuração.

![mobile-local-js.png](/mobile-local-js.png)

# Iniciando o ambiente

![mobile-readme.png](/mobile-readme.png)

Abra o ambiente pelo VSCode ou outro editor de preferência. 

Em um celular android você deve ativar a opção **Depuração USB** dentro do **Opções do Desenvolvedor**. Essas configurações podem variar dependendo do modelo do dispositivo, usualmente para ativá-la é necessário apertar repetidamente em cima da **Versão do Kernel** em **Sobre o Telefone**.

Conecte o telefone via USB ao computador.

![mobile-adb-devices.png](/mobile-adb-devices.png)

Após isso, os comandos yarn install e yarn dev devem funcionar corretamente.
(Caso necessário, [instale o yarn](https://classic.yarnpkg.com/lang/en/docs/install/#windows-stable))

## `yarn install`

![mobile-yarn-install.png](/mobile-yarn-install.png)


## `yarn run dev:browser`

Esse comando permite executar o mobile em um navegador. 

![mobile-yarn-run-browser.png](/mobile-yarn-run-browser.png)

Após a finalização, acesse o link destacado como startPage no console.

![mobile-running-browser.png](/mobile-running-browser.png)
