---
title: Dicionário
description: Termos comuns usados para edição
published: true
date: 2024-01-17T13:47:21.415Z
tags: 
editor: markdown
dateCreated: 2024-01-17T13:47:19.547Z
---

# Dicionário

### Theme(Tema)
###### Camadas referentes às regras de negócio, tendo cada uma seu contexto.

Exemplo:
>
> - **Quadra**: Tema que guarda geometrias do tipo **`Polígono(Polygon)`** e se refere aos quarteirões da cidade;
> - **Vias trecho**: Tema que guarda geometrias do tipo **`Linha(LineString)`** e se refere às ruas da cidade;
> - **Habite-se**: Tema que guarda geometrias do tipo **`Ponto(Point)`** e se refere às casas ou pontos de interesse;

---

### Layer(Camadas)
###### Camadas globais criadas para exibir ou manipular as features).

Exemplo:
> - EditionLayer (Camada onde são carregadas as features recuperadas do banco);
> - SketchLayer (Camada de feedback do desenho)
> - DraftLayer(Camada de histórico do desenho que foi feito)
> - HightLightLayer (Camada de features que foram selecionados)

### FeatureCollection
###### Objeto retornado pelo server contendo a feature description(metadados) e a coleção de features(entidade).

Exemplo:
```json
"featureCollection": [
    {
        "description": {...},
        "features": [...]
    }
]
```
---
### Feature
###### Entidade vinda do banco, normalmente convertida para o tipo Feature(OpenLayers) pelo client.

Exemplo:
```json
Feature: {
    "values": [
        2475, //pk
        null,
        null,
        null,
        null,
        null,
        null,
        null
    ],
    "geometriesWKB": [
        "0106000020110F000001000000010300000001000000040000009D664E0E7A6753C1D98E04502B2E44C17954CA35706753C12291B27A2E2E44C11A2F5C8D776753C18D944618392E44C19D664E0E7A6753C1D98E04502B2E44C1"
    ]
}

```
---

### Feature(OL) - também chamado de Feição
###### Classe e Objeto pentencente ao **Open Layers** e que contém dados referente as feature, como Geometria, id do banco(gid) e entre outras.

Exemplo:
```json
"Feature": {
    "disposed": false,
    "pendingRemovals_": {},
    "dispatching_": {},
    "listeners_": {
        "change:geometry": [
            null
        ],
        "change": [
            null
        ],
        "propertychange": [
            null
        ]
    },
    "revision_": 4,
    "ol_uid": "2401",
    "values_": {
        "geometry": {
            "disposed": false,
            "pendingRemovals_": null,
            "dispatching_": null,
            "listeners_": {
                "change": [
                    null
                ]
            },
            "revision_": 0,
            "ol_uid": "2402",
            "values_": null,
            "extent_": [
                -5086696.223535207,
                -2645106.189653939,
                -5086656.840474241,
                -2645078.625139099
            ],
            "extentRevision_": 0,
            "simplifiedGeometryMaxMinSquaredTolerance": 0,
            "simplifiedGeometryRevision": 0,
            "layout": "XY",
            "stride": 2,
            "flatCoordinates": [
                -5086696.223535207,
                -2645078.625139099,
                -5086656.840474241,
                -2645084.95857443,
                -5086686.208751464,
                -2645106.189653939,
                -5086696.223535207,
                -2645078.625139099
            ],
            "ends_": [
                8
            ],
            "flatInteriorPointRevision_": -1,
            "flatInteriorPoint_": null,
            "maxDelta_": -1,
            "maxDeltaRevision_": -1,
            "orientedRevision_": -1,
            "orientedFlatCoordinates_": null
        },
        "values": [
            2475,
            null,
            null,
            null,
            null,
            null,
            null,
            null
        ],
        "id": 2475,
        "themeId": 1188
    },
    "geometryName_": "geometry",
    "style_": [
        {
            "geometry_": null,
            "fill_": null,
            "image_": null,
            "renderer_": null,
            "hitDetectionRenderer_": null,
            "stroke_": {
                "color_": "#f9f900",
                "lineDash_": null
            },
            "text_": null
        },
        {
            "geometry_": null,
            "fill_": null,
            "image_": {
                "opacity_": 1,
                "rotateWithView_": false,
                "rotation_": 0,
                "scale_": 1,
                "scaleArray_": [
                    1,
                    1
                ],
                "displacement_": [
                    0,
                    0
                ],
                "canvas_": {},
                "hitDetectionCanvas_": null,
                "fill_": {
                    "color_": "#f9f900"
                },
                "origin_": [
                    0,
                    0
                ],
                "points_": null,
                "radius_": 8,
                "angle_": 0,
                "stroke_": {
                    "color_": "#f9f900",
                    "lineDash_": null,
                    "width_": 2
                },
                "size_": [
                    18,
                    18
                ],
                "renderOptions_": {
                    "strokeStyle": "#f9f900",
                    "strokeWidth": 2,
                    "size": 18,
                    "lineDash": null,
                    "lineJoin": "round",
                    "miterLimit": 10
                }
            },
            "renderer_": null,
            "hitDetectionRenderer_": null,
            "stroke_": null,
            "text_": null
        }
    ],
    "geometryChangeKey_": {
        "target": {
            "disposed": false,
            "pendingRemovals_": null,
            "dispatching_": null,
            "listeners_": {
                "change": [
                    null
                ]
            },
            "revision_": 0,
            "ol_uid": "2402",
            "values_": null,
            "extent_": [
                -5086696.223535207,
                -2645106.189653939,
                -5086656.840474241,
                -2645078.625139099
            ],
            "extentRevision_": 0,
            "simplifiedGeometryMaxMinSquaredTolerance": 0,
            "simplifiedGeometryRevision": 0,
            "layout": "XY",
            "stride": 2,
            "flatCoordinates": [
                -5086696.223535207,
                -2645078.625139099,
                -5086656.840474241,
                -2645084.95857443,
                -5086686.208751464,
                -2645106.189653939,
                -5086696.223535207,
                -2645078.625139099
            ],
            "ends_": [
                8
            ],
            "flatInteriorPointRevision_": -1,
            "flatInteriorPoint_": null,
            "maxDelta_": -1,
            "maxDeltaRevision_": -1,
            "orientedRevision_": -1,
            "orientedFlatCoordinates_": null
        },
        "type": "change"
    }
}
```
---
### Geometry
###### Classe e objeto referente ao desenho criado e que guarda coordenadas(Coordinate), podendo ser tratado como **Multi** ou **Single** e com os tipos sendo:

- **Polygon(LinearRing)**: sempre contém uma coordenada a mais do que representada visualmente, pois a primeira e última coordenada são iguais;
- **LineString**: Desenho de linha e precisa de pelo menos 2 coordenadas;
- **Point** - Contém apenas uma coordenada;

Exemplo:
```json
"Polygon": {
    "disposed": false,
    "pendingRemovals_": null,
    "dispatching_": null,
    "listeners_": {
        "change": [
            null
        ]
    },
    "revision_": 0,
    "ol_uid": "2402",
    "values_": null,
    "extent_": [
        -5086696.223535207,
        -2645106.189653939,
        -5086656.840474241,
        -2645078.625139099
    ],
    "extentRevision_": 0,
    "simplifiedGeometryMaxMinSquaredTolerance": 0,
    "simplifiedGeometryRevision": 0,
    "layout": "XY",
    "stride": 2,
    "flatCoordinates": [
        -5086696.223535207,
        -2645078.625139099,
        -5086656.840474241,
        -2645084.95857443,
        -5086686.208751464,
        -2645106.189653939,
        -5086696.223535207,
        -2645078.625139099
    ],
    "ends_": [
        8
    ],
    "flatInteriorPointRevision_": -1,
    "flatInteriorPoint_": null,
    "maxDelta_": -1,
    "maxDeltaRevision_": -1,
    "orientedRevision_": -1,
    "orientedFlatCoordinates_": null
}

```


---
### Coordinate
###### Um array numérico de duas posições contendo o número da posição de cada coordenada no mapa, sendo a primeira posição(0) `X` referente a posição horizontal no mapa e a segunda(1) referente a posição vertical no mapa.

Exemplo:
```json
"Coordinates": {
    [
        [
            -5086696.223535207, //x
            -2645078.625139099 //y
        ],
        [
            -5086656.840474241,
            -2645084.95857443
        ],
        [
            -5086686.208751464,
            -2645106.189653939
        ],
        [
            -5086696.223535207,
            -2645078.625139099
        ]
    ]
}
```
