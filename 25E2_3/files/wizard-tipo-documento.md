---
title: Wizard - Tipo de Documento
description: 
published: true
date: 2025-04-17T14:52:00.815Z
tags: 
editor: markdown
dateCreated: 2025-04-04T19:58:17.386Z
---

# Wizard - Tipo de documento

<br>

## Introdução

Visando dar mais autonomia aos usuários do sistema de alvará e melhorar a quantidade de solicitações feitas ao suporte para atendimentos simples, desenvolvemos uma ferramenta que o usuário administrador do nosso sistema possa através de interfaces gerenciar informações do sistema.

<br>

### Ferramenta

A ferramenta é acessível através do menu da aplicação, na opção Painel de Administração:

![1.png](/fluxo/wizard-tipo-documento/1.png){.align-center}

Após clicar na opção, será redirecionado para a página inicial do Painel de Administração. Nessa página, no Painel Administrativo, encontram-se diversas ferramentas úteis para o usuário administrador do sistema. Dentre elas, estará o kit de ferramentas de Gestão de processos:

![2.png](/fluxo/wizard-tipo-documento/2.png){.align-center}

Esse kit de ferramentaa nos dá algumas opções de ações que o usuário pode realizar, se tratando da qual é o assunto deste documento, o Documento personalizado. Essa ferramenta permite a criação e a edição dos tipos de documentos que existem no sistema. Dando a praticiade de em simples ações, a realização dessas atividades.

<div style="display: flex; justify-content: center;">
  <img src="/fluxo/wizard-tipo-documento/3-1.png" style="width: 50%;" />
  <img src="/fluxo/wizard-tipo-documento/3-2.png" style="width: 50%;" />
</div>

<br>

### Novo documento

Nesse primeiro momento vamos abordar a criação de um novo documento, passando por cada uma das opções disponíveis para a configuração. O preenchimento dos campos são obrigatórios para garantir a configuração e funcionamento correto. Para exemplificar, criaremos um documento e posteriormente editaremos.

O documento que criaremos será o Boletim de Informações Cadastrais (BIC). O preenchimento do nome da sigla, será feito nos dois primeiros campos de digitação:

![4.png](/fluxo/wizard-tipo-documento/4.png){.align-center}

Seguimos para Obrigatoriedade do documento, que nele, escolhemos entre as opções Sim ou Não:

![4-1.png](/fluxo/wizard-tipo-documento/4-1.png){.align-center}

O próximo passo, é a seleção de Extensões do arquivo de documento. Nesse selectlist é apresentado opções que poderão ser selecionadas parao tipo do arquivo que poderá ser inserido pelo munícipe, podendo ser escolhido mais de uma opção.

![4-2.png](/fluxo/wizard-tipo-documento/4-2.png){.align-center}

Por fim, a seleção de Qual ação deseja executar neste documento, podendo selecionar uma de três opções:

![4-3.png](/fluxo/wizard-tipo-documento/4-3.png){.align-center}

Após o preenchimento de todos os campos, basta clicar no botão Adicionar documento que o novo documento será criado com sucesso:

![4-4.png](/fluxo/wizard-tipo-documento/4-4.png){.align-center}

<br>

### Documento existente

Essa funcionalidade irá mostrar a lista de todos os documentos existentes e a possibilidade de editá-los.

> 
> Apenas a Obrigatoriedade do documento, Extensões do arquivo de documento e Qual ação deseja executar neste documento serão possíveis de editar.
{.is-info}

![5-1.png](/fluxo/wizard-tipo-documento/5-1.png){.align-center}

Há uma barra de pesquisa para realizar a procura de um documento desejado e logo abaixo, a listagem de documentos. Quando não pesquisado, listará todos os documentos.
Para realizar uma pesquisa, basta digitar o nome do documento que deseja no campo Pesquisar documento e em seguida, clicar no ícone de lupa para realizar a busca. Como criamos o documento Boletim de Informações Cadastrais (BIC), vamos utiliza-lo como exemplo.

![5-2.png](/fluxo/wizard-tipo-documento/5-2.png){.align-center}

Após encontrado o documento, ele será apresentado nesse card, contendo seu nome e dois ícones, de obrigatoriedade e edição respectivamente. O ícone de obrigatoriedade possui duas cores para representar se um documento é obrigatório ou não: na cor vermelha o documento é obrigatório, ja na cor azul, o documento não é obrigatório.

<div style="display: flex; justify-content: center;">
  <img src="/fluxo/wizard-tipo-documento/5-3.png" />
  <img src="/fluxo/wizard-tipo-documento/5-4.png" />
</div>

<br>

> Lembrando que a obirgatoriedade é configurada na criação de um documento ou pode ser alterada na edição de documentos já existentes.
{.is-info}

O ícone de edição, representado pelo lápis, irá abrir a janela de edição do documento selecionado e nele, mostrando as opções de edição do documento.

![5-5.png](/fluxo/wizard-tipo-documento/5-5.png){.align-center}

Como mencionado anteriormente e ilustrado na imagem, as opções de edição são: Obrigatoriedade do documento, Extensões do arquivo de documento e Qual ação deseja executar neste documento.
Observa-se que as informações mostradas nessas opções são as informações que escolhemos no momento da criação do Boletim de Informações Cadastrais.

- Obrigatoriedade: Sim
- Extensões: pdf,png,jpg,jpeg
- Ação: Anexar

Neste momento, vamos editar as informações desse documento para ilustrar o funcionamento. As configurações escolhidas foram as seguintes:

![5-6.png](/fluxo/wizard-tipo-documento/5-6.png){.align-center}

Após escolher as opções, clicar no botão Editar para encerrar a edição e salvar o arquivo. Uma mensagem de sucesso irá aparecer e a janela será fechada automaticamente.

![5-7.png](/fluxo/wizard-tipo-documento/5-7.png){.align-center}

Para confirmar a edição, vamos pesquisar o documento novamente e abrir a janela de edição para verificar os dados:

![5-8.png](/fluxo/wizard-tipo-documento/5-8.png){.align-center}

<br>

### Configuração da funcionalidade

Nesse momento, será abordado a configuração da ferramenta no banco de dados com o intuito de mostrar seu funcionamento por um aspecto técnico. De início, o funcionamento da funcionalidade depende de duas tabelas sendo a segunda, uma nova tabela:

- doctypes
- *document_type_extensions*

Na tabela doctypes, ficará registrada todas as infromações referente ao documento: nome, nome abreviado, obrigatoriedade, extensões e ação, sendo os atributos na tabela respectivamente:

- name
- short_name
- mandatory
- extensions
- upload_actions_id

![6-1.png](/fluxo/wizard-tipo-documento/6-1.png){.align-center}

A tabela document_type_extensions irá armazenar as extensões de arquivo disponíveis no selectlist: Extensões do arquivo de documento. Nela, irão conter os atributos:

- id
- extensions
- display_name

No atributo extensions, a extensão de arquivo propriamente dita e no atributo display_name, o nome que será mostrado no selectlist:

![6-2.png](/fluxo/wizard-tipo-documento/6-2.png){.align-center}

Para registrar as ações realizadas pelo usuário na criação e edição de documentos pela funcionalidade, uma nova tabela foi criada denominada doctypes_log. Essa tabela irá registrar:

- doctypes_id: id do documento na doctypes
- user_id: id do usuário que realizou a ação
- modification_type: qual o tipo de ação que foi realizada (CREATE/UPDATE)
- doctype_data: json contendo as informações do documento
- action_date: data e hora da ação

![6-3.png](/fluxo/wizard-tipo-documento/6-3.png){.align-center}
