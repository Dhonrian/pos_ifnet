---
title: Apostila Edição
description: 
published: true
date: 2023-11-17T17:19:33.718Z
tags: 
editor: markdown
dateCreated: 2023-08-14T17:19:46.698Z
---

# Módulo Edição | Geopixel Cidades^®^  ![favicon.png](/favicon.png =3%x)

`SUMÁRIO`

**1.Iniciando a Edição e Criação de Geometrias: O que são os Dados Vetoriais e Matriciais?**
*1.1 Mas o que Pode Estar Contido em um Mapa?*
**2. Entendendo as Ferramentas para Criar uma Geometria**
*2.1 Criando Familiaridade com a Plataforma: Ferramentas de Edição*
*2.1.1 Como Funciona o Manual de Ferramentas para Edição?*
*2.1.2 Para que Servem os Botões de Atalho e Configuração?*
*2.1.3 Como eu Sei em Qual Tema Editar?*
*2.1.4 Para que Utilizar o Snap?*
*2.1.5 Para que Servem as Linhas Guias?*
*2.1.6 O Que é a Ferramenta de Topologia?*
**3. Criando as Primeiras Geometrias**
*3.1 Colocando a Mão na Massa: Como Criar a Primeira Geometria*
*3.1.2 Ferramentas de Criação: Pontos*
*3.2.1 Mapas*
*3.2.2 Temas Disponíveis*
**4.  Editando as Geometrias que Foram Criadas**
*4.1 Quais os Modos de Edição?*
*4.1.1 Relembrando Funcionalidades do Mapa para Editar*
*4.2 Usando as Ferramentas de Edição e Modificação de Geometrias*
*4.2.1 Ferramentas de Edição*
*4.2.2 Ferramentas de Alteração*
*4.2.3 Ferramentas de Vértice*
*4.2.4 Ferramentas de histórico*
*4.2.5 Ferramentas de Linha Guia*
*4.2.6 Ferramentas de Mover*
**5. Interações Entre as Ferramentas e Camadas**
*5.1 Dicas Práticas com as Ferramentas Analíticas para Criação e Edição de Geometrias*

## Neste módulo você vai:
- [x] **Entender o que são os dados geográficos**
- [x] **Compreender o que está contido em um mapa**
- [x] **Dar os primeiros passos para compreender as ferramentas de edição e criação de uma geometria**  
- [x] **Aprender sobre o uso de cada ferramenta com linhas, pontos e polígonos**
- [x] **Editar cada tipo de geometria**
- [X] **Dicas para otimização da sua vetorização**

## 1. Iniciando a Edição e Criação de Geometrias: O que são os Dados Vetoriais e Matriciais?🌎
**Olá usuário**! 🙋‍

Para iniciarmos nossa trajetória na edição e criação de geometrias, é necessário entendermos suas origens em um `Sistema de Informação Geográfica (SIG)`. 

> SIG (Sistema de Informações Geográficas) nada mais é do que a integração de diversos **recursos geográficos, metodológicos, tecnológicos** e **humanos** para aplicação, análise e promoção de dados para geração de **geoinformação**.
{.is-info}

As **geometrias** podem representar diversos tipos de estruturas físicas, como edificações, ruas, praças, quadras, lotes, áreas verdes, rios, lagos etc. 

Essas geometrias, em plataformas de `geoprocessamento`, são representadas a partir de **pontos, linhas** e **polígonos**, formando assim, os chamados **vetores**. As informações que podem estar contidas nesses vetores se originam por meio de um `sistema de coordenadas`. 

> O **sistema de coordenadas** vem lá dos conceitos matemáticos para definir a **localização** de valores que podem ser representados em diversos **planos dimensionais** ou em um sistema **local, regional** ou **global** (coordenadas geográficas). O geoprocessamento usa desses sistemas e outros  recursos para obter, projetar e criar **geoinformações**.
{.is-info}

Além dos vetores, os `dados geográficos` contidos em uma geometria são formados a partir de matrizes, que ocorrem por meio de `células` ou `pixels` carregando informações associadas aos **insumos** disponibilizados pela prefeitura, que de forma visual, formam **mapas temáticos** e **gráficos**, demonstrando as informações necessárias que devem ser passadas ao seus usuários.

> Células ou pixels são responsáveis por formar **elementos de imagens** a partir da combinação múltipla de seus elementos e **cores**.
{.is-info}

### 1.1 Mas o que Pode Estar Contido em um Mapa? 🗺
Um mapa tem por objetivo **comunicar informações** de forma **visual, interativa, didática** e **prática**, ou seja, é a forma simplificada de passar para o usuário diversas informações que se relacionam entre si. Essas informações, para serem passadas de forma simples, precisam de uma **linguagem** que represente de forma abrangente o espaço em que se forma esse mapa. 

Portanto, essa linguagem acontece por meio da **simbologia**, que nada mais é do que o destaque de **elementos pontuais, lineares ou zonais** (que são as geometrias citadas no começo desse capítulo) que representam por exemplo, localidades, diversas formas de vias, áreas florestais, terrenos, comércios e afins, como demonstrado na **Figura 1** abaixo.

![simbologia.png](/simbologia.png =50%x)
**Figura 1**: Exemplo de simbologias em um mapa.

Para localizar essas simbologias, será necessário mais algumas informações que determinam suas singularidades, ou seja, as `informações específicas de cada símbolo`. 

> As **informações específicas** de cada **símbolo** são obtidas a partir dos dados coletados pela **Geopixel^®^** associados aos dados disponibilizados pela **prefeitura**. Nos próximos capítulos veremos como associá-las às **geometrias criadas** e **editadas**.
{.is-warning}

Esses nomes chamaremos de **Toponímia**, que determinarão as referências específicas dessas simbologias, como por exemplo, o tipo de relevo, clima e outras características geográficas que também podem estar contidas em um mapa e na localização de seus elementos.

As informações associadas a uma localização, como um endereço, chamaremos de **Geocodificação**, que dependem de um par de **coordenadas** bidimensional, ou seja, coordenadas cartesianas X e Y.

Agora com todos os elementos vetoriais e matriciais e informações associadas, será possível entendermos e interpretarmos um mapa!

> **Muito bem**! A partir de agora podemos seguir com os **primeiros passos** para criação e edição de geometrias 👏🥳.
{.is-success}

## 2. Entendendo as Ferramentas para Criar uma Geometria🌎

### Neste capítulo você vai:
- [x] ~~Entender o que são os dados geográficos~~
- [x] ~~Compreender o que está contido em um mapa~~
- [x] **Dar os primeiros passos para compreender as ferramentas de edição e criação de uma geometria** 
- [ ] Aprender sobre o uso de cada ferramenta com linhas, pontos e polígonos
- [ ] Editar cada tipo de geometria
- [ ] Dicas para otimização da sua vetorização


### 2.1 Criando Familiaridade com a Plataforma: Ferramentas de Edição ✏

Após logar e abrir a página da **Geopixel Cidades^®^**, ao clicar no ícone de "lápis" ![lapis_edição.png](/lapis_edição.png =2%x) localizado no **canto superior direito da plataforma** (abaixo da ferramenta de seleção), será possível observar uma série de ferramentas disponíveis para darmos início a criação de uma geometria, como demonstrado na figura abaixo.

![ferramentasedição.png](/ferramentasedição.png)
**Figura 2**: Ferramentas de edição e criação de geometrias.

Ao todo são disponibilizadas **07 ferramentas** para edição e criação, em que cada uma possui **diversas funcionalidades** diferentes (**não se preocupe, detalharemos o uso de cada uma delas no próximo capítulo**). 

![ferramentas_edicao_edt.png](/ferramentas_edicao_edt.png)
**Figura 3**: Funcionalidades de cada ferramenta.

> A criação e a edição de geometrias só poderá ser realizada com a **camada** a ser editada **habilitada**! Sempre verifique se a camada habilitada, ou seja, tema ativo, é a que você gostaria de editar (Como já abordado no módulo de mapas temáticos)💡.
{.is-warning}

Além da **visualização** e **entendimento** das ferramentas de **criação** e **edição**, algumas funcionalidades serão necessárias para sua adaptação, como uma forma de facilitar algumas interações com a interface da **Geopixel Cidades^®^**.

As **funcionalidades** que são **essenciais** para seu **conhecimento** são:
- [x] Manual de Ferramentas; 
- [x] Botão de Atalhos;
- [x] Botão de Configuração;
- [x] Seleção do Tema a ser Editado;
- [x] Botão de Snap;
- [x] Botão de Linhas Guias;
- [x] Topologia das Linhas Guias.

> O Manual de ferramentas e o botão de atalhos são **essenciais** para verificar o **uso** e **funcionalidade** de **cada ferramenta**, utilizado por meio dos **atalhos** via teclado para facilitação do seu uso. Veremos o **detalhamento** de como usá-las a seguir 😉.
{.is-info}

#### 	2.1.1 Como Funciona o Manual de Ferramentas para Edição?📚 
Ao clicar nas **3 barras** ![barras_menu.png](/barras_menu.png =2%x) do **menu lateral esquerdo** da plataforma, é possível acessar o manual, que se encontra no penúltimo botão listado.

Automaticamente uma janela com uma **lista de todos os botões de edição**, com o nome da ferramenta e o ícone de cada uma aparece. 

Clicando no **ícone** referente a uma ferramenta, uma nova janela se abre e nesta consta a **descrição da ferramenta selecionada**, com as instruções de utilização de cada uma. 

![manualed_v3.png](/manualed_v3.png)
**Figura 4**: Manual de edição das ferramentas.

#### 2.1.2 Para que Servem os Botões de Atalho e Configuração?⚙
Os botões de "**atalho**" e "**configuração**" carregam **funcionalidades** para **informação** e ajuste de algumas ferramentas que **auxiliam** na edição e criação.

O **atalho**, que pode ser acessado por meio da **setinha**  ![setinha_atalho.png](/setinha_atalho.png =2%x) no **canto inferior direito da página**, possui a informação de comandos relativos a página no **geral** e no **modo** **de edição**. Neste modo, são exibidas algumas funcionalidades que podem ser **ativadas** via **teclado**, como **ativação do snap**, **desativar edição** e assim por diante. 

![atalho_ed.png](/atalho_ed.png)
**Figura 5**: Atalhos do modo de edição.

No caso do **botão de configuração** ![configuração.png](/configuração.png =2%x), que pode ser acessado na **barra vertical direita** da tela com as **ferramentas de edição**, é possível encontrar a habilitação do **Snap**, **Linhas Guias** e **Topologia**, que serão descritas mais a frente.

![ferramenta_confg.png](/ferramenta_confg.png)
**Figura 6**: Ferramenta de configuração.

#### 2.1.3 Como eu Sei em Qual Tema Editar?🔧
Relembrando a ativação de Tema já abordado no **módulo básico**, a seleção de temas para edição ocorre ao selecionar a camada a ser editada na caixa dos **Mapas** ![captura_de_tela_2023-08-25_092114.png](/captura_de_tela_2023-08-25_092114.png =2%x), nos **temas ativos**. Quando selecionada e habilitada, é possível utilizar as ferramentas para criação e edição das geometrias de acordo com o **tema alvo**, que estará destacado com as cores da camada habilitada na tela, de acordo com a **escala da imagem**.

![temas_edição.png](/temas_edição.png)
**Figura 7**: Tema de edição habilitado.

> A **camada** no mapa **habilitada** pode ser **verificada** ao lado do botão de atalhos, no canto **inferior direito da página**, a edição das geometrias **só** vai ocorrer se a camada estiver habilitada nos **Temas Ativos**.
{.is-warning}

#### 2.1.4 Para que Utilizar o Snap?📐
Essa funcionalidade é um **auxílio** para quando se está editando um **polígono**. Por exemplo, ela permite que, ao vetorizar um polígono, feche seus pontos com maior facilidade, pois ao se aproximar do vértice a ser fechado, esta entende que aquele ponto é o ponto final e **liga-se** a ele.

**O Snap pode ser desligado ou pode alterar a tolerância em pixel**, que corresponde a distância que o snap faz a aproximação do ponto do vetor.

![ferramentasnap_editado.png](/ferramentasnap_editado.png)
**Figura 8**: Ferramenta de snap.

>Um **snap** com valor **muito baixo**, diminui a precisão correta do vetor para se fechar um polígono, por isso, recomenda-se manter a **tolerância em pixel** sempre abaixo de **10**". 
{.is-warning}

#### 2.1.5 Para que Servem as Linhas Guias?📏
As linhas guias **ortogonais** e **angulatórias**, quando habilitadas, facilitam uma **vetorização** mais **angulada**, criando geometrias com **ângulos retos (90°)** ou **proporcional** a angulação de suas linhas, de forma ortogonal. 

É possível utilizar a ferramenta de "**Linhas Guias**" na caixa de seleção da edição, em configurações, habilitando/desabilitando ambas, uma ou nenhuma durante a vetorização. 

![linhasguias_editado.png](/linhasguias_editado.png)
**Figura 9**: Habilitação das linhas guias.

> Para **habilitá-las** e **desabilitá-las** de forma mais **ágil**, é possível utilizar o atalho via teclado clicando em **<kbd>CTRL</kbd> + <kbd>E</kbd>**. Recomenda-se sempre o seu uso para uma melhor **vetorização**.
{.is-info}

#### 2.1.6 O Que é a Ferramenta de Topologia? ⚒
A ferramenta de **Topologia** diz respeito ao **armazenamento** das informações das linhas guias e identificadores que compõem os **polígonos**. O ideal é que ela sempre esteja ativada (também encontrada no botão de configurações ![configuração.png](/configuração.png =2%x)).

`Nos capítulos seguintes abordaremos com mais detalhes o uso e aplicabilidades de todas as funcionalidades da edição, elucidando melhor o seu uso.`

> **Parabéns**! Agora que entendemos como utilizar os **recursos** de **criação** e seus **auxílios**, daremos continuidade aos **próximos** **capítulos**! 🥳👏
{.is-success}

## 3. Criando as Primeiras Geometrias🌎

### Neste capítulo você vai:
- [x] ~~Entender o que são os dados geográficos~~
- [x] ~~Compreender o que está contido em um mapa~~
- [x] ~~Dar os primeiros passos para compreender as ferramentas de edição de uma geometria~~ 
- [x] **Aprender sobre o uso de cada ferramenta com linhas, pontos e polígonos**
- [ ] Editar cada tipo de geometria
- [ ] Dicas para otimização da sua vetorização

### 3.1 Colocando a Mão na Massa: Como Criar a Primeira Geometria🏠

Como apresentado no capítulo anterior, para darmos inicio a criação de uma geometria, o primeiro passo a ser tomado é **habilitar o botão de edição** e a **camada** (tema ativo) a ser editada.

Todas as ferramentas apresentadas a seguir, abarcam as funcionalidades de **pontos**, **linhas** e **polígonos**.

![ferramentasedicao_editadooo.png](/ferramentasedicao_editadooo.png)
**Figura 10**: Ferramentas de criação.

Para exemplificar o uso das ferramentas, utilizaremos camadas de teste para demonstrar o **passo a passo** para criação de uma geometria. Nestas camadas, é possível utilizarmos **ferramentas lineares e para criação de polígonos**.

> A depender da **camada** a ser **editada**, você perceberá que a disposição de ferramentas pode mudar, dependendo do tipo de **Simbologia** a ser editada, podendo se diferenciar de modo **pontual**, **linear** ou **zonal** (Como vimos no primeiro capítulo). Por exemplo, em camadas que utilizarão apenas ferramentas de "**pontos**", **NÃO** haverá a criação de **polígonos**. Detalharemos melhor mais pra frente 😉.
{.is-warning}


### 3.1.1 Ferramentas de Criação: Linhas e Polígonos🌐
Ao clicar com o botão esquerdo na habilitação da ferramenta de edição, aparecerão ao lado esquerdo do ícone seus subitens, como **destacados em vermelho** na figura abaixo.

![ferram_linhaspoligonos.png](/ferram_linhaspoligonos.png)
**Figura 11**: Funcionalidades das ferramentas de criação.

O primeiro subitem é a ferramenta de Criação, que possui **diversos itens para criação e edição** de **linhas** e **polígonos**.

> Algumas ferramentas de **criação**, como alguns tipos de **arcos** também serão utilizáveis para a criação de **linhas**. Abaixo estarão contidas no passo a passo a **utilização** para cada tipo de **simbologia**.
{.is-info}

#### Ferramenta Polígono/Linha
Essa ferramenta tem por função **desenhar linhas ou polígonos** com o auxilio de ferramentas de angulação e distância das retas, ou seja, o desenho de **polígonos**, como lotes ou **linhas** com **ângulo reto**, como vias, rios, etc, por exemplo.

Para utilizá-la, você irá:
1. **Clicar** na ferramenta;
2. Com o **botão esquerdo** do mouse, **desenhar a geometria** correspondente ao seu interesse e camada;
3. Ao finalizar, **clicar** com o **botão direito** do mouse, **salvando** **automaticamente** a geometria;

![poligonolinha_editadoo.png](/poligonolinha_editadoo.png)
**Figura 12**: Passo a passo da criação de uma geometria.

> Em qualquer camada para **vetorização** de **polígonos** ou **linhas**, será esse o processo com a ferramenta. Caso você feche sem querer a **caixa de edição**, clique **novamente** na ferramenta, selecione a geometria e verifique-a.
{.is-info}

#### Retângulo
A ferramenta **Retângulo** permite ao usuário desenhar um **polígono** a partir da criação de sua primeira aresta. Muito utilizada para a criação de piscinas, lotes, quadras etc. 

Para seu uso, você vai: 
1. **Clicar** na ferramenta;
2. Com seu **primeiro** clique com o **botão esquerdo do mouse**, desenhe a **primeira** **aresta**.
3. Seguir com o cursor do mouse a **direção** em que pretende **desenhar** sua **geometria**, ele **automaticamente** irá desenhar o retângulo a partir da sua **primeira aresta**;
4. Após conclusão do polígono, clique com o botão esquerdo do mouse para finalizar a **vetorização** e **salvar** a geometria;

![retangulo_editadoo.png](/retangulo_editadoo.png)
**Figura 13**: Passo a passo da criação de um retângulo.

#### Ferramenta de Círculo
A ferramenta permite que o usuário possa desenhar **geometrias**, por meio de **polígonos**, em formatos **circulares**.
Para seu uso, o usuário precisará:
1. Clicar na ferramenta com o **botão esquerdo** do mouse;
2. Clicar com o **botão esquerdo** na **borda** que gostaria de iniciar o desenho;
3. Ao **finalizar**, clicar com o **botão esquerdo** para **salvar** a geometria;

![circulo_editadoo.png](/circulo_editadoo.png)
**Figura 14**: Passo a passo da criação de um círculo.

> É importante ressaltar que o **clique inicial** para desenhar a geometria deverá ser feito **na borda do objeto** identificado, e **não** no seu centro, pois o primeiro clique define o **diâmetro de abertura do circulo**, conforme o movimento do mouse e direção. 
{.is-warning}

#### Ferramenta de Elipse 
A ferramenta de elipse pode ser utilizada para **vetorização de polígonos**, a partir do seu desenho definido pelo **raio da geometria**.

Para seu uso, você terá que:
1. **Clicar** na ferramenta;
2. Utilizar o **botão esquerdo do mouse** para fazer o desenho do **primeiro raio**;
3. Ao finalizar, **clicar novamente** com o **botão esquerdo**  e **mova o mouse** para iniciar o desenho do **segundo raio**;
4. Finalize o desenho **clicando** com o **botão esquerdo do mouse**, assim **salvando** a geometria.

![elipse_editadoo.png](/elipse_editadoo.png)
**Figura 15**: Passo a passo para a criação da elipse.

> As funcionalidades dessa ferramenta são **similares** as da ferramenta de círculo, então comece com o **primeiro clique** para **definição do raio**. Mas nesse caso, **NÃO necessariamente** pela borda, e sim pelo **centro da geometria**.
{.is-warning}

#### Ferramentas de Curva
Essa ferramenta possui **4 tipos** de funcionalidade diferentes para utilização:

- Curva Livre de 3 pontos;
- Curva Fixa de 3 pontos;
- Arco de 3 pontos;
- Arco de 2 pontos.

![curvas.png](/curvas.png)
**Figura 16**: Ferramentas de curva e arco.

`Para a vetorização linear, apenas as ferramentas de arco e desenho livre estarão disponíveis.`
> As **ferramentas de curva** são essenciais para geometrias **curvilíneas** ou **disformes**, como ruas, piscinas, quadras e lotes curvos, rios, lagos e afins. Todas são possíveis de serem usadas para temas **lineares** ou **zonais** (com polígonos) 💡.
{.is-info}

##### Curva Livre de 3 Pontos 
Essa ferramenta tem por função transformar uma **linha reta de um polígono** em uma **curva**, podendo ser direcionada para **qualquer ângulo**, conforme a movimentação que o usuário fizer com o **cursor do mouse**, como demonstrado na figura abaixo.

![curvalivre3p_editadoo.png](/curvalivre3p_editadoo.png)
**Figura 17**: Passo a passo curva livre de 3 pontos.

Para uso da ferramenta, você precisará:
1. **Criar uma linha reta** (ou um **polígono**);
2. Clicar com o **botão esquerdo** do mouse na ferramenta **curva livre de 3 pontos**;
3. Clicar na **aresta** a ser aplicada a curva, **movimentando** por meio do cursor do mouse e conforme a **direção** que se adapte a necessidade da **geometria**;
4. Clicar com o **botão direito** do mouse para **finalização** da curva. Após esse passo, ela será salva automaticamente; 

> Para uso dessa ferramenta, é necessário ter uma **linha** desenhada com a ferramenta **"polígono"**, em que o **primeiro** e o **último ponto** da linha, serão as **extremidades** da curva.
{.is-warning}

##### Curva Fixa de 3 Pontos
Assim como a curva livre de 3 pontos, a ferramenta de **curva fixa de 3 pontos** permite ao usuário **transformar** uma **linha reta de um polígono** em uma **curva**. No caso desta ferramenta, o **diferencial** é que a curva formada mantém uma **mesma angulação** ao longo de **toda** a **curva**.

![curvafixa3p_editado.png](/curvafixa3p_editado.png)
**Figura 18**: Passo a passo curva fixa de 3 pontos.

Para uso da ferramenta, será necessário você:
1. **Selecionar** a ferramenta de **curva fixa**;
2. Clicar com o **botão esquerdo** na **aresta** que deseja **transformar** em uma **curva**;
3. Clicar com o **botão esquerdo** no ponto que gostaria que fosse o **mais alto** da **curva** (**ponto fora da geometria, perpendicular a aresta**);
4. Assim que escolher qual seria o **ponto** mais **alto**, clicar com o **botão direito do mouse** para salvar a geometria.

> **Diferente** da **curva livre**, a **definição** da **direção** da curva é **única**, sendo definida por um **único clique,** sendo esse o ponto de **maior inclinação** da curva.
{.is-warning}

##### Arco de 2 Pontos
Essa ferramenta consiste em um processo de **transformação** de uma **aresta** em **curva** similar as funções anteriores das ferramentas de curva. 

Seu **diferencial** é que ao selecionar a **direção** em que a curva será formada (novamente sendo definida por um clique e não como a movimentação da curva livre), será digitado o **raio específico** da curva (Como demonstrado nas figuras após o passo a passo).

> Para uso dessa ferramenta, a criação da geometria (seja por **linhas** ou **polígonos**) deve ocorrer **antes** de seu uso, com pontos na extremidade da aresta para se formar a curva depois.
{.is-warning}

Para seu uso, você precisará:
1. **Habilitar** a **ferramenta**;
2. **Selecionar** uma das **arestas** ou **linha** para **transformar** em **curva**;
3. Após selecioná-la, **dois círculos pontilhados** aparecerão, possuindo como área comum da sua interseção das partes a **aresta** selecionada;
4. **Digite** o **raio** da curva (**em números**) na parte **inferior esquerda** da **tela** (vide figura);
5. **Clique** na **curvatura** de um dos círculos, conforme sua direção (**convexa ou concava**);
6. Clicar com o **botão direito do mouse** na geometria, salvando automaticamente sua geometria.

![arco2p_editado.png](/arco2p_editado.png)
**Figura 19**: Passo a passo arco de 2 pontos.

##### Arco de 3 Pontos
A ferramenta de **arco de 3 pontos** permite ao usuário transformar uma **linha reta** (criada com a ferramenta **polígono ou linha**) em uma linha com **inclinação curva** com **3 pontos fixos**, ou seja, onde o **ângulo** da **curva** é o **mesmo** em toda sua **extensão**.

Para seu funcionamento, a ferramenta cria um **meio círculo** a partir da **linha** que terá como ponto de **maior inclinação** da curva o **local** onde será feito o **clique** (assim como a ferramenta anterior).

Para uso dessa ferramenta:
1. **Selecione-a**;
2. Clique com o **botão esquerdo** em uma **aresta** que deseja transformar em **curva**;
3. Clique com o **botão esquerdo** exatamente onde gostaria que fosse o ponto **mais alto da inclinação**;
4. Clique com o **botão direito do mouse** para **finalizar** e **salvar** sua geometria.

![arco3p_editado.png](/arco3p_editado.png)
**Figura 20**: Passo a passo arco de 3 pontos.

#### Ferramenta de Desenho Livre 
Ela permite ao usuário **desenhar** uma geometria **livremente**, podendo ser de forma linear ou poligonal, com o auxílio da **linha guia** e através da **movimentação** do **cursor** do **mouse**. 
Para utilizar a ferramenta, você vai:
1. **Clicar** na ferramenta;
2. Clicar no local que deseja desenhar utilizando o **botão esquerdo do mouse** para fazer o desenho (seguindo a **movimentação do cursor do mouse**);
3. Ao finalizar o desenho, clique com o **botão direito do mouse**, salvando **automaticamente** a geometria;

![desenholivre_editado.png](/desenholivre_editado.png)
**Figura 21**: Passo a passo desenho livre. 

> **Eba**! Agora você já pode fazer suas **geometrias lineares e poligonais**! 🥳 
Que tal vermos agora como usar as ferramentas de **criação para pontos**? Vamos nessa continuar o capítulo 😉.
{.is-success}

### 3.1.2 Ferramentas de Criação: Pontos 📌
Ao clicar com o **botão esquerdo** para habilitar a **ferramenta de edição**, aparecerão ao lado **esquerdo** do ícone seus **subitens**.

![ferramenta_pontoo.png](/ferramenta_pontoo.png)
**Figura 22**: Funcionalidades da ferramenta de ponto.

O segundo subitem é a **ferramenta de ponto**, que cria pontos para camadas e simbologias **pontuais**.

> Para se criar um ponto, sempre será utilizado o **botão esquerdo do mouse** para pontuar e o **direito** para **finalização** e **salvamento**. Para verificar os atributos, será necessário **fechar** a edição e selecionar o ponto na **camada**. Esse processo será melhor detalhado no próximo capítulo 😉.
{.is-info}

Para **elucidação** dos passos para uso das ferramentas de **criação de pontos**, aqui usaremos a camada de **Atendimento Cidadão**. 

`⚠ Não se esqueça de habilitar a camada de interesse para edição nos temas ativos!⚠`

####	Criando um ponto 
Para se criar um ponto iremos:
1. Selecionar a ferramenta de criação com o **botão esquerdo** do mouse;
2. Clique no **local** desejado para se criar um **ponto no mapa**;
3. Um **círculo laranja** irá surgir, mostrando que o ponto ainda não está salvo, e sim **em edição**;
4. Para **salvá-lo**, clique com o **botão direito** do mapa.

![ponto_editado.png](/ponto_editado.png)
**Figura 23**: Passo a passo criação de ponto.

> Além da criação do ponto, um **passo importante** após salvar o ponto criado é o **preenchimento dos atributos** associados as informações do ponto. Essas informações poderão ser obtidas por meio do **cadastro** disponibilizado pela **prefeitura** de atuação ou **coleta direta** dos dados.
{.is-info}

![atributos_ed.png](/atributos_ed.png)
**Figura 24**: Preenchimento de atributos (ordem de 1 a 4).  

Agora, algumas **informações importantes** para **criação** e **preenchimento** de um **ponto**:

- [X] Ao criar **pontos consecutivos**, as informações preenchidas no **ponto anterior** poderão ser **carregadas** para os **pontos conseguintes**. Neste caso é só fazer as **alterações necessárias** e **salvar**, ou **manter** caso os itens de preenchimento forem os mesmos;
- [X] No caso de ser um ponto de dúvida ou alinhamento, como no tema de alinhamento prefeitura por exemplo, o preenchimento dos atributos se dá a partir da dúvida ou solicitação desejada pelo usuário;
- [X] Um ponto com a **borda laranja** sinaliza que o mesmo está em **edição**, podendo **não** estar com as **informações** **salvas**. Nesse caso, sempre **verifique** e **salve o ponto**, que ficará com a **cor preenchida** com base no tema ativo;
- [X] Pontos com **cores** e **ícones** **diferentes** referem-se a **informações** **diferentes**. Para saber o significado de cada uma, clique na **camada** de **atuação** (tema ativo) do ponto desejado com o botão direito do **mapa** e em seguida clique em "**legenda**" com o **botão esquerdo**;

![legenda_editadoo.png](/legenda_editadoo.png)
**Figura 25**: Legenda do ponto "habite-se". 

- [X] Para **selecionar um ponto**, sempre utilize a ferramenta "**selecionar**" com o **ícone** ![captura_de_tela_2023-08-25_145956.png](/captura_de_tela_2023-08-25_145956.png =2%x). Ela permite selecionar a geometria desejada e fazer **edições** nos **atributos** da mesma ou salvar após criar/mover. (As edições e movimentação de geometrias veremos nos próximos capítulos 😉).
 
>  **Parabéns**!! 🏆 Agora você concluiu mais um capítulo e está pronto pra criar suas geometrias no **Geopixel Cidades^®^**! Muito bem! Agora que tal aprendermos a **editar** essas **geometrias**? 🚀
{.is-success}

## 4. Editando as Geometrias que Foram Criadas🌎

### Neste capítulo você vai:
- [x] ~~Entender o que são os dados geográficos~~
- [x] ~~Compreender o que está contido em um mapa~~
- [x] ~~Dar os primeiros passos para compreender as ferramentas de edição e criação de uma geometria~~
- [X] ~~Aprender sobre o uso de cada ferramenta com linhas, pontos e polígonos~~
- [X] **Editar cada tipo de geometria**
- [ ] Dicas para otimização da sua vetorização

### 4.1 Quais os Modos de Edição? ✂
Dando início a este capítulo, para uso das **ferramentas de edição**, é importante entendermos como funciona a dinâmica dos seus usos. 

A edição de geometrias pode ocorrer de acordo com a **necessidade** do **usuário**, podendo ser a partir da **atualização** ou **ajuste** dos **atributos** de alguma **simbologia**, da alteração por meio da **movimentação** da geometria ou até para **deletá-la**.  

> Para edição de uma **geometria**, além do uso de **ferramentas**, a edição de **atributos** é feita quando a ferramenta de edição é **fechada** e a seleção ocorre a partir do **tema ativo** e seleção da **geometria**. Falaremos sobre isso mais à frente 😉. 
{.is-info}

#### 4.1.1 Relembrando Funcionalidades do Mapa para Editar 📚
Assim como abordado no **Módulo Mapa Temático**, algumas **funcionalidades** do mapa/plataforma são **importantes** de serem relembradas rapidamente para se evitar alguns erros **durante** a **edição**.

- [X] **Clicar** no ícone ![captura_de_tela_2023-08-25_092114.png](/captura_de_tela_2023-08-25_092114.png =3%x) de cada **tema** no mapa **não** significa que ele **esteja** em **edição**, apenas está disponível para **visualização** do mapa;
- [X] Para **selecionar** o **tema alvo** de edição e deixá-lo **ativo**, clique em cima dele e verifique se o mesmo está **ativo** para **edição** no canto **inferior direito da tela**;
- [X] Dependendo do **zoom/escala** em que o tema esteja, ele pode **não** estar **disponível** para **edição**. Sempre **confira** a **escala** para cada **tema** de **edição**. 
- [X] **Temas diferentes, funcionalidades diferentes**: As **ferramentas** de **edição** não serão as mesmas **disponíveis** em todas as **camadas**, a depender do tipo de **simbologia**.

> O botão de **configuração de edição**, como citado nos capítulo anteriores, possui as funcionalidades de configurar o **snap, linhas guias** e **topologia**, que podem auxiliar durante a **criação** de uma geometria.
{.is-info}

`Agora seguiremos para o uso das ferramentas de edição!✂⚙🛠 ` 

### 4.2 Usando as Ferramentas de Edição e Modificação de Geometrias 🔧

#### 4.2.1 Ferramentas de Edição 📝
Após clicar no ícone de **habilitar** **edição**, dentro das ferramentas de edição/criação, **4** possuem a função de **redimensionar o beiral, girar**, **deletar** e **duplicar** a **geometria**, como ilustrado abaixo.

![ferramentas_edicao_editadoooooo.png](/ferramentas_edicao_editadoooooo.png)
**Figura 26**: Funcionalidades da ferramenta de edição.

(I) **Beiral**: A ferramenta de **beiral** possibilita o usuário **delimitar** uma geometria **poligonal** e retirar o **excesso** de **telhado** correspondente ao **beiral** (parte que vai além da edificação). Seu uso permite que a área correspondente a uma construção seja apenas a de **área construída**, gerando uma geometria com a nova medida configurada em todas as bordas. 

Para uso da ferramenta, você necessitará: 

- **Selecionar** a ferramenta em "**ferramentas de edição**";
- Em seguida, selecione a **geometria**;
- **Configure** a **distância** (em **metros**) que gostaria de **descontar** do **beiral** na **barra inferior** da plataforma;
- Após definir a **distância**, clique em <kbd>Enter</kbd> e em seguida clique em "**ok**" para **confirmar** o recorte;
- Clique com o **botão direito do mouse** na tela e **salve** a geometria nova.

![beiral_editadoo.png](/beiral_editadoo.png)
**Figura 27:** Passo a passo da ferramenta de beiral.

 (II) **Girar geometria**: Essa ferramenta permite ao usuário **rotacionar** geometrias em torno de um **ponto ancorado** no mapa.
 Para usá-la:
 
 - Clique na ferramenta de **girar** **geometria**;
 - Clique com o **botão esquerdo** do mouse na **geometria** **escolhida**, sendo necessário clicar uma **segunda vez** para começar a movimentar e geometria;
 - Com o **cursor do mouse**, indique a direção em que gostaria de **girar** a geometria;
 - Clicando com o **botão direito**, **salve** a geometria.
 ![girar_editado.png](/girar_editado.png)
 **Figura 28**: Passo a passo para girar a geometria.
 
 (III) **Duplicar geometria**: A ferramenta Duplicar Geometria permite ao usuário copiar geometrias, de temas poligonais, lineares ou pontuais.
 Para seu uso, você precisará: 
 
 - Clicar na ferramenta **Duplicar Geometria** em **Ferramentas de Edição**;
 - Clicar com o **botão esquerdo** na geometria a ser **duplicada**;
 - Clicar novamente com o **botão esquerdo** para **movimentar** a geometria duplicada;
 - Clicar com o **botão direito** para **salvar** a **geometria nova** (duplicada).
 
 ![duplicar_editado.png](/duplicar_editado.png)
**Figura 29**: Passo a passo para duplicar geometria.
 
 (IV) **Deletar geometria**: Para deletar uma geometria, poligonal, linear ou pontual, será necessário:
 
 - Com a ferramenta "**seleção**" em **ferramentas de edição**, clicar na geometria a ser **deletada**;
 - Com a geometria **selecionada**, clicar na ferramenta de **deletar geometria**;
 - Clicar em "**sim**" para **deletar** a **geometria**.
 
 ![deletar_editado.png](/deletar_editado.png)
 **Figura 30**: Passo a passo para deletar uma geometria.
 
#### 4.2.2 Ferramentas de Alteração 🖍
O **segundo bloco** de **ferramentas**, abaixo da ferramenta de edição, é o bloco das **ferramentas de alteração**, que possui **2** subitens: **unir** **geometrias** e **desmembrar** **geometrias**. Ambas as ferramentas podem ser utilizadas em temas **poligonais**.

![ferramentas_alteracao_editado.png](/ferramentas_alteracao_editado.png)
**Figura 31**: Funcionalidades da ferramenta de alteração. 

(I) Para se utilizar a ferramenta de `unir geometria`, o usuário precisará:

- Selecionar a ferramenta de **Unir Geometria**;
- Clicar com o **botão esquerdo do mouse** nas geometrias a serem **unificadas**;
- Clicar com o **botão direito do mouse** para **salvar** a **nova** **geometria** unificada.

![unir_editado.png](/unir_editado.png)
**Figura 32**: Passo a passo para unir geometrias. 

(II) Para se utilizar a ferramenta de `desmembrar geometrias`, o usuário precisará:

- **Selecionar** a ferramenta de **desmembramento**;
- **Desenhar** (com o **botão esquerdo do mouse**) uma **linha** separando a geometria a ser **desmembrada**;
- Ao finalizar o desenho da linha, clicar com o **botão direito do mouse** na tela;
- Clicar em "**sim**" para **salvar** as **geometrias** **desmembradas**.

![desmembrar_editado.png](/desmembrar_editado.png)
**Figura 33**: Passo a passo para desmembrar geometrias.

#### 4.2.3 Ferramentas de Vértice 📐
No **terceiro bloco** de **ferramentas**, estão contidas as **ferramentas de** **vértices** e seus subitens: **adicionar vértice**, **remover vértice**, **definir testada** e **pontos memoriais**.

![ferramentas_vertice_editadoooooo.png](/ferramentas_vertice_editadoooooo.png =30%x)
**Figura 34**: Funcionalidades das ferramentas de vértice.

> As ferramentas de vértice ativas para **temas lineares** serão apenas as ferramentas de **adicionar** e **remover vértices**.
{.is-warning}

(I) **Adicionar Vértice**: Essa ferramenta permite ao usuário **incluir** **vértices** em **temas** como **polígonos** e **linhas**.
Para sua utilização, o usuário deverá:

- Clicar na ferramenta de **adicionar vértice** contida nas **ferramentas de vértices**;
- Com o cursor do mouse em cima da geometria escolhida, verificar a **marcação dos vértices** (em laranja) e com o **botão esquerdo** do mouse **adicionar** o vértice no local de preferência;
- Clicando com o **botão direito** do mouse, **salve** a geometria.

![advertice_editado.png](/advertice_editado.png)
**Figura 35**: 	Passo a passo para adicionar vértice.

(II) **Remover Vértice**: A ferramenta permite ao usuário **remover** vértices de  temas como **polígonos** e **linhas**. Para utilizá-la:

- Clicar na ferramenta de **remover vértice** contida nas **ferramentas de vértices**;
- Ir para a **geometria** escolhida e passando o **cursor do mouse** por cima dela, é possível verificar quais os **vértices** **ativos** que poderão ser **removidos**;
- Clique no vértice com o **botão esquerdo** do mouse e para **salvar** a **alteração**, clique com o **botão direito**.

![remvertice_editadoo.png](/remvertice_editadoo.png)
**Figura 36**: Passo a passo para remover vértice.

(III) **Definir Testada**: A ferramenta Definir Testada, **define** a **direção** em que a testada segue em um lote e **limpa** pontos que são considerados **desnecessários** na **geometria**. Portanto, seu uso se dá para temas **poligonais**. 
Para utilizá-la o usuário precisará:

- Selecionar a ferramenta na caixa de **Ferramentas de Vértice**;
- Com o **botão esquerdo** do mouse, selecionar a **geometria** a ser definida a **testada**, apertando um de seus **vértices**;
- Para definir a **direção** da testada, use a seta "**pra cima**" do teclado;
- Após definição, clicar com o **botão direito** do mouse, optando por **salvar** a geometria.

![testada_editado.png](/testada_editado.png)
**Figura 37:** Passo a passo para definição de testada.

(IV) **Pontos Memoriais**: Os Pontos Memoriais permitem **configurar** informações de **polígonos**, a fim de auxiliar no **memorial descritivo**, sendo possível nomear e estabelecer regras para **arco** e **curvas**. Por exemplo, ao invés de aparecer ponto 1 com 30cm de A até B, ponto 2 com 10cm de B até C e assim por diante, o usuário poderá configurar que os pontos 1 a 12 formem **uma curva**, somando a extensão e aparecendo como uma **única** **curva**. 
Para utilizá-la:

- **Selecione** a ferramenta;
- Logo após, selecione o **ponto** (vértice) **inicial** de sua geometria;
- Com a tecla "pra cima" do teclado escolha a direção de ordem dos pontos (horário ou anti horário);
- Pressione a tecla <kbd>Enter</kbd> do teclado para abrir a janela de configuração para assim adicionar as regras, ponto inicial e final; 
- Por fim, salve a geometria.

![pontomemo_editado.png](/pontomemo_editado.png)
**Figura 38**: Passo a passo pontos memoriais.

> Para cada geometria encontrada no **interior da selecionada**, será adicionado na **contagem** da mesma os pontos memoriais, mantendo a **topologia existente**. Nesta janela ainda pode-se escolher quais os **temas selecionados**, antes de **salvar** para **armazenagem** no banco de dados.
{.is-info}

#### 4.2.4 Ferramentas de histórico ↩
No **quarto bloco** estão contidas as **ferramentas de histórico**, com duas opções de alteração: **undo** e **redo**. 
Essa funcionalidade é permissível em qualquer ação de qualquer tema ativo e suas simbologias. 

- "**Undo**" refere-se a **desfazer ações** na criação ou edição de uma geometria, como o <kbd>CTRL</kbd> + <kbd>Z</kbd>; 
- "**Redo**" refere-se a **refazer uma ação** de criação ou geometria que foi desfeita, assim como as teclas <kbd>CTRL</kbd> + <kbd>Y</kbd>.

![ferramentas_historico_editado.png](/ferramentas_historico_editado.png)
**Figura 39**: Uso da ferramenta de histórico.

#### 4.2.5 Ferramentas de Linha Guia 🪡
No **quinto bloco** de **ferramentas**, estão contidas as **ferramentas** de **linha guia**, possuindo como subitem as ferramentas de **linha guia paralela** e **linha guia aleatória**.
Ambas as linhas possuem função de auxiliar na vetorização de alguma geometria, poligonal ou linear.

![ferramentas_linhaguia_editado.png](/ferramentas_linhaguia_editado.png)
**Figura 40**: Ferramentas de linhas guia.

(I) `Linha guia paralela:` Para uso dela o usuário precisará selecionar a ferramenta, clicar com o **botão esquerdo no vértice** da geometria escolhida e a partir desse ponto, uma **linha paralela** a ele aparecerá, permitindo ao usuário selecioná-la com o **botão direito** para **fixá-la**.

(II) `Linha guia aleatória:` Para uso dessa ferramenta o usuário precisará **selecioná-la** e em seguida **clicar** em **qualquer ponto** na tela para **fixar** o **primeiro ponto**, podendo ser gerado vários pontos seguindo na construção da linha. Para fixá-la, é só **clicar** com o **botão direito** do mouse.

![linhasaleatoriaparalela_editado.png](/linhasaleatoriaparalela_editado.png)
**Figura 41**: Uso da ferramenta de linha guia paralela e linha guia aleatória.

> As linhas guias ficam **ativas** para auxílio durante a **vetorização** ou **edição** de uma geometria. Caso queria **apagá-las**, clique com o **botão esquerdo do mouse** em "**limpar seção**" no ícone ![limparsecao.png](/limparsecao.png) ou clique em "**fechar a edição**".
{.is-info}

#### 4.2.6 Ferramentas de Mover 🎯
No **sexto e último bloco**, estão contidas as **ferramentas de mover**, possuindo como subitens a ferramenta de **mover ponto**, **mover geometria** e **mover aresta**. Todas possuem a funcionalidade de ajuste da edição de geometrias, por meio de seu **posicionamento**, **dimensão** ou ajuste conforme a **projeção da imagem**.

![ferramentas_mover_editado.png](/ferramentas_mover_editado.png)
**Figura 42**: Ferramentas de mover. 

(I)`Mover Ponto`: A ferramenta de **Mover Ponto** permite ao usuário movimentar um **ponto específico**, de dentro para fora da geometria, conforme sua **preferência** e **necessidade**. Com ela é possível movimentar pontos de temas **poligonais**, **lineares** ou por **pontos**.
Para utilizá-la:

- **Selecione** a ferramenta;
- Selecione na geometria escolhida, com o **botão esquerdo do mouse**, um **vértice** para **movimentá-lo** conforme sua escolha;
- Clique com o **botão direito do mouse** para **finalizar** e **salvar** a mudança.

![moverponto_editado.png](/moverponto_editado.png)
**Figura 43**: Passo a passo da ferramenta de mover ponto.

(II) `Mover Geometria`: A ferramenta permite ao usuário **movimentar** uma **geometria inteira** e de modo **unitário**, por meio de **polígonos** ou **linhas contínuas**. Para movimentar uma geometria:

- **Selecione** a ferramenta;
- Selecione a geometria escolhida com o **botão esquerdo do mouse** e em seguida, a mesma ficará na tonalidade **azul**, indicando estar em **edição**;
- Conforme a **movimentação** do **cursor** do mouse, movimente a **geometria** até o **local** que gostaria de **fixá-la**;
- Clique com o **botão direito do mouse** para **finalizar** e **salvar** a geometria editada.

![movergeometria_editado.png](/movergeometria_editado.png)
**Figura 44**: Passo a passo da ferramenta de mover geometria.

(III) `Mover Aresta`: A ferramenta **Mover Aresta** permite ao usuário mover arestas de geometrias **previamente selecionadas**. Seu uso se dá para **temas poligonais** e **lineares**. Para utilizá-la, o usuário precisará:

- **Selecionar** a geometria;
- Movimentando o mouse até a **aresta** da geometria, clique com o **botão esquerdo do mouse** na aresta escolhida, que estará sendo indicada por um **quadradinho vermelho**;
- **Movimentando** a aresta, posicione-a no **local** desejado, conforme movimentação do **cursor do mouse**;
- Clique com o **botão direito do mouse** para **finalizar** e **salvar** a geometria. 

![moveraresta_editado.png](/moveraresta_editado.png)
**Figura 45**: Passo a passo da ferramenta de mover aresta.

> **Uhuul!** Mais um capítulo **concluído** com sucesso, **PARABÉNS**!🏆🥳
A partir de agora, você poderá **criar** e **editar** suas geometrias com as ferramentas do **Geopixel Cidades^®^**! Agora iremos para nosso **último capítulo**!💯👌
{.is-success}

## 5. Interações Entre as Ferramentas e Camadas🌎
### Neste capítulo você vai:
- [x] ~~Entender o que são os dados geográficos~~
- [x] ~~Compreender o que está contido em um mapa~~
- [x] ~~Dar os primeiros passos para compreender as ferramentas de edição e criação de uma geometria~~
- [X] ~~Aprender sobre o uso de cada ferramenta com linhas, pontos e polígonos~~
- [X] ~~Editar cada tipo de geometria~~
- [X] **Dicas para otimização da sua vetorização**

### 5.1 Dicas Práticas com as Ferramentas Analíticas para Criação e Edição de Geometrias 📈

Neste **último capítulo** serão reiteradas algumas **informações** já abordadas **neste módulo** e no **módulo básico**, apenas para reforçar algumas **informações** para os usuários que estarão utilizando as ferramentas do **Geopixel Cidades** para **vetorização**.


> ✅Para camadas de vetorização com **temas poligonais**, utilize sempre o auxílio da **Visão Panorâmica**, pois os detalhes como formatos de quadras, lotes e edificações - até mesmo os **andares das edificações** - **otimizam** sua vetorização, fazendo com que fique o mais próximo possível da **área real** de suas **geometrias**.
{.is-info}

> ✅A **escala** utilizada para vetorização das camadas varia conforme o **tema de edição ativo**. 
Isso ocorre para otimizar o tempo de **vetorização** para cada camada e para não sobrecarregar as informações que podem ser carregadas pela **plataforma**. 
Você pode **alterar** essa **escala** a depender da sua necessidade de vetorização seguindo o caminho: **Botão direito do mouse na camada> Editar estilo >**
{.is-info}

> ✅Por último mas não menos importante, os **insumos** associado a **plataforma** utilizada contém as **informações** mais **atualizadas** referentes a **cada camada**, portanto, qualquer dúvida a respeito das **informações** para complemento de alguma edição de atributos e afins, como área construída, pode estar contido nos **insumos disponibilizados**. 
{.is-info}

> 🚀🏆 Agora você está **apto** à utilizar as **ferramentas** de edição da **plataforma** Geopixel Cidades. **PARABÉNS**!!!! 🏆🚀
{.is-success}







