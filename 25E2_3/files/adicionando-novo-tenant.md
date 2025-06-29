---
title: Adicionando um Novo Tenant
description: Passos para a adição de um novo Tenant.
published: true
date: 2024-04-29T19:37:38.501Z
tags: configuração v3, configuração, v3, multi-tenant, tenant, multitenant, multi tenant, multi, adicionar, adição
editor: markdown
dateCreated: 2024-04-23T14:34:14.049Z
---

# Adicionando um Novo Tenant

Para adicionarmos um novo tenant, precisamos adicionar configurações e realizar alterações apenas no projeto do servidor.

## Alterações em Código

Devemos adicionar o nome do novo tenant a um enumerador de tenants.

### Adicionando o Novo Tenant ao Enumerador de Tenants

Para isto, adicionamos ao enum `PrefectureTenant` do arquivo `src/main/java/br/com/geopixel/platform/config/multitenant/PrefectureTenant.java` o nome da cidade no formato **SCREAMING_SNAKE_CASE** sem acentos.

```java
// src/main/java/br/com/geopixel/platform/config/multitenant/PrefectureTenant.java

public enum PrefectureTenant {
    CACAPAVA,
    SAO_SEBASTIAO, // Tenants já existentes
    ...

    NOVO_TENANT, // Novo tenant adicionado

    ...
    DEFAULT,
    ;

    ...
}
```

## Configurações do Novo Tenant

Devemos adicionar os arquivos de configuração do novo tenant.

### Criando a Pasta de Configuração do Novo Tenant

Para isto, criamos no diretório `resources/server` uma nova pasta com o nome da cidade no formato `snake_case` sem acentos.

```bash
.
└── /resources
    └── /server
        ├── /cacapava
        ├── /sao_sebastiao # Tenants já existentes
        ├── ...
        └── "/novo_tenant" # Novo tenant adicionado
```

### Adicionando os Arquivos de Configuração

As configurações são as mesmas da arquitetura pré multi tenant.

Então criamos uma nova pasta `config` dentro da pasta de configuração que criamos no tópico [Criando a Pasta de Configuração do Novo Tenant](#criando-a-pasta-de-configura%C3%A7%C3%A3o-do-novo-tenant).

```bash
.
└── /resources
    └── /server
        └── /novo_tenant
            └── "/config" # Pasta de configurações
```

#### {.tabset}
##### Configurações de Banco de Dados

Dentro da pasta `config` criada no tópico [Adicionando os Arquivos de Configuração](#adicionando-os-arquivos-de-configura%C3%A7%C3%A3o), criamos um arquivo chamado `database.json`.

```bash
.
└── /resources
    └── /server
        └── /novo_tenant
            └── /config
                └── "database.json" # Arquivo de configuração do banco de dados
```

Então inserimos as configurações do banco de dados do novo tenant seguindo as orientações expostas na documentação sobre a configuração de banco de dados em [Configuração de Banco de Dados](/v3/arquivos-de-configuração/database).

##### Configurações de Aplicação

Dentro da pasta `config` criada no tópico [Adicionando os Arquivos de Configuração](#adicionando-os-arquivos-de-configura%C3%A7%C3%A3o), criamos um arquivo chamado `application.json`.

```bash
.
└── /resources
    └── /server
        └── /novo_tenant
            └── /config
                └── "application.json" # Arquivo de configuração da aplicação
```

Então inserimos as configurações do novo tenant seguindo as orientações expostas na documentação sobre a configuração de aplicação em [Configuração de Aplicação](/v3/arquivos-de-configuração/application).

##### Certificate

Também há na pasta do tenant uma outra dedicada ao certificado daquele tenant, então devemos também criá-la para o novo tenant e adicionar seu arquivo de certificado.

```bash
.
└── /resources
    └── /server
        └── /novo_tenant
            └── "/certificate" # Pasta para o arquivo de certificado
                └── "arquivo-de-certificado.ext" # Arquivo de certificado do tenant
```

##### Arquivos de Imagens

Há também uma série de arquivos de imagens compartilhadas na aplicação, como ícones, backgrounds, entre outras, e há também imagens específicas do tenants. Para elas, dedicamos 2 pastas `image` e `images`, portanto também devemos criá-las na pasta do tenant e dentro dela popular com as imagens referentes ao tenant.

```bash
.
└── /resources
    └── /server
        └── /novo_tenant
            ├── "/image"
            └── "/images"
```

##### Arquivos Relacionados ao PGV

Há uma pasta reservada a um arquivo de configuração do PGV a qual também deve ser criada na pasta do novo tenant e dentro dela o arquivo de configuração do PGV daquele tenant.

```bash
.
└── /resources
    └── /server
        └── /novo_tenant
            └── "/pgv"
                └── "arquivo-de-configuração-pgv.json"
```

##### Private Key e Public Key

Temos pastas reservadas para algumas chaves criptográficas utilizadas para a aplicação, um par de chave pública e privada encontradas em pastas dedicadas que também devemos criá-las para o novo tenant e populá-las com seus respectivosarquivos.

```bash
.
└── /resources
    └── /server
        └── /novo_tenant
            └── "/privateKey"
                └── "privateKey.pem"
            └── "/publicKey"
                └── "publicKey.pub"
```

##### Arquivos de Configuração de Reports

Temos uma pasta reservada para arquivos que relacionados à feature de reports, a qual também devemos adicionar ao tenant.

```bash
.
└── /resources
    └── /server
        └── /novo_tenant
            └── "/reports"
```

##### Arquivos de Schema

Temos uma pasta dedicada a arquivos de schemas utilizados em algumas features pela aplicação, a qual também devemos criá-la e populá-la com os schemas do tenant.

```bash
.
└── /resources
    └── /server
        └── /novo_tenant
            └── "/schemas"
                └── "arquivo-de-schema.ext"
```

##### Outros Arquivos

Demais arquivos relacionados ao tenant podem ser inseridos dentro da pasta específica do tenant criada no tópico [Adicionando os Arquivos de Configuração](#adicionando-os-arquivos-de-configura%C3%A7%C3%A3o).

```bash
.
└── /resources
    └── /server
        └── /novo_tenant
            ├── /config
            └── "/pasta-para-outros-arquivos" # Pasta para organizar outros arquivos
                └── "outros-arquivos.ext" # Arquivo usado pelo tenant
```

### Criando a Pasta para Arquivos Temporários do Novo Tenant

Para isto, criamos no diretório `temp` uma nova pasta com o nome da cidade no formato `kebab-case` sem acentos.

```bash
.
└── /temp
    ├── /bertioga
    ├── /cacapava
    └── "/novo_tenant" # Pasta do novo tenant
```

Por fim, dentro da pasta criada, criamos uma nova pasta de nome `reports` e dentro dela criamos um arquivo chamado `.gitkeep` para versionarmos as novas pastas.

```bash
.
└── /temp
    ├── /bertioga
    ├── /cacapava
    └── /novo_tenant # Pasta do novo tenant
        └── "/reports" # Pasta onde serão salvos os arquivos de reports temporários do tenant
            └── ".gitkeep" # Arquivo para manter a estrutura de pasta versionada
```