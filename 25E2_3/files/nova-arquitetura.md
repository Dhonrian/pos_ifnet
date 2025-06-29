---
title: DS - Nova arquitetura de Front-end
description: Definições sobre a arquitetura de front-end adotadas pela Geopixel.
published: true
date: 2023-08-14T18:53:42.333Z
tags: frontend, design system, ds
editor: markdown
dateCreated: 2023-08-01T18:27:21.318Z
---

# Nova Arquitetura de Frontend

## Estrutura de pastas

```
.
└── /ds
    └── /styles
        ├── /core
        ├── /constants
        └── /helpers
            ├── /extensions
            ├── /functions
            ├── /mixins
            └── /variables
```
## pastas {.tabset}
### /core
Conterá geralmente arquivos globais basilares, geralmente o reset de estilos e definições básicas de classes e estilização inicial de tags.

**Regras**:
- Não conterá definição de estilos;
- Não será importado por arquivos que não estejam fora de helpers.

### /constants
Conterá arquivos de constantes para serem utilizadas por outros arquivos sass que tão somente exercerá o papel de variável de controle na criação de lógica em arquivos sass, como lista de cores, por exemplo, que podem ser iteradas em funções ou mixins sass.

**Regras**:
- Não conterá definição de estilos;
- Não será importado por arquivos que não estejam fora de helpers.

### /helpers
Grupos de arquivos que servem como utilitários para a definição de arquivos de estilo.

### /extensions
Arquivos que implementam alguma extensão sass.

**Regras**:
- Conterá tão somente definição de extensões utilizando `%extension`;
- Poderá importar qualquer outro helper.

### /functions
Arquivos que implementam alguma função sass.

**Regras**:
- Conterá tão somente definição de funções utilizando `@function`;
- Poderá importar somente arquivos da pasta `constants/`.

### /mixins
Arquivos que implementam algum mixin sass.

**Regras**:
- Conterá tão somente definição de mixins sass;
- Poderá importar somente outros helpers e arquivos da pasta `constants/`.

### /variables
Arquivos que implementam alguma variável sass.

**Regras**:
- Conterá tão somente declarações de variáveis sass;
- Poderá importar outros arquivos de variáveis sass tão somente para fins de composição.

## Nomenclatura de arquivos

Os arquivos de estilo devem conter como prefixo a inicial de sua categoria, para as listadas no tópico Estrutura de pastas teríamos:

```
.
├── /constants
│   └── c_constant-file.scss
└── /helpers
    ├── /extensions
    │   └── e_extension-file.scss
    ├── /functions
    │   └── f_function-file.scss
    ├── /mixins
    │   └── m_mixin-file.scss
    └── /variables
        └── v_variable-file.scss
```

> A pasta `core` não necessita de prefixo.
{.is-warning}

## Guia de estilo

Convenções acatadas pelo time.

### Desenvolvimento Mobile First

No desenvolvimento mobile first, a estilização default deve ser sempre a orientação mobile enquanto os demais tamanhos de dispositivos devem ter sua estilização definida dentro do escopo de media queries.

#### {.tabset}
##### Exemplo
Está errada qualquer variação que não segue a ordem definida abaixo, isto é, se os estilos de mobile estiverem dentro do escopo de um media query, ou melhor se a ordem dos estilos não está inserida de maneira crescente, não corresponde ao pensamento "mobile first".

**Regras:**
- Os breakpoints dos media queries devem ser determinados por variáveis;
- Os estilos de mobile não devem ser definidos dentro do escopo de um media query;
- Os estilos de tablet e desktop devem ser definidos dentro do escopo de um media query.

```scss
.component-class {
  // mobile style
  max-width: 600px;
  
  @​media screen and (min-width: $min-tablet-width /* 600px */) {
    // tablet style
    max-width: 1000px;
  }
  
  @​media screen and (min-width: $min-desktop-width /* 1000px */) {
    // desktop style
    max-width: none;
  }
}
```

### Uso correto das unidades de medidas
### {.tabset}

#### rem
Unidade de medida relativa e escalável que varia de acordo com a dimensão definida pelo elemento raíz do DOM, no caso `<html>`, que por sua vez é tido o valor das configurações do navegador. Geralmente `1rem` equivale a `16px`, segundo as configurações padrão do navegador.

> **Quando usar**
> Deve ser a unidade de medida preferencial da aplicação, podendo ser utilizada em todo o projeto, pois deste modo irá torná-lo mais acessível e adaptável.
{.is-success}

> **Dica**
> ```scss
> html {
> 	font-size: 62.5%; // 10px
> }
> 
> body {
> 	font-size: 1.6rem; // 16px
> }
> ```
> Podemos tornar mais fácil de escalonar o valor em `rem` fazendo com que o valo de `rem` seja equivalente a `10px`, de modo que consigamos obter valores mais claros ao utilizarmos múltiplos de `10` ao invés de `16`.
{.is-info}


#### em
Unidade de medida relativa que varia de acordo com o tamanho de fonte definido no elemento sobre o qual está sendo aplicado.

> **Quando usar**
> Pode ser ideal utilizar em preenchimentos, alturas de linhas e margens.
{.is-success}


#### px
Unidade de medida absoluta.

> **Quando usar**
> Ideal para ajustes finos, bordas, raios, etc.
{.is-success}

### Evitar o uso de `!important`
O usdo de `!important` torna mais difícil de dar manutenção aos estilos. Verifique as alternativas e consulte outras pessoas antes de decidir usá-lo.

### Usar `z-index` com variáveis
Definir uma variável ou utilizar uma das disponíveis sempre que for utilizar um `z-index`.
