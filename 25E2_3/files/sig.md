---
title: POC - SIG
description: Documentação de como demonstrar cada item do SIG
published: true
date: 2023-11-29T20:29:09.946Z
tags: poc sig cidades geopixelcidades funcionalidades demonstração prova conceito
editor: markdown
dateCreated: 2023-11-23T17:00:39.994Z
---

# Prova de Conceito

Esta página contém informações sobre como demonstrar as capacidades e funcionalidades do SIG durante uma Prova de Conceito (POC).

## Sumário
 - [Checklist Prévio](#checklist)
 - [Itens não funcionais](#nao-funcionais)
	- [Características SaaS](#caracteristicas-saas)
	- [Características de Infraestrutura do Sistema](#caracteristicas-infraestrutura)
	- [Segurança](#seguranca)
	- [Base de Dados](#base-dados)
 - [Itens funcionais](#funcionais)


<a id="checklist"></a>
## Checklist Prévio

Todos estes itens devem ser verificados pelo menos uma semana antes da POC.

- [ ] Verificar se a máquina de demonstração está acessível: https://demonstracao.geopixel.com.br/gisweb_poc/login.html (IP 10.0.0.142)

- [ ] Garantir que os seguintes navegadores estejam instalados na máquina onde a POC será demonstrada: Google Chrome, Mozilla Firefox e Microsoft Edge.

<a id="nao-funcionais"></a>
## Itens não funcionais

Nesta sessão estão detalhadas as orientações de como comprovar cada item não funcional da POC.

### CARACTERÍSTICAS DE INFRAESTRUTURA DO SISTEMA

Item | Requisito | Como demonstrar
---- | ----------| -----
1 | A plataforma deverá ser online (100% Web) sem limite de acessos e usuários, compatível, no mínimo, com os navegadores de internet Google Chrome, Mozilla Firefox e Windows Edge. | Abrir a [aplicação](https://demonstracao.geopixel.com.br/gisweb_poc/login.html) em cada um dos navegadores e executar o processo de autenticação.
2 |O sistema deverá funcionar em Sistemas Gerenciadores de Banco de Dados (SGBD) de mercado, que atendam a especificação do SQL-ANSI e possuam as seguintes características: suporte a dados geográficos, mecanismos de segurança para impedir acessos não autorizados, mecanismos de transação e de backup. | Se conectar ao servidor de demonstração através do DBeaver utilizando o IP 10.0.0.142, abrir a funcionalidade de consulta, e executar o seguinte comando SQL: **select version()** e **select postgis_version()**.

---
**Item 1**
- [ ] A plataforma deverá ser online (100% Web) sem limite de acessos e usuários, compatível, no mínimo, com os navegadores de internet Google Chrome, Mozilla Firefox e Windows Edge.

**Como demonstrar:**

Abrir a [aplicação](https://demonstracao.geopixel.com.br/gisweb_poc/login.html) em cada um dos navegadores e executar o processo de autenticação.

---
**Item 2**
- [ ] O sistema deverá funcionar em Sistemas Gerenciadores de Banco de Dados (SGBD) de mercado, que atendam a especificação do SQL-ANSI e possuam as seguintes características: suporte a dados geográficos, mecanismos de segurança para impedir acessos não autorizados, mecanismos de transação e de backup.

**Como demonstrar:**

Se conectar ao servidor de demonstração através do DBeaver utilizando o IP 10.0.0.142, abrir a funcionalidade de consulta, e executar o seguinte comando SQL: **select version()** e **select postgis_version()**.

---

# Sistema de Informação Geográfica

<a id="caracteristicas-saas"></a>
## Características SaaS

### Item 1
> O licenciamento do sistema será realizado na modalidade de Software como serviço (SaaS).
{.is-info}

> {.is-success}

### Item 2
> Ficará a cargo da CONTRATADA garantir ajustes no ambiente onde o sistema será implantado levando em consideração utilização de dados ou acesso ao sistema.
{.is-info}

> {.is-success}

### Item 3
> Os dados e informações não estáticas, armazenados no sistema deverão dispor de backup diário incremental e backup semanal completo de responsabilidade da CONTRATADA.
{.is-info}

> {.is-success}

<a id="caracteristicas-infraestrutura"></a>
## Características de Infraestrutura

### Item 1
> A plataforma deverá ser online (100% Web) sem limite de acessos e usuários, compatível, no mínimo, com os navegadores de internet Google Chrome, Mozilla Firefox e Windows Edge.
{.is-info}

> Abrir a [aplicação](https://demonstracao.geopixel.com.br/gisweb_poc/login.html) em cada um dos navegadores e executar o processo de autenticação. {.is-success}

### Item 2
> O sistema deverá funcionar em Sistemas Gerenciadores de Banco de Dados (SGBD) de mercado, que atendam a especificação do SQL-ANSI e possuam as seguintes características: suporte a dados geográficos, mecanismos de segurança para impedir acessos não autorizados, mecanismos de transação e de backup.
{.is-info}

> Se conectar ao servidor de demonstração através do DBeaver utilizando o IP 10.0.0.142, abrir a funcionalidade de consulta, e executar o seguinte comando SQL: **select version()** e **select postgis_version()**. {.is-success}

### Item 3

> O sistema deverá estar baseado nos padrões de interoperabilidade estabelecidos pelo OGC (Open Geospatial Consortium). {.is-info}

> {.is-success}

### Item 4

> O sistema deverá ser capaz de acessar dados legados de outros sistemas, gerenciados por SGBD que sigam o padrão SQL-ANSI, permitindo no mínimo acesso aos SGBD PostgreSQL versão 9 ou superior, com extensão PostGIS ou Oracle versão 10G ou superior ou SQL Server 2008 ou posterior, acessíveis através da Internet ou Intranet da Prefeitura. O acesso deve ser feito em tempo real, sem a necessidade de transferência de tabelas, bastando a liberação do acesso às tabelas legadas e a definição dos dicionários de dados correspondentes. {.is-info}

> {.is-success}

### Item 5

> O sistema deverá ser capaz de acessar dados legados através de serviços Web, caso disponíveis, utilizando os padrões SOAP ou REST, garantindo a recuperação de dados em tempo real, a partir das chaves de acesso específicas disponibilizadas para os referidos serviços.  {.is-info}

> {.is-success}

### Item 6

> O Sistema de Informação Web a ser fornecido deverá permitir a integração com o sistema tributário legado do município. {.is-info}

> {.is-success}

<a id="seguranca"></a>
## Segurança

### Item 1

> O servidor que hospedará a plataforma deverá estar configurado com somente a porta de acesso exposta (via navegador por https), sendo protegido por um Firewall/IDS/IPS de forma igual,
tanto para conexões internas como externas, e mantido todos os
aplicativos e sistema operacional atualizados com correções e
patches de segurança disponíveis.
{.is-info}

>  {.is-success}


### Item 2

> A forma de acesso deverá ser feita por meio de um servidor web que deverá, obrigatoriamente, utilizar uma conexão segura criptografada com protocolo SSL/TLS.
{.is-info}

>  {.is-success}

### Item 3

> O sistema deverá ter sido submetido a testes de segurança cibernética, garantindo no mínimo ser seguro quanto às principais formas de ataque preconizados pelo Open Security Application Project (OWASP TOP 10). A comprovação deverá ser realizada através de certificado ou documento equivalente emitido pela entidade homologadora responsável.
{.is-info}

>  {.is-success}


<a id="base-dados"></a>
## Base de Dados

### Item 1

> Os dados dos mapas georreferenciados devem ser armazenados no Banco de dados utilizando o padrão OGC SFS, para garantir a interoperabilidade do sistema
{.is-info}

>  {.is-success}

### Item 2

> As imagens georreferenciadas deverão ser mantidas utilizando exclusivamente formatos abertos (como por exemplo GeoTIFF), armazenadas no banco de dados ou sistema de arquivos, como um mosaico contínuo de toda a região. Quando aplicável, o armazenamento deverá conter a multiresolução associada.
{.is-info}

>  {.is-success}

### Item 3

> Para apresentação de imagens, o portal deverá ser capaz de acessar repositórios de imagens multiresolução, de tamanho 256x256 pixels, cobrindo toda área de abrangência do município com capacidade de mostrar imagens com resolução original, nos formatos jpg ou png, compatível com o protocolo OCG TMS ou “de facto” XYZ
{.is-info}

>  {.is-success}

### Item 4

> O sistema deverá permitir acesso a imagens armazenadas com mosaico multiresolução, no padrão XYZ, disponibilizados como serviços Web, abertos ou mediante licenciamento junto ao proprietário, tais como Open Street Map, Google, Bing entre outros.
{.is-info}

>  {.is-success}

### Item 5

> O sistema deverá permitir acesso a servidores, utilizando o padrão OGC WMS para imagens e mapas geográficos
{.is-info}

>  {.is-success}

### Item 6

> A plataforma para publicação de dados espaciais e aplicativos de mapeamento interativos para web, no servidor, deve ser capaz de realizar os serviços OWS (OGC Web Services, podendo utilizar MapServer 6.0 ou superior, ou GeoServer 2.6 ou superior.
{.is-info}

>  {.is-success}

### Item 7

> Os estilos de apresentação dos mapas deverão ser especificados utilizando os padrões definidos pelo OGC SLD (Style Layer Definition) ou similares
{.is-info}

>  {.is-success}