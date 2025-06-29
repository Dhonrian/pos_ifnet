---
title: Agendamento de Fiscalização
description: Procedimentos de implantação e manutenção da funcionalidade de Agendamento de Fiscalização.
published: true
date: 2024-10-09T11:52:18.297Z
tags: alvara
editor: markdown
dateCreated: 2024-10-08T20:41:58.496Z
---

# Agendamento de Fiscalização

<br>

## Introdução

A funcionalidade de Agendamento de Fiscalização está presente no formulário de requerimento dos processos no sistema de fluxo. Com ela, será possível para os servidores agendarem fiscalizações que estarão ligadas diretamente a um processo no sistema de alvará de obras, informando:

1. Dia e turno;
2. Data de agendamento;
3. Região;
4. Status.

As informações dos campos descritos acima serão armazenadas em uma nova tabela contida na versão 00128 da app_database_version, chamada de tab_inspection_schedule.

![tab-inspect-schedule-db-version.png](/tab-inspect-schedule-db-version.png){.align-center}

<br>

## Definições

A seguir, serão apresentados os atributos que compõem a tab_inspection_schedule.

- **day_and_shift** (string): armazenamento do dia da semana e turno a qual será realizada a fiscalização;

- **scheduling_date** (string): armazenamento da data da fiscalização;

- **proc_id** (integer): armazenamento do id do processo;

- **id** (integer): armazenamento do número sequencial para cada agendamento;

- **region** (string): armazenamento da região territorial da fiscalização;

- **status** (string): armazenamento do status do agendamento.

<br>

## Instruções para Implantação

Em um primeiro momento, será necessária a adição de código nos formulários de requerimento. Lembrando que os formulários agora se encontram no banco de dados, precisamente na tabela flow_form.
Os fields estarão sob o id update_schedule e serão referenciados pelo padrão 'nome_atributo_tabela':'nome_atributo_form_requerimento'. Como attributes, os campos deverão estar com hidden. Segue o código exemplo a seguir:

>	{
>	"field": "{'day_and_shift':'data_turno_fiscal','status':'status_fiscal','region':'regiao_fiscal','scheduling_date':'data_agendamento'}",
>	"id": "update_schedule",
> "name": "update_schedule_name",
> "attributes": ["hidden"]
>}

Note que, 'data_turno_fiscal', 'status_fiscal', 'regiao_fiscal' e 'data_agendamento' são os atributos que constam no formulário para inserção dos dados. Segue abaixo:

![cod_form.png](/fluxo/cod_form.png){.align-center}

![form-requerimento-atributos.png](/fluxo/form-requerimento-atributos.png){.align-center}

> O bloco de código do update_schedule deverá ser inserido no "theme": "ROW_NUM_PROCESSO".
{.is-warning}

<br>

## Validação dos dados

Para cada processo inserido na tab_process, uma row será criada na tab_inspection_schedule contendo o **proc_id** referente ao processo e o **id** referente a row. Inicialmente, os atributos **day_and_shift**, **scheduling_date**, **region**, **status** estaráo null até que sejam salvos os dados nos campos do formulário referentes ao agendamento de fiscalização.

1. tab_inspection_schedule com as rows geradas

![tab-inspect-schedule-1.png](/fluxo/tab-inspect-schedule-1.png){.align-center}

2. Relação dos dados tab_process/tab_inspection_schedule

![tab-inspection-schedule-rel.png](/fluxo/tab-inspection-schedule-rel.png){.align-center}

3. Validação dos dados no formulário de Requerimento

![proc-rel-agend.png](/fluxo/proc-rel-agend.png){.align-center}
