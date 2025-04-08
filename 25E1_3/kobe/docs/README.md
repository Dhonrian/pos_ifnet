# Kobe - Análise de Dados


# GITHUB
O projeto está disponível no github: https://github.com/Dhonrian/pos_ifnet/tree/main/25E1_3/kobe/, toda a documentação e este `README.md` se encontra na pasta `docs/`

## Dados

Este projeto análisa os arremessos do Kobe Bryant e tenta prever se o arremesso acertou ou não. Os dados utilizados foram retirados do enunciado do projeto e possuem as seguintes colunas:

```
action_type
combined_shot_type
game_event_id
game_id
lat
loc_x
loc_y
lon
minutes_remaining
period
playoffs
season 
seconds_remaining
shot_distance
shot_made_flag (this is what you are predicting)
shot_type
shot_zone_area
shot_zone_basic
shot_zone_range
team_id
team_name
game_date
matchup
opponent
shot_id
```

As colunas utilizadas foram:
| Coluna | Tipo | Descrição |
|--------|------|-----------|
|lat | contínuo | Latitude do arremesso |
|lng | contínuo | Longitude do arremesso |
|minutes remaining | discreto | Minutos restantes do quarto |
|period | discreto | Período do jogo |
|playoffs | discreto | Se o jogo é playoffs ou não |
|shot_distance | contínuo | Distância do arremesso |
|shot_made_flag | discreto | Se o arremesso foi convertido ou não |


# Respostas

## Diagramas

### Preparação de Dados
![Processamento de Dados](/25E1_3/kobe/data/08_reporting/pipeline1.png)

### Treinamento dos modelos
![Treinamento](/25E1_3/kobe/data/08_reporting/pipeline2.png)

### Aplicação
![Aplicação](/25E1_3/kobe/data/08_reporting/pipeline3.png)

## Como as ferramentas Streamlit, MLFlow, PyCaret e Scikit-Learn auxiliam na construção dos pipelines descritos anteriormente?

R: As ferramentas citadas facilitam a construção dos pipelines de várias maneiras: 
- **O Streamlit** ajuda na criação de interfaces para o usuário, assim como na visualização dos dados e resultados. Dessa forma é possível criar tanto dashboards para visualização de dados quanto interfaces para a interação com o modelo.
- **O MLFlow** permite o rastreamento de experimentos e o gerenciamento de vários modelos. Também é possível registrar as métricas e parâmetros, o que facilita a comparação entre diferentes modelos e versões ao longo do tempo. A integração com o kedro permite o uso do catálogo para melhor manuseio dos dados. Pelo MLFlow é possível também fazer o deploy dos modelos, tornando rápida a troca de versões em produção caso a saúde comece a cair.
- **O PyCaret** automatiza o processo o fluxo de treinamentos de modelos, o que torna rápido a comparação entre algoritmos e a escolha do melhor modelo.  
- **O Scikit-Learn** é uma das principais bibliotecas para aprendizado de máquina. Nela existem várias funções para pré-processamento, treinamento, avalição e outras funções que ajudam na construção de modelos.

## 4 - Artefatos gerados
Durante a execução do projeto, foram gerados os seguintes artefatos:
 - Na **preparação dos dados** gerou-se o arquivo `dataset_filtered.parquet` que são os dados filtrados sem os valores nulos e com as colunas necessárias para o treinamento do modelo. Dos 24.271 arremessos realizados foram mantidos 20.285 para as 6 features selecionadas. Em seguida o dataset foi dividido em treino e teste, gerando os arquivos `base_train.parquet` e `base_test.parquet`.
 - Na fase de **Treinamento** foram gerados arquivos pickle dos modelos treinados que são os arquivos `treinamento_logistical_regression.pkl` e `treinamento_decision_tree.pkl`. Esses arquivos são salvos na pasta do mlflow.
- A **aplicação** do modelo gerou o `predictions.parquet` que é o arquivo com a saída do modelo, se o arremesso foi convertido ou não. Outro artefato gerado foi um gráfico `roc_auc_lot.png` que mostra a curva ROC do modelo.


## 6 - MLFlow e Métricas

A primeira tela do MLFlow mostra os experimentos realizados com algumas informações.
![MLFlow](/25E1_3/kobe/data/08_reporting/mlflow.png)

Entrando na run `__default__` é possível ver os parâmetros e métricas de cada modelo.
![MLFlow](/25E1_3/kobe/data/08_reporting/mlflow_run.png)

Bem como os artefatos gerados.
![MLFlow](/25E1_3/kobe/data/08_reporting/mlflow_artifacts.png)

E as métricas em forma de gráfico.  
![MLFlow](/25E1_3/kobe/data/08_reporting/mlflow_metrics.png)

O modelo escolhido para produção foi o `Logistic Regression` por apresentar métricas melhores que o `Decision Tree`.

## 7 - Aplicação
### A) O modelo é aderente a essa nova base? O que mudou entre uma base e outra? Justifique.
R: Apesar de possuir as mesmas colunas, por ter dados distribuidos de maneira diferente o modelo não é aderente a nova base. Como pode-se notar nas métricas o f1_score ficou como 0. Isso indica que o modelo não é capaz de prever as classes de maneira correta. Uma possível causa seria que os dados utilizados para treinamento não são significativos para a previsão dos arremessos, uma possível solução seria utilizar outras colunas disponíveis no dataset original.  

### B) Descreva como podemos monitorar a saúde do modelo no cenário com e sem a disponibilidade da variável resposta para o modelo em operação.
R: Utilizando o MLFlow é possível monitorar a saúde do modelo. Caso exista a resposta é possível utilizar métricas como f1_score para verificar a performance e caso o modelo comece a cair é possível retreinar com novos dados. Em caso da resposta não existir pode-se monitorar mudanças que podem ocorrer nos dados, como por exemplo a distribuição dos novos dados (data drift), ou a mudança no tipo de alguma entrada (feature drift).

### C) Descreva as estratégias reativa e preditiva de retreinamento para o modelo em operação.
R: A estratégia reativa consiste em retreinar o modelo quando a performance começa a cair, por exemplo quando o f1_score fica abaixo de um limite. Já a estratégia preditiva consiste em prever quando o modelo pode começar a cair e retreiná-lo antes que isso aconteça, de forma programada a cada X meses ou quando os dados começam a apresentar uma distribuição diferente.

## 8 - Streamlit
O Streamlit foi utilizado para criar uma interface em que se pode fazer a inferência de um arremesso. Cada arremesso é adicionado em uma figura que pode ser visualizada no GIF. 
![Streamlit](/25E1_3/kobe/data/08_reporting/streamlit.gif) 

# Como rodar o projeto
O projeto foi desenvolvido utilizando o Kedro com python 3.12 e as dependências estão no arquivo `requirements.txt`. Para rodar o projeto é necessário ter o Kedro instalado e o MLFlow. Para iniciar o projeto:

```bash
kedro run
```
Após isso, para iniciar o MLFlow, basta rodar o seguinte comando:
```bash
mlflow ui --backend-store-uri mlflow_runs   
```
O streamlit pode ser iniciado com o seguinte comando:
```bash
streamlit streamlit/app.py
```
