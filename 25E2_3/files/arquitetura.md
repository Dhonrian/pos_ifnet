---
title: Arquitetura
description: Apresentação da arquitetura utilizada para criar e manter as ferramentas de edição
published: true
date: 2024-01-17T13:44:20.318Z
tags: 
editor: markdown
dateCreated: 2024-01-17T13:41:49.349Z
---

# Arquitetura

### Herança

- **AbstractMapTool.ts** -
    Classe abstrata herdada por todas as ferramentas, contendo métodos dos eventos de comandos do usuário e outros métodos de validação e ciclo de vida importantes.

- **DrawTool.ts**
    Classe herdada pelas ferramentas que desenham geometrias, implementando os métodos da AbstractMapTool, contendo regras gerais do funcionamento de cada interação do usuário para desenhar.

- **SelectTool.ts**
    Classe herdada pelas ferramentas que selecionam geometrias, implementando os métodos da AbstractMapTool, contendo regras gerais do funcionamento de cada interação do usuário para selecionar.

### Camadas

- **MapToolService.ts** - Classe que interage com o objeto do mapa contendo métodos referentes a criação e edição das camadas do mapa.

#### Camadas de desenho

- **EditionLayer** – Camada que recebe as feições vindas do banco

- **CurrentLayer** – Camada que recebe as feições do tema corrente

- **SketchLayer** – Camada responsável por mostrar o feedback dos desenhos feitos no mapa. (Pontos clicados e Ponto futuro)

- **DraftLayer** – Camada invisível gêmea da SketchLayer, usada principalmente pelo Undo Redo.(Pontos clicados)

- **ModifyLayer** – Camada utilizada para visualizar geometrias que serão modificadas/editadas.


#### Guias

- **Snap** – Verifica se existe geometrias próximas e utilizada com a ferramenta de desenho, consegue “puxar” o ponto criado para essa geometria encontrada.
![image-21.png](/ferramentas-edição/image-21.png)

- **Linha guia angular** – Linhas que auxiliam a criação de linhas nos ângulos de 45, 90 e 180 graus.
![image-19.png](/ferramentas-edição/image-19.png)

- **Linha guia ortogonal** – Linha que auxilia no fechamento da geometria em 90 graus.
![image-20.png](/ferramentas-edição/image-20.png)

#### Utils

- **Geometry Utils** – Classe que contém métodos de validação e auxílio para a construção de geometrias e desenhos.

- **Geometry Service** – Classe que contém métodos de serviço que auxiliam no comportamento entre server e cliente.
