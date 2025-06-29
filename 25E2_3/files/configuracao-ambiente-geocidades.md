---
title: Configuração do ambiente Geopixel Cidades (V3)
description: 
published: true
date: 2024-04-03T12:48:17.971Z
tags: 
editor: markdown
dateCreated: 2023-08-21T16:29:28.267Z
---

# 1. Configuração inicial
Antes de iniciar, faça a configuração das VPNs que liberam acesso aos repositórios do GitLab. Essa configuração pode ser realizada em conjunto ao pessoal de suporte. 

# 2. Acesso aos repositórios

Com a VPN conectada, acesse o link do gitlab: https://gitlab.geopixel.com.br/
Nele, os seguintes repositórios devem aparecer para clonar: 
* [GPX Client](https://gitlab.geopixel.com.br/platform-gpx/gpx-client)
* [GPX Server](https://gitlab.geopixel.com.br/platform-gpx/gpx-server).

![gpxcidades-repositorios.png](/gpxcidades-repositorios.png)


Caso algum dos dois projetos não esteja aparecendo, peça a liberação para o seu usuário.

# 3. Instalação do Git

Acesse o link (https://git-scm.com/) para download do Git.

![gpxcidades-instalar-git.png](/gpxcidades-instalar-git.png)

Após instalado, alguns comandos úteis para utilização do git:
- •	git pull [remote] [Branch-name]
	- • O git pull atualiza o seu código local com todas as alterações do repositório remoto.
	- • No remote, por padrão, o valor é o origin, mas isso pode ser consultado por outro comando
- • git remote
	- • Esse comando lista todos os repositórios remotos 
	- • Existe o comando “-v” que exibe os nomes dos repositórios e os seus respectivos links: “git remote -v”
- • Git checkout [remote (opcional)] [Branch-name]
	- • Esse comando altera a Branch local para a Branch desejada
	- • Existe o comando -t, onde ele faz o tracking da Branch, garantindo que o código local não sobrescreva o código que está vindo, ficando da seguinte forma: git checkout -t origin/[Branch-name]

# 4. Configurando o gpx-server

## Clonar o repositório

Primeiramente, execute o clone do projeto em uma pasta que deseja:

* git clone https://gitlab.geopixel.com.br/platform-gpx/gpx-server.git

![gpxcidades-server-clone.png](/gpxcidades-server-clone.png)


## Instalação do Java 8

Para o funcionamento do gpx-server, é recomendado a instalação do Java 8. Outras versões mais atualizadas podem ser utilizadas, porém algumas funcionalidades podem causar problemas.

(https://www.oracle.com/br/java/technologies/javase/javase8-archive-downloads.html)
![gpxcidades-jdk8.png](/gpxcidades-jdk8.png)

Faça o download e instale-o.

### Variáveis de ambiente

O próprio executável do jdk deve criar as variáveis de ambiente, porém confirme as informações

![gpxcidades-java-home.png](/gpxcidades-java-home.png)

![gpxcidades-path-java8.png](/gpxcidades-path-java8.png)

## Configuração do Maven

Para o funcionamento do gpx-server, é necessário a configuração do maven. Esse item faz a compilação necessária do java.

![gpxcidades-maven.png](/gpxcidades-maven.png)

Execute o download do arquivo e armazene em um local de fácil acesso. Ele não é instalado na máquina, apenas precisaremos dele em uma variável de ambiente.

![gpxcidades-maven-download.png](/gpxcidades-maven-download.png)

Após isso, basta criar uma variável de ambiente com o nome de M2_HOME e, no valor colocar o endereço armazenado da pasta, como no exemplo abaixo.

![gpxcidades-m2-home.png](/gpxcidades-m2-home.png)

## Variáveis de ambiente

É necessário a configuração de mais uma variável chamada SERVER_SERVLET_CONTEXT_PATH. Ela possui um valor fixo de "/server"

![gpxcidades-server-servlet-context-path.png](/gpxcidades-server-servlet-context-path.png)

## GDAL

Essa funcionalidade usa uma biblioteca chamada ogr, que cria arquivos espaciais, como o shapefile.
Para configurar, é necessário ter os binários da biblioteca em sua máquina.

Faça o download dos seguintes arquivos, descompacte e os armazene. Precisaremos do path do local armazenado posteriormente: 

[Gdal.zip](https://geopx.sharepoint.com/:u:/r/sites/GeopixelDesenvolvimentoSuporte2/Documentos%20Compartilhados/General/Desenvolvimento/GEOPIXEL%20CIDADES%20V3/Ambiente/GDAL.zip?csf=1&web=1&e=yOIljT)

[GdalExec.zip](https://geopx.sharepoint.com/:u:/r/sites/GeopixelDesenvolvimentoSuporte2/Documentos%20Compartilhados/General/Desenvolvimento/GEOPIXEL%20CIDADES%20V3/Ambiente/GDALExec.zip?csf=1&web=1&e=pHVmQr)

É preciso configurar variáveis de ambiente que apontam para esses binarios, para que, no código, a biblioteca leia e consiga executar as operações.

Primeiro, copie o PATH da pasta  **GDALEXEC\projlib** e crie uma variável de ambiente com o nome **PROJ_LIB**.

![gpxcidades-gdal-projlib.png](/gpxcidades-gdal-projlib.png)

Ainda com o PATH do GdalExec, adicione dois valores à variável **PATH**:
1. Caminho da pasta GdalExec
2. Caminho da pasta GdalExec\projlib

![gpxcidades-gdal-exec-path.png](/gpxcidades-gdal-exec-path.png)

Já com a outra pasta Gdal, adicione os seguintes valores à variável **PATH**:
![gpxcidades-gdal-path.png](/gpxcidades-gdal-path.png)

## Configuração da IDE

### Opção 1: Visual Studio Code

Para a IDE, pode ser utilizado o Visual Studio Code. (https://code.visualstudio.com/)

![gpxcidades-vscode.png](/gpxcidades-vscode.png)

Faça o download e instale-o.

#### Extensões necessárias do java.

Para a execução do java, algumas extensões foram necessárias no momento da configuração. 

1. Extension pack for Java

![gpxcidades-vscode-extension-java.png](/gpxcidades-vscode-extension-java.png)

2. Maven for Java (instalado automaticamente pelo extension pack)

![gpxcidades-vscode-maven-java.png](/gpxcidades-vscode-maven-java.png)


#### Launch.json

Abra o VSCode e a pasta do projeto. 
Na aba de Debug, busque pelo launch.json. Caso não exista, crie o arquivo para que possamos configurá-lo. 

![gpxcidades-vscode-launch.png](/gpxcidades-vscode-launch.png)

No arquivo que se abre, faça as alterações adicionando o block “env”. 

![gpxcidades-vscode-launch-config.png](/gpxcidades-vscode-launch-config.png)

Coloque logo abaixo do "mainClass" dentro do "configurations", um bloco de "env" representados os valores das variáveis de ambiente.

> "env": {
		"JAVA_HOME": "[**Caminho da pasta do Java**]",
		"GPX_HOME": "[**Caminho da pasta do servidor**]\resources",
    "GPX_DATA": "[**Caminho da pasta do servidor**]\data",
    "GPX_TEMP": "[**Caminho da pasta do servidor**]\temp",
		"SERVER_SERVLET_CONTEXT_PATH": "/server", (Esse ultimo é fixo)
}

Então por exemplo:

> "env": {
		"JAVA_HOME": "C:\\\Program Files\\\Java\\\jdk1.8.0_211",
		"GPX_HOME": "C:\\\DEV\\\Projects-Geopixel\\\gpx-server\\\resources",
		"GPX_DATA": "C:\\\DEV\\\Projects-Geopixel\\\gpx-server\\\data",
    "GPX_TEMP": "C:\\\DEV\\\Projects-Geopixel\\\gpx-server\\\temp",
		"SERVER_SERVLET_CONTEXT_PATH": "/server",
}

#### Executando a aplicação

Para a execução da aplicação, faça o build da aplicação com:
> mvn clean install -DskipTests

Em seguida busque pela classe PlatformApplication. Nela, é possível fazer a execução pela legenda que aparece em cima do método main.

![gpxcidades-vscode-run.png](/gpxcidades-vscode-run.png)

### Opção 2: Eclipse

Uma outra opção a IDE do server, pode ser utilizado o Eclipse (https://www.eclipse.org/downloads/)

![gpxcidades-eclipse.png](/gpxcidades-eclipse.png)

Faça o download e instale-o.

#### Configuração do Java 8 no eclipse.

Normalmente, ao instalar o eclipse, é baixado uma versão do java própria do eclipse, porém não utilizaremos ela, mas sim, a que foi baixada no inicio do manual.
Para isso, abra a pasta onde foi instalado o eclipse.

![gpxcidades-eclipse-folder.png](/gpxcidades-eclipse-folder.png)

Abra o arquivo eclipse.ini com um editor de texto.

No item "-vm", informe o caminho da pasta java instalada. Caso não existente, crie uma.
Faça a conferência dos valores da versão do java requerida também, conforme na imagem

![gpxcidades-eclipse-vm.png](/gpxcidades-eclipse-vm.png)

#### Importando projeto.

Importe o projeto à workspace do eclipse.

![gpxcidades-eclipse-existing-maven.png](/gpxcidades-eclipse-existing-maven.png)

![gpxcidades-eclipse-pom-xml.png](/gpxcidades-eclipse-pom-xml.png)

Ao confirmar, o eclipse já deve começar o download das bibliotecas necessárias para subir a aplicação. Aguarde todo o processo executado (A janela de progress mostra o status das operações).

#### Compile do maven pelo eclipse

Originalmente, ao importar o projeto, o eclipse faz a compilação automaticamente do projeto, deixando o pronto para execução. Porém, a compilação do projeto também pode ser executada pelo atalho Alt+F5

![gpxcidades-eclipse-maven-compile.png](/gpxcidades-eclipse-maven-compile.png)

Certifique-se que o projeto do gpx-server esteja marcado e pressione Ok. A compilação se inicia.

#### Execução do projeto

Para a execução da aplicação, faça o build da aplicação com:
> mvn clean install -DskipTests

Para execução do projeto, da mesma forma que no Visual Studio Code, busque pela classe "PlatformApplication.java" >> botão direito >> Run As >> Java Application

![gpxcidades-eclipse-run-application.png](/gpxcidades-eclipse-run-application.png)

# 5. Configurando o gpx-client

## Linguagem

Aqui está sendo usado o NodeJS. Baixe e instale. (https://nodejs.org/en/).
Obs.: Para o client, a versão do Node não está influenciando diretamente no seu funcionamento, portanto a versão LTS será o suficiente.

![gpxcidades-client-node.png](/gpxcidades-client-node.png)

## Ambiente

Execute os comandos de configuração do npm no terminal do VSCode:

`npm install`

![gpxcidades-client-install.png](/gpxcidades-client-install.png)

`npm run dev` (Vai demorar um pouco por conta de uma verificação do typescript)

![gpxcidades-client-run-dev.png](/gpxcidades-client-run-dev.png)

Após execução do “npm run dev”, uma tela deverá se abrir, com o endereço http://localhost:4000/

![gpxcidades-client-running.png](/gpxcidades-client-running.png)

Com usuário e senha admin/admin, você conseguirá realizar o login do sistema.

## Bugs conhecidos.

### Problema nos estilos criados CssExports

Sempre que acontecer o erro do estilo não existir no CssExports, deverá ser excluído o arquivo “.d.ts” respectivo.

![gpxcidades-bugs-tsc.png](/gpxcidades-bugs-tsc.png)

Após reexecução do npm da aplicação, o arquivo será gerado novamente com a correção feita.