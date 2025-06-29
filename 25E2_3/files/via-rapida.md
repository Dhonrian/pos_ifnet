---
title: Integração JUCESP/REDESIM - Via Rápida
description: Esta página contêm as funcionalidades da integração com o sistema da JUCESP para os serviços do Via Rápida, bem como as configurações necessárias para sua disponibilidade nos clientes
published: true
date: 2024-07-01T15:52:50.861Z
tags: configuração, alvara, fluxo, integração, via, rapida, via rapida, jucesp, redesim, via rapida jucesp, via rapida redesim, integracao, funcionalidade, funcionalidades, configuracao
editor: markdown
dateCreated: 2024-06-24T12:18:19.184Z
---

# Funcionalidades Via Rápida
A integração com o sistema da JUCESP/REDESIM para o serviço do Via Rápida disponibiliza aos clientes uma interface dentro do sistema do fluxo capaz de realizar as ações necessárias que a prefeitura normalmente faz utilizando o próprio site da JUCESP.

Para as prefeituras configuradas para permitir a integração, as funcionalidades podem ser acessadas no **Painel de Administração**, conforme as imagens abaixo exemplificando o caminho:

![hamburguer-painel-administracao.png](/via-rapida/hamburguer-painel-administracao.png){.align-center}
![hamburguer-admin.png](/via-rapida/hamburguer-admin.png){.align-center}
![home-via-rapida.png](/via-rapida/home-via-rapida.png)

Ressaltando que, esta interface está disponível apenas para usuários no perfil de **Administrador**.

## Inscrição Municipal
A inscrição municipal é uma funcionalidade que permite a prefeitura informar o número de funcionamento para um estabelecimento.
Para tal, é necessário acessar sua respectiva interface, realizar a pesquisa por protocolo, CNPJ ou um intervalo de data da solicitação, selecionar uma solicitação na tabela de resultados e clicar no botão para informar o número de inscrição.

### Tela de pesquisa
![home-insc-mun.png](/via-rapida/home-insc-mun.png){.align-center}
Nesta interface, o usuário deve pesquisar a solicitação que deseja informar o número de inscrição por uma das três formas de pesquisa:
- Protocolo: Deve informar um número de protocolo conhecido para encontrar a respectiva solicitação
- CNPJ: Deve informar um CNPJ válido que tenha uma solicitação de inscrição municipal
- Data: O Usuário deve escolher um intervalo de datas de no máximo *7 dias* entre a data inicial e final, por exemplo, entre 07/01 até 14/01

Após a escolha do método de pesquisa, o usuário pode clicar no botão **Pesquisar** para solicitar a consulta.

### Resultado da consulta
Após uma consulta com sucesso, será exibida ao usuário a tabela abaixo com as solicitações encontradas:

![pesquisa-insc-mun.png](/via-rapida/pesquisa-insc-mun.png){.align-center}

Aqui, o usuário deve escolher sobre qual solicitação deseja trabalhar, para isso basta clicar no *botão rádio* na coluna *Selecionar* da tabela.
Após a escolha da solicitação, o usuário tem três opção para seguir, cada uma com seu respectivo botão:
- Criar processo: Ao clicar neste botão, o usuário poderá criar um processo comum da ferramenta do fluxo, onde ele pode seguir com os procedimentos formais para a avaliação da solicitação de inscrição municipal.
 ***Não é obrigatório a criação de um processo para informar a análise.***
- Informar análise: Ao clicar aqui, o usuário terá acesso a uma janela onde o mesmo pode informar o resultado da análise da inscrição municipal.
- Link/botão *Consultar* na tabela: Ao clicar aqui, o usuário será redirecionado para uma outra página contendo as informações disponibilizadas pela JUCESP sobre a solicitação de inscrição municipal.

### Janela de informar análise
Ao clicar no botão *Informar análise*, a seguinte janela será aberta ao usuário

![informar-analise-insc-mun.png](/via-rapida/informar-analise-insc-mun.png){.align-center}

O usuário então deve selecionar qual será o resultado da análise, conforme as opções abaixo:

![opcoes-informar-analise.png](/via-rapida/opcoes-informar-analise.png){.align-center}

- Aprovada: Caso o usuário deseje aprovar a solicitação de inscrição municipal e informar o número da mesma, deve-se utilizar está opção.
- Indeferida: Utilizada para casos onde deseja-se negar a solicitação de inscrição municipal.
- Não se aplica: Para as situações onde não cabe a informação da inscrição municipal.

#### Aprovada
![aprovada.png](/via-rapida/aprovada.png){.align-center}

Nesta opção, o usuário deve obrigatóriamente informar o número da inscrição municipal e uma justificativa.
Deve se atentar ao número da inscrição, pois **apenas números são permitidos**, qualquer outro caractér será considerado inválido.

#### Indeferida
![indeferida.png](/via-rapida/indeferida.png){.align-center}

Aqui, o usuário deve informar, obrigatóriamente, apenas uma justificativa para o indeferimento.

#### Não se aplica
![nao-se-aplica.png](/via-rapida/nao-se-aplica.png){.align-center}

Em casos onde informar a inscrição municipal não se aplica, não é necessário nenhuma informação complementar para finalizar a análise.

Após qualquer uma das ações sendo tomadas, a solicitação de inscrição municipal será considerada como concluída no sistema da JUCESP.


## Licenciamento
A integração de Licenciamento com a JUCESP permite ao usuário avaliar uma solicitação de licenciamento e informar um parecer sobre a mesma, permitindo assim a geração da CLI com a resposta da prefeitura.

![licenciamento.png](/via-rapida/licenciamento.png){.align-center}

### Consulta
Seguindo pelo caminho da consulta, o usuário é levado até a tela abaixo, onde o mesmo pode escolher a forma na qual quer encontrar os pedidos de licenciamento disponíveis

![consulta.png](/via-rapida/consulta.png){.align-center}

Nesta interface, o usuário deve pesquisar a solicitação que deseja consultar por uma das três formas de pesquisa:
- Protocolo: Deve informar um número de protocolo conhecido para encontrar a respectiva solicitação
- CNPJ: Deve informar um CNPJ válido que tenha uma solicitação de inscrição municipal
- Data: O Usuário deve escolher um intervalo de datas de no máximo *1 dia* entre a data inicial e final, por exemplo, entre 07/01 até 08/01

Feito a pesquisa, caso um resultado tenha sido encontrado, a seguinte tabela será apresentada na interface

![consulta-resultado.png](/via-rapida/consulta-resultado.png){.align-center}

A tabela apresenta algumas informações básicas dos pedidos de licenciamento e mais detalhes podem ser vistos clicando no link "Ver detalhes" no pedido que se deseja saber mais

![consulta-detalhes.png](/via-rapida/consulta-detalhes.png){.align-center}

### Análise
Com a análise, o usuário pode informar um parecer ou desfecho sobre a solicitação de licenciamento após a análise do mesmo.

Ao escolher a opção de análise, a seguinte tela será apresentada

![analise.png](/via-rapida/analise.png){.align-center}

Nesta interface, o usuário deve pesquisar a solicitação que deseja analisasr por uma das três formas de pesquisa:
- Protocolo: Deve informar um número de protocolo conhecido para encontrar a respectiva solicitação
- CNPJ: Deve informar um CNPJ válido que tenha uma solicitação de inscrição municipal
- Data: O Usuário deve escolher um intervalo de datas de no máximo *1 dia* entre a data inicial e final, por exemplo, entre 07/01 até 08/01

Feito a pesquisa, caso um resultado tenha sido encontrado, a seguinte tabela será apresentada na interface

![analise-consulta.png](/via-rapida/analise-consulta.png){.align-center}

Na tabela, o usuário pode expandir uma das linhas para ver mais algumas informações sobre a solicitação.

Para prosseguir, deve-se escolher qual solicitação dejesa analisar clicando no *botão rádio* da coluna Selecionar na tabela, e em seguida clicar no botão Prosseguir

![analise-detalhes.png](/via-rapida/analise-detalhes.png){.align-center}

Na tela seguinte, mais informações estão disponíveis sobre a solicitação, bem como as ações que podem ser realizadas.
Na tabela de Licenças disponíveis, estarão exibidas as licenças já concluídas ou solicitadas pelo requerente da solicitação e, dentre elas, a licença da prefeitura.

Note que, apenas a licença pertinente à prefeitura poderá ser selecionada e sofrer uma ação, todas as outras estarão descritas com "Não se aplica" no lugar do *botão rádio*

Após a seleção da licença da prefeitura, alguma ação pode ser realizada sobre ela, baseado na situação atual da licença.

- Pendente de interação no orgão: Nesta situação, após selecionar a licença, o usuário obrigatóriamente deve clicar no botão Criar processo, para que um processo de análise da solicitação de licenciamento seja criado. Neste momento, o sistema da Geopixel informará ao sistema da JUCESP que a solicitação está sendo análisada pela prefeitura.
***Este passo é obrigatório.***
- Em andamento no orgão: Nesta situação, o processo interno já foi criado e agora é necessário informar um parecer sobre a situação da solicitação. O usuário deve escolher a ação Informar licença e clicar no botão Informar licença para avançar para a próxima tela.
- Deferida: Significa que a licença foi emitida com sucesso e um número e data de válidade foi informado à JUCESP.
- Indeferida: A solicitação foi recusada pela prefeitura, e o requerente deverá entrar com um novo pedido de licenciamento, caso queira que seja análisado novamente.
- Cassada: A licença emitida foi cassada pela prefeitura e o solicitante deve regularizar a situação de seu estabelecimento junto à prefeitura.
- Cassação liberada: Após a regularização na prefeitura de uma solicitação cassada, a cassação é liberada e o requerente pode fazer uma nova solicitação.

Mediante a situação do pedido de licenciamento, o usuário deve escolher a ação adequada a ser aplicada, conforme as opções abaixo.

![acoes.png](/via-rapida/acoes.png){.align-center}

*Antes de realizar qualquer ação, caso a situação da licença seja **Em andamento no orgão**, é necessário realizar a criação do processo interno para a análise da solicitação de licenciamento, conforme descrito no tópico acima sobre situações.*


- Informar Licença: Para informar o parecer da análise de uma licença que se encontra na situação Em andamento no orgão, deve-se escolher essa opção e seguir para a tela seguinte.
- Cassar Licença: Só é possível cassar uma licença que tenha sido deferida com sucesso, para isso, a situação da licença deve ser a de *Deferida*
- Liberar Licença Cassada: Após a regularização de uma licença cassada, a sua liberação deverá ocorrer para que o requerente possa entrar com uma nova solicitação de licenciamento, para tal ação, é necessário que a licença esteja na situação de *Cassada*

#### Informar Licença
Após selecionar a ação de Informar Licença, a tela abaixo será apresentada

![informar.png](/via-rapida/informar.png){.align-center}

Informar uma licença consiste em deferir, ou seja, liberar e informar a data de validade e o número da licença, ou indeferir, retornar ao requerente que a licença não está apta a ser utilizada, para isso, deve-se escolher a opção correspondente no menu de seleção de Ação pendente

![analise-informar.png](/via-rapida/analise-informar.png){.align-center}

Após a seleção de qual será o desfecho, o usuário deve clicar no botão Confirmar para que seja apresentado o modal correspondente

#### Informar Licença (Emissão)
![emissao.png](/via-rapida/emissao.png){.align-center}

Neste modal, o usuário necessita informar o número da licença que será emitida, bem como a data de validade da licença que, por padrão é de três anos, mas pode ser alterada.
Caso a licença tenha alguma restrição quanto ao funcionamento, na tabela abaixo é possível escolher as restrições a serem atreladas ao licenciamento.
Após isso, basta no final da página clicar no botão de confirmar para que a licença seja emitida.

#### Informar Licença (Irregularidade)
![irregularidade.png](/via-rapida/irregularidade.png){.align-center}

Caso a licença deva ser negada, neste modal o usuário poderá fazer isso, para tal, deve-se informar ao menos um motivo para a negação do pedido de licenciamento.
Após a escolha dos motivos, basta clicar no botão de salvar ao final da página, resultando no retorno da solicitação ao solicitante.

#### Cassar Licença
Para cassar uma licença, deve-se escolher a opção de cassar no menu de ações da licença.
Feito a escolha, um modal irá se abrir onde o usuário deve escolher os motivos da cassação, sendo obrigatório ao menos um motivo.
Feito a escolha dos motivos, basta clicar no botão de confirmação ao fim da página para realizar a cassação.

#### Liberar Licença Cassada
Para liberar a cassação de uma licença, deve-se escolher a opção de liberação de licença cassada no menu de ações da licença.
Após a seleção da ação, o usuário será encaminhado para uma nova página, com algumas informações sobre a situação da licença e, ao fim dela, um botão para realizar a liberação definitiva.
Ao clicar no botão ao fim da página, a cassação será liberada e o requerente poderá entrar com um novo pedido de solicitação de licença.

# Configurações Via Rápida

Todo município que já trabalhe com o sistema da JUCESP realizando as ações diretamente na página da própria JUCESP está elegível para utilizar a integração no sistema da Geopixel, bastando solicitar à JUCESP as credenciais de acesso à eles.

Tendo as devidas permissões da prefeitura para utilização da integração, é então necessário realizar algumas configurações na aplicação de modo a integração funcionar corretamente.

## Váriaveis do arquivo de configuração
As variáveis referentes à integração do Via Rápida estão descritas [aqui](/alvara/configuracao-txt#configurações-da-integração-via-rápida).

## Configurações no banco de dados
A configuração do banco de dados se faz necessária para que seja possível a criação dos processos do fluxo referentes à integração, sendo necessário criar um tipo de processo para os processos de licenciamento e um para inscrição municipal.
Os valores de **task** e **taskGroup** gerados pela criação dos tipo de fluxo devem ser utilizados nas variáveis corretas no arquivo de configuração.

## Configuração dos requerimentos
Os requerimentos utilizados nos processos da integração devem estar disponíveis para acesso da aplicação.
Os processos são criados a partir das informações disponibilizadas pela JUCESP, por isso, não é possível uma alteração muito grande nos dados exibidos pelo requerimento.
Deve-se atentar também para os nomes dos atributos das informações do requerimento, pois o sistema espera que o requerimento tenha determinados nomes de forma a exibir os dados na visualização do requerimento.
***Nota: Qualquer alteração nos requerimentos deve ser consultada com a equipe de desenvolvimento do fluxo para checar a viabilidade técnica da alteração***