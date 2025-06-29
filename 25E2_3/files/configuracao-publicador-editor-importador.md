---
title: Configuração publicador, importador e editor no arquivo de configuração
description: 
published: true
date: 2025-02-21T12:28:28.253Z
tags: 
editor: markdown
dateCreated: 2025-02-21T12:28:28.253Z
---

# Guia de Configuração do Geoserver

Este documento orienta sobre como configurar o arquivo de configuração do projeto para que cada cidade utilize valores personalizados. Essa configuração é essencial para o funcionamento do **Publicador de Temas**, que além de publicar o tema, também publica a camada no **GeoServer**, com base nas informações fornecidas.

## Parâmetros de Configuração

Ajuste os seguintes parâmetros no arquivo de configuração do seu projeto:

```json
{
    "geoserverHost": "https://l1.geopx.com.br/geoserver_gisweb_poc/Platform_GPX/wms",
    "geoserverWorkspace": "geopixelcidades3_dev",
    "geoserverLink": "https://homologacao.geopixel.com.br",
    "geoserverName": "geoserver",
    "geoserverDatastore": "geopixelcidades3_dev",
    "geoserverAuth": "admin:geoserver"
}
```

## Descrição dos Parâmetros

- **`geoserverHost`**: URL do serviço WMS do GeoServer.
- **`geoserverWorkspace`**: Nome do workspace utilizado no GeoServer.
- **`geoserverLink`**: URL base do GeoServer.
- **`geoserverName`**: Identificação do serviço do GeoServer.
- **`geoserverDatastore`**: Nome do datastore dentro do workspace configurado.
- **`geoserverAuth`**: Credenciais de autenticação no formato `usuário:senha`.

## Aplicação da Configuração

Certifique-se de que o arquivo de configuração está devidamente atualizado antes de iniciar o serviço. Em caso de dúvidas, consulte a equipe de implantação.

---

Caso haja necessidade de ajustes futuros, favor entrar em contato com o time responsável pelo GeoServer.

