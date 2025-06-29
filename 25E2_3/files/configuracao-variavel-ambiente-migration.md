---
title: Configuração de variável de ambiente - Migrations
description: Tutorial de configuração de variável de ambiente para execução de migrations em ambientes de desenvolvimento 
published: true
date: 2023-12-18T11:29:44.755Z
tags: configuração, migration, migrations, variável, de, ambiente, variável de ambiente
editor: markdown
dateCreated: 2023-11-30T10:45:03.443Z
---

# Configuração de variável de ambiente para execução de migrations em contextos de desenvolvimento

Recentemente na V3, em decorrência de alguns problemas relacionados à migrações de dados, alteramos a estrutura e a forma como são realizadas as migrações para ambientes no geral e em ambientes de desenvolvimento. Diante disso, separamos as migrações em duas pastas: `common` e `development`.

As migrações que ficam dentro do escopo `common` são comuns a todos os bancos de dados, e se referem a alterações estruturais de tabelas, adição de colunas, índices, relacionamentos etc, que são necessárias para o correto funcionamento da V3. Essas migrações serão válidas para todos os bancos, independente dad cidade.

As migrações que ficam dentro do escopo `development` são as migrações que somente são utilizadas para auxílio do desenvolvedor, no momento do desenvolvimento. Normalmente essas migrações se referem à adição ou modificação de dados. Essas migrações não deverão ser executadas no ambiente de produção.

Em relação a este contexto, para que seja possível executar as migrações no ambiente de desenvolvimento (por esse ambiente entende-se os computadores dos desenvolvedores, o ambiente de testes e o ambiente de homologação), se faz necessária a configuração de uma variável de ambiente para que o Spring Boot consiga identificar que se encontra no contexto correto (ou perfil) e executar as migrations que estão em `development`. Para isso, caso você seja um desenvolvedor e esteja utilizando o sistema operacional Windows, siga os passos a seguir:

## 1. Clique no menu iniciar e pesquise por "Variáveis de ambiente"
![imagem_2023-11-30_075754439.png](/configuracao-variavel-de-ambiente/imagem_2023-11-30_075754439.png)

## 2. Clique na opção "Editar as variáveis de ambiente do sistema"
![imagem_2023-11-30_075950441.png](/configuracao-variavel-de-ambiente/imagem_2023-11-30_075950441.png)

## 3. Dentro da tela "Propriedades do sistema", na aba "Avançado", clique em "Variáveis de ambiente"
![imagem_2023-11-30_080058174.png](/configuracao-variavel-de-ambiente/imagem_2023-11-30_080058174.png)

## 4. No escopo das variáveis de sistema, clique em "Novo..."
![imagem_2023-11-30_080202299.png](/configuracao-variavel-de-ambiente/imagem_2023-11-30_080202299.png)

## 5. Como nome da variável, digite "spring_profiles_active" e como valor, digite "dev". Após isso clique em "OK"
![imagem_2023-11-30_080315780.png](/configuracao-variavel-de-ambiente/imagem_2023-11-30_080315780.png)

## 6. Pronto, a variável está configurada. Após isso só clicar em "OK" novamente, até fechar todas as telas de configuração.
![imagem_2023-11-30_080440786.png](/configuracao-variavel-de-ambiente/imagem_2023-11-30_080440786.png)

## 7. Reinicie sua IDE, e rode o server. O sistema deverá ser capaz agora de enxergar ambos os contextos `development` e `common`. Isso pode ser observado no log de inicialização do Spring
![imagem_2023-11-30_081110379.png](/configuracao-variavel-de-ambiente/imagem_2023-11-30_081110379.png)

## Extra - Configuração das variáveis diretamente na IDE
Também é possível configurar a variável de ambiente diretamente na IDE, sem que seja necessário seguir os passos anteriormente. Isso nos traz uma facilidade no momento de rodar algum contexto específico, sem que precisemos necessariamente modificar a variável para isso. Dado esse cenário, seguem os tutoriais de como configurar em cada IDE:

### IntelliJ

#### 1. Abrir as configurações de execução
![imagem_2023-12-15_080651144.png](/configuracao-variavel-de-ambiente/imagem_2023-12-15_080651144.png)

#### 2. Adicionar uma nova configuração do tipo application
![imagem_2023-12-15_080752498.png](/configuracao-variavel-de-ambiente/imagem_2023-12-15_080752498.png)

#### 3. Nomear a configuração a seu gosto. Sugiro colocar um nome que remeta se esse configuração possui, ou não, a variável.

![imagem_2023-12-15_081614541.png](/configuracao-variavel-de-ambiente/imagem_2023-12-15_081614541.png)

#### 4. No campo Main Class, selecione a classe `PlatformApplication.java`
![imagem_2023-12-15_081633987.png](/configuracao-variavel-de-ambiente/imagem_2023-12-15_081633987.png)

#### 5. Clique na opção `Modify options` e marque a opção `Add dependencies with "provided" scope do classpath`
![imagem_2023-12-15_081646277.png](/configuracao-variavel-de-ambiente/imagem_2023-12-15_081646277.png)

#### 6. No campo `Environment variables` configure a variável de ambiente, separando a chave/valor por "=". Ficará assim `spring_profiles_active=dev`.
![imagem_2023-12-15_081705327.png](/configuracao-variavel-de-ambiente/imagem_2023-12-15_081705327.png)

#### 7. Agora é só aplicar as alterações e pronto, você terá uma configuração específica com a variável de ambiente, diretamente no IntelliJ. Sugiro que crie outra configuração, mas sem a variável `dev`, pois assim você conseguirá rodar ambos os contextos de maneira fácil e rápida!
![imagem_2023-12-15_081826820.png](/configuracao-variavel-de-ambiente/imagem_2023-12-15_081826820.png)

### VSCode

#### Abrir as configurações de execução
Acesse os menus: `Run > Open Configurations`
![01-configuracoes-vscode.png](/01-configuracoes-vscode.png)

#### Configure a variável de ambiente
Será aberto o arquivo `lauch.json`, basta adicionar a configuração de profile no parâmetro de argumentos (`args`) na configuração existente para o `Java`.
> "args": "--spring.profiles.active=dev",

![02-definir-profile-active.png](/02-definir-profile-active.png)