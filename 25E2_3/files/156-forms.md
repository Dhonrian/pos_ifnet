---
title: Implantação de Formulários do 156
description: Este documento visa auxiliar na implantação de formulários para o 156 definindo o que é necessário para a implantação do mesmo
published: true
date: 2025-04-08T18:45:35.830Z
tags: formulario, 156, mobilidade, mobile
editor: markdown
dateCreated: 2024-06-04T11:04:10.014Z
---

# 156 - Implantação de Formulários

O projeto do 156 está passando por uma reestruturação que permitirá um funcionamento similar ao que possuímos com o Mobilidade e Cidades. O mesmo possuirá uma tabela específica para a definição de formulários que aparecerão para seleção dos usuários sendo possível definir, editar e remover formulários sem a necessidade de gerar uma nova versão da aplicação.


--- 

## Tabela de Formulários

A nova tabela se chama `app_156_forms`. Com a definição de uma nova tabela separada do Cidades e Mobilidade torna possível um fluxo diferente para cada etapa do processo de um mesmo `tema`. Então o fluxo poderá tramitar entre 156, Cidades e Mobilidade com um formulário que contenha apenas as informações relevantes para cada etapa do processo.

Essa nova tabela segue uma estrutura similar a que já conhecemos porém com alguns campos necessários para a exibição correta para o 156. Abaixo segue um descritivo de cada coluna presente:


| Coluna    							| Descrição 																																																													|
| ----------------------	| ----------------------------------------------------------------------------------------------------------------------------		|
| form_name  								| O nome que aparecerá para o usuário na listagem de requisições. (Poda de árvores, Cata Bagulho, Ilum. Pública)    																																																									|
| form_description 					| Em uma versão futura do projeto, este campo será utilizado como um descritivo do serviço    																													 				|
| theme_id    						| O número do tema implantado para o tipo de solicitação (Poda de árvores, Cata Bagulho)    		|
| sla_in_days 				| Um campo que definirá o período em dias corridos que a prefeitura se compromete com a realização do serviço. 																																																	|
| form_json 	| Campo contendo o formulário que o usuário irá de fato preencher para a requisição. A estrutura é a mesma utilizada no Cidades e Mobilidade 																																																															|
| \*base64_icon 	| Os formulários do 156 possuem um ícone/foto que aparecerão ao lado do nome do formulário. Esse ícone deve ser convertido em base64 no formato de data-uri   																																																															|
| expire_date | Este campo é importante para quando a prefeitura não quer mais oferecer um serviço para os usuários. Caso esteja preenchido com a data de expiração o mesmo não aparecerá na listagem de serviços |

\* Pode ser utilizado o site [base64guru] para a conversão de imagens para base64 no formato necessário


<details>
<summary> Visualização de Formulários 156 </summary>
  
  Lista de formulários disponíveis e seus ícones
  ![156_available_forms.png](/156/156_available_forms.png)
  
  Lista com todas as requisições do usuário
  ![156_user_requests.png](/156/156_user_requests.png)
  
</details>


## 156, Cidades e Mobilidade

É necessário que a solicitação do usuário seja possível tramitar entre o 156, Cidades e o Mobilidade. Para que isso seja possível, todos devem apontar para uma mesma tabela que representa os dados tabulares do tema. Caso possível, o ideal seria que todos possuam o mesmo ID do tema, dessa forma uma foto tirada em campo pela prefeitura através do aplicativo Mobilidade ficará disponível para a visualização do requerente nas informações da requisição.

Vale ressaltar que as informações que estarão disponíveis para a visualização do requerente na página da solicitação tem de ser definidas como `popup` na `app_permissao`.

<details>
<summary> Página com a solicitação concluída </summary>
  
  Informações da solicitação finalizada e Feedback para avaliação
  ![156_user_request_data.png](/156/156_user_request_data.png)
  
</details>

## Estrutura obrigatória para temas do 156

Assim como a tabela do Mobilidade necessita de alguns campos para o funcionamento correto, (gid, geom, done), o 156 também necessita de colunas específicas e algumas são compartilhadas entre o Mobilidade:

| Coluna    							| Tipo | Descrição |
| ----------------------	| ---- | --- |
| gid | serial int | Será a chave primária para identificação da requisição|
| protocol | varchar | Será utilizado para preencher automaticamente pelo SIG o valor de protocolo para o tema ou integração|
| geom | geometry(3857) | Será a informação geométrica para indicar o local onde a requisição deve ser atendida|
| done | boolean | Usado para exibição do status da solicitação para o requerente|
| userid | int | Usado para exibição do status da solicitação para o requerente|
| nome | varchar | Utilizado para armazenar informação de identificação do requerente|
| cpf | varchar | Utilizado para armazenar informação de identificação do requerente|
| email | varchar | Utilizado para armazenar informação de identificação do requerente|
| rua | varchar | Informação que será preenchida automaticamente caso a cidade tenha suporte ao Geocoding reverso|
| numero | varchar | Informação que será preenchida automaticamente caso a cidade tenha suporte ao Geocoding reverso|
| bairro | varchar | Informação que será preenchida automaticamente caso a cidade tenha suporte ao Geocoding reverso|
| telefone | varchar | Utilizado para armazenar informação de identificação do requerente|
| rating | int | Armazenará a avaliação do requerente após a finalização da solicitação pela prefeitura ou o prazo de SLA tenha sido excedido|
| status_ocorrencia | varchar | Controle da prefeitura sobre o status da solicitação, sendo obrigatório um valor 'default' para indicar o andamento da solicitação para o requerente|
| device_token | varchar | Identificador que será utilizado para envio de notificações push|

### Formulários

Os formulários do 156 seguem o mesmo padrão do Cidades e Mobilidade, porém sem qualquer suporte à `functionSpecific`. O formulário segue apenas a estrutura básica e todos eles devem seguir um padrão onde no topo ficará as informações do requerente (nome, email, cpf e telefone) e o resto será os campos específicos para a solicitação que serão definidos pela prefeitura.

<details>
<summary> Exemplo de Formulário </summary>

```json
	{
  	"divisions": [
      {
        "content": [
          {
            "text": "Dados da Ocorrência",
            "id": "dado",
            "alignment": "center",
            "font": "title3"
          },
          {
            "text": "placeholder$$$###!@#",
            "id": "placeholder",
            "required": true,
            "alignment": "center",
            "font": "title4"
          },
          {
            "field": "Nome",
            "id": "nome",
            "required": true,
            "width": 70,
            "events": [
              "input=validate:required",
              "beforeprint=validate:required"
            ]
          },
          {
            "field": "Telefone",
            "id": "telefone",
            "required": true,
            "width": 30,
            "mask": "set::phone",
            "events": [
              "input=validate:required"
            ]
          },
          {
            "field": "CPF",
            "id": "cpf",
            "required": true,
            "width": 35,
            "mask": "set::cpf",
            "events": [
              "input=validate:cpf",
              "input=validate:required"
            ]
          },
          {
            "field": "Email",
            "id": "email",
            "required": true,
            "width": 65,
            "events": [
              "input=validate:required"
            ]
          },
          {
            "selectlist": "A Árvore está perto da rede elétrica",
            "id": "nearelectric",
            "required": true,
            "width": 30,
            "options": "Não;Sim"
          },
          {
            "selectlist": "A Árvore está em via pública",
            "id": "viapublic",
            "required": true,
            "width": 30,
            "options": "Não;Sim"
          },
          {
            "textarea": "Observações",
            "id": "obs",
            "width": 100,
            "heigth": 100
          },
          {
            "text": "Dados da Localização",
            "id": "placeholder2",
            "required": true,
            "alignment": "center",
            "font": "title4"
          },
          {
            "field": "Rua",
            "id": "rua",
            "required": true,
            "width": 70,
            "events": [
              "input=validate:required",
              "beforeprint=validate:required"
            ]
          },
          {
            "field": "Número",
            "id": "numero",
            "required": true,
            "mask": "set::number",
            "width": 30,
            "events": [
              "input=validate:number",
              "input=validate:required"
            ]
          },
          {
            "field": "Bairro",
            "id": "bairro",
            "required": true,
            "width": 50,
            "events": [
            "input=validate:required"
            ]
          }
      	]
  		}
		]
	}
```


[base64guru]: https://base64.guru