---
title: Guia de Uso - Editor de Estilos v1
description: 
published: true
date: 2025-02-18T18:33:31.393Z
tags: editor de estilo
editor: markdown
dateCreated: 2025-02-18T18:18:25.682Z
---

# Guia de Uso - Editor de Estilos v1

## Visão Geral

O **Editor de Estilos v1** é uma nova funcionalidade que permite a edição de estilos aplicados a temas. Nesta versão, o editor **suporta apenas temas com estilos simples** atrelados a camadas no **GeoServer**.

> **Atenção:** Estilos com condicionais **não aparecerão** na lista de temas exibidos por perfil, para evitar possíveis erros de uso.

## Critérios para um Tema Ser Elegível no Editor

Para que um tema seja exibido na lista de edição de estilos da interface, ele deve atender aos seguintes critérios:

- O nome do estilo **simples** precisa estar presente no **GeoServer**.
- Esse nome deve estar registrado na coluna `sld` da tabela `app_param`.

O sistema utiliza esse nome para buscar o estilo no GeoServer e verificar se ele é **simples** ou contém **condicionais**. Caso o estilo possua condicionais, o tema **não será exibido na interface**.

## Processo de Edição de Estilos

1. Edição personalizada via interface de edição, logo após o usuário selecionar o tema.
2. O usuário pode selecionar um **estilo** dentro da **biblioteca de estilos** (que reúne todos os estilos disponíveis no GeoServer).
3. Caso o estilo escolhido contenha **condicionais**, **o sistema não impedirá a associação**, porém:
   - O tema deixará de ser visível na lista de temas elegíveis do perfil.
   - O valor da coluna `sld` será atualizado com o nome do novo estilo selecionado.

### Como Reverter uma Edição Indevida?

Se um usuário associar um estilo **com condicional** e quiser voltar ao que era antes, ele precisará:

1. **Manualmente definir o nome do estilo simples** na coluna `sld` da tabela `app_param`.
2. Refazer o processo de edição de estilos para esse tema **ou editar diretamente no GeoServer**.

### Como posso fazer para que meu tema apareça como elegivel?

1. Basta colocar manualmente o nome de qualquer estilo simples que desejar na coluna 'sld' da tabela 'app_param'. Feito isso, seu tema voltará a ficar disponível na lista. A partir daí, você conseguirá buscar o estilo anterior na lista exibida pela biblioteca ou simplesmente criar um estilo simples do zero pela aba de edição de estilo.

## Novos Temas Criados pelo Publicador

Para **novos temas gerados pelo Publicador de Temas**, o sistema **automaticamente atribuirá um estilo padrão** do GeoServer, de acordo com o tipo geométrico do tema.


## Guia de uso

- **Lista de temas disponíveis com temas simples elegíveis por perfil.**

Selecione o perfil para carregar a lista de temas que possuem estilos simples configurados na coluna **sld** da tabela **app_param**.

![captura_de_tela_2025-02-18_145952.png](/v3/captura_de_tela_2025-02-18_145952.png)


- **Campo de edição do estilo**

O campo de edição exibirá seu estilo simples pré-carregado. Faça as alterações conforme sua preferência e clique no botão **"Aplicar"**.

![captura_de_tela_2025-02-18_150210.png](/v3/captura_de_tela_2025-02-18_150210.png)


- **Biblioteca de estilos**

A biblioteca conterá toda a lista de estilos no GeoServer, incluindo tanto os simples quanto os que possuem condicionais. 

> **Lembre-se:** Nesta primeira versão do editor de estilos, estamos lidando apenas com estilos simples. Portanto, caso você escolha um estilo com condicionais, ele deixará de aparecer na lista de estilos válidos.


![captura_de_tela_2025-02-18_150052.png](/v3/captura_de_tela_2025-02-18_150052.png)


## Melhorias Futuras

Nas próximas fases do desenvolvimento do publicador de estilos, não atenderemos apenas a temas com estilos simples, mas a todos os tipos de estilos. A funcionalidade será inteligente o suficiente para identificar se o estilo fornecido é simples ou possui condicionais. Se for um estilo com condicionais, faremos toda a edição das condições. Além disso, caso o usuário clique sobre um estilo na aba "Biblioteca", seremos capazes de exibir apenas os estilos compatíveis com o tema, proporcionando uma melhor usabilidade e maior assertividade para o usuário. 

## Conclusão

O Editor de Estilos v1 facilita a gestão de estilos, garantindo maior controle sobre as configurações visuais dos temas. No entanto, é fundamental estar atento às regras de exibição para evitar problemas com estilos condicionais.




