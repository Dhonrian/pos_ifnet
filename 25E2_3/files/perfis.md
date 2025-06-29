---
title: Configuração de Perfis
description: Tutorial para validação e configuração de perfis
published: true
date: 2023-11-08T19:05:55.392Z
tags: checklist, checklists, perfil, perfis, configuração, validação, geocidades
editor: markdown
dateCreated: 2023-11-08T19:05:53.639Z
---

# Configuração de Perfis

O presente artigo procura elucidar os requisitos mínimos para o levantamento de informações e configurações mínimas para a implantação de um perfil.

## Etapa 1 | Levantamento de perfis e camadas

O levantamento de perfis e camadas, a estarem disponíveis em cada perfil, deverá ser realizado junto ao cliente. Para isso, deverá ser utilizado artefato de Definição de Perfis e Camadas, com a relação de todas as camadas do sistema e as devidas permissões, por perfil.

- [Artefato *Definição de Perfis e Camadas*](https://geopx.sharepoint.com/:x:/s/ImplantaoProdutos-Negcios/ETKAGKRKfdZMsyTpDgzjN8gBdDv8RY-MKPSxdZilN3tQ7Q?e=NzaTfc)
{.links-list}

Ao abrir o artefato, você irá perceber que existem 3 perfis padrão: Administrador, Servidores e Público. Por mais que sejam renomeados, esses perfis são os acessos mínimos a serem disponibilizados para o cliente. No mesmo artefato, precisam ser listadas todas as camadas disponíveis no sistema, incluindo o MDU.

O perfil Servidores pode servir como base para replicação de camadas para demais perfis a serem criados, como exemplo perfis atrelados a outras secretarias. Isso facilita na hora da implantação e impede que uma secretaria precise alterar o perfil para visualizar determinada informação, que já estaria "liberada" para ela no perfil Servidores.

> É essencial que seja levantado, nesta etapa, a visualização dos dados do Cadastro Imobiliário (disponibilizados após a integração) para cada perfil, principalmente aos atributos que são referentes a dados pessoais e/ou sensíveis (CPF, nome do contribuinte, endereço de correspondência etc).
{.is-warning}

## Etapa 2 | Configurações mínimas

Após implantados, existem algumas configurações mínimas a serem atendidas, visando uma melhor experiência do usuário durante o uso do sistema. São elas:

- [X] Inicialização
- [X] Most Used

### Inicialização

A Inicialização do sistema corresponde às camadas disponibilizadas ("ligadas" ou "desligadas") assim que o sistema é aberto. Essa configuração pode ser realizada por perfil, deixando as camadas que o setor/secretaria mais utilizam com acesso facilitado. Como essa etapa é diferente para cada perfil, é preciso que seja realizado um levantamento prévio de quais são as camadas mais visualizadas e quais são as camadas editáveis por cada perfil.

### Most Used

O Most Used, também chamado de Pesquisa Rápida, é a barra de pesquisa presente na parte superior do Geocidades. Ele possui algumas opções de pesquisa, por tema e atributos definidos, e pode ser configurado de acordo com a disponibilidade de camadas no sistema.

Por exemplo, é possível disponibilizar a pesquisa por bairros, logradouros inscrição imobiliária e até mesmo por endereço (puxando direto de um atributo da integração ou concatenando* atributos de "Rua" e "Número").

> **Concatenação** é um termo usado em computação para designar a operação de unir o conteúdo de duas strings. Por exemplo, considerando as strings "casa" e "mento" a concatenação da primeira com a segunda gera a string "casamento".
{.is-info}

O primeiro atributo de pesquisa, disponível com a abertura do sistema, acompanha também o Tema Corrente (parte inferior do Geocidades, que define qual informação será mostrada ao clicar na geometria do tema indicado). Ou seja, se a primeira opção de pesquisa do Most Used estiver configurada para o tema Logradouro, o Tema Corrente também estará configurado para Logradouro.
_______
Para assegurar-se de que todas as informações necessárias estão sendo solicitadas na criação de um novo perfil, pode ser utilizado o modelo abaixo:

**Nome:** Urbanismo
**Camadas de visualização:** replicar do perfil Serviores
**Camadas de edição:** replicar do perfil Administrador
**Inicialização:** <inserir print das camadas na inicialização, indicando quais estarão "ligadas" e quais estarão "desligadas">
**Most used:**
- Camada 1: atributo X
- Camada 2: atributo Y

## Checklist de aferição

- [X] Preenchimento do artefato Definição de Perfis e Camadas
- [X] Levantamento da Inicialização, por perfil
- [X] Levantamento do Most Used, por perfil
- [X] Abertura de card para implantação dos perfis