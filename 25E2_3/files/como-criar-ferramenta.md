---
title: Como criar uma ferramenta
description: Passo a passo para criar uma nova ferramenta utilizando a arquitetura
published: true
date: 2024-01-17T13:56:02.340Z
tags: 
editor: markdown
dateCreated: 2024-01-17T13:56:00.520Z
---

# Como criar uma ferramenta

Primeiramente criamos o arquivo (.ts) na pasta concrete tool.

![image.png](/ferramentas-edição/image.png)

> Vale destacar que toda ferramenta é somente uma classe typescript que herda eventos e usa esses eventos para manipular as camadas que ficam acima do mapa.

![image-1.png](/ferramentas-edição/image-1.png)

Portanto, após criarmos nossa ferramenta precisamos pensar no fluxo de inicialização, em vias de regra, as ferramentas são inicializadas a partir de botões na action bar (`ActionBar.tsx`).

![image-2.png](/ferramentas-edição/image-2.png)

Esses botões nada mais fazem do que compor alguns dados e enviá-los para factor que criará uma instância da nossa ferramenta (`ToolFactory.ts`).

![image-3.png](/ferramentas-edição/image-3.png)

![image-4.png](/ferramentas-edição/image-4.png)

Nós utilizamos as interações do openlayer para definir a ferramenta vigente e existem métodos que já estão no fluxo que removem as ferramentas em uso e adiciona a nova instância.

![image-5.png](/ferramentas-edição/image-5.png)

Vale destacar que uma ferramenta pode ser principal ou não principal, sendo que as principais não podem concorrer com outras.

![image-6.png](/ferramentas-edição/image-6.png)
![image-7.png](/ferramentas-edição/image-7.png)
![image-8.png](/ferramentas-edição/image-8.png)

Após termos criado a classe e direcionado o fluxo de inicialização, precisamos começar a mapear seus eventos.

Os principais eventos são:

- OnClick
    ![image-9.png](/ferramentas-edição/image-9.png)

- OnMouseMove

    ![image-11.png](/ferramentas-edição/image-11.png)

- OnContextMenu

    ![image-10.png](/ferramentas-edição/image-10.png)

A maior parte das ferramentas tem o seu fluxo inicializado pelo `OnClick` e a partir daí utiliza-se o `OnMouseMove` para fazer algumas ações e por último utiliza-se do `OnContextMenu` para fechar o fluxo.


Observações importantes:

- Snap e Linhas guias - Devem ser inicializados dentro de cada ferramenta principal

    ![image-12.png](/ferramentas-edição/image-12.png)
    ![image-13.png](/ferramentas-edição/image-13.png)
    ![image-14.png](/ferramentas-edição/image-14.png)

- Finalização de uma ferramenta - Assim como inicializamos uma ferramenta, precisamos pensar em como vamos finalizá-la, para isso há um método que herdamos da AbstractMapTool que será chamado sempre no fluxo de troca de ferramenta. Portanto, se sua ferramenta inicializou algo ou precisa desmontar alguma coisa ao finalizar, sobrescreva esse método para adaptar o seu funcionamento.

    ![image-15.png](/ferramentas-edição/image-15.png)

**Como selecionar uma feição?**

Utilize o método tryGetFeatureByClicked, nele você pode passar parâmetros que definem se quer selecionar por arresta, vértice ou ponto interno.

![image-16.png](/ferramentas-edição/image-16.png)

**Como achar as coordenadas do meu mouse?**

Existem 2 maneiras de obter uma coordenada do mapa:
1.	Utilizando o this.currentMouseCoordinates, lá você terá acesso a coordenada exata do seu mouse.

    ![image-17.png](/ferramentas-edição/image-17.png)

2.	Utilizando a snapLayer, lá você terá acesso ao seu mouse ajustado pelo snap

    ![image-18.png](/ferramentas-edição/image-18.png)

**As Layers tem ação refletida:**

Então se você adiciona uma feição em duas layers e alterar uma delas, a outra será alterada. Para evitar isso use o ``GeometryUtils.duplicateNewFeature`` para duplicar sua feição.

MapToolService vai ter todos os métodos para modificar uma layer.