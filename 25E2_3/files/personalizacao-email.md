---
title: Personalização do envio de e-mail
description: Envio de e-mail personalizado para um step definido no fluxo
published: true
date: 2025-04-04T19:59:07.884Z
tags: 
editor: markdown
dateCreated: 2025-01-06T15:07:54.979Z
---

# Personalização para o envio de e-mail

<br>

## Introdução

Hoje em nosso sistema de alvará enfrentamos alguns barramentos em relação ao envio de e-mail aos usuário após alguma movimentação tomada sobre o processo, dessa forma se faz necessário flexibilizar o envio de e-mail ao tomar uma ação sobre o processo.

Para realizar isso iremos atuar de forma parecida com a geração de certidões no sistema atribuindo um VALUE ao botão de forma que esse valor seja a referência do ID do e-mail.

<br>

## Configuração

Com base no button goNext, a funcionalidade será configurada de forma simples. Será necessário:

1. Configurar um template de e-mail na email_template;
2. Configurar o button na tab_buttons.

Em um primeiro momento, será necessário possuir o id do e-mail a qual será utilizado no button.

![id_email.png](/fluxo/id_email.png){.align-center}

Com o e-mail configurado e id estabelecido, será necessário adicionar um parâmetro no código do botão, na coluna button_code. O parâmetro possuir nome "value" e como dado, o id do e-mail.

![id_button.png](/fluxo/id_button.png){.align-center}

<br>

> A clareza e especificdade na nomenclatura dos novos botões serão essenciais para organização manutenibilidade.
{.is-warning}

Após realizada as configurações, inserir o id do botão no step do fluxo desejado na workflow. O botão sendo utilizado, o e-mail configurado será enviado para o usuário.

![email_teste.png](/fluxo/email_teste.png){.align-center}
