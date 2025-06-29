---
title: Observatório
description: Observatório
published: true
date: 2025-06-10T13:20:50.605Z
tags: observatorio
editor: markdown
dateCreated: 2025-04-23T18:12:47.324Z
---

Esta página contêm informações de implantação e configuração do módulo de Observatório dentro da plataforma SIG

---

O módulo do Observatório, dentro da aplicação do Geopixel Cidades, é responsável por fornecer ao usuário as funcionalidades de cálculos e simulação de valores de IPTU, Valor Venal do Imóvel (VVI), Valor Venal de Construção (VVC) e Valor Venal do Terreno (VVT) dos imóveis do município, seguindo as leis e regras de cada prefeitura para a realização dos cálculos necessários.

Devido a natureza do módulo, sua configuração pode se tornar um tanto quanto complexa, por isso, essa página tem como objetivo orientar, explicar e exemplificar sua configuração, bem como uma breve introdução aos conceitos do móudlo e sua utilização do ponto de vista do usuário.

# Tabelas de configuração do módulo
### Tabelas de configuração do módulo {.tabset}
#### gpx_observatory_tables {.tabset}
A tabela *gpx_observatory_tables* é onde são definidas e declaradas as tabelas do sistema que o módulo utilizará para realizar ações de cada contexto específico. Nesta tabela, deverão conter entradas o suficiente para que todos os contextos disponíveis estejam presentes, do contrário, o módulo do Observatório não funcionará corretamente.

##### Atributos {.tabset}
###### id
Atributo identificador da linha no banco de dados. Gerado automáticamente ao fazer uma nova inserção.
###### table_name
Nome da tabela utilizada para o determinado contexto associado.
###### context
O contexto ao qual a tabela será utilizada. Os valores possíveis são fixos e restringidos através de uma constraint.

Contextos disponíveis no momento:
- OMI_DATABASE: Define a tabela principal do módulo, que contêm as geometrias dos imóveis, seus dados e seus fatores;
- ISOTIMA_TABLE: Define a tabela isótima do módulo, que contêm a informação das áreas isótimas da cidade, associados com as regiões e valores de m²;
- CONSTRUCTED_SQUARE_METER_VALUE_TABLE: Define a tabela de valores de m² construído da cidade, associados com os padrões e tipos de cada construção;
- ALIQUOT_TABLE: Define a tabela das aliquotas do módulo, associando os cada faixa de valor a uma porcentagem fixa a ser utilizada como aliquota no cálculo do IPTU;
- PHYSICAL_TABLE: Define a tabela onde estão as informações dos imóveis. Esta tabela não pode ser uma *v**iew***, pois os dados da mesma serão editados pelo módulo.

#### gpx_observatory_used_attributes {.tabset}
A tabela *gpx_observatory_tables* é onde são definidas e declaradas as tabelas do sistema que o módulo utilizará para realizar ações de cada contexto específico. Nesta tabela, deverão conter entradas o suficiente para que todos os contextos disponíveis estejam presentes, do contrário, o módulo do Observatório não funcionará corretamente.

##### Atributos {.tabset}
###### id
Atributo identificador da linha no banco de dados. Gerado automáticamente ao fazer uma nova inserção.
###### attribute_name
Nome do atributo a ser utilizado pelo contexto associado.
###### context
Contexto ao qual o atributo será utilizado. Os valores possíveis são fixos e restringidos através de uma constraint.

Contextos disponíveis no momento:
- ISOTIMA_ATTRIBUTE: Nome da coluna na tabela definida para o contexto ISOTIMA_TABLE que contenha o código da área isótima;
- IMMOBILE_DESCRIPTION_ATTRIBUTE: Nome da coluna onde estão as descrições dos tipos de imóveis na tabela definida para o contexto CONSTRUCTED_SQUARE_METER_VALUE_TABLE;
- IMMOBILE_TYPE_ATTRIBUTE: Nome da coluna onde estão os tipos de imóveis da tabela do contexto ISOTIMA_TABLE;
- IMMOBILE_CODE_TYPE_ATTRIBUTE: Nome da coluna onde estão os códigos dos tipos de imóveis da tabela do contexto ISOTIMA_TABLE;
- IMMOBILE_CLASSIFICATION_TYPE_ATTRIBUTE: Nome da coluna onde estão os padrões de imóveis da tabela do contexto CONSTRUCTED_SQUARE_METER_VALUE_TABLE;
- IMMOBILE_VVI_SIMULATION_ATTRIBUTE: Nome da coluna onde o valor do VVI simulado é salvo na tabela do contexto PHYSICAL_TABLE;
- IMMOBILE_VVC_SIMULATION_ATTRIBUTE: Nome da coluna onde o valor do VVC simulado é salvo na tabela do contexto PHYSICAL_TABLE;
- IMMOBILE_VVT_SIMULATION_ATTRIBUTE: Nome da coluna onde o valor do VVT simulado é salvo na tabela do contexto PHYSICAL_TABLE;
- IMMOBILE_IPTU_SIMULATION_ATTRIBUTE: Nome da coluna onde o valor do IPTU simulado é salvo na tabela do contexto PHYSICAL_TABLE;
- IMMOBILE_SIMULATED_IPTU_KEY: Nome da variável do contexto dos cálculos da simulação que guarde o valor do IPTU simulado;
- IMMOBILE_SIMULATION_RESULT: Atributo utilizado no contexto dos cálculos da simulação para identificar em qual chave está o objeto que representa o resultado da mesma. Esse valor se repete como uma váriavel na configuração da tabela ***gpx_observatory_variables***;
- CURRENT_YEAR_IPTU_ATTRIBUTE: Nome da coluna que contenha o valor do IPTU já calculado do ano corrente na tabela definida no contexto OMI_DATABASE. Este atributo é utilizado para o cálculo do IPTU total atual da cidade;
- IMMOBILE_JOIN_ATTRIBUTE: Nome da coluna de ligação da tabela do contexto PHYSICAL_TABLE. Utilizado para determinar qual registro da tabela do contexto PHYSICAL_TABLE será atualizado com novos valores de VVI, VVC, VVT e IPTU;
- IMMOBILE_PRIMARY_KEY_ATTRIBUTE: Nome da coluna de chave primário da tabela do contexto OMI_DATABASE;

#### gpx_observatory_terrain_value_columns {.tabset}
A tabela *gpx_observatory_terrain_value_columns* é onde são definidas as opções disponíveis para o **Select** na interface do módulo onde o usuário deve escolher qual será a coluna a ser utilizada com o valor do m² do terreno.

##### Atributos {.tabset}
###### id
Atributo identificador da linha no banco de dados. Gerado automáticamente ao fazer uma nova inserção;
###### column_alias
Apelido da coluna, será também o texto que será exibido ao usuário durante a seleção;
###### column_name
Nome da coluna da tabela da tabela do contexto ISOTIMA_TABLE que contenha o valor do m² do terreno;
###### is_default_column
Valor booleano que define se a coluna é a padrão ou não. Caso seja, a opção será selecionada automaticamente para o usuário. Deve existir apenas uma coluna padrão.

#### gpx_observatory_execution_steps {.tabset}
Na tabela *gpx_observatory_execution_steps* é defindo a ordem de execução dos passos dos cálculos das simulações. Esta tabela se relaciona diretamente com as tabelas *gpx_observatory_equations* e *gpx_observatory_variables*.

Todos os *steps*, passos, devem ser utilizados, por uma, e exatamente uma, das duas tabelas mencionadas acima.

##### Atributos {.tabset}
###### id
Atributo identificador da linha no banco de dados. Gerado automáticamente ao fazer uma nova inserção.
Este ID é referênciado pelas tabelas *gpx_observatory_equations* e *gpx_observatory_variables* e não deve existir um ID sem referência, do contrário, ocorrerá um erro quando o usuário tentar utilizar o módulo.
E também só deve ser utilizado por uma das tabelas por vez, nunca por duas ao mesmo tempo.
###### step_order
Define a ordem do de execução do passo no contexto da simulação. Este valor deve ser único, garantido por uma constraint na tabela.

### Tabelas de configuração do módulo {.tabset}
#### gpx_calculator_interface_description {.tabset}
##### id
Atributo identificador da linha no banco de dados. Gerado automáticamente ao fazer uma nova inserção.
#### component_group
Identifica à qual grupo aquele componente pertence, atualmente podendo ser ***IPTU_CALCULATOR*** ou ***ITBI_CALCULATOR***, sendo o componente exibido apenas na interface correspondente durante a utilização pelo usuário.

#### component_description
Um JSON que descreve o componente, contendo todas as propriedades e atributos referentes à ele, bem como a identificação de qual componente deve ser montado na interface.

Existem diversos componentes suportados, e a lista e a descrição de como configurar adequadamente o JSON de cada um encontra-se na seção [Descrição JSON dos componentes das calculadoras](https://wiki.flow.geopixel.com.br/pt-br/observatorio#descri%C3%A7%C3%A3o-json-dos-componentes-das-calculadoras).

#### display_order
Um número que define qual a ordem de aparição do componente dentro da interface, ordenado de cima para baixo.
Dentro de um mesmo *component_group*, a ordem deve ser única, bem como, a ordem apenas é referete para o grupo em questão.

#### gpx_observatory_variables {.tabset}
Na tabela *gpx_observatory_variables* estão definidas as variaveis utilizadas no processo dos cálculos de uma dada simulação.

Essas variáveis podem ser fatores, valores fixos, valores calculados e etc.

Cada linha dessa tabela representa uma variável que é guardada e acessada dentro de um contexto durante a simulação.

Em conjunto com a tabela *gpx_observatory_equations*, estas duas tabelas formam o **núcleo** dos cálculos do módulo.

##### Atributos {.tabset}
###### id
Atributo identificador da linha no banco de dados. Gerado automáticamente ao fazer uma nova inserção.

###### variable_name
Define o nome que aquela variável terá no contexto da simulação. Nomes repetidos farão com que o valor anterior seja sobrescrito.
###### variable_type
Define o tipo daquela variável, não confundir com o tipo do dado que a variável armazena.
O tipo da variável deve ser um dos valores previstos, garantidos por meio de uma constraint na tabela, sendo esses valores/tipos os seguintes:
- COPY_ATTRIBUTE: Copia o valor de uma variável para a nova, sem alterá-lo;
- DEFINED_VALUE: A variável será instânciada sempre com o valor fixo, predefinido nas configurações da variável;
- IN_RANGE_ALIQUOT: Este tipo de variável é específico para a declaração e cálculo de aliquotas onde espera-se que dado um VVI de um imóvel, este valor de VVI esteja dentro das faixas estabelecidas, retornando o valor da aliquota para a faixa encontrada. ***Este tipo de variável pode não ser utilizado em todas as prefeituras em razão das regras de como a aliquota é calculada para cada uma***;
- MAP: Define uma variável sendo do tipo da estrutura de dados ***Map***, permitindo adicionar valores e outras variáveis dentro dela. ***A estrutura de dados do tipo Map, pode ser entendida como um JSON, sendo representada como chave e valor, no formato `{"chave": "valor"}`;***
- SIMPLE: Define uma variável simples, onde seu valor é obtido através do acesso a "data sources", que nada mais são que outras variáveis do tipo ***Map***.
###### variable_data_Type
Define o tipo do dado que aquela variável irá guardar e representar.
Os tipos suportados são restringidos a um conjunto fixo e garantido por uma constraint na tabela, sendo eles:
- BOOLEAN: Valor do tipo verdadeiro ou falso (true/false);
- DOUBLE: Valor numérico do tipo double, que suporta casas decimais, como por exemplo, `42,42`, `-1,42` e `0,42`;
- INTEGER: Valor numérico do tipo inteiro, que não suporta casas decimais, como por exemplo `42`, `1000000` e `-42`
- MAP: Valor do tipo ***Map***, que representa uma estrutura de dados, usado principalmente para a criação de "data sources" para agrupar outras variáveis. ***A estrutura de dados do tipo Map, pode ser entendida como um JSON, sendo representada como chave e valor, no formato `{"chave": "valor"}`;*** 
- STRING: Valor do tipo texto, represeta uma cadeia de caracteres.
###### gpx_observatory_execution_steps_id
Chave estrangeira que aponta para um ID na tabela *gpx_observatory_execution_steps*, a referência deve ser única e não pode já estar sendo utilizada pela tabela *gpx_observatory_equations*.
Esta coluna define, através do *step_order* na tabela *gpx_observatory_execution_steps* qual será a ordem de execução e criação das variáveis.
###### custom_properties
Uma coluna do tipo JSON, `{"chave": "valor"}` que define as propriedades que serão utilizadas pela variável no momento de sua inicialização.
Cada tipo de variável possui um esquema JSON específico, com suas próprias chaves e valores esperados. Esses esquemas estão descritos na aba **variable_type**.

#### gpx_observatory_equations {.tabset}
Na tabela *gpx_observatory_equations* estão definidas as fórmulas que serão executadas para a realização dos cálculos de uma simulação.

Após a execução dos cálculos, seus valores são salvos no contexto da simulação como variáveis, disponíveis para serem utilizadas posteriormente

Em conjunto com a tabela *gpx_observatory_variables*, estas duas tabelas formam o **núcleo** dos cálculos do módulo.

##### Atributos {.tabset}
###### id
Atributo identificador da linha no banco de dados. Gerado automáticamente ao fazer uma nova inserção.

###### equation
Um texto que define a fórmula matemática a ser executada para a obtenção de um valor.

Verifique a seção [Equações](https://wiki.flow.geopixel.com.br/pt-br/observatorio#equa%C3%A7%C3%B5es) para ver as formas de criação de equações.

###### equation_result_name
Define o nome da variável que irá guardar o valor após sua fórmula ser executada. Esse nome pode ser utilizado por passos subsequentes para a utilização do valor em outras fórmulas.
###### execution_condition
Define uma condição a ser checada antes da execução da fórmula. Caso a condição seja nula, a fórmula sempre será executada, do contrário, a condição deve retornar um valor booleano que indique se a execução deve ocorrer ou não.

Verifique a seção [Condições de execução](https://wiki.flow.geopixel.com.br/pt-br/observatorio#condi%C3%A7%C3%B5es-de-execu%C3%A7%C3%A3o) para ver as formas de criação de condições de execução.

###### gpx_observatory_execution_steps_id
Chave estrangeira que aponta para um ID na tabela *gpx_observatory_execution_steps*, a referência deve ser única e não pode já estar sendo utilizada pela tabela *gpx_observatory_variables*.
Esta coluna define, através do *step_order* na tabela *gpx_observatory_execution_steps* qual será a ordem de execução e criação das variáveis.

# Equações
Equações são textos que são interpretados pela aplicação e realizam operações matemáticas básicas, com o adicional, neste caso, de operações condicionais.
Para se criar uma equação a ser executada, pode-se utilizar números ou nomes de "variables" presentes no "context", onde seus nomes são substituidos por seus respetivos valores.
Ao utilizar variables, atente-se ao seu tipo de dado, apenas aquelas de tipo numérico, para equações, podem ser utilizadas.
Para entender o que é o "context" e suas "variables", recomenda-se a leitura da seção [Context](https://wiki.flow.geopixel.com.br/pt-br/observatorio#h-2a-etapa-cria%C3%A7%C3%A3o-do-context-da-simula%C3%A7%C3%A3o).

Abaixo estão exemplificados a forma de utilização de cada operação:
- Adição: ( + ) Realiza a operação de adição, por exemplo:
  - 1 + 1
  - current_iptu + 100
  - current_iptu + 500 + specific_tax
- Subtração ( - ) Realiza a operação de subtração, por exemplo:
  - 5 - 10
  - year_vvc - 50
  - iptu_imovel - vvi_imovel - 200
- Multiplicação ( * ) Realiza a operação de multiplicação, por exemplo:
  - 3 * 10
  - vvi_imovel * 0.01
  - iptu_imovel * vvc_imovel * 2
- Divisão ( / ) Realiza a operação de divisão, por exemplo:
  - 10 / 2
  - taxa_imovel / 10
  - taxa_imovel / valor_terreno / 2
- Agrupamento ( () ) Agrupa uma parte da equação para garantir a correta execução, por exemplo:
  - (10 + 2) / 2
  - (vvi_imovel * aliquota) * 2
    - Na equação acima, tem o agrupamento, o resultado seria 11, pois a divisão seria executada primeiro, com o agrupamento, o resultado é 6, pois a adição é feita antes da divisão
- Condicionais ( ? > < : != == ) Realiza operações condicionais e comparativas para checar qual parte da equação deve ser executada, onde cada operador possuí os seguintes significados:
  - ( != ): Operador diferente, checa se dois valores são diferentes entre si, retornando um valor booleano como resultado, por exemplo:
    - 10 != 5
    - (10 + 10) != 20
    - iptu_imovel != vvi_imovel
  - ( == ) Operador igualdade, checa se dois valores são exatamente iguais, retornando um valor booleano como resultado, por exemplo:
    - 10 == 5
    - (10 + 10) == 20
    - iptu_imovel == vvi_imovel
  - ( < ) Operador menor que, checa se o valor da esquerda é menor que o da direita, retornando um valor booleano como resultado, por exemplo:
    - 20 < 10
    - (2 * 2) < 2
    - iptu_atual < iptu_estimado
  - ( > ) Operador maior que, checa se o valor da esquerda é maior que o da direita, retornando um valor booleano como resultado, por exemplo:
    - 20 > 10
    - 10 > (10 / 2)
    - vvc_imovel > vvt_imovel
  - ( ? : ) Operador ternário, checa se um valor é **true** ou **false**, e irá executar a parte da equação correspondente em razão do valor recebido. "?" demarca o início do operador ternário e ":" demarca as partes que podem ser eventualmente executadas em razão do valor booleano. Um exemplo simplificado pode ser descrito assim, `<true/false> ? <caso_true> : <caso_false>`, por exemplo:
    - 10 > 2 ? 5 + 5 : 10 - 5
      - A operação irá checar se o valor "10" é maior que 2, como é, será retornado o valor "true", em seguida, a operação irá executar a equação da esquerda e retornar seu valor, ou seja, "5 + 5" será executado e o valor "10" será retornado.
    - (10 > 2) ? (5 + 5) : (10 - 5)
      - O agrupamento pode ser utilizado para ajudar a distinguir melhor as partes da operação ternária.
    - ((10 > 2) ? (5 + 5) : (10 - 5)) * 5
      - Toda a operação ternária pode ser agrupada, garantindo que o valor resultante possa ser utilizado após sua execução. Por exemplo, no caso acima, a operação ternária retornará o valor "10", que em seguida será multiplicado por 5, resultando em um retorno da equação de valor "50".
    - (10 > 2) ? ((5 != 5) ? (8) : (2)) : (10 - 5)
      - O operador ternário pode ser aninhado dentro de outro, resultando em condições mais complexas, no caso acima, para a primeira condição, será checado se 10 é maior que 2, retornando o valor "true", em seguida, será executado a outra operação ternária "(5 != 5) ? (8) : (2)", que nos retornará o resultado "2", resultando no final da execução dos dois operador, o retorno do valor "2".
      
# Condições de execução
Para steps do tipo "variable" ou "equation", ambos podem ser atrelados a uma condição para sua execução durante um cálculo. Essas condições são feitas em forma de texto e devem sempre retornar um valor booleano.
Para saber mais sobre os steps em si, recomenda-se a leitura da seção [Steps](https://wiki.flow.geopixel.com.br/pt-br/observatorio#h-1a-etapa-obten%C3%A7%C3%A3o-dos-steps-para-a-simula%C3%A7%C3%A3o).

As condições são interpretadas pela aplicação utilizando os mesmos mecânismos para a execução das [Equações](https://wiki.flow.geopixel.com.br/pt-br/observatorio#equa%C3%A7%C3%B5es), por isso, as mesmas formas de utilização podem ser reaproveitadas, o operador ternário, em especial, mostra-se muito útil para condições.

As condições necessitam retornar um valor booleano, `true` ou `false`, do contrário, não será possível continuar a operação e uma exceção ira parar a execução da aplicação.

Em adição aos operadores já exemplificados na seção de equações, os operadores `and` e `or` também podem ser utilizados nas condições, conforme exemplos abaixo:

- `simulationType == 'ITBI' and isFinancing == false`
  - Ambos `simulationType` e `isFinancing` são valores lidos do contexto e substituidos onde necessário na condição, após a interpretação, a expressão acima retorna adequadamente um valor booleano
  
- `immobileType == 'Edificados Residenciais' or immobileRegionType == 'D'`
  - Novamente, os nomes das variables são substituidos por seus respectivos valores dentro do contexto e a expresão retorna adequadamente um valor booleano

- `constructedArea > 50`
  - Condições também podem conter números, desde que seu retorno seja um valor booleano
  
- `constructedArea - demolishedArea`
  - O exemplo acima não é uma condição válida, pois retorna um valor não booleano
  
- `50 / 2`
  - Novamente, outra operação inválida, pois não retorna um valor booleano


# Custom Properties
Abaixo estão exemplos e as descrição de cada JSON utilizado como "custom property" para os tipos de variáveis descritos na tabela "gpx_observatory_variables".

Verifique a seção [Condições de execução](https://wiki.flow.geopixel.com.br/pt-br/observatorio#condi%C3%A7%C3%B5es-de-execu%C3%A7%C3%A3o) para ver as formas de criação de condições de execução.

## Custom Properties {.tabset}
### SIMPLE
```
{
  "variableValueSource": "string",
  "sourceAttribute": "string",
  "executionCondition": "string"
}
```

- variableValueSource: Nome da variável do tipo MAP que será usada como fonte do valor;
- sourceAttribute: Nome do atributo dentro da fonte declarada em `variableValueSource` cujo o valor será retornado;
- executionCondition: Atributo opcional, caso ausente, a variável sempre será criada no contexto, caso declarado, deve retornar um valor booleano, `true` ou `false` que indique se a variável deve ser incializada ou não.

### DEFINED
```
{
  "attributeValue": "string" | int | double | boolean | map,
  "executionCondition": "string"
}
```

- attributeValue: Valor a ser atributo no momento da criação da variável, deve-se ser um valor do tipo `string`, `int`, `double`, `boolean` ou `map`.
- executionCondition: Atributo opcional, caso ausente, a variável sempre será criada no contexto, caso declarado, deve retornar um valor booleano, `true` ou `false` que indique se a variável deve ser inicializada ou não.

### IN_RANGE_ALIQUOT
```
{
  "vviAttribute": "string",
  "immobileTypeAttribute": "string",
  "executionCondition": "string"
}
```

- vviAttribute: Nome do atributo dentro do contexto que contenha o valor do VVI do imóvel;
- immobileTypeAttribute: Nome do atributo dentro do contexto que contenha o valor do tipo do imóvel.
- executionCondition: Atributo opcional, caso ausente, a variável sempre será criada no contexto, caso declarado, deve retornar um valor booleano, `true` ou `false` que indique se a variável deve ser inicializada ou não.

### MAP
```
{
  "variableValueSource": "string",
  "contextAttributesList": [
    "string",
    "string",
    ...
    "string"
  ],
  "executionCondition": "string"
}
```

- variableValueSource: Nome da variável do tipo MAP que será usada como fonte dos valores;
- contextAttributesList: Uma lista de nomes dos atributos que serão pegos da fonte declarada em `variableValueSource` e adicionados ao mapa, onde o nome declarado será a chave para o valor ser acessado.
- executionCondition: Atributo opcional, caso ausente, a variável sempre será criada no contexto, caso declarado, deve retornar um valor booleano, `true` ou `false` que indique se a variável deve ser inicializada ou não.

### COPY_ATTRIBUTE
```
{
  "variableValueSource": "string",
  "attributeToCopy": "string",
  "executionCondition": "string"
}
```

- variableValueSource: Nome da variável do tipo MAP que será usada como fonte dos valores;
- attributeToCopy: Nome do atributo que será copiado da fonte declarada em `variableValueSource`.
- executionCondition: Atributo opcional, caso ausente, a variável sempre será criada no contexto, caso declarado, deve retornar um valor booleano, `true` ou `false` que indique se a variável deve ser inicializada ou não.

### CUMULATIVE_ALIQUOT

```
{
  "vviAttribute": "string",
  "immobileTypeAttribute": "string",
  "executionCondition": "string"
}
```

- vviAttribute: Nome do atributo dentro do contexto que contenha o valor do VVI do imóvel;
- immobileTypeAttribute: Nome do atributo dentro do contexto que contenha o valor do tipo do imóvel.
- executionCondition: Atributo opcional, caso ausente, a variável sempre será criada no contexto, caso declarado, deve retornar um valor booleano, `true` ou `false` que indique se a variável deve ser inicializada ou não.

# Descrição JSON dos componentes das calculadoras
## Descrição JSON dos componentes das calculadoras {.tabset}
### INPUT
O componente de input define um campo ao qual o usuário pode digitar algum valor a ser utilizado posteriormente no calculo das calculadoras, sendo esse componente descrito pelo JSON abaixo:

```
{
  "component": "INPUT",
  "variableName": "string",
  "dataType": "string",
  "disabled": boolean,
  "lockContext": boolean,
  "label": "string"
  "isVisible": boolean
}
```

- component: Um valor do tipo texto que define qual componente aquela descrição representa, para inputs, o valor deve sempre ser **INPUT**;
- variableName: Um valor do tipo texto que associa o componente à uma variavel do contexto dos cálculos, o valor da variável é exibido no input bem como seu valor também é alterado caso o usuário altere o valor no input;
- dataType: Um valor do tipo texto que define qual o tipo de dado o input irá suportar, os valores válidos para esse campo são:
  - MONETARY: Valores do tipo monetário, dinheiro, no padrão R$ e com formatação adequada;
  - TEXT: Valores do tipo texto, string;
  - METRIC: Valores do tipo métrico, para distâncias ou áreas, com suporte à duas casas decimais e formatação adequada;
  - NUMBER: Valores do tipo numérico, que aceita apenas caracteres numéricos.
- disabled: Valor do tipo booleano `true` ou `false` que define se o usuário pode alterar ou não o valor daquele input;
- lockContext: Valor do tipo booleano `true` ou `false` que define se o valor do input pode ser sobrescrito durante o calculo da simulação. Exemplificando, durante a execução dos steps, a variável cujo o valor é controlado pelo input pode ser calculada dinamicamente durante o processo, fazendo com que o valor editado do usuário seja sobrescrito e ignorado, ao definir lockContext como `true`, o valor do usuário será utilizado;
- isVisible: Valor do tipo booleano `true` ou `false` que define se o input está visivel ou não ao usuário. 


### TEXT
O componente de text define um texto simples a ser exibido ao usuário, sendo esse componente descrito pelo JSON abaixo:

```
{
  "component": "TEXT",
  "text": "string",
  "fontSize": "string",
  "fontWeight": "string",
  "color": "string
}
```

- component: Um valor do tipo texto que define qual componente aquela descrição representa, para texts, o valor deve sempre ser **TEXT**;
- text: Um valor do tipo texto que será o texto a ser exibido ao usuário;
- fontSize: Um valor do tipo texto que define o tamanho da fonte do texto, seu valor deve ser no padrão "00px", "00rem" ou qualquer outro valor CSS válido para tamanho de fonte;
- fontWeight: Um valor do tipo texto que define o "peso" da fonte, podendo ser qualquer valor CSS válido para a propriedade, como "regular", "bold" e etc;
- color: Um valor do tipo texto que define qual será a cor do texto, podendo ser qualquer valor CSS válido para a propriedade, como valores hex "#ffffff" ou nomes de cores como "white".

### SELECT
O componente de select define um campo ao qual o usuário pode escolher um valor a ser utilizado posteriormente no calculo das calculadoras, sendo esse componente descrito pelo JSON abaixo:

```
{
  "component": "SELECT",
  "variableName": "string",
  "disabled": boolean,
  "lockContext": boolean,
  "label": "string",
  "options": [
    {
      "label": "string",
      "value": number | "string"
    },
    ...
  ]
}
```

- component: Um valor do tipo texto que define qual componente aquela descrição representa, para selects, o valor deve sempre ser **SELECT**;
- variableName: Um valor do tipo texto que associa o componente à uma variavel do contexto dos cálculos, a opção cujo o valor corresponder ao valor da variável será exibida no select;
- disabled: Valor do tipo booleano `true` ou `false` que define se o usuário pode alterar ou não a opção do select;
- lockContext: Valor do tipo booleano `true` ou `false` que define se o valor do input pode ser sobrescrito durante o calculo da simulação. Exemplificando, durante a execução dos steps, a variável cujo o valor é controlado pelo select pode ser calculada dinamicamente durante o processo, fazendo com que o valor editado do usuário seja sobrescrito e ignorado, ao definir lockContext como `true`, o valor do usuário será utilizado.
- options: Uma lista de JSONs que descrevem as opções daquele select, sendo o JSON com a seguinte estrura:
  - label: Valor do tipo string que será o texto a ser exibido para aquela opção ao usuário;
  - value: Valor do tipo string ou number que aquela opção representará. Ao selecionar a opção, esse valor será associado à variable do select.

### LINK
O componente de link define um texto simples a ser exibido ao usuário e que o mesmo pode clicar para acessar uma URL qualquer, sendo esse componente descrito pelo JSON abaixo:

```
{
  "component": "LINK",
  "id": "string",
  "linkText": "string",
  "isVisible": boolean,
  "url": "string",
  "fontSize": "string",
  "fontWeight": "string"
}
```

- component: Um valor do tipo texto que define qual componente aquela descrição representa, para texts, o valor deve sempre ser **LINK**;
- id: Um valor do tipo texto que define um ID ao link, utilizado quando se deseja realizar alguma ação sobre o link por meio de outros componentes;
- linkText: Um valor do tipo texto que será o texto a ser exibido ao usuário;
- url: Um valor do tipo texto que será a ser acessada;
- fontSize: Um valor do tipo texto que define o tamanho da fonte do texto, seu valor deve ser no padrão "00px", "00rem" ou qualquer outro valor CSS válido para tamanho de fonte;
- fontWeight: Um valor do tipo texto que define o "peso" da fonte, podendo ser qualquer valor CSS válido para a propriedade, como "regular", "bold" e etc;
- color: Um valor do tipo texto que define qual será a cor do texto, podendo ser qualquer valor CSS válido para a propriedade, como valores hex "#ffffff" ou nomes de cores como "white";
- isVisible: Valor do tipo booleano `true` ou `false` que define se o input está visivel ou não ao usuário.

# Visão geral
![simulador1.png](/observatory/simulador1.png){.align-center}

O módulo de simulação é acessível através dos botões **Observatório -> Simulador PVG**, sendo ele responsável por realizar a simulação dos valores de VVT, VVC, VVI e IPTU para todos os imóveis do município, mediante configurações do usuário.

## Simulador
![simulador2.png](/observatory/simulador2.png){.align-center}

Ao acessar a interface, o usuário pode alterar parâmetros que irão afetar o resultado do campo *Valor Simulado*

- Percentual do Valor Venal Atribuído: Este campo define quanto deve ser usado do VVI para fins de cálculo do IPTU, caso deixado *0,00%*, o valor total é utilizado;
- Limitar aumento percentual do IPTU para: Limita o quanto, ao máximo, o IPTU pode ser aumentado em relação ao valor base já existente no banco de dados, por exemplo, caso o IPTU base seja R$ 100,00 e define-se que o limite seja 20%, o IPTU simulado não pode ultrapassar R$ 120,00, caso ultrapasse, o valor de R$ 120,00 será utilizado;
- Deducação de IPTU: Define um valor fixo que será deduzido do VVI antes da aplicação da aliquota para o cálculo do IPTU.

Os campos **Valor Atual** e **Valor Simulado** são, respectivamente, o valor total atual da soma de todos os IPTUs já na base de dados e o resultado após a simulação ser realizada.

O usuário pode também marcar a caixa de seleção **Salvar simulação** para que seus parâmetros e resultados sejam salvos, podendo ser consultado e reutilizado através da **Simulações Salvas** no topo da página.

### Tabela de aliquotas

![simulador3.png](/observatory/simulador3.png){.align-center}

Na aba **Tabela de Alíquotas** o usuário pode visualizar as aliquotas base do município e realizar a edição de seus valores como achar necessário.

- Tipo: Um campo de seleção que permite ao usuário selecionar sobre qual tipo de imóvel aquela aliquota deverá ser realizada;
- Valor mínimo: Define o valor mínimo no qual o VVI do imóvel deve se encontrar para que a aliquota seja aplicada sobre ele;
- Valor máximo: Define o valor máximo no qual o VVI do imóvel deve se encontrar para que a alíquota seja aplicada sobre ele;
- Aliquota: O valor da alíquota que será aplicada ao VVI do imóvel caso o mesmo se encaixe entre os valores mínimos e máximos;
- Botão de exclusão: Exclui a aliquota da tabela. A aliquota é excluida apenas para a sessão de simulação atual, não sendo excluida da tabela real do banco de dados. Caso o usuário feche a interface do módulo e a abra novamente, a tabela de aliquotas será carregada com os valores padrões presentes no banco de dados;
- Botão Adicionar novos valores: Ao fim da tabela encontra-se um botão no qual o usuário pode adicionar uma nova faixa de aliquota a ser considerada na sessão atual da simulação.

#### Comportamento dos campos valor mínimo e máximo
Para uma dada alíquota, caso ambos os campos estejam preenchidos, o valor do VVI deve-se encontrar entre a faixa estabelecida para que a alíquota em questão seja aplicada, ou seja, **<valor_minimo> >= VVI <= <valor_maximo>**.
Caso apenas o campo valor máximo esteja preenchido, isso significa que o VVI deve ser qualquer valor MENOR que o valor máximo para que a alíquota seja aplicada, ou seja, **VVI <= <valor_maximo>**.
Para as situações onde apenas o campo valor mínimo esteja preenchido, o VVI deve ser MAIOR que o valor minímo para que a alíquota seja aplicada, ou seja, **VVI >= <valor_minimo>**.

#### Diferenças entre alíquotas de municípios
O comportamento da tabela de alíquotas pode variar de município para município dependendo do tipo da alíquota configurada no banco de dados, atualmente existem dois tipos de alíquotas que podem ser utilizadas durante o momento da configuração dos cálculos:

###### IN_RANGE_ALIQUOT
Define que, dado um VVI, a alíquota aplicada sobre ele será aquela cujo o VVI esteja dentro da faixa de valores encontrados na tabela, por exemplo, dado uma alíquota de 3% para VVIs entre R$ 10.000,00 e R$ 20.000,00, caso o VVI seja R$ 15.000,00, esta alíquota de 3% será a escolhida para ser aplicada ao VVI, contúdo, caso o VVI fosse R$ 25.000,00, estaria fora da faixa e seria então escolhida outra alíquota correspondente;

***Atenção: Para este tipo de alíquota, é necessário que para todo VVI calculado, este VVI se encaixe em uma das faixas e tipos da tabela, do contrário, ocorrerá um erro na aplicação e a simulação será abortada.***

###### CUMULATIVE_ALIQUOT
Para este tipo, são definidos faixas de valores nas quais o VVI é dividido e cada fração é aplicada uma alíquota correspondente à fração, sendo que ao final da aplicação, os valores individuais de cada faixa são somados para se ter o IPTU final. Por exemplo, para um imóvel de VVI R$ 30.000,00, onde existem três faixas de, R$ 0,00 a R$ 10.000,00 (1% de alíquota), R$ 10.000,01 a R$ 20.000,00 (2% de alíquota) e R$ 20.000,01 (3% de alíquota) em diante, o valor do VVI é dividido por entre essas faixas e aplicado a alíquota correspondente, como abaixo:

R$ 0,00 a R$ 10.000,00 -> R$ 10.000,00 são removidos do VVI original e aplicado a alíquota de 1% sobre esses R$ 10.000,00

R$ 10.000,01 a R$ 20.000,00 -> R$ 10.000,00 são removidos do VVI original e aplicado a alíquota de 2% sobre esses R$ 10.000,00

R$ 20.000,01 em diante -> Os R$ 10.000,00 restantes são removidos do VVI original e aplicado a alíquota de 3% sobre esses R$ 10.000,00

Então, os valores individuais são somados para se ter o IPTU efetivo.

Note que, durante a utilização desse tipo de alíquota, para facilidade de implantação, ao invés do retorno ser o valor do IPTU com a soma das partes, é retornado uma aliquota "equivalente" que pode ser aplicada ao VVI total que resultará no mesmo valor caso o procedimento de separação das faixas fosse feito manualmente. Por exemplo, no exemplo acima, o IPTU seria de R$ 600,00, ao invés desse valor ser retornado, é retornado a alíquota de 2%, onde 30.000 x 0,02 = 600.

## Ciclo de uma simulação
Uma simulação, seja ela para IPTU (simulador/calculadora) ou ITBI (calculadora), ocorre seguindo os mesmos passos e mesmas etapas, aplicadas individualmente para cada imóvel.
### 1ª Etapa - Obtenção dos "steps" para a simulação
Nesta etapa, as tabelas **gpx_observatory_variables** e **gpx_observatory_equations** são carregadas na memória da aplicação e suas linhas são transformadas em "steps", respeitando a ordem definida pela tabela **gpx_observatory_execution_steps**, onde, cada "step" é aplicado em ordem sobre os dados do imóvel para o cálculo adequado da simulação.
Existem dois tipos de "steps", steps de variables e steps de equações, separados por suas tabelas correspondentes mencionadas acima.
- **Steps do tipo variables**: São aqueles declarados na tabela **gpx_observatory_variables** e podem ser dos tipos declarados na descrição da tabela na seção [Tabelas de configuração do módulo](https://wiki.flow.geopixel.com.br/pt-br/observatorio#tabelas-de-configura%C3%A7%C3%A3o-do-m%C3%B3dulo). O atributo "custom property" de cada tipo é encontrado em [Custom Properties](https://wiki.flow.geopixel.com.br/pt-br/observatorio#custom-properties).
- **Steps do tipo equation**: São aqueles declarados na tabela **gpx_observatory_equations**, e sua maior diferença entre as variables são que seu valor é computado através de uma equação. A descrição de como criar uma equação pode ser encontrada na seção [Equações e condições]().

### 2ª Etapa - Criação do "context" da simulação
O "context", ou contexto, é uma estrutura de dados do tipo MAP capaz de armazenar as "variables" criadas pelos "steps". Ele pode ser entendido como um JSON com diversas chaves e valores, onde são guardados os resultados gerados pelos steps.
Para cada simulação, existe um context que é compartilhado, em partes, com todos os imóveis. Para cada imóvel, alguns dados e informações encontrados dentro do context são fixos e não mudam durante a simulação, para essas informações, seus nomes são reservados e não podem ser utilizados como nomes de "variables", sendo eles:
- context: O contexto em si, onde todos os dados são armazenados e podem ser lido e alterados posteriormente pelos "steps";
- simulationType: Uma "variable" fixa, que não pode ser editada por steps que informa qual é o tipo de simulação sendo executada, seus valores podem ser "IPTU" e "ITBI";
- increaseLimit: Variable fixa, contêm o valor definido pelo usuário na interface "Simulador" para o campo "Limitar aumento percentual do IPTU para". Contêm o número *double* que representa a porcentagem;
- urbanBuildingTaxDeduction: Variable fixa, contêm o valor definido pelo usuário na interface "Simulador" para o campo "Dedução de IPTU". Contêm o número *double* que representa o valor monetário;
- maximumUsableVvi: Variable fixa, contêm o valor definido pelo usuário na interface "Simulador" para o campo "Percentual do Valor Venal Atribuído". Contêm o número *double* que representa a porcentagem;
- terrainValueColumnName: Variable fixa, contêm o nome da coluna cujo o valor do m² do terreno deve ser obtido. Esse valor é definido na tela anterior ao Simulador;
- aliquotsTable: Variable fixa, contêm a tabela de alíquotas definida pelo usuário na interface "Tabela de Alíquotas";
- immobileData: Representa a estrutura de dados que contêm os dados dos imóveis, sendo seu valor atualizado a cada iteração de imóvel, preenchendo com os dados do próximo imóvel.

### 3ª Etapa - Execução dos steps
Após a criação do context, para cada imóvel, os steps são aplicados sobre o imóvel.

Após a finalização da execução dos steps, para a execução do Simulador, os resultados devem ser agrupados dentro de uma variable do tipo MAP que contenha o VVT, VVC, VVI, IPTU e um atributo identificador único. Este procedimento é feito através da criação de um step do tipo MAP e é de responsabilidade de quem faz a implantação do módulo na prefeitura.

- O nome desta variable MAP deve ser declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_SIMULATION_RESULT**
- O atributo VVT deve ser o mesmo declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_VVT_SIMULATION_ATTRIBUTE**
- O atributo VVC deve ser o mesmo declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_VVC_SIMULATION_ATTRIBUTE**
- O atributo VVI deve ser o mesmo declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_VVI_SIMULATION_ATTRIBUTE**
- O atributo IPTU deve ser o mesmo declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_IPTU_SIMULATION_ATTRIBUTE**
- O atributo identificador único deve ser o mesmo declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_JOIN_ATTRIBUTE** e deve representar uma coluna existente na tabela declarada em **gpx_observatory_tables** para o tipo **PHYSICAL_TABLE**

Para a finalização também é necessário que na tabela **gpx_observatory_used_attributes** o tipo **IMMOBILE_SIMULATED_IPTU_KEY** esteja declarado e tenha o nome do atributo dentro do context que tenha o valor final do IPTU.

Após isso, os resultados são agrupados, o contexto é limpo de todas as variables pertinentes ao imóvel e o próximo imóvel da lista é utilizado para executar novamente os steps, até que todos os imóveis acabem.

### 4ª Etapa - Atualização dos valores simulados (apenas para Simulador)
Os resultados agrupados são então persistidos na tabela declarada em **gpx_observatory_tables** para o tipo **PHYSICAL_TABLE**.
Essa tabela deve conter as colunas de VVT, VVC, VVI e IPTU simulados, com os mesmos nomes que foram utilizados na 3ª etapa em:

- O nome desta variable MAP deve ser declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_SIMULATION_RESULT**
- O atributo VVT deve ser o mesmo declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_VVT_SIMULATION_ATTRIBUTE**
- O atributo VVC deve ser o mesmo declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_VVC_SIMULATION_ATTRIBUTE**
- O atributo VVI deve ser o mesmo declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_VVI_SIMULATION_ATTRIBUTE**
- O atributo IPTU deve ser o mesmo declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_IPTU_SIMULATION_ATTRIBUTE**

E também a coluna com o atributo identificador em:

- O atributo identificador único deve ser o mesmo declarado na tabela **gpx_observatory_used_attributes** para o tipo **IMMOBILE_JOIN_ATTRIBUTE** e deve representar uma coluna existente na tabela declarada em **gpx_observatory_tables** para o tipo **PHYSICAL_TABLE**

### 5ª Etapa - Salvar o cenário simulado (apenas para Simulador)
Caso o usuário tenha marcado a opção para salvar o cenário da simulação, então todos os parâmetros e resultados gerados na simulação são salvos para que o mesmo possa consultar posteriormente.

### 6ª Etapa - Finalização
Para cada tipo de execução, calculadoras ou simulador, o resultado apropriado é então retornado para ser exibido na tela ao usuário.

# Configurações via arquivo de configurações JSON
O módulo atualmente é dependente de duas configurações no arquivo de configurações da publicação, sendo elas:

```
{
	...,
	"observatory.allowDebugging": <boolean>,
	"observatory.simulation.paginationSize": <int>,
  ...
}
```

- observatory.allowDebugging: Configuração com valor do tipo `boolean`, do tipo `true` ou `false`. Essa configuração habilita alguns logs de debugs que podem ser vistos acessando o arquivo `catalina.out` durante a utilização do módulo.
- observatory.simulation.paginationSize: Configuração com valor do tipo `int`, númerico. Essa configuração informa à aplicação, durante a utilização da ferramenta de simulação, quantos registros da view de imóveis devem ser processados por iteração.
  - Por exemplo, dada uma view de imóveis com 200 mil registros, caso o valor da configuração seja `20000`, a aplicação irá carregar em memória de 20 mil em 20 mil registros por vez e processar suas respectivas simulações, sendo necessários, nesse caso, 10 iterações para cobrir toda a base de dados;
  - ***ATENÇÃO: Esta configuração impacta diretamente no desempenho da aplicação e do módulo. Valores acima de `50000` podem resultar no travamento da aplicação toda por falta de memória disponível, por isso, recomenda-se a utilização do valor `25000`.
  Ative a opção de debugging para visualizar o tempo de execução da simulação para tomar a decisão de qual valor é o mais adequado à ser configurado.***

# Passo a passo implantação do módulo de Simulação
Adiante estão os passos para a implantação do módulo de Simulação do Observatório. Dado o conhecimento prévio sobre o módulo explicado em [Simulador](https://wiki.flow.geopixel.com.br/pt-br/observatorio#simulador), termos e referências serão mencionados no guia.

### 1º Passo - Verificação da base de dados e estrutura do banco de dados
O módulo de simulação necessita que um tema referente ao Observatório esteja devidamente publicado e associado ao perfil adequado, este tema, é composto, na maior parte dos casos, por uma tabela que contenha as geometrias dos lotes e uma tabela de dados, onde cada linha deve representar um imóvel, contendo as colunas de valores de VVT, VVC, VVI e IPTU base já calculados, bem como todos os valores de fatores, classificações do imóvel e outras informações pertinentes devidamente configuradas.
Verifique se as tabelas de sistema (metadados) estão presentes, são aquelas mencionadas [aqui](https://wiki.flow.geopixel.com.br/pt-br/observatorio#tabelas-de-configura%C3%A7%C3%A3o-do-m%C3%B3dulo).
A tabela de dados dos imóveis necessita conter 4 colunas especiais, que são utilizadas pelo sistema para salvar os resultados de uma simulação, essas colunas são:
- vlr_vvt_simulado: numeric not null default 0, para registrar o VVT simulado;
- vlr_vvc_simulado: numeric not null default 0, para registrar o VVC simulado;
- vlr_vvi_simulado: numeric not null default 0, para registrar o VVI simulado;
- vlr_iptu_simulado: numeric not null default 0, para registrar o IPTU simulado.

Caso estas colunas não estejam presentes, será necessário sua criação.

### 2º Passo - Entendimento das regras do município
Cada município/prefeitura possuí suas próprias regras e particularidades para o cálculo do IPTU da simulação, como por exemplo, uma prefeitura pode considerar um fator durante o cálculo que outra não considera.
Todo município possuí essas regras descritas e previstas em lei, portanto, antes de começar a manipulação das tabelas do sistema, é importante possuir o material para consulta.

### 3º Passo - Criação da view da base de dados
Com as tabelas de dados dos imóveis e lotes do município devidamente estabelecidas no banco de dados, realize a criação de uma "view" para a união das duas tabelas.
Identifique qual é a coluna de ligação entre as duas tabelas.
Em seguida, crie a view, realizando a ligação (join) pelo atributo identificado. De regra, todos os atributos da tabela de dados dos imóveis são utilizados, e apenas o atributo de geometria da ID da tabela de lotes é trazido para a view.
Existem dois atributos que são computados pela view e devem ser criados neste momento, sendo eles `percentual_aumento_iptu` e `tipo_alteracao`, esses atributos são necessários para a criação de dashboards futuramente.
Para padronização, o nome da view que que realiza a junção das tabelas deve ser **vw_gpx_observatory_database**;

A SQL para a criação da view será algo parecido com o fragmento adiante:

```
CREATE OR REPLACE VIEW public.vw_gpx_observatory_database
AS SELECT db.id AS database_id,
    lote.gid,
    lote.geom,
    db.numero_cadastro,
    db.inscricao_cadastral,
    db.inscricao,
		..., -- Restante dos atributos
    CASE
        WHEN db.iptu_ufg = 0 THEN 0::numeric(18,0)
        ELSE (db.vlr_iptu_simulado / db.iptu_ufg * 100 - 100)::numeric(18,0)
    END AS percentual_aumento_iptu,
    CASE
        WHEN db.vlr_iptu_simulado > db.iptu_ufg THEN 'AUMENTO'::text
        WHEN db.vlr_iptu_simulado < db.iptu_ufg THEN 'REDUÇÃO'::text
        ELSE 'SEM MODIFICAÇÃO'::text
   END AS tipo_alteracao
   FROM gpx_observatory_database db
     JOIN vet_gpx_cadastral_lotes_edif lote ON lote.inscricao::text = db.inscricao::text
  WHERE lote.expiredate IS NULL;
```

***Nota: O fragmento SQL acima para a criação da view é apenas para exemplo e referência, para cada município, os nomes das colunas e tabelas provavelmente serão diferentes e será necessário adaptação.***

Pode ser necessário não incluir certos registros que estejam com problema nos seus dados, ou realizar ajustes nos valores, para tal, essas condições podem ser resolvidas através de tratamento dos dados pela view, como adicionando mais condições ao WHERE ou formatando os valores selecionados.

### 4º Passo - Criação de indexes
Essa view e as tabelas físicas podem conter centenas de milhares de registros, que são lidos e modificados a cada simulação, por isso, para aumentar a performance, é necessário a criação de indexes.
Dois indexes devem ser criados, uma para a tabela de dados dos imóveis e um para tabela de lotes, em seus respectivos atributos de ligação.

```
CREATE INDEX idx_gpx_observatory_database_inscricao ON gpx_observatory_database(inscricao);
CREATE INDEX idx_vet_gpx_cadastral_lotes_inscricao ON vet_gpx_cadastral_lotes(inscricao);
```

Caso o atributo de ligação não seja o mesmo atributo identificador mencionado [aqui](https://wiki.flow.geopixel.com.br/pt-br/observatorio#h-4a-etapa-atualiza%C3%A7%C3%A3o-dos-valores-simulados-apenas-para-simulador), o mesmo também necessita a criação de um index.

### 5º Passo - Criação da tabela de alíquotas
Alíquotas costumam ser diferentes de município para município, o primeiro passo é identificar qual é o tipo de alíquota para o município em questão. Para tal, será necessário consultar a documetação fornecida com as leis do município.
Atualmente, o sistema suporta dois tipos de alíquotas distintas, que são [IN_RANGE_ALIQUOT](https://wiki.flow.geopixel.com.br/pt-br/observatorio#in_range_aliquot) e [CUMULATIVE_ALIQUOT](https://wiki.flow.geopixel.com.br/pt-br/observatorio#cumulative_aliquot). Através da documentação, identifique qual tipo de aliquota o município se encaixa.
Caso não se encaixe em nenhum, é necessário solicitar à equipe de desenvolvimento a criação do suporte para o novo tipo de alíquota. Essas solicitações já estão previstas e são esperadas pela equipe de desenvolvimento.

Dado que um dos padrões de alíquotas atende ao município, pode-se então começar a criação e população da tabela de alíquotas.

Caso a tabela não exista, a SQL abaixo realiza sua criação:

```
CREATE TABLE public.gpx_observatory_aliquots (
	id serial4 NOT NULL,
	tipo_de_imovel varchar NOT NULL,
	mini numeric NULL,
	maxi numeric NULL,
	menor_igual numeric NULL,
	maior_igual numeric NULL,
	aliquota numeric NOT NULL,
	CONSTRAINT gpx_observatory_aliquots_pk PRIMARY KEY (id)
);
```

Para os dois tipos suportados até o momento, a tabela de alíquotas possuí o seguinte formato:

![simulador4.png](/observatory/simulador4.png){.align-center}

Onde:

- tipo_de_imovel: O tipo de imóvel no qual aquela alíquota pode ser aplicada, este valor deve ser igual a uma das possibilidades de tipo de imóvel na base de dados.
- mini: Preenchido apenas se a alíquota será aplicada caso o VVI esteja dentro da faixa entre mini e maxi. Determina o valor mínimo que o VVI esteja para entrar na faixa da alíquota.
- maxi: Preenchido apenas se a alíquota será aplicada caso o VVI esteja dentro da faixa entre mini e maxi. Determina o valor máximo que o VVI esteja para entrar na faixa da alíquota.
- menor_igual: Preenchido apenas se a alíquota será aplicada caso o VVI seja MENOR ou IGUAL ao valor indicado. Caso preenchido, os campos mini, maxi e maior_igual devem ser nulos.
- maior_igual: Preenchido apenas se a alíquota será aplicada caso o VVI seja MAIOR ou IGUAL ao valor indicado. Caso preenchido, os campos mini, maxi e menor_igual devem ser nulos.
- aliquota: Determina o valor da alíquota que será aplicada ao VVI naquela faixa estabelecida.

### 6º Passo - Configuração da tabela gpx_observatory_tables
Esta é uma tabela do sistema (metadado) que deve ser criada automáticamente, contúdo, caso não seja, a SQL abaixo realiza sua criação:

```
CREATE TABLE public.gpx_observatory_tables (
	id serial4 NOT NULL,
	table_name varchar NOT NULL,
	context varchar NOT NULL,
	CONSTRAINT gpx_observatory_tables_check CHECK (((context)::text = ANY (ARRAY[('OMI_DATABASE'::character varying)::text, ('ISOTIMA_TABLE'::character varying)::text, ('CONSTRUCTED_SQUARE_METER_VALUE_TABLE'::character varying)::text, ('ALIQUOT_TABLE'::character varying)::text, ('PHYSICAL_TABLE'::character varying)::text]))),
	CONSTRAINT gpx_observatory_tables_pk PRIMARY KEY (id),
	CONSTRAINT gpx_observatory_tables_unique UNIQUE (context)
);
```

Nesta tabela estão configuradas, identificadas por contexto, quais são as tabelas a serem utilizadas pelo sistema para cada situação.

Para o Simulador, é necessário a declaração de 3 contextos, sendo eles:

- OMI_DATABASE: Nome da view que une a tabela de geometrias de lotes com a tabela de dados dos imóveis.
- ALIQUOT_TABLE: Nome da tabela de alíquotas.
- PHYSICAL_TABLE: Nome da tabela física de dados dos imóveis. Essa declaração é utilizada para salvar os dados simulados.

Mais informações sobre essa tabela, podem ser encontradas na seção [Tabelas de configuração do módulo](https://wiki.flow.geopixel.com.br/pt-br/observatorio#tabelas-de-configura%C3%A7%C3%A3o-do-m%C3%B3dulo).

### 7º Passo - Configuração da tabela gpx_observatory_terrain_value_columns
Esta é uma tabela do sistema (metadado) que deve ser criada automáticamente, contúdo, caso não seja, a SQL abaixo realiza sua criação:

```
CREATE TABLE public.gpx_observatory_terrain_value_columns (
	id serial4 NOT NULL,
	column_alias varchar(255) NOT NULL,
	column_name varchar(255) NOT NULL,
	is_default_column bool DEFAULT false NOT NULL,
	CONSTRAINT gpx_observatory_terrain_value_columns_pkey PRIMARY KEY (id)
);
```

Esta tabela define quais colunas contêm o valor do m² do terreno do município. Ela é utilizada para popular o campo de seleção na página inicial do módulo, conforme [aqui](https://wiki.flow.geopixel.com.br/pt-br/observatorio#introdu%C3%A7%C3%A3o).

![simulador5.png](/observatory/simulador5.png){.align-center}

- column_alias: Texto que será exibido ao usuário no campo de seleção.
- column_name: Nome da coluna que aquela opção representa. Este valor fica disponível no "context" da simulação através do nome reservado "terrainValueColumnName", ficando a cargo de quem realizou a implantação fazer a utilização desse valor.
- is_default_column: Define se a opção já será previamente seleciada para o usuário ou não.

Mais informações sobre essa tabela, podem ser encontradas na seção [Tabelas de configuração do módulo](https://wiki.flow.geopixel.com.br/pt-br/observatorio#tabelas-de-configura%C3%A7%C3%A3o-do-m%C3%B3dulo).

### 8º Passo - Configuração da tabela gpx_observatory_used_attributes
Esta é uma tabela do sistema (metadado) que deve ser criada automáticamente, contúdo, caso não seja, a SQL abaixo realiza sua criação:

```
CREATE TABLE public.gpx_observatory_used_attributes (
	id serial4 NOT NULL,
	attribute_name varchar NOT NULL,
	context varchar NOT NULL,
	CONSTRAINT gpx_observatory_used_attributes_check CHECK (((context)::text = ANY (ARRAY[('ISOTIMA_ATTRIBUTE'::character varying)::text, ('IMMOBILE_DESCRIPTION_ATTRIBUTE'::character varying)::text, ('IMMOBILE_TYPE_ATTRIBUTE'::character varying)::text, ('IMMOBILE_CODE_TYPE_ATTRIBUTE'::character varying)::text, ('IMMOBILE_CLASSIFICATION_TYPE_ATTRIBUTE'::character varying)::text, ('IMMOBILE_VVI_SIMULATION_ATTRIBUTE'::character varying)::text, ('IMMOBILE_VVC_SIMULATION_ATTRIBUTE'::character varying)::text, ('IMMOBILE_VVT_SIMULATION_ATTRIBUTE'::character varying)::text, ('IMMOBILE_IPTU_SIMULATION_ATTRIBUTE'::character varying)::text, ('IMMOBILE_JOIN_ATTRIBUTE'::character varying)::text, ('IMMOBILE_SIMULATION_RESULT'::character varying)::text, ('CURRENT_YEAR_IPTU_ATTRIBUTE'::character varying)::text, ('IMMOBILE_SIMULATED_IPTU_KEY'::character varying)::text, ('IMMOBILE_PRIMARY_KEY_ATTRIBUTE'::character varying)::text]))),
	CONSTRAINT gpx_observatory_used_attributes_pk PRIMARY KEY (id),
	CONSTRAINT gpx_observatory_used_attributes_unique UNIQUE (context)
);
```

Nesta tabela são definidos nomes de colunas que são utilizados pelo módulo de Simulação.

![simulador6.png](/observatory/simulador6.png){.align-center}

Abaixo estão os atributos que devem ser declarados para o funcionamento do módulo:

- IMMOBILE_JOIN_ATTRIBUTE: Indica qual coluna será utilizada para identificar um imóvel no momento de salvamento dos resultados da simulação;
- CURRENT_YEAR_IPTU_ATTRIBUTE: Declara qual coluna da tabela OMI_DATABASE contêm o valor do IPTU base já previamento calculado;
- IMMOBILE_SIMULATED_IPTU_KEY: Define qual "variable" dentro do "context" contêm o resultado da simulação do IPTU;
- IMMOBILE_SIMULATION_RESULT: Define qual "variable" do tipo MAP dentro do "context" contêm os resultados da simulação do imóvel;
- IMMOBILE_VVC_SIMULATION_ATTRIBUTE: Define qual "variable" dentro de IMMOBILE_SIMULATION_RESULT contêm o valor do VVC da simulação. O nome dessa variable também deve ser igual ao da coluna da tabela onde será salva os resultados da simulação;
- IMMOBILE_VVI_SIMULATION_ATTRIBUTE: Define qual "variable" dentro de IMMOBILE_SIMULATION_RESULT contêm o valor do VVI da simulação. O nome dessa variable também deve ser igual ao da coluna da tabela onde será salva os resultados da simulação;
- IMMOBILE_VVT_SIMULATION_ATTRIBUTE: Define qual "variable" dentro de IMMOBILE_SIMULATION_RESULT contêm o valor do VVT da simulação. O nome dessa variable também deve ser igual ao da coluna da tabela onde será salva os resultados da simulação;
- IMMOBILE_IPTU_SIMULATION_ATTRIBUTE: Define qual "variable" dentro de IMMOBILE_SIMULATION_RESULT contêm o valor do IPTU da simulação. O nome dessa variable também deve ser igual ao da coluna da tabela onde será salva os resultados da simulação;
- IMMOBILE_PRIMARY_KEY_ATTRIBUTE: Define qual atributo será considerado a chave primária única dentro da tabela OMI_DATABASE.

**Nota: Alguns atributos dessa tabela só serão possíveis de ser preenchidos após a criação dos "steps".**

Mais informações sobre essa tabela, podem ser encontradas na seção [Tabelas de configuração do módulo](https://wiki.flow.geopixel.com.br/pt-br/observatorio#tabelas-de-configura%C3%A7%C3%A3o-do-m%C3%B3dulo).

### Passo 9º - Criação dos "steps"
Os "steps" são as etapas que serão executadas para realizar a simulação, neste ponto, o pleno entendimento da base de dados e das documentações de como são realizados os cálculos pela prefeitura são de extrema importância.
Ao todo, os steps são compostos por 3 tabelas, sendo elas:

- gpx_observatory_execution_steps: Esta tabela define a ordem em que cada step será executado, onde sua chave primária só pode ser referênciada por uma das tabelas seguintes;
- gpx_observatory_variables: Define uma "variable" a ser executada em um passo específico;
- gpx_observatory_equations: Define uma "equation" a ser executada em um passo específico.

![simulador7.png](/observatory/simulador7.png){.align-center}
![simulador8.png](/observatory/simulador8.png){.align-center}
![simulador9.png](/observatory/simulador9.png){.align-center}

Para construir um step, primeiro deve-se criar sua ordem de execução na tabela gpx_observatory_execution_steps, em seguida, escolha qual será o seu tipo, variable ou equation, e crie a entrada na tabela respectiva preenchendo suas colunas adequadamente.

Os valores de parametrização fornecidos pelo usuário, conforme explicado na seção [Simulador](https://wiki.flow.geopixel.com.br/pt-br/observatorio#simulador) são de responsabilidade de quem realiza a implantação dos steps de fazer o uso adequado deles.

Note que, ao mesmo tempo que uma "order" da tabela gpx_observatory_execution_steps só deve ser referenciada ou pela tabela gpx_observatory_variables ou pela tabela gpx_observatory_equations, também não deve existir uma order que não seja referenciada por nenhuma das duas.

Com exceção dos nomes reservados declarados [aqui](https://wiki.flow.geopixel.com.br/pt-br/observatorio#h-2a-etapa-cria%C3%A7%C3%A3o-do-context-da-simula%C3%A7%C3%A3o), caso uma variable ou equation repita o nome mais de uma vez, o seu valor será sobrescrito no "context" da simulação.

São com os steps que os cálculos e resultados são de fato realizados, de forma que atenda às especificações do município, por isso, não existe um padrão ou melhor forma de se fazer, mas atente-se que, principalmente para os steps de equations que necessitam "parsear" a equação para poder executa-lá, cada passo é realizado uma vez por imóvel encontrado na view, ou seja, para uma cidade cujo a view tenha 400 mil imóveis, o passo será executado 400 mil vezes, então para fins de performance, é aconselhado que se tente utilizar a menor quantia possível de steps.

A SQL abaixo pode ser utilizada para ter uma visão mais clara de todos os steps já criados, ordenados pela sua ordem de execução:

```
select * from gpx_observatory_execution_steps goes
	left join gpx_observatory_variables gov on goes.id = gov.gpx_observatory_execution_steps_id
	left join gpx_observatory_equations goe on goes.id = goe.gpx_observatory_execution_steps_id
	order by goes.step_order asc;
```

Mais informações sobre essas tabelas, podem ser encontradas na seção [Tabelas de configuração do módulo](https://wiki.flow.geopixel.com.br/pt-br/observatorio#tabelas-de-configura%C3%A7%C3%A3o-do-m%C3%B3dulo).
Para os steps do tipo variable, consulte as seções [Custom Properties](https://wiki.flow.geopixel.com.br/pt-br/observatorio#custom-properties) e [Context](https://wiki.flow.geopixel.com.br/pt-br/observatorio#h-2a-etapa-cria%C3%A7%C3%A3o-do-context-da-simula%C3%A7%C3%A3o).
Para as alíquotas e seus comportamentos, consulte a seção [Tabela de Alíquotas](https://wiki.flow.geopixel.com.br/pt-br/observatorio#tabela-de-aliquotas).
Para steps do tipo equation e como declarar uma equação, consulte a seção [Equações](https://wiki.flow.geopixel.com.br/pt-br/observatorio#equa%C3%A7%C3%B5es).
Para a criação de condições de execução de um step, consulte a seção [Condições de execução](https://wiki.flow.geopixel.com.br/pt-br/observatorio#condi%C3%A7%C3%B5es-de-execu%C3%A7%C3%A3o).

### 10º Passo - Escolha ou criação do perfil que terá acesso ao módulo
Realize a criação do perfil ou escolha um já existente que terá acesso ao módulo de simulação.

### 11º Passo - Configuração das "functionalities" do perfil
Existem 2 functionalities que devem ser atribuidas ao perfil que terá acesso à simulação, elas são:

- OBSERVATORY_MODULE_TOOL: Faz com que o módulo esteja visível ao usuário no perfil em questão na barra da esquerda, com o nome "Observatório";
- PGV_TAB: Disponibiliza ao usuário o botão responsável para abrir a interface de configuração e utilização da simulação;

### 12º Passo - Configuração do tema do observatório
Crie um novo tema, o associando ao perfil cujo terá acesso à simulação, para este tema, defina como a tabela tabular e a geometrica, a view criada no [3º Passo](https://wiki.flow.geopixel.com.br/pt-br/observatorio#h-3o-passo-cria%C3%A7%C3%A3o-da-view-da-base-de-dados).
Associe esse tema ao contexto de temas **GPX_THEME_CONTEXT_OBSERVATORY_MODULE**.
Realize também toda a configuração comum de temas, como dicionários, permissões, mapa, parâmetros e etc., se atentando também com as configurações do GeoServer.

O tema em questão será utilizado também para a geração de dashboards, por isso, os atributos de VVT, VVC, VVI e IPTU simulados devem ser visiveis ao usuário, bem como as informações cálculadas diretamente pela view referente à porcentagem de aumento ou redução de IPTU e tipo de alteração também.

### 13º Passo - Associe o perfil aos usuários desejados
Escolha os usuários que deverão ter acesso ao perfil e faça a associação dos mesmos.

### Finalização e possíveis erros
Após a conclusão dos passos acima, será possível realizar os testes adequados para a validação da implantação do módulo de simulação.
Caso ocorra algum problema durante a simulação, a mesma será interrompida e o erro pode ser visualizado ao acessar a máquina e acessar os logs do servidor Tomcat no arquivo catalina.out.

Nem sempre a base de dados pode estar 100% correta, alguma coluna de um registro em específico pode conter um valor inesperado e causar um problema durante a execução dos steps que resulte na simulação sendo abortada, sendo necessário visualizar o log de erros do servidor para entender o que aconteceu. Para esses casos, o indicado é tentar corrigir pontualmente o registro com erro, ou excluí-lo da base de dados.

# Passo a passo implantação do módulo de Calculadoras
Adiante estão os passos para a implantação do módulo de Calculadoras do Observatório. Dado o conhecimento prévio sobre o módulo explicado em Simulador, alguns termos e referências serão mencionados no guia.

O módulo de Calculadoras depende diretamente da correta configuração do módulo de Simulação, pois utiliza a mesma sequência de *steps* para realizar os cálculos, por isso, certifique-se antes que os steps estão devidamente configurados e funcionais.

### 1º Passo - Definição das informações que serão exibidas na calculadora
Antes iniciar, faça uma lista das informações que vem ser exibidas na calculadora, como quais dados do imóvel devem estar disponíveis, quais campos serão editáveis e etc.

### 2º Passo - Configuração das "functionalities" do perfil
Para cada calculadora, IPTU e ITBI, existe uma functionality que deve ser associada ao perfil para que o usuário consiga visualizar o botão para abrir a calculadora, essas functionalities devem ser associadas ao perfil adequada para isso, sendo elas:
- OBSERVATORY_CALCULATOR_IPTU: Functionality para associar a calculadora de IPTU ao perfil;
- OBSERVATORY_CALCULATOR_ITBI: Functionality para associar a calculadora de ITBI ao perfil;

### 3º Passo - Configuração da tabela da interface das calculadoras
A interface e componentes exibidos ao usuário durante a utilização de uma calculadora é montada através da leitura dos componentes descritos na tabela *gpx_calculator_interface_description*, com a lista definida, comece a inserção dos dados na tabela para declarar os componentes de interface.

A descrição de o que são cada coluna na tabela e como preencher seus valores podem ser vistas na seção [Tabelas do módulo](https://wiki.flow.geopixel.com.br/pt-br/observatorio#tabelas-de-configura%C3%A7%C3%A3o-do-m%C3%B3dulo).

### 4º Passo - Testes e validações
Faça os testes necessários e as validações cabiveis para certificar-se de que tudo está funcionando como o esperado.