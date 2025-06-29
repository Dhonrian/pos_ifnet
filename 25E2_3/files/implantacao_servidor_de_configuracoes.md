---
title: Implantação Servidor de Configurações
description: Esta página visa trazer o conhecimento para implantação de novas Cidades e manutenção de configuraçõs de cidades já cadastradas.
published: true
date: 2024-10-07T17:00:17.674Z
tags: mobile de campo, mobile, servidor de config, servidor de configurações
editor: markdown
dateCreated: 2024-03-08T14:35:08.404Z
---

# Servidor de Configurações (Mobile)

O servidor de configurações é projetado para otimizar a escalabilidade do aplicativo móvel da Geopixel, permitindo a criação de um aplicativo único capaz de adaptar-se dinamicamente a cada cidade, ao invés de desenvolver uma versão específica para cada uma. Isso é possível graças à centralização das informações no servidor.


--- 

## Acesso

Para acessar qualquer um dos ambientes, é necessário criar uma conta. Solicitações para criação de usuário devem ser direcionadas à equipe de Mobile

## Ambientes de Homologação e Produção

Existem duas versões do servidor de configurações, acessíveis por URLs específicas: uma destinada à [homologação] e outra à [produção]. É crucial observar que cada ambiente requer aplicativos distintos, disponíveis para download diretamente no servidor de configurações.

## Estrutura do Servidor de Configurações

O servidor conta com seis tabelas essenciais para configurar o ambiente móvel de uma Cidade/Cliente: Clientes, Clientes Mobile, Configurações Mobile, Tiles Mobile e Aplicativos Mobile. A presença de todas é fundamental para a implementação de um novo cliente.

### Aplicativos Mobile (Mobile Apks)

Esta seção hospeda as versões dos aplicativos versão 3.0 ou superiores, inclusive versões de teste. O time de desenvolvimento é responsável por disponibilizar essas versões nos ambientes de homologação e produção. A tabela Clientes Mobile permite determinar a versão do aplicativo para cada cliente, e atualizações são realizadas por meio de ajustes nesta tabela.

### Clientes (Clients)

Define a adição de novos clientes. Após serem adicionados, os clientes são listados na seleção de municípios no aplicativo móvel.

<details>
<summary> screenshots </summary>

  Adicionando Cliente Hortolândia. O banner não é necessário no contexto móvel.
	![add_client_gpx_config_server.png](/gpx_config_server/add_client_gpx_config_server.png)
  
  Cliente de Hortolândia adicionado com sucesso.
  ![added_client_gpx_config_server.png](/gpx_config_server/added_client_gpx_config_server.png)
  
  Listagem de Clientes Aplicativo Móvel.
  ![client_list_mobile.png](/gpx_config_server/client_list_mobile.png)
  
</details>

### Clientes Mobile (Mobile Clients)

Responsável por indicar a versão atual do SIG e associar uma versão específica do aplicativo ao cliente.

<details>
<summary> screenshots </summary>

  Definindo a versão do SIG e Aplicativo para Homologação.
  ![add_mobile_client_gpx_config_server.png](/gpx_config_server/add_mobile_client_gpx_config_server.png)
  
</details>



### Configurações Mobile (Mobile Configs)

Estabelece configurações básicas como a URL do servidor das cidades, a URL do logo da cidade, a posição inicial no mapa e os níveis de zoom disponíveis. Relaciona-se diretamente com o modelo Cliente.

Ele se relaciona diretamente com o modelo Cliente.

Exemplo utilizado para Homologação

| Coluna    							| Valor 																																																													|
| ----------------------	| ----------------------------------------------------------------------------------------------------------------------------		|
| Cliente  								| Homologação    																																																									|
| URL do Server 					| https://homologacao.geopixel.com.br/gisweb_poc_2_1_3_server    																													 				|
| Logo URL*    						| https://cacapava.geopx.com.br/geopixelcidades-cacapava_server/rest/resource/getResource?file=/image/prefeitura.png##80px    		|
| Posição Inicial 				| Clique sobre a Cidade no mapa 																																																	|
| Escala de Zoom Inicial 	| 12 																																																															|
| Escala de Zoom Máximo 	| 22 																																																															|

\* Foi utilizado a rota do servidor para retornar o arquivo dentro de `image/prefeitura.png`, adeque para o nome do brasão da prefeitura definido no arquivo `.txt` do servidor.

---

<details>
<summary> screenshots </summary>
  
  Configurações para o Homologação
	![add_mobile_config_gpx_config_server.png](/gpx_config_server/add_mobile_config_gpx_config_server.png)
	
</details>

### Tiles Mobile (Mobile Tiles)

Define quais mapas estarão disponíveis no aplicativo móvel. Assemelha-se à tabela `app_param` que possuímos. Nela poderemos definir quais os tileUrls serão disponibilizado para um cliente, sendo que definir pelo menos um é obrigatório e é possível definir múltiplos tileUrls para uma cidade, permitindo a escolha no aplicativo.

Exemplo utilizado para Homologação

| Coluna    							| Valor 																																																													|
| ----------------------	| ----------------------------------------------------------------------------------------------------------------------------		|
| Cliente  								| Homologação    																																																									|
| ID do Perfil* 					| 1    																													 																																	|
| URL do Tile  						| https://cacapava.geopx.com.br/ORTOMOSAICO_2010/{z}/{x}/{y}.jpg 																																	|
| Nome do Tile		 				| Ortomosaico 2010 - 1m 																																																					|

\* O ID do Perfil atualmente não trás funcionalidade nenhuma, não estamos separando tiles por perfil atualmente.

---

<details>
<summary> screenshots </summary>
  
  Configurações para o Homologação
	![add_mobile_tile_gpx_config_server.png](/gpx_config_server/add_mobile_tile_gpx_config_server.png)
  
  
  Listagem de Mapas disponíveis Mobile
  ![mobile_tiles_list_mobile.png](/gpx_config_server/mobile_tiles_list_mobile.png)
	
</details>

### Camadas Offline Mobile (Mobile Offline Layers)

Centraliza as definições de temas disponíveis para download e uso offline no aplicativo móvel. É importante ressaltar que para uma camada seja possível de visualizar no mobile, ele obrigatoriamente precisa haver **GEOM**.

Camadas como cadastro imobiliário, que precisam de informações de serviços e tabelas externas da prefeitura não são possíveis de exibir no mobile, a menos que esses dados sejam salvos em uma tabela nossa de forma estática e com **GEOM**


Exemplo utilizado para Homologação

| Coluna    							| Valor 																																																													|
| ----------------------	| ----------------------------------------------------------------------------------------------------------------------------		|
| Cliente  								| Homologação    																																																									|
| Nome					 					| Quadras																												 																																	|
| ID do Perfil						| 1																																																																|
| ID do Tema							| 13																																																															|
| Escala de Zoom Mínima*  | 16																																																															|
| Escala de Zoom Máximo   | 24																																																															|
| SLD                     | SLD da camada do Geoserver                                                                                                     	|

\* É bom se atentar à escala de zoom mínima porque pode deixar o aplicativo muito lento. Para camadas muito pesadas deixar o zoom entre 18 e 19 e realizar testes.

<details>
<summary> screenshots </summary>
  
  Configurações para o Homologação
	![add_mobile_offline_layer_gpx_config_server.png](/gpx_config_server/add_mobile_offline_layer_gpx_config_server.png)
  
  Listagem dos Temas no aplicativo móvel
  ![mobile_offline_layer_list_mobile.png](/gpx_config_server/mobile_offline_layer_list_mobile.png)
	
</details>

## Atualizações no Aplicativo.

Qualquer mudança no servidor de configurações requer sincronização no aplicativo, acessível pelo menu lateral em `Verificar Atualizações`. Novas versões do aplicativo serão notificadas por um pop-up, permitindo o download e instalação subsequentes.

<details>
<summary> screenshots </summary>
  
  Menu lateral do Aplicativo Móvel.
  ![mobile_side_menu.png](/gpx_config_server/mobile_side_menu.png)
  
  Processo de Verificação de Atualizações.
  ![successfully_update_check_mobile.png](/gpx_config_server/successfully_update_check_mobile.png)
  
  Notificação de Nova Versão Disponível.
  ![new_mobile_version_available_modal.png](/gpx_config_server/new_mobile_version_available_modal.png)
	
</details>



[produção]: https://services.geopixel.com.br/admin/
[homologação]: https://config.flow.geopixel.com.br/admin/
