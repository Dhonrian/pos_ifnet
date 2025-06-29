---
title: Configurações de Aplicação
description: Explicação para as variáveis definidas no arquivo application.json.
published: true
date: 2024-04-24T14:19:49.403Z
tags: ambiente v3, configuração v3, geocidades, v3, ambiente, json, application, application.json, cidades
editor: markdown
dateCreated: 2024-04-23T15:15:16.174Z
---

# Arquivo de Configuração da Aplicação
Your content here


## Definições das Variáveis

**urlClient**: URL do cliente que irá consumir o servidor em execução.
**urlServer**: URL para a api do servidor em execução.

**smtpHost**: -
**serverSmtpConfig**: -
**smtpPort**: -
**smtpUserName**: -
**smtpPassword**: -

**profileForNewUsers**: Perfil padrão inicialmente atribuído a novos usuários.

**geoserverHost**: URL do endpoint wms do Geoserver.
**geoserverWorkspace**: -

**adminEmail**: -


**cityName**: -
**cityLogo**: -
**footerLogo**: -
**gpxLogo**: -
**backgroundInterface**: -
**pgvFile**: -

**enableAnonymousLogin**: -
**anonymousLogin**: -
**anonymousPassword**: -
**anonymousProfileName**: -

## Exemplo de Configuração
Configuração para o tenant Caçapava no ambiente local.

```json
// application.json
{
    "urlClient": "http://cacapava.localhost:4000",
    "urlServer": "http://localhost:8080/server",
    "smtpHost": "smtp.office365.com",
    "serverSmtpConfig": "mail.smtp.starttls.enable=true",
    "smtpPort": 587,
    "smtpUserName": "sistema@geopixel.com.br",
    "smtpPassword": "y,oV3BeWzq!1",
    "profileForNewUsers": "Público",
    "geoserverHost": "https://l1.geopx.com.br/geoserver_gisweb_poc/Platform_GPX/wms",
    "geoserverWorkspace": "Platform_GPX",
    "adminEmail": "barbara.port@geopixel.com.br",
    "gpxLogo": "/images/logo.png",
    "cityLogo": "/images/brasao.png",
    "pgvFile": "/pgv/pgv_json.json",
    "cityName": "São José dos Campos",
    "footerLogo": "/images/footerLogo.svg",
    "backgroundInterface": "/images/interface.jpg",
    "enableAnonymousLogin": true,
    "anonymousLogin": "anonimo",
    "anonymousPassword": "geopixel_anonimo",
    "anonymousProfileName": "Anônimo",
    "googleApiKey": "",
    "serpro.enabled": false,
    "serpro.client.id": "?",
    "serpro.client.secret": "?",
    "serpro.path.token": "",
    "serpro.path.cpf": "",
    "serpro.path.cnpj": "",
    "srs.planar": 31983,
    "srs.geographic": 4326,
    "srs.map": 3857,
    "map.center.longitude": -45.687815,
    "map.center.latitude": -23.129639,
    "map.zoomLevel": 12,
    "panoramic.uri": "https://cacapava.geopx.com.br/panoramica",
    "movidesk.corporateName": "Plataforma - Testes DEV - (Por favor Cancelar)",
    "movidesk.relationships": "1881717838",
    "movidesk.path.persons": "https://api.movidesk.com/public/v1/persons",
    "movidesk.path.tickets": "https://api.movidesk.com/public/v1/tickets",
    "movidesk.token": "972acd91-2519-49ef-af33-320bdbc3bfcd",
    "movidesk.path.fileUpload": "https://api.movidesk.com/public/v1/ticketFileUpload",
    "movidesk.adminId": "",
    "movidesk.publicId": "",
    "movidesk.anonymousId": "",
    "intervalForRequests": 3,
    "rateLimitingMaxRequestsWithToken": 1000,
    "rateLimitingMaxRequestsWithoutToken": 25,
    "blockTime": 120,
    "maxLoginAttemptsPerUser": 5,
    "userBlockInterval": 30,
    "userBlockTimeUnit": "MINUTES",
    "allowReplaceAllImportType": false,
    "service.converter.dwg": "https://l1.geopx.com.br/geopixelcidades-21_server/rest/converter/convert",
    "keystore": "/certificate/certificate-pkcs12.p12",
    "keystore.password": "geopixel@qwert",
    "has.gov": false,
    "pdf.resource": "",
    "image.file.path": "images/brasao.png",
    "geocoding.tableName": "enderecos_cacapava",
    "geocoding.addressColumn": "logradouro",
    "geocoding.addressNumberColumn": "numero",
    "geocoding.geometryColumn": "geom",
    "geocoding.neighborhoodColumn": "bairro",
    "ldap.urls": "ldap://localhost:10389",
    "ldap.base": "ou=User,dc=example,dc=com",
    "ldap.username": "cn=qauser,ou=User,dc=example,dc=com",
    "ldap.password": "qa1234",
    "ldap.attribute.identifier": "cn",
    "authentication.privateKey": "/privateKey/privateKey.pem",
    "authentication.publicKey": "/publicKey/publicKey.pub",
    "mosaicURL": "https://demonstracao.geopixel.com.br/ImageLayer/image/cacapava/",
    "monitoring.theme.columns.name": "{\"ocurrenceClassColumn\": \"cd_class\",\"cycleColumn\": \"ciclo\",\"dateColumn\": \"cd_date\",\"profileColumn\": \"perfil_responsabilidade\", \"done\": \"Feito\",\"userid\": \"Userid\"}",
    "enableGeoportalLogin": false,
    "geoportalLogin": "geopixel_geoportal",
    "geoportalPassword": "geoportal"
}
```
