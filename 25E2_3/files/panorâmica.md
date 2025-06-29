---
title: Panorâmica
description: 
published: true
date: 2023-10-10T21:49:31.767Z
tags: 
editor: markdown
dateCreated: 2023-10-10T19:17:11.438Z
---

# Configuração da funcionalidade panorâmica
## Ferramenta
> ![captura_de_tela_2023-10-10_183255.png](/captura_de_tela_2023-10-10_183255.png)
## Contexto
> Para que a ferramenta de panorâmica funcione é necessário criar o contexto
Esse contexto é criado na tabela 'gpx_theme_context'.

> **Esse contexto terá as seguintes informações**
context_type = GPX_THEME_CONTEXT_PANORAMIC
description = 'Contexto para o tema de imagens panorâmicas'
{.is-info}

> Esse contexto será usado dentro da aplicação no endpoint de caminho '/getInfo'.
`Theme theme = themeService.findByProfileIdAndContextContextType(profileId,
                ThemeContextType.GPX_THEME_CONTEXT_PANORAMIC);`

## Configurações na aplicação
> Algumas configurações ficarão dentro da aplicação, especificamente no documento application.json.
Esse documento pode ser encontrado dentro da pasta 'resource/server/config', ou se estiver utilizando um máquina virtual ele fina na '/opt/gpx_home/<sua-aplicação>/config'.

> **As configurações serão**
"panoramic.uri" e "srs.planar"

## Tema
> Também será necessário trazer a tabela do banco relativa a esse tema, essa tabela terá todas as imagens que serão usadas na panorâmica.
No banco de limeira essa tabela chama-se panoramic, mas ela pode apresentar outros nomes.

## Configuração do tema
> Depois de trazer a tabela precisamos mapear suas colunas na tabela 'app_dicionario_dado'. Lá iremos registrar as colunas da nossa tabela panorâmica.

> Depois de registrar em app_dicionario_dado precisamos fazer o mapeamento na tabela de atributos 'app_permissão'. Lá vamos mapear os atributos que aparecerão no nosso feature description.

> Para que a ferramenta de panorâmica funcione corretamente também vamos ter que criar um registro em 'app_tema' com as informações da nossa tabela.
