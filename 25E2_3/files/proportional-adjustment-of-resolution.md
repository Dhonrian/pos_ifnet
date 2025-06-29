---
title: Ajuste de Resolução
description: Entendendo resolução e como o zoom é ajustado pela resolução.
published: true
date: 2024-11-12T13:10:43.450Z
tags: v3, open layers, open-layers, resolução, zoom, resolution, getresolution, setresolution, mercator, ajuste proporcional
editor: markdown
dateCreated: 2024-11-12T13:10:41.640Z
---

# Funcionamento do Ajuste Proporcional da Resolução no OpenLayers

No OpenLayers, a resolução de um mapa define a quantidade de metros no mundo real que são representados por cada pixel na tela. Em projeções como a **projeção Mercator**, as distâncias e áreas no mapa são distorcidas à medida que você se afasta do Equador. Isso cria a necessidade de ajustar a resolução do mapa de forma proporcional para garantir uma representação precisa em pontos específicos.

## Conceitos Importantes

### 1. Resolução
- **Definição**: A resolução define quantos metros do mundo real correspondem a cada pixel na tela.
- **Referência**: Na projeção Mercator, a resolução é baseada na linha do Equador, onde as distâncias são representadas com precisão e sem distorção.

### 2. Resolução em um Ponto
- **Definição**: A resolução em um ponto é a resolução ajustada para um ponto específico no mapa, levando em consideração a distorção causada pela projeção.
- **Fórmula**: `pointResolution = resolution / cos(latitude)`
  onde:
  - `latitude` é a latitude do ponto, em radianos.
  - `cos(latitude)` ajusta a `resolution` para refletir a distorção no ponto específico.

## Ajuste Proporcional da Resolução
Para aplicar corretamente uma nova resolução ao mapa de acordo com uma escala desejada, o OpenLayers usa um ajuste proporcional. Isso garante que a nova resolução seja consistente em todo o mapa, considerando as distorções de latitude.

### Fórmula do Ajuste Proporcional
`newResolution = (currentResolution * newPointResolution) / currentPointResolution`

### Explicação
1. **Multiplicação**: Multiplicamos a `currentResolution` pela `newPointResolution` para escalar a resolução atual de acordo com a nova escala desejada.
2. **Divisão**: Dividimos pelo `currentPointResolution` para corrigir a distorção específica no ponto atual, garantindo que a resolução seja ajustada proporcionalmente.

### Demonstração

Para demonstrar que:

`newResolution = (currentResolution * newPointResolution) / currentPointResolution`

vamos substituir `currentPointResolution` pela sua definição:

1. Sabemos que:
`currentPointResolution = currentResolution / cos(latitude)`
onde `latitude` é a latitude do ponto em radianos.

2. Substituindo na fórmula de `newResolution`:
`newResolution = (currentResolution * newPointResolution) / (currentResolution / cos(latitude))`

3. Simplificando a expressão:
`newResolution = newPointResolution * cos(latitude)`

Observe que obtemos um fator constante da fórmula (`cos(latitude)`). Isto implica que resoluções distintas para um mesmo ponto latitudinal só pode ser justificada por variação na resolução base, que por sua vez significa que variou a quantidade de metros por pixel na linha do equador, efeito ao qual chamamos de "zoom". Portanto, se `newPointResolution` for maior do que `currentPointResolution`, isso indica que precisamos aumentar a resolução (o zoom é "afastado"). Se for menor, precisamos diminuir a resolução (o zoom é "aproximado").


### Por Que o Ajuste é Necessário?
A projeção Mercator distorce as distâncias de forma não uniforme:
- **No Equador**: A distorção é mínima, e a `currentResolution` é precisa.
- **Próximo aos Polos**: A distorção aumenta significativamente, fazendo com que a `currentPointResolution` seja muito maior. O ajuste proporcional garante que o mapa seja exibido corretamente, mesmo em latitudes elevadas.

## Conclusão
O ajuste proporcional da resolução é fundamental para garantir que o mapa seja exibido de forma precisa, mesmo em regiões onde a distorção da projeção Mercator é significativa. Ao aplicar a fórmula de ajuste, o OpenLayers corrige as diferenças de resolução com base na latitude, proporcionando uma representação espacial mais precisa e consistente.
