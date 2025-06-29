---
title: Documentação de publicação do Geopixel Cidades
description: 
published: true
date: 2024-11-23T18:30:29.834Z
tags: 
editor: markdown
dateCreated: 2023-09-19T11:53:12.018Z
---

# Introdução
Este documento descreve o processo de como realizar a geração de uma versão nova do Geopixel Cidades. No momento, este processo se aplica à família 3.x. Serão descritos os passos do processo bem como detalhamento de como disponibilizar os arquivos gerados no processo. 

# Preparação do repositório local
O primeiro passo para a geração da versão é preparar o repositório local para a realização dos ajustes. Sendo assim, é necessário atualizar os repositórios do cliente e do servidor de forma que eles fiquem com todos os commits do repositório principal. 

Para isso, no atual momento, é utilizada a branch develop em ambas frentes (client e server).
![deploy-client-develop.png](/deploy-client-develop.png)

![deploy-server-develop.png](/deploy-server-develop.png)

# Geração dos arquivos para publicação 
Esta sessão descreve os passos para a geração do conteúdo que será publicado. 
Para o servidor, será gerado um arquivo war. 
Para o client, será gerada uma pasta contendo um conjunto de arquivos que representam a aplicação cliente. 

## Server
Para o servidor, é necessário gerar o arquivo war para ser publicado. 
Em todas as etapas a seguir, um arquivo será gerado na pasta /target. Esse arquivo será utilizado para implantação.

![deploy-server-target.png](/deploy-server-target.png)

### Visual Studio Code
Caso esteja utilizando o Visual Studio Code, siga os passos para gerar o war:
1. Nos ícones à **esquerda**, abra a aba **Explorer**;
2. Dentro de ***Explorer***, busque pela aba do Maven localizado na parte inferior da tela;
3. Dentro de ***Maven***, busque por plugins;
4. Dentro de ***Plugins***, clique em war;
5. Dentro de ***war***, busque pelo war e clique no ícone de "*play*" à direita.

![deploy-server-vscode.png](/deploy-server-vscode.png)

O console do Visual Studio Code deve se abrir, executando a *build*.

![deploy-server-vscode-running.png](/deploy-server-vscode-running.png)

### Eclipse
Caso esteja utilizando o Eclipse, utilize o plugin do Maven para gerar o build.
Siga os passos para gerar o war:
1. Com o botão **direito**, clique no projeto para **abrir o submenu**;
2. Vá em **Run As** e abra o submenu;
3. Clique em **Maven build**;

![deploy-server-eclipse-1.png](/deploy-server-eclipse-1.png)

4. No campo **Goals**, digite **"package"**;
5. **(Opcional)** Marque a opção *Skip Tests* para agilizar o build;
6. Clique em ***"Run"***.

![deploy-server-eclipse-2.png](/deploy-server-eclipse-2.png)

O console do Eclipse deve se abrir, executando a *build*.
![deploy-server-eclipse-running.png](/deploy-server-eclipse-running.png)

### Cmd

Caso não esteja utilizando nenhum dos citados acima ou não deseja, existe a forma do CMD.
1. Abra o console na pasta do server.
2. Digite `mvn clean install`
	2.1. Opcionalmente, como no eclipse, existe a forma sem executar os testes para agilizar o build 
  `mvn clean install -DskipTests`

![deploy-server-cmd.png](/deploy-server-cmd.png)

## Client

Para o cliente, são necessários dois comandos. O primeiro irá garantir que todas as dependências estão disponíveis localmente, e o segundo irá processar os arquivos e gerar na pasta de saída o conteúdo a ser publicado. 

Obs.: Executar os comandos no terminal, tendo como base a pasta raiz do projeto cliente 


1. npm install
	Baixa todas as dependências e prepara o ambiente local;

![deploy-client-install.png](/deploy-client-install.png)

2. npm run build 
	Processa os arquivos e gera o conteúdo a ser publicado com base no arquivo **webpack.prod.config.js**
  Obs.: Esse é um processo demorado, em torno de 15~30 minutos.

![deploy-client-build-1.png](/deploy-client-build-1.png)

![deploy-client-build-2.png](/deploy-client-build-2.png)

Observação: Caso ocorram erros relacionados à estilos na hora de executar o comando npm run build, será necessário apagar os arquivos da pasta do projeto com a seguinte extensão: scss.d.ts. 

Estes comandos irão gerar o seguinte conteúdo na pasta /dist/gpx_platform_client: 

![deploy-client-result.png](/deploy-client-result.png)

# Banco de dados

O banco de dados deve ser configurado no arquivo `gpx-server/resources/server/config/database.json` com as informações da base de dados que será utilizada na publicação.
![database-json.png](/database-json.png)

Para este exemplo apontaremos para o banco de dados de homologação, no endereço 10.0.0.146:5432, com nome de geopixelcidades3_dev.

![banco-homolog.png](/banco-homolog.png)

Por hora, não é necessário nenhuma outra configuração de banco para essa aplicação.

# Configuração e Atualização de arquivos de resource 

O primeiro passo é a definição da variável de ambiente que irá apontar para a pasta onde os arquivos de configuração serão disponibilizados. Para isso, devemos criar ou atualizar o conteúdo do arquivo `/opt/tomcat/bin/setenv.sh` e configurar nele a seguinte variável de ambiente `GPX_HOME` apontando para a pasta onde serão disponibilizados os arquivos de configuração (neste momento também podemos configurar `GPX_DATA` e `GPX_TEMP`). A seguir um exemplo do conteúdo do arquivo `setenv.sh`: 

> export GPX_HOME=/opt/gpx_home
> export GPX_DATA=/opt/gpx_data
> export GPX_TEMP=/opt/gpx_temp

E por consequência a criação dessas mesmas pastas em disco:
> mkdir /opt/gpx_home
> mkdir /opt/gpx_data
> mkdir /opt/gpx_temp

O passo seguinte é a publicação dos arquivos de configuração e de resources na pasta do servidor que o sistema irá acessar e que foi configurada no passo anterior. O conteúdo base que pode ser utilizado como referência se encontra dentro do repositório do servidor, na seguinte pasta: `/resources/{context_path}`.

![deploy-server-resources.png](/deploy-server-resources.png)

Note que `{context_path}` representa o context path do servidor tomcat onde o servidor do Geopixel cidades será publicado. Em geral, o context_path é derivado do nome do arquivo war. Como exemplo, caso a publicação do arquivo war chamado `gpx_platform_server.war` tenha sido realizada, o tomcat irá publicar os arquivos na seguinte subpasta `/opt/tomcat/webapps/gpx_platform_server`. 

Neste caso, gpx_platform_server irá representar o context_path. Consequentemente, a pasta em disco onde os arquivos serão publicados deverá ser `${GPX_HOME}/gpx_platform_server/`. A figura a seguir ilustra a estrutura de pastas neste exemplo. 

![deploy-server-folder.png](/deploy-server-folder.png)

![deploy-server-folder-config.png](/deploy-server-folder-config.png)

> Importante destacar que se uma publicação já existir, é necessário tomar cuidado para não sobrescrever os arquivos de configuração. Neste caso, é preferível abrir os arquivos que configuram a aplicação ou o banco de dados e apenas atualizar caso necessário. Os arquivos de configuração se encontram na subpasta config e podem ser vistos na figura a seguir: 
{.is-warning}

A pasta de dados `GPX_DATA` pode permanecer vazia, enquanto a pasta temporária `GPX_TEMP` deverá contemplar subpastas para cada tenant configurado, contando ainda com uma subpasta chamada `reports`, seguindo o padrão "*/gpx_data/**\<tenant>**/reports*":
Ex.:
- .../gpx_temp/cacapava/reports
- .../gpx_temp/bertioga/reports

Para criar a estrutura de pastas desejada, execute o comando a seguir substituindo o nome do tenant conforme necessidade e em seguida fornece o permissionamento:
> mkdir -p /opt/gpx_temp/\<tenant>/reports

Após findado o processo de criação das pastas de disco, é necessário conceder o permissionamento necessário para a app salvar os arquivos em tempo de execução, para isso use:
> chmod -R 777 /opt/gpx_data
> chmod -R 777 /opt/gpx_temp/\<tenant>

# Configurações do TomcCat
## Deploy automatico
Para que o Tomcat reconheça alteração nos artefados da pasta `.../tomcat/webappss`, a configuração de `autoDeploy` deve estar ativada.
O arquivo a ser alterado é: `/opt/tomcat/config/server.xml` e o trecho que descreve o `Host` deve ficar como:
![autodeploy-tomcat.png](/autodeploy-tomcat.png)

Eventualmente o autodeploy pode falhar por algum motivo, se isso acontecer, esteja pronto para forçar que o Tomcat com o comando `touch`, por exemplo:
> touch /opt/tomcat/webapps/geopixelcidades3_server.war

## Referência do GDAL
A aplicação têm como uma de suas dependências a Biblioteca de Abstração de Dados Geoespaciais chamada GDAL.
A correta configuração para que o Tomcat consiga encontrar essa dependência se divide em três etapas:
1. Compilar o JAR do GDAL na versão 3.5.0 na máquina que receberá a publicação;
2. Criar um link simbólico para o JAR do GDAL a partir da pasta de bibliotecas do Tomcat;
3. Referenciar a pasta do JAR do GDAL na variável de ambiente LD_LIBRARY_PATH;
4. Corrigir o owner do tomcat.

### Compilar o JAR do GDAL na versão 3.5.0 na máquina que receberá a publicação

Instalamos as dependências necessárias para realizar o build do gdal executando os comandos abaixo:

```bash
apt-get update && apt-get install -y \
    build-essential \
    wget cmake swig ant libgeos-dev \
    libproj-dev proj-data proj-bin swig \
    libkml-dev libxml2-dev libsqlite3-dev \
    libspatialite-dev
```

Baixar depois o código fonte do GDAL na versão correta, para tanto executamos os comandos abaixo:

```bash
cd /tmp
wget -N https://github.com/OSGeo/gdal/releases/download/v3.5.0/gdal-3.5.0.tar.gz
tar -xzf gdal-3.5.0.tar.gz
```

Realizamos então o build do GDAL com os comandos abaixo:

```bash
cd gdal-3.5.0 && mkdir build && cd build && \
    cmake .. -DBUILD_JAVA_BINDINGS=ON -DBUILD_PYTHON_BINDINGS=OFF -DOGR_ENABLE_DRIVER_GPKG=ON -DCMAKE_INSTALL_PREFIX=/usr && \
    cmake --build . --target install -- -j12
```

### Criar um link simbólico para o JAR do GDAL a partir da pasta de bibliotecas do Tomcat
O link simbólico deve ser criado na pasta `lib` do Tomcat.
Para criar o link simbólico basta utilizar o comando a seguir:
> ln -s /usr/share/java/gdal-3.5.0.jar /opt/tomcat/lib/gdal.jar

A instrução é responsável por criar um link simbólico chamado `gdal.jar` apontando para o JAR do GDAL configurado no passo anterior.
O resultado deve ser semelhante a este:
![link-simbolico-gdal.png](/link-simbolico-gdal.png)

### Referenciar a pasta do JAR do GDAL na variável de ambiente LD_LIBRARY_PATH
O Tomcat possui um arquivo de configuração de variáveis que é executado quando o startup do servidor de aplicação se dá a partir do arquivo `.../tomcat/bin/startup.sh`, o nome deste arquivo é `setenv.sh`.
Devemos alterá-lo para especificar os caminhos aos quais o Tomcat precisa procurar bibliotecas compartilhadas, essa configuração é feita através da variável de ambiente `LD_LIBRARY_PATH`.
Garanta que o arquivo `setenv.sh` expõe tal variável apontando para o a pasta compartilhada da Java em que configuramos o JAR do GDAL no passo 1.
> export LD_LIBRARY_PATH=:/lib:/usr/lib/x86_64-linux-gnu:/usr/share/java

### Corrigir o owner do Tomcat
O tomcat pode vir configurado com usuário `root` como owner e precisamos alterar para que o usuário `tomcat` seja o owner. Para isto executamos o comando abaixo.
```bash
chown -R tomcat:tomcat /opt/tomcat
```
![owner_do_tomcat.png](/owner_do_tomcat.png)

### Configuração de variáveis de ambiente do Tomcat
Atualmente temos duas possíveis variáveis de ambiente para a aplicação relacionadas a contextos específicos, citados na sessões a seguir.
Para ambientes que existam diversas instâncias do GeoPixel Cidades 2 ou 3, é aconselhavel que as variáveis de ambiente sejam criadas de forma escopada para cada instância específica da aplicação.
Para isso, deve ser criado um arquivo em `$CATALINA_HOME/conf/Catalina/localhost/` de mesmo nome que o artefato (war) com a extensão `xml`, para o artefato `geopixelcidades3_server.war` é esperado `$CATALINA_HOME/conf/Catalina/localhost/geopixelcidades3_server.xml`, por exemplo.

## Configuração de ambiente de testes
As migrations são divididas entre dois grupos `common` e `development`.
- Migrations `common`: devem ser executadas para todas as bases de dados para garantir o correto funcionamento do GeoPixel Cidades 3
- Migrations `development`: devem ser executadas apenas nos ambientes de testes, geralmente gerando massa de testes.

As migrations `development` são acionadas por uma configuração que indica que o ambiente que está executando a aplicação é de `dev`. Isso é feito via variável de ambiente, args do java ou configuração no Tomcat.

Deve ser criado/editado o arquivo `/opt/tomcat/conf/Catalina/localhost/geopixelcidades3_server.xml`, contendo a seguinte declaração de `<Environment>`:
> \<Context>
		\<Environment name="**spring.profiles.active**" value="**dev**" type="java.lang.String" override="false" />
  \</Context>

***OU*** para ambientes locais/containerizados que possuam instâncias únicas, basta criar uma variável de ambiente com:
> export **spring_profiles_active**="**dev**"

## Configurações de *singletenant*
> Essa sessão deve ser considerada apenas para publicação da versão do Geopixel Cidades 3 Multitenant!
{.is-danger}

Mapeamos dois cenários da publicação do Geopixel Cidades 3 para o ambiente produtivo, são eles:
- **Multitenant (default)**: Aplicação única implantada na Oracle Cloud (ao que tudo indica) com múltiplos subdomínios configurados para cada prefeitura/tenant. 
*Ex.*: 
	- `https://www.bertioga.gpxcidades3.com.br`;
  -	`https://www.cacapava.gpxcidades3.com.br`;
  - `https://www.barueri.gpxcidades3.com.br`;
  - etc.
- **Singletenant**: Aplicação implantada na infraestrutura da própria prefeitura funcionando com apenas um tenant (a própria prefeitura). Nesse caso não há subdomínios específicos, apenas um único domínio como: `https://www.bertioga.sp.gov.br/gpxcidades3` (ou qualquer outro), ao invés disso, há uma variável de ambiente que define para qual prefeitura/tenant será utlizada na aplicação.

Para publicações do time singletenant a variável de ambiente deve ser definida da seguinte forma:
Deve ser criado/editado o arquivo `/opt/tomcat/conf/Catalina/localhost/geopixelcidades3_multitenant_server.xml`, contendo a seguinte declaração de `<Environment>`:
> \<Context>
		\<Environment name="**defaultTenant**" value="**cacapava**" type="java.lang.String" override="false" />
  \</Context>

***OU*** para ambientes locais/containerizados que possuam instâncias únicas, basta criar uma variável de ambiente com:
> export **defaultTenant**="**cacapava**"

Atualmente os valores possíveis são:
- `cacapava`;
- `barueri`;
- `sao_sebastiao`;

# Publicação do cliente e servidor 

O passo final é a publicação do cliente e do servidor. Essencialmente, iremos copiar o conteúdo gerado na pasta `/opt/tomcat/webapps`. 

Para o servidor, basta copiar o arquivo war para a pasta `/opt/tomcat/webapps`. Por padrão o tomcat irá realizar a publicação de forma automatizada assim que o arquivo for copiado.

![deploy-server-war.png](/deploy-server-war.png)

Já para o cliente, devemos criar manualmente a pasta para representar o context_path e copiar nele o conteúdo da pasta /dist/gpx-platform-client. 

Um passo importante é garantir que o arquivo configurations.json aponte corretamente para o servidor que foi publicado no outro context_path. Caso o arquivo já exista, a melhor estratégia ao publicar o cliente é não substituir este arquivo uma vez que ele já vai estar apontando corretamente para o endereço do servidor. 

![deploy-scp-client-configuration.png](/deploy-scp-client-configuration.png)
Com o caminho da pasta do war gerada pelo tomcat.

# Geoserver 

O GeoServer é um servidor que permite a publicação e compartilhamento de dados geoespaciais na web. É projetado para ser uma plataforma robusta e escalável para publicação de dados geoespaciais em formatos padrão da indústria, como Web Map Service (WMS) e o Web Feature Service (WFS). 

## Login
Primeiro, acesse o geoserver e faça o login. 

![deploy-geoserver-login.png](/deploy-geoserver-login.png)

## Espaços de trabalho

Para configurá-lo primeiro precisamos criar um novo espaço de trabalho:

![deploy-geoserver-workjob-create.png](/deploy-geoserver-workjob-create.png)

![deploy-geoserver-workjob-details.png](/deploy-geoserver-workjob-details.png)
Para o exemplo criado, utilizamos os dados:
* Nome: geopixelcidades3
* URI*: https://homologacao.geopixel.com.br/geoserver/geopixelcidades3/

A URI é um endereço que, por hora, deve ser criado com base no nome atribuido e o endereço do geoserver. Ele será referenciado no armazém.

## Armazéns

Após a criação do espaço de trabalho precisamos configurar o armazém de dados, neste processo é estabelecido a conexão do banco de dados a ser utilizado para a publicação das camadas. 

![deploy-geoserver-armazem.png](/deploy-geoserver-armazem.png)

Selecione a opção do PostGIS

![deploy-geoserver-armazem-postgis.png](/deploy-geoserver-armazem-postgis.png)

Informe os valores de conexão ao banco de dados.

![deploy-geoserver-armazem-database.png](/deploy-geoserver-armazem-database.png)

Clique em "Guardar".

## Camadas

Após a criação do espaço de trabalho e a conexão com o nosso banco de dados, realizaremos a publicação de uma camada. 

![deploy-geoserver-layers.png](/deploy-geoserver-layers.png)

Selecione o armazém criado para publicar suas camadas

![deploy-geoserver-layers-armazem.png](/deploy-geoserver-layers-armazem.png)

Escolha a camada a ser publicada e clique em "Publicar"
![deploy-geoserver-layers-publish.png](/deploy-geoserver-layers-publish.png)

Nas configurações da camada é muito importante definir o retângulo envolvente, que se refere a uma caixa retangular que delimita a área geográfica coberta pela camada. Essa caixa é definida por um conjunto de coordenadas geográficas que representam os limites da área de interesse. 

Para realizar essa configuração, desça a página e marque a opção “**Calcular a partir dos dados**” e “**Calcular a partir dos limites nativos**”. Essa configuração nos permite utilizar os dados definidos dos nossos temas no banco de dados. 

![deploy-geoserver-layers-publish-config.png](/deploy-geoserver-layers-publish-config.png)
 
Após guardar os dados, devemos fazer o mesmo processo de publicação de camadas com todas as camadas nas quais desejamos utilizar. 

## POSSÍVEIS SOLUÇÕES DE PROBLEMAS NA PUBLICAÇÃO 

### `Camadas não aparecem ao ser ativadas no menu camadas.`

Solução: Verificar se a camada está publicada, verificar se o tema escolhido possuí dados na coluna geométrica.  

### `BAD REQUEST Request Header is too Large `

Este problema ocorre devido a url ultrapassar os limites de tamanho do cabeçalho inserido na requisição.  

Solução: Podemos configurar aumentando o tamanho do header. Para configurar podemos acessar o servidor remoto pelo Winscp e abrir o arquivo server.xml localizado em /opt/tomcat/conf  e adicionar essa configuração: 

maxHttpHeaderSize="65536" 

![deploy-tomcat-config-header-size.png](/deploy-tomcat-config-header-size.png)

# Anexos

Queries de exemplo para migração da tabela app_param do servidor L1 para Homologação: 


> update app_param
 set url = 'https://homologacao.geopixel.com.br/geoserver/geopixelcidades3/wms' 
 where url = 'https://l1.geopx.com.br/geoserver_gisweb_poc/Platform_GPX/wms' 
 or url = 'https://homologacao.geopixel.com.br/geoserver/Platform_GPX/wms'; 
