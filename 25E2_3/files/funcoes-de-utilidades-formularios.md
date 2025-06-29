---
title: Funções de utilidades para formulários
description: Nesta página estão documentadas as funções que podem ser utilizadas nos formulários a fim de entregar alguma funcionalidade ou comportamento específico ao usuário utilizando um formulário
published: true
date: 2025-05-13T00:40:15.862Z
tags: alvara, fluxo, formulario, json, funcionamento, funcao, função, funcão, funçao, form, formulário, util, utils, utilidade, utilidades, comportamentos, comportamento, obras
editor: markdown
dateCreated: 2024-09-16T19:57:10.026Z
---

# Introdução
Nesta página estão documentadas as funções JavaScript que podem ser utilizadas nos formulários das aplicações do Fluxo/Alvará, funções estas que entregam novas funcionalidades ao usuário utulizando um formulário.

## Funções
Abaixo estão documentadas as funções disponíveis para utilização nos formulários, bem como exemplos de utilização e observações necessárias em cada uma delas.
A compreenção adequada pode exigir um certo conhecimento técnico, em caso de dúvidas, consulte algum desenvolvedor da equipe do Fluxo.

### copyInputValue
Funcionalidade: Copia o valor de um input para outro.
Parâmetros:
- `sourceInputId: string`: ID do input no qual o valor será pego.
- `targetInputId: string`: ID do input no qual o valor pego será colocado.

Retorno da função: `void`

Assinatura da função: `copyInputValue(sourceInputId: string, targetInputId: string): void`  
                
Observações: A função checa se os IDs fornecidos apontam para elementos que existam no HTML, caso não existam, a operação é abortada silenciosamente. Caso os IDs apontem para elementos que existam no HTML, a função checa se esses elementos são do tipo `<input>`, caso um deles não seja, a operação é abortada silenciosamente.

Exemplo de uso:
>     {
>       "button": "Copiar valores",
>       "id": "copiar_valores",
>       "name": "copiar_valores",
>       "color": "red",
>       "width": 10,
>       "attributes": [
>         "onclick=copyInputValue('inputValor', 'inputAlvo')"
>       ]
>     }

### calculateRegularizationAreaResume
Funcionalidade: Realiza o calculo do quadro de áreas de regularização, aplicando a formula esperada aos valores das áreas.
Parâmetros:
- `areaInformationDiscriminator: string`: ID do quadro de áreas, usado para identificar os quadros pertencentes à aquele quadro
- `existentTotalAreaInputId: string`: ID do input onde deverá ser exibido a soma final dos quadros de área existente
- `newConstructionTotalAreaInputId: string`: ID do input onde deverá ser exibido a soma final dos quadros de obra nova
- `additionTotalAreaInputId: string`: ID do input onde deverá ser exibido a soma final dos quadros de área de acréscimo
-	`demolitionTotalAreaInputId: string`: ID do input onde deverá ser exibido a soma final dos quadros de área de demolição
- `reformTotalAreaInputId: string`: ID do input onde deverá ser exibido a soma final dos quadros de área de reforma
- `totalAreaInputId: string`: ID do input onde deverá ser exibido o calculo final de área total do quadro de obras

Retorno da função: `void`

Assinatura da função: `calculateRegularizationAreaResume(areaInformationDiscriminator: string, existentTotalAreaInputId: string, newConstructionTotalAreaInputId: string, additionTotalAreaInputId: string,
	demolitionTotalAreaInputId: string, reformTotalAreaInputId: string, totalAreaInputId: string): void`
  
Observações: A função faz certas validações, como se os IDs fornecidos existem ou se o valor inserido pelo usuário é valido nos campos de áreas de cada quadro e, em caso de problemas, a execução da mesma é abortada.

Exemplo de uso:
>     {
>       "button": "Calcular resumo de áreas",
>       "id": "calculate_areas_resume",
>       "name": "calculate_areas_resume",
>       "color": "yellow",
>       "width": 33,
>       "attributes": [
>           "onclick=calculateRegularizationAreaResume('QUADRO_AREAS','area_existente_total','area_nova_total', 'area_ampliada_total', 'area_demolida_total', 'area_reformada_total', 'area_total_construcao')"
>       ]
>     }

### calculateToBuildAreaResume
Funcionalidade: Realiza o calculo do quadro de áreas de regularização, aplicando a formula esperada aos valores das áreas.
Parâmetros:
- `areaInformationDiscriminator: string`: ID do quadro de áreas, usado para identificar os quadros pertencentes à aquele quadro
- `existentSourceInputValueId: string`: ID do input de onde o valor da área existente total será obtido e utilizado no calculo
- `existentTotalAreaInputId: string`: ID do input onde deverá ser exibido o valor copiado da área existente total obtido pelo parâmetro `existentSourceInputValueId`
- `newConstructionTotalAreaInputId: string`: ID do input onde deverá ser exibido a soma final dos quadros de obra nova
- `additionTotalAreaInputId: string`: ID do input onde deverá ser exibido a soma final dos quadros de área de acréscimo
-	`demolitionTotalAreaInputId: string`: ID do input onde deverá ser exibido a soma final dos quadros de área de demolição
- `reformTotalAreaInputId: string`: ID do input onde deverá ser exibido a soma final dos quadros de área de reforma
- `totalAreaInputId: string`: ID do input onde deverá ser exibido o calculo final de área total do quadro de obras

Retorno da função: `void`

Assinatura da função: `calculateToBuildAreaResume(areaInformationDiscriminator: string, existentSourceInputValueId: string, existentTotalAreaInputId: string, newConstructionTotalAreaInputId: string, additionTotalAreaInputId: string,
	demolitionTotalAreaInputId: string, reformTotalAreaInputId: string, totalAreaInputId: string): void`
  
Observações: A função faz certas validações, como se os IDs fornecidos existem ou se o valor inserido pelo usuário é valido nos campos de áreas de cada quadro e, em caso de problemas, a execução da mesma é abortada.

Exemplo de uso:
>     {
>       "button": "Calcular resumo de áreas",
>       "id": "calculate_areas_resume",
>       "name": "calculate_areas_resume",
>       "color": "yellow",
>       "width": 33,
>       "attributes": [
>           "onclick=calculateToBuildAreaResume('QUADRO_AREAS_construir','area_existente_total', 'area_existente_total_construir', 'area_nova_total_construir', 'area_ampliada_total_construir', 'area_demolida_total_construir', 'area_reformada_total_construir', 'area_total_construcao_construir')"
>       ]
>     }

### replicableSum
Funcionalidade: Faz o somatório de um campo replicável e insere o valor em um campo de resultado.
Parâmetros:
- `parcelaId: string`: ID do input replicável que deseja-se fazer o somatório
- `totalId: string`: ID do input no qual o valor do somatório será colocado.

Retorno da função: `void`

Assinatura da função: `replicableSum(parcelaId: string, totalId: string): void`             

Exemplo de uso:
>     {
>       "button": "Somar valores",
>       "id": "somar_valores",
>       "name": "somar_valores",
>       "color": "red",
>       "width": 10,
>       "attributes": [
>         "onclick=replicableSum('id_input_parcela', 'id_input_total')"
>       ]
>     }

### setFieldState
Funcionalidade: altera o estado de um campo com base na opção escolhida de um campo selectlist.

Parâmetros:

- `selectFieldContext: HTMLElement`: parâmetro que recebe o próprio elemento HTML (this);
- `optionValue: string`: o valor que será comparado com o valor atual do selectFieldName;
- `targetFields: string`: ID's dos campos que terão o estado alterado.

Retorno da função: `void`.

Assinatura da função: `setFieldState(selectFieldContext: HTMLElement, optionValue: string, targetFields: string);`

Exemplo de uso:

>     {
>      	"selectlist": "Select",
>      	"id": "select_option_id",
>      	"name": "select_option_name",
>      	"options": ";Opção 1;Opção 2;Opção 3",
>      	"width": 30,
>      	"attributes": [
>       		"onchange=setFieldState(this, 'Opção 2', ['campo_1_id', 'campo_2_id']);"
>      	]
>      }



### loginIntegration
###
Funcionalidade: Preenche um campo com o login do usuário e executa o que estiver no "onchange" desse campo.

Finalidade: A função foi criada para atender a demanda dos sistemas de fluxo de atendimento digital, onde usuários são criados automaticamente com o nº da inscrição municipal como login.

Parâmetros:
- `field_id: string`: ID do input que será preenchido com o usuário do login

Retorno da função: `void`

Assinatura da função: `loginIntegration(field_id: string): void`             

Exemplo de uso: Digamos que em um sistema de fluxo, onde o CPF é o login dos usuários do sistema, exista esse campo de CPF que faz a validação do cpf via integração com a Serpro:
>     {
>      	"field": "CPF*",
>      	"id": "cpf_id",
>      	"name": "cpf_name",
>      	"width": 30,
>      	"attributes": [
>       		 "onchange=setValuesSerproCpf(this);"
>      	]
>      }

Para fazer o preenchimento automático do campo com o login e executar a integração configurada no onchange (setValuesSerproCpf(this)) a partir de um botão, basta adicionar o seguinte botão no formulário:

>     {
>      	"button": "Exemplo",
>      	"id": "button_id",
>      	"name": "button_name",
>      	"width": 30,
>      	"attributes": [
>       		 "onclick=loginIntegration('cpf_id');"
>      	]
>      }



### buscaInscricaoCPFCNPJ
Funcionalidade: Consulta se o CNPJ informado já possui cadastro na Prefeitura. Se confirmado, o requerente é notificado e redirecionado à página inicial.

Finalidade: Função que evita o recadastramento de um mesmo CNPJ, prevenindo duplicidade de inscrição municipal nos sistemas de funcionamento.

Parâmetros:

- `obj: HTMLElement`: parâmetro que recebe o próprio elemento HTML (this);
- `tma_id: string`: Tema que acessa a base de empresas da prefeitura (geralmente de integração);
- `col_cnpj: string`: Coluna da tabela de empresas que guarda o CNPJ.
- `col_inscricao: string`: Coluna da tabela de empresas que guarda a inscrição municipal.
- `col_situacao: string`: Coluna da tabela de empresas que guarda a situação do cadastro.
- `situacoes_validas: string`: situações de cadastro que permitem que a empresa seja cadastrada no município novamente. podem ser inseridas mais de uma situação, separadas por virgula.


Retorno da função: `void`.

Assinatura da função: `buscaInscricaoCPFCNPJ(obj: HTMLElement, tma_id: string, col_cnpj: string, col_inscricao: string, col_situacao: string, situacoes_validas = '': string);`

Exemplo de uso:

>       {
>            "field": "CNPJ*",
>            "id": "cnpj_id",
>            "name": "cnpj_name",
>            "required": true,
>            "hint": "Digite o CNPJ",
>            "mask": "cnpj",
>            "width": 32,
>            "attributes": [
>                 "onchange=buscaInscricaoCPFCNPJ(this,'1146','cpf_cnpj','inscricao_municipal','situacao','Inativo');"
>            ]
>        },