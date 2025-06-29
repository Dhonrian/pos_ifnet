---
title: Compartilhar Processo
description: Documentação da descrição e modo de implantação do compartilhar processo
published: true
date: 2024-10-16T13:57:48.521Z
tags: fluxo, compartilhar, alvará
editor: markdown
dateCreated: 2024-10-15T13:44:42.792Z
---

![](https://wiki.flow.geopixel.com.br/template_geo/geopixel_logo_2022.png)

# Introdução

Uma das maiores dificuldades no sistema de fluxo é a atuação de outros setores num determinado processo. O tramitar supre essa necessidade mas é uma ação que demora e depende da movimentação do processo por diversos setores.

Pensando em aliviar este problema foi criada a ação de “Compartilhar Processo” para que seja possível outros setores trabalharem em cima de um processo sem que ele saia do passo atual.

## Compartilhar Processo

A ação de compartilhar processo é feita a partir do botão “Criar Solicitação"

![](/criarsolicitacao.png)

O botão de Criar Solicitação é adicionado pelo conversor e pode ser colocado em qualquer passo do fluxo.  
 

Ao clicar no botão será aberto um modal com as seguintes opções:

![](/modalsolicitacao.png)

## Modal Criar Solicitação

A **primeira seção** da imagem contém o **número** e o **status atual** do processo assim como no novo tramitar.

---

Na **segunda seção** encontra-se um campo com os tipos de Solicitação disponíveis para seleção, atualmente os tipos disponíveis são **Requerimento** e **Documento.** 

![](/tiposolicitacao.png)

Quando a ação de Documentos for selecionada todos os documentos que foram previamente **verificados** ficarão disponíveis para escolha:

![tiposdocumentos.png](/tiposdocumentos.png)

Quando uma solicitação é criada os documentos selecionados serão duplicados para todos os usuários selecionados.

> Para usar a opção de documentos não é possível selecionar a opção **qualquer usuário no setor** pois é necessário o documento estar associado a um usuário
{.is-warning}

---

Na **terceira seção** é possível selecionar as secretarias e os usuários que serão escolhidos 

![usuarioperfil.png](/usuarioperfil.png)

O campo de usuários é prenchido após a escolha de uma secretaria, assim como no novo tramitar, e adicionado numa lista de "perfil: usuário". Entretanto uma nova adição é que é possível criar um grupo de perfis para serem reutilizados, sem que haja a necessidade de repetir os mesmos usuários:

![solicitacaogrupo.png](/solicitacaogrupo.png)

Outra diferença é no campo de usuários em que existe a opção **qualquer pessoa do setor**.

![qualquerpessoa.png](/qualquerpessoa.png)

Nesta opção a solicitação é direcionada ao setor podendo qualquer pessoa assumir a solicitação e tratá-la.

> Esta opção é semelhante ao assumir responsabilidade utilizada nos fluxos.
{.is-info}

Para finalizar a criação da solicitação basta pressionar o botão de **Enviar** ao final do modal, fazendo com que o botão de solicitações fique preto.

![botaopreto.png](/botaopreto.png)

## Tratando processos compartilhados

Para os processos compartilhados não se confundirem com a análise dos processos do dia a dia foi criada uma paginação entre as duas tabelas através de abas.

![abasolicitacoes.png](/abasolicitacoes.png)


Os processos que são compartilhados (ou solicitações criadas) podem ser encontradas na nova aba criada na tela principal do sistema. Quando uma solicitação é criada uma notificação inidica algo novo na aba do sistema.

![notificacao.png](/notificacao.png)

---

A tabela de solicitações é semelhante à tabela de processos, tendo colunas parecidas e a coluna **Tipo de Solicitação** indicando qual tipo de solicitação foi criado. Por enquanto a diferença entre os tipos é que a solicitação de Documentos trás o botão de documentos com os documentos do processo.

![solicitacoestabela.png](/solicitacoestabela.png)

---

Após ser finalizada a análise do processo o técnico da prefeitura deve clicar no botão **Finalizar Solicitação** onde será exibido um campo para digitar um parecer que será adicionado ao histórico do processo.

![finalizarsolicitacao.png](/finalizarsolicitacao.png)

## Banco de Dados

No banco de dados foi criado uma nova tabela para salvar os processos que são compartilhados chamada **process_requests**

![tabelabanco.png](/tabelabanco.png)

- **id**: id sequencial da tabela.
- **process_id**: chave estrangeira que representa o *proc_id* da tabela *tab_process*.
- **request_type**: tipo de solicitação criada, as opções por enquanto são *DOCUMENTOS* ou *REQUERIMENTO*.
- **creation_user_id**: chave estrangeira que representa o usuário que criou a solicitação, liga com o *user_id* da tabela *app_usuario*.
- **profile_id**: chave estrangeira que representa à qual perfil foi direcionada a solicitação, representa o prf_id da *app_perfil*.
- **requested_user_id**: chave estrangeira que indica qual usuário foi escolhido para solicitação. Também se conecta a *user_id* da *app_usuario*.
- **id_buttons**: IDs que serão buscados da tabela *tab_buttons* de forma automática dependendo da solicitação.
- **insert_date**: data que foi criada a solicitação.
- **expire_date**: data que a solicitação foi finalizada.
- **is_read**: indica se a solicitação já foi vista, determinando se aparecerá a notificação ou não.

### tab_steps

A tabela **tab_steps** também foi alterada, tendo como adição da coluna **process_request_id**  que é preenchida quando uma solicitação é criada naquela passo.

![tabsteps.png](/tabsteps.png)
