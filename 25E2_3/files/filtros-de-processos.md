---
title: Filtros de Processos
description: Filtros de Processos são os filtros encontrados na página da tabela de processos, capazes de permitir ao usuário personalizar sua busca de processos sendo exibidos
published: true
date: 2024-10-17T18:21:28.759Z
tags: alvara, fluxo, processo, processos, filtro, filtros, botões
editor: markdown
dateCreated: 2024-10-16T14:45:35.401Z
---

# Filtros de Processos
Os filtros de Processos são campos disponíveis aos usuários onde permitem a ele realizar uma busca ou filtragem dos processos disponíveis na tabela de processos de acordo com os campos dos filtros preenchidos.

![filtros1.png](/fluxo/filtros1.png){.align-center}

Os filtros se encontram logo acima da tabela. Para se utilizar os filtros, o usuário necessita preencher os campos que deseja aplicar ao filtro e clicar no botão "Filtrar"

## Configuração
Os filtros são configurados no banco de dados de cada prefeitura, ou seja, cada prefeitura pode ter um filtro único e exclusivo que atenda as suas necessidades.
Eles funcionam por perfil e por contexto, para um dado perfil, ele pode ter associado a ele até dois filtros diferentes, um para cada contexto disponível, PROCESS e REQUEST, sendo **obrigatório** a existência do filtro do tipo PROCESS, do contrário, nenhum processo será exibido ao usuário.
Os filtros podem ser configurados na tabela "process_filter", conforme abaixo:

![filtros2.png](/fluxo/filtros2.png){.align-center}

### Descrição das colunas
### Descrição das colunas {.tabset}
#### id
Identificação única da linha no banco, valor gerado automáticamente
#### profile_id
ID do perfil ao qual aquele filtro será associado
#### filter_context
Contexto do filtro, os valores permitidos são PROCESS e REQUEST

****Note que, no momento, apenas filtros do tipo PROCESS são utilizados pelo sistema.***
#### filter_json
JSON que descreve o filtro a ser exibido ao usuário


## JSON do filtro
O filtro armazenado no banco é um texto JSON que descreve a query utilizada e os componentes que preenchem os valores dessa query. Abaixo, um breve exemplo da estrutura base de um JSON:

>     {
>         "defaultQuery": "(status != 1)",
>         "componentsRelation": "(<1> AND (<2>) AND <3>)",
>         "components": [
>         ...
>         ]
>     }
{.is-info}

## JSON do filtro {.tabset}
### defaultQuery
Query utilizada como "where clause" na busca pelos processos. Este valor é utilizado quando nenhum componente do filtro é usado pelo usuário, resultando na seguinte query utilizada para buscar no banco de dados dos processos "select * from tab_process where \<defaultQuery>"
### componentsRelation
Query utilizada como "where clause" na busca pelos processos. Este valor é utilizado quando o usuário usa ao menos um dos componentes do filtro.
Dentro da query de componentsRelation, para utilizar o valor de um componente na query, deve-se utilizar a identificação do componente dentro da query, conforme no exemplo acima, com os valores <1>, <2>, etc.
### components
É uma lista de objetos onde cada um representa um componente sendo utilizado no filtro.

## Componentes
Os componentes são os campos disponíveis ao usuário no filtro, onde o mesmo pode utilizar para filtrar os processos a serem exibidos.
Para cada componente abaixo, com exceção do Option, todos possuem mais uma chave opcional chamada componentProperties.
Essa chave, permite passar propriedades particulares como atributos ou estilos ao componente, podendo ser utilizado da seguinte forma:

>     {
>         ...
>         "componentProperties": {
>             "styles": {
>                 "width": "20%"
>             },
>             "attributes": {
>                 "onclick": "console.log('print')"
>             }
>         },
>         ...
>     }

Dentro de styles, qualquer propriedade CSS pode ser utilizada, e dentro de attributes qualquer propriedade HTML pode ser utilizada.

Os componentes permitidos atualmente são os descritos abaixo

### Componentes {.tabset}
#### Checkbox
>         {
>             "componentType": "CHECKBOX",
>             "componentId": 1,
>             "valueType": "QUERY",
>             "label": "Apenas meus processos",
>             "query": "assigned_user = <SESSION_USER_ID>",
>             "unusedQuery": "1 = 1",
>             "defaultChecked": false
>         }
##### Chaves {.tabset}
###### componentType
Tipo do valor: string

Tipo do componente, para checkboxes, o valor obrigatóriamente deve ser "CHECKBOX"
###### componentId
Tipo do valor: number

ID numérico ÚNICO do componente DENTRO do filtro, necessário para utilizar o componente na query da chave "relationsComponent".
###### valueType
Tipo do valor: string

Tipo do valor daquele componente, para checkboxes, o valor deve ser obrigatóriamente do tipo "QUERY"
###### label
Tipo do valor: string

Texto que será apresentado na label ao lado da checkbox
###### query
Tipo do valor: string

O fragmento da query ao qual o componente representa, valor este que será substituído dentro de "relationsComponent". Este valor será usado para quando o checkbox estiver selecionado pelo usuário;
###### unusedQuery
Tipo do valor: string

O fragmento de query que será utilizado para caso o usuário não selecione o checkbox.
###### defaultChecked
Tipo do valor: boolean

Estado inicial do checkbox

#### Select
>     {
>                 "componentType": "SELECT",
>                 "componentId": 2,
>                 "query": "<value>",
>                 "unusedQuery": "1 = 1",
>                 "valueType": "QUERY",
>                 "componentProperties": {
>                     "styles": {
>                         "width": "20%"
>                     }
>                 },
>                 "options": []
>     }

##### Chaves {.tabset}
###### componentType
Tipo do valor: string

Tipo do componente, para selects, o valor obrigatóriamente deve ser "SELECT"
###### componentId
Tipo do valor: number

ID numérico ÚNICO do componente DENTRO do filtro, necessário para utilizar o componente na query da chave "relationsComponent".
###### valueType
Tipo do valor: string

Tipo do valor daquele componente, para checkboxes, o valor deve ser obrigatóriamente do tipo "QUERY"
###### label
Tipo do valor: string

Texto que será apresentado na label ao lado da checkbox
###### query
Tipo do valor: string

O fragmento da query ao qual o componente representa, valor este que será substituído dentro de "relationsComponent". Este valor será usado para quando o checkbox estiver selecionado pelo usuário;
###### unusedQuery
Tipo do valor: string

O fragmento de query que será utilizado para caso o usuário não selecione o checkbox.
###### defaultChecked
Tipo do valor: boolean

Estado inicial do checkbox
###### options
Tipo do valor: Lista de Option

A lista de objetos do tipo Option que descrevem as opções daquele select

#### Option
>     {
>         "value": "status != 1",
>         "label": "Todos os Processos",
>         "defaultSelected": true,
>         "disabled": false
>     }
  
##### Chaves {.tabset}
###### value
Tipo do valor: string

Valor que aquela opção representa
###### label
Tipo do valor: string

Texto que será exibido ao usuário para identificar a opção
###### defaultSelected
Tipo do valor: boolean

Valor booleano que define se a opção deverá começar selecionada ou não. Caso existe mais de uma opção com o valor "true", a última encontrada na lista será a selecionada
###### disabled
Tipo do valor: boolean

Valor booleano que define se a opção poderá ser selecionada pelo usuário ou não

#### Input
>     {
>       "componentType": "INPUT",
>       "componentId": 4,
>       "valueType": "STRING",
>       "query": "insc_municipal IN (SELECT insc_fisico FROM vw_integracaosig_imovel WHERE imovel_bairro like <%value%>)",
>       "unusedQuery": "1 = 1",
>       "componentProperties": {
>         "styles": {
>           "width": "40%"
>         },
>         "attributes": {
>           "placeholder": "Loteamento"
>         }
>       }
>     }
##### Chaves {.tabset}
###### componentType
Tipo do valor: string

Tipo do componente, para inputs, o valor obrigatóriamente deve ser "INPUT"
###### componentId
Tipo do valor: number

ID numérico ÚNICO do componente DENTRO do filtro, necessário para utilizar o componente na query da chave "relationsComponent".
###### valueType
Tipo do valor: string

Tipo do valor daquele componente, podendo variar entre QUERY, STRING e INTEGER
###### label
Tipo do valor: string

Texto que será apresentado na label ao lado da checkbox
###### query
Tipo do valor: string

O fragmento da query ao qual o componente representa, valor este que será substituído dentro de "relationsComponent". Este valor será usado para quando o checkbox estiver selecionado pelo usuário
###### unusedQuery
Tipo do valor: string
  
## Tipos especiais
Dentro do JSON, existem alguns tipos especiais utilizados para a elaboração dos componentes, sendo conjuntos de valores permitidos para determinadas chaves.

### Tipos {.tabset}
#### ComponentType
Utilizado pela chave "componentType", define qual componente aquele objeto JSON descreve.
Valores permitidos: "SELECT", "CHECKBOX", "INPUT"
#### ComponentDataType
Utilizado pela chave "valueType", define qual é o tipo do valor daquele componente, por exemplo, um INPUT com valueType do tipo INTEGER, seu valor será tratado como um inteiro.
Valores permitidos: "STRING", "INTEGER", "QUERY"
#### QUERY
Tipo especial que representa uma query ou fragmento de query utilizada para buscar os processos no banco de dados.
Utilizado pelas chaves "query", "unusedQuery", "componentsRelation" e "defaultQuery".
Este tipo faz uso de algumas ferramentas que permitem substituir valores dentro da query, permitindo uma maior flexibilidade na sua utilização. Esses valores são reconhecidos com os caracteres "<" e ">", todas as suas utilizações estão descritas mais abaixo.
  
## Valores de sessão
Dentro do tipo QUERY, existe um conjunto especial de valores substituíveis que representam atributos da sessão do usuário.

### Valores de sessão {.tabset}
#### USER_ID
Representa o ID do usuário atual, utilizado dentro da QUERY com a identificação <SESSION_USER_ID>
#### PROFILE_ID
Representa o ID do perfil atual do usuário, utilizado dentro da QUERY com a identificação <SESSION_USER_PROFILE_ID>
#### PROFILE_NAME
Representa o nome do perfil atual do usuário, utilizado dentro da QUERY com a identificação <SESSION_USER_PROFILE_NAME>
Note que, o valor substituído provavelmente deve ser utilizado como uma string dentro da query, então é recomendo que se faça uso de aspas simples (') ao redor da identificação.

## Utilização dos valores dos componentes dentro da QUERY
Cada componente possui seus tipos de valores permitidos, para se utilizar o valor captado por um componente dentro de uma QUERY, utiliza-se a identificação \<value> dentro da chave "query" e "unusedQuery" dos componentes.
Para casos de utilização de "like clauses", pode ser necessário adicionar as wildcards "%", comuns nestas situações, para tal, existe as variações \<%value>, \<%value%> e \<value%>.
 
## Utilização dos componentes dentro de "componentsRelation"
Para utilizar o fragmento de QUERY de um componente na query final, utilizamos o "componentId" declarado dentro do componente, ressaltando que, este valor deve ser único para cada componente dentro do filtro.
Basta adicionar a identificação \<\<componentId>> dentro da query de "componentsRelation", por exemplo:
>     {
>         ...,
>         "componentsRelation": "<1> OR <2>",
>         ...
>     }
Sendo esta chave o único local onde o "componentId" é utilizado.

# Processos retornados pelo filtro
Devido a natureza do filtro, ele permite, se assim configurado, que pessoas do perfil X possam trazer processos de um perfil Y ou de outras pessoas.
Para essas situações, se o usuário A no perfil X, realizar um filtro que traga um processo do usuário B ou do perfil Y, esse processo terá um conjunto de botões diferentes, definidos pela tabela "foreign_process_button".

## Tabela foreign_process_button
![filtros3.png](/fluxo/filtros3.png){.align-center}

Nesta tabela estão definidos os botões que serão exibidos para processos que NÃO pertecem perfil atual do usuário, por exemplo, se o usuário atual está no perfil 16, e o filtro trouxer processos que não são do perfil 16, então os botões exibidos para esses processos serão os botões 1,2,3 e 51, como no exemplo da tabela acima.