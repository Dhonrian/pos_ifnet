---
title: Configuração do ambiente Geopixel Cidadão (mobile-156)
description: 
published: true
date: 2023-10-27T13:35:31.203Z
tags: 
editor: markdown
dateCreated: 2023-09-28T19:53:51.765Z
---

# Configuração inicial

Passo-a-passo detalhado para a configuração do ambiente do geopixel-cidadão (mobile 156).
Embora o [README](https://gitlab.geopixel.com.br/mobile/geopx-cidadao/-/blob/master/README.md) do projeto esteja completo, alguns detalhes fazem a diferença na configuração do mesmo, por isso a criação desse manual.

Faça o clone do projeto:
`git clone https://gitlab.geopixel.com.br/mobile/geopx-cidadao.git`

# Instalação do Node
Para esse projeto, é necessária a instalação do Node.js na versão **14.15.0 ~ 14.16.1** (Outras versões foram testadas, porém sem sucesso, por isso essas em específico).

Para isso, utiliza-se o NVM para download. 
Instale o NVM seguindo esse [tutorial](https://www.freecodecamp.org/news/node-version-manager-nvm-install-guide/) ou faça o download nesse link (https://github.com/coreybutler/nvm-windows/releases).

Após instalação do NVM, a execução do comando pelo CMD deve ser possível:
![mobile-instalacao-nvm.png](/mobile-instalacao-nvm.png)


Após a instalação do NVM, execute os comandos:
`nvm install 14.16.1`
![156-node-install.png](/156-node-install.png)

`nvm use 14.16.1`
![156-node-use.png](/156-node-use.png)

Após isso, os passos do ReadMe devem ser suficientes.

# Instalação do quasar

Após set da versão corrente, faça a instalação dos pacotes do quasar/cli. (É importante esse passo ser seguido após o set da versão)
Para esse passo, a versão do quasar é indiferente.

Novamente no cmd, execute
`npm install -g @quasar/cli`
![mobile-instalacao-quasar.png](/mobile-instalacao-quasar.png)

# Instalação do yarn

Após set da versão corrente, faça a instalação dos pacotes do yarn. (É importante esse passo ser seguido após o set da versão)
![156-node-yarn.png](/156-node-yarn.png)

# Instalação das dependências

`yarn` ou `yarn install`

![156-yarn-install.png](/156-yarn-install.png)

# Execução

## Porta 
Para isso, caso a alteração da porta de execução seja necessária, abra o arquivo `quasar.conf.js` na raiz do projeto.
![156-set-execution-port.png](/156-set-execution-port.png)

## Endereço server
Para alterar o endereço da API a ser consumida, acesse:
> ...\geopx-cidadao\src\config\env\156_cacapava_redux.json

![156-url-api-server.png](/156-url-api-server.png)

> **IMPORTANTE**: 
Há configurações distintas para cada um dos ambientes e para cada uma delas, um arquivo de configuração específico em: ```src/config/env```.
O arquivo ```src/config/env/current_config.js``` é o responsável por indicar qual arquivo de configuração JSON será utilizado.
![config-156.png](/gitlab-ci/config-156.png)
> {.is-warning}


## Execução
Para executar a aplicação, execute `yarn run dev`

![156-quasar-dev.png](/156-quasar-dev.png)

![156-running.png](/156-running.png)