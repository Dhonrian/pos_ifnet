---
title: Consulta monitoramento
description: Endpoints disponíveis e como usar para consultar dados no monitoramento
published: true
date: 2024-12-11T19:43:48.754Z
tags: monitoramento, alvará, processo, api
editor: markdown
dateCreated: 2024-12-11T19:43:45.145Z
---

![](https://wiki.flow.geopixel.com.br/template_geo/geopixel_logo_2022.png)

# Introdução

Alguns novos endpoints foram implementados para consulta de dados de processos, abaixo eles serão descritos.

É importante frisar que todas as respostas seguem o seguinte formato, alterando se apenas o campo **data**:

```JSON
{
	"msg": "dados recuperados",
	"data": "dados a serem utilizados",
  "timestamp": "horário da resposta"
}
```

## Requerimento de um processo

Para recuperar o requerimento (conhecido como form_data na tabela do fluxo) é utilizado o caminho `/process/formData` passando um `processId`como parâmetro.

O campo da resposta **data** será um JSON do requerimento.

O requerimento do fluxo tem o seguinte formato onde cada conjunto representa um **input** do HTML:
```JSON
{
  "name": "nome do campo",
  "value": "valor do campo"
}
```


![image-20241206-192445.png](/consulta-monitoramento/image-20241206-192445.png) exemplo de resposta


## Documentos de um processo

Para saber os documentos anexados à um processo é utilizado o caminho `/process/documents` que recebe um `processId` como parâmetro.

Aqui o **data** será uma lista com os metadados de todos os arquivos anexados ao processo: 

```JSON
{
	data: [
    {
  		"doctype": "nome do tipo de documento",
      "name": "nome do arquivo",
      "doc_id": 123
    }
  ]
}
```
Exemplo de resposta com os documentos disponíveis em um processo
![image-20241211-143408.png](/consulta-monitoramento/image-20241211-143408.png)



## Receber apenas um documento

A partir dos docs id é possível requisitar um documento específico. Para isso é usado o caminho `/process/document` utilizando o parâmetro `documentId`

O **data** da resposta conterá o **file_name**, **hash_name**, **doc_id**, **extension**	e o **base64** do arquivo:

```JSON
{
	data: [
    {
      "base64": "base64",
      "file_name": "arquivo"
      "hash_name": "arquivo_g590h9.pdf",
      "extension": ".pdf",
      "doc_id": 123
    }
  ]
}
```

Um exemplo de resposta ![imagem_(2).png](/consulta-monitoramento/imagem_(2).png)