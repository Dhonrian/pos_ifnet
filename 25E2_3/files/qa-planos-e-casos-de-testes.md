---
title: Planos e Casos de Testes
description: Está página tem como objetivo explicar o que são planos e casos de testes, como são realizados hoje dentro do time de desenvolvimento, gerenciamento e sua importância no processo de desenvolvimento de um sistema.
published: true
date: 2023-08-30T14:12:37.105Z
tags: planos de testes, casos de testes, qualidade, testes, qa, desenvolvimento, tecnologia, sistema
editor: markdown
dateCreated: 2023-08-18T13:38:54.437Z
---

# Planos de Testes
O plano de testes é um documento que define como os testes serão feitos em um projeto de software. Ele detalha objetivos, métodos e cronograma para garantir que o software atenda aos requisitos e funcione como esperado.

É extremamente importante no processo de desenvolvimento de software, pois seu objetivo é assegurar a qualidade do produto final, mitigar riscos e garantir a satisfação do usuário.

Ele desempenha várias funções cruciais, por exemplo:

- Detectar Defeitos: Identificar erros antes do lançamento, permitindo correções prévias.

- Garantir Qualidade: Manter a qualidade, cumprindo padrões e proporcionando confiabilidade.

- Atender Requisitos: Verificar se o software cumpre requisitos, assegurando expectativas.

Atualmente, a criação deste documento é responsabilidade do Analista de Qualidade de Software e seu processo de criação se inicia quando uma História do Usuário está pronta com todos os critérios de aceite e detalhamento finalizados.

Para criar um plano de testes, usa-se o item **Plano de testes** ou **Grupo de Plano de Testes** no Jira. A diferença de **Plano de testes** para **Grupo de Plano de Testes** está em uma coleção de planos de testes ou somente um em individual que contemple aquela funcionalidade desenvolvida.

![planodetestes.png](/planodetestes.png)

## Indicadores e ciclo de vida de um plano de testes

INDICADOR DE PLANOS - Indica a % em cada etapa de desenvolvimento dos planos de teste. 

![ind-plano-de-teste.png](/ind-plano-de-teste.png)

Legenda do ciclo de status de um plano de teste:

- BACKLOG - Indica a % de planos identificamos mas que ainda não foram criados; 

- EM DESENVOLVIMENTO - Indica a % de planos em construção;

- PLANO DEFINIDO - Indica a % de planos definidos com todos casos de teste;

- EXECUTADO MANUALMENTE - Indica a % de planos executados;

- EM AUTOMAÇÃO - Indica a % de planos em automação;

- CONCLUÍDO - Indica a % de planos de teste automatizados.

Obs: Para cada plano de testes é necessário identificar qual status ele está e atualizar, afim de manter sempre atualizado.

# Casos de Testes
Um caso de teste é uma descrição detalhada de um cenário ou situação específica que um sistema pode ou deve enfrentar durante os testes.
Seu principal objetivo é garantir que um sistema funcione conforme o esperado e atenda aos requisitos definidos, além de identificar possíveis erros ou falhas. Ele inclui informações sobre os passos a serem seguidos, entradas a serem fornecidas, ações a serem executadas e os resultados esperados.

### Qual a conexão de um caso de testes com um plano de testes?

O caso de testes define como iremos testar um cenário em especifico, o plano de testes engloba vários cenários de testes para garantir o funcionamento de uma funcionalidade. Um caso de teste depende de 1 plano de teste e um plano de testes depende de 1 a N casos de testes.

## Como criar um caso de teste?
Antes de criarmos um caso de testes, precisamos entender alguns conceitos importantes que são usados em sua criação.

- Desenvolvimento Orientado pelo Comportamento (BDD, Behavior-Driven Development): é uma abordagem que combina a comunicação entre desenvolvedores, testadores e partes interessadas para criar um sistema mais focado nos resultados desejados. Prioriza a colaboração entre equipes de desenvolvimento, testes e partes interessadas para criar um entendimento compartilhado dos comportamentos desejados do sistema. Isso é alcançado por meio da descrição de cenários de uso em uma linguagem natural compreensível por todos os envolvidos, o que facilita a criação de um sistema alinhado com as necessidades e expectativas das partes interessadas.

- Gherkin: É uma linguagem de notação simples e legível usada para escrever especificações de comportamento seguindo algumas palavras chaves, que são elas **Dado, Quando, Então, E, Mas**. Junto ao BDD esses casos de teste descrevem interações de usuário, ações e resultados desejados de uma maneira que todos os envolvidos possam entender, promovendo uma visão compartilhada e uma base sólida para o desenvolvimento iterativo e testes contínuos.

Agora que temos enraízado estes conceitos, iremos pensar em como criar estes casos.

1. Identificar um Cenário: Pensar em um cenário específico que você deseja descrever e testar. Por exemplo, um sistema de registro de usuários.

2. Definir a Estrutura do Cenário em Gherkin: Utilizar a sintaxe simples do Gherkin para definir a estrutura do cenário. A estrutura básica inclui uma funcionalidade e um cenário.

> **Funcionalidade:** Registro de Usuário.
> **Cenário:** Registro bem-sucedido de um novo usuário.


  
3. Descrever Etapas com Palavras-chave: Divida o cenário em etapas usando palavras-chave em ordem como **Dado**, **Quando** e **Então**. O Dado define o contexto inicial, o Quando descreve a ação e o Então define o resultado esperado.

> **Funcionalidade:** Registro de Usuário
> **Cenário:** Registro bem-sucedido de um novo usuário
> **Dado** que um novo usuário deseja se registrar
> **Quando** o usuário preenche os campos obrigatórios
> **E** clica no botão "Registrar"
> **Então** o usuário deve ser redirecionado para a página de boas-vindas
> **E** deve receber um email de confirmação
    
5. Colaboração e Execução: Compartilhe a especificação com a equipe e partes interessadas para alinhar as expectativas. Os desenvolvedores e analistas de qualidade podem usar esses cenários como base para implementação de testes automatizados.

Conclusão:
O Gherkin é uma linguagem poderosa para criar casos de teste em um formato legível e colaborativo. O BDD enraíza a comunicação eficaz entre as equipes, usando Gherkin para expressar comportamentos esperados. Ao criar cenários detalhados e compartilhados, melhora a compreensão de todos e a colaboração, resultando em sistema que atende melhor às necessidades dos usuários.

## Documentando caso de teste no Jira

Dentro do item plano de testes (explicado a cima), pode-se criar um sub-item.

![casodeteste.png](/casodeteste.png)

Após informar no título o cenário definido, basta clicar em **Criar**, abrir o caso de teste e informar as ações, comportamentos e resultado esperado.

![casodeteste1.png](/casodeteste1.png)

## Indicadores e ciclo de vida de um caso de testes

INDICADOR DE CASOS DE TESTE - Indica a % em cada etapa de desenvolvimento dos casos de teste. 

![captura_de_tela_2023-08-30_111015.png](/captura_de_tela_2023-08-30_111015.png)

Legenda do ciclo de status de um caso de teste:

- BACKLOG - Indica a % de casos ainda não foram criados; 

- EM DESENVOLVIMENTO - Indica a % de casos em construção;

- DEFINIDO - Indica a % de casos definidos;

- EXECUTADO MANUALMENTE - Indica a % de casos executados manualmente;

- EM AUTOMAÇÃO - Indica a % de casos em automação;

- CONCLUÍDO - Indica a % de planos de teste automatizados.

Obs: Para cada caso de testes é necessário identificar qual status ele está e atualizar, afim de manter sempre atualizado.