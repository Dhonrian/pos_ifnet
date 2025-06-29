---
title: Diretrizes do Log de Edição na V3
description: Diretrizes do Log de Edição na V3
published: true
date: 2024-01-17T13:51:02.341Z
tags: de, log de edição, log, edição, diretrizes, regra de negócio, histórico, histórico de edição
editor: markdown
dateCreated: 2024-01-17T12:57:47.069Z
---

# Diretrizes do Log de edição na V3

## Prefácio
Este documento tem por objeto definir algumas diretrizes para o funcionamento do registro de edições (log) na versão 3 do `Geopixel Cidades`. Majoritariamente, as regras são bem semelhantes com as regras definidas pela versão 2 do sistema, havendo pequenas diferenciações que, no nosso entendimento, facilitariam e melhorariam a compreensão do histórico de edição de uma feição.

## Detalhamento da tabela
O registro da edição de uma feição (log) é armazenado em uma tabela do sistema de nome `app_log`. Ela possui algumas colunas que auxiliam o sistema a identificar qual tabela, feição ou operação foi realizada a partir da edição de uma feição. Essa tabela possui as seguintes colunas:

- `pk`: Referencia o identificador de cada log de edição. É também a chave primária desta tabela. Importante se atentar que essa coluna representa o identificador do LOG e NÃO da FEIÇÂO editada, sendo esta abordada em outra coluna.
- `times_temp`: Referencia a data e a hora que o log de edição foi persistido.
- `table_name`: Referencia o nome da tabela em que foram inseridas/alteradas as informações das feições.
- `gid`: Referencia o identificador da FEIÇÃO editada, dado um determinado tema. Este sim é o identificador que representa a feição editada. Portanto se pesquisarmos na tabela de origem por este identificador, teremos como resultado a feição que foi editada.
- `type_value`: Referencia o tipo de operação realizada utilizando as ferramentas de edição. Essas podem ser, por exemplo: `insert`, `update`, `delete`, `union`, `desmembramento` etc
- `user_id`: Referencia o identificador do usuário que realizou a operação.
- `process`: Normalmente essa informação é proveniente de formulários. Referencia o número do processo que originou tal edição.
- `motive`: Normalmente essa informação é proveniente de formulários. Referencia o motivo da edição realizada.
- `prf_id`: Referencia o identificador do perfil do usuário que realizou a operação.
- `previous`: Referencia o identificador do log de edição anterior (pk), se houver. Ou seja, no caso de atualizações após uma inserção, por exemplo, ele referenciará o identificador do log de insert que originou a feição.
- `next`: Referencia o identificador do log de edição posterior (pk), se houver. Ou seja, tomando como exemplo o item anterior, no log de insert ele referenciará o identificador do log de update que ocorreu após a inserção da feição.
- `chave_table`: Referencia o nome do atributo que representa a chave primária do tema editado, concatenado com o identificador da feição. Por exemplo: `id:12345`. É utilizado somente para consulta visual de desenvolvedores.
- `user_name`: Referencia o nome do usuário que realizou a operação.
- `requester`: Normalmente essa informação é proveniente de formulários. Referencia o requisitante da edição.
- `observation`: Normalmente essa informação é proveniente de formulários. Referencia as observações de uma determinada operação.

## Detalhamento das operações
### Operação de inserção
Ao se inserir uma nova feição, será persistido um novo registro na tabela `app_log`, conforme o exemplo abaixo:

|pk|times_temp|table_name|gid|type_value|user_id|process|motive|prf_id|previous|next|chave_table|user_name|requester|observation|
|--|----------|----------|---|----------|-------|-------|------|------|--------|----|-----------|---------|---------|-----------|
|113025|2024-01-17 09:17:10.807|caca_lote_3857|209447|insert|2411| | |273| | |fid:209447|Administrador| | |

Perceba que as colunas de previous e next não possuem dados, pois sendo essa uma operação de inserção, ela não provém de uma operação anterior (previous) e nem houve uma atualização posterior (next)

### Operação de atualização
Ao se atualizar uma feição, será persistido um novo registro na tabela `app_log`, conforme o exeplo abaixo:

|pk|times_temp|table_name|gid|type_value|user_id|process|motive|prf_id|previous|next|chave_table|user_name|requester|observation|
|--|----------|----------|---|----------|-------|-------|------|------|--------|----|-----------|---------|---------|-----------|
|113026|2024-01-17 09:17:26.184|caca_lote_3857|209448|update|2411| | |273|113025| |fid:209448|Administrador| | |
|113025|2024-01-17 09:17:10.807|caca_lote_3857|209447|insert|2411| | |273| |113026|fid:209447|Administrador| | |

Perceba que tanto previous, quanto next, referenciam os respectivos logs anteriores e posteriores.

### Operação de deleção
Ao se atualizar uma feição, será persistido um novo registro na tabela `app_log`, conforme o exeplo abaixo:

|pk|times_temp|table_name|gid|type_value|user_id|process|motive|prf_id|previous|next|chave_table|user_name|requester|observation|
|--|----------|----------|---|----------|-------|-------|------|------|--------|----|-----------|---------|---------|-----------|
|113027|2024-01-17 09:18:26.184|caca_lote_3857|209448|delete|2411| | |273|113026| |fid:209448|Administrador| | |
|113026|2024-01-17 09:17:26.184|caca_lote_3857|209448|update|2411| | |273|113025| 113027 |fid:209448|Administrador| | |
|113025|2024-01-17 09:17:10.807|caca_lote_3857|209447|insert|2411| | |273| |113026|fid:209447|Administrador| | |

Perceba que tanto previous, quanto next, referenciam os respectivos logs anteriores e posteriores.

### Operação de inserção de temas duais (temas vesgos)
Ao se inserir uma feição de uma tema vesgo, serão persistidos dois novos registros na tabela `app_log`, conforme o exeplo abaixo:

|pk|times_temp|table_name|gid|type_value|user_id|process|motive|prf_id|previous|next|chave_table|user_name|requester|observation|
|--|----------|----------|---|----------|-------|-------|------|------|--------|----|-----------|---------|---------|-----------|
|113008|2024-01-17 08:30:25.612|caca_lote_3857|209441|insert|2411| |  |273| |113010|fid:209441|Administrador| | |
|113007|2024-01-17 08:30:25.607|caca_cad_imob|81031|insert|2411| | |273|  |113009|id:81031|Administrador| | |

Neste caso, foi inserida uma nova feição no tema de Cadastro Imobiliário (Tabular), e como ele possui como camada o tema de Lote, consequentemente foi inserida uma nova feição no tema de Lote (Geométrico).

### Operação de atualização de temas duais (temas vesgos)

Ao se atualizar uma feição de um tema vesgo, serão persistidos mais dois novos registros na tabela `app_log`, conforme o exeplo abaixo:

|pk|times_temp|table_name|gid|type_value|user_id|process|motive|prf_id|previous|next|chave_table|user_name|requester|observation|
|--|----------|----------|---|----------|-------|-------|------|------|--------|----|-----------|---------|---------|-----------|
|113010|2024-01-17 08:36:49.266|caca_lote_3857|209442|update|2411| | |273|113008| |fid:209442|Administrador| | |
|113009|2024-01-17 08:36:49.222|caca_cad_imob|81032|update|2411| | |273|113007| |id:81032|Administrador| | |
|113008|2024-01-17 08:30:25.612|caca_lote_3857|209441|insert|2411| |  |273| |113010|fid:209441|Administrador| | |
|113007|2024-01-17 08:30:25.607|caca_cad_imob|81031|insert|2411| | |273|  |113009|id:81031|Administrador| | |

### Operação de desmembramento de feições (split)
Ao se desmembrar uma feição, serão persistidos os seguintes registros na tabela, seguindo a lógica de que, a partir de uma feição desmembrada, surgirão N feições:

|pk|times_temp|table_name|gid|type_value|user_id|process|motive|prf_id|previous|next|chave_table|user_name|requester|observation|
|--|----------|----------|---|----------|-------|-------|------|------|--------|----|-----------|---------|---------|-----------|
|112997|2024-01-17 08:11:24.146|caca_lote_3857|209437|insert|2411| | |273|112995| |fid:209437|Administrador| | |
|112996|2024-01-17 08:11:24.139|caca_lote_3857|209436|insert|2411| | |273|112995| |fid:209436|Administrador| | |
|112995|2024-01-17 08:11:24.125|caca_lote_3857|209435|Desmembramento|2411| | |273|112994|112996 112997|fid:209435|Administrador| | |
|112994|2024-01-17 08:11:14.618|caca_lote_3857|209435|insert|2411| | |273| |112995|fid:209435|Administrador| | |

Para facilitar a compreensão, segue uma ilustração representativa da operação realizada:

![imagem_2024-01-17_104708219.png](/imagem_2024-01-17_104708219.png)

### Operação de união de feições (union)
Ao unir feições, serão persistidos os seguintes registros na tabela, seguindo a lógica de que, a partir de N feições unidas, surgirá uma nova feição:


|pk|times_temp|table_name|gid|type_value|user_id|process|motive|prf_id|previous|next|chave_table|user_name|requester|observation|
|--|----------|----------|---|----------|-------|-------|------|------|--------|----|-----------|---------|---------|-----------|
|113000|2024-01-17 08:11:34.735|caca_lote_3857|209438|insert|2411| | |273|112998 112999| |fid:209438|Administrador| | |
|112999|2024-01-17 08:11:34.753|caca_lote_3857|209437|union|2411| | |273|112997|113000|fid:209437|Administrador| | |
|112998|2024-01-17 08:11:34.696|caca_lote_3857|209436|union|2411| | |273|112996|113000|fid:209436|Administrador| | |
|112997|2024-01-17 08:11:24.146|caca_lote_3857|209437|insert|2411| | |273|112995| 112999 |fid:209437|Administrador| | |
|112996|2024-01-17 08:11:24.139|caca_lote_3857|209436|insert|2411| | |273|112995| 112998 |fid:209436|Administrador| | |
|112995|2024-01-17 08:11:24.125|caca_lote_3857|209435|Desmembramento|2411| | |273|112994|112996 112997|fid:209435|Administrador| | |
|112994|2024-01-17 08:11:14.618|caca_lote_3857|209435|insert|2411| | |273| |112995|fid:209435|Administrador| | |

Para facilitar a compreensão, segue uma ilustração representativa da operação realizada:

![imagem_2024-01-17_105022384.png](/imagem_2024-01-17_105022384.png)