---
title: Consulta Certidão V3
description: Configuração do consulta certidão na V3
published: true
date: 2025-05-16T18:34:16.869Z
tags: v3, consultacertidao, consultacertidaov3, certidao
editor: markdown
dateCreated: 2025-05-16T18:30:18.085Z
---

# Consulta Certidão – v3

 - 🛠️ Como configurar o Consulta Certidão na v3
 <br>

### 📁 Configuração no banco de dados
<br>

#### **Tabela: `APP_CONSULTA_CERTIDAO`**

- Foi criada uma nova tabela chamada **`app_consulta_certidao`**, onde estão concentradas todas as configurações do módulo **Consulta Certidão**, como login, usuário, tema, perfil, etc.
- Na **v2**, essas configurações estavam centralizadas em no arquivo de configuração. Agora, na **v3**, elas foram migradas para essa nova estrutura.
- Os nomes das colunas permanecem compatíveis com a configuração da v2, facilitando a portabilidade.

> 🔍 Exemplo de configuração da tabela em Itatiba:

![Configuração APP_CONSULTA_CERTIDAO](/v3/captura_de_tela_2025-05-16_150817.png)

<br>

#### **Tabela: `APP_CERTIDOES`**

- Na **v2**, os formulários eram armazenados na tabela **`app_form`**, onde um único JSON (form) englobava todas as certidões e suas particularidades. Essa abordagem dificultava a manutenção futura por conta da complexidade e tamanho do arquivo.
- Na **v3**, cada certidão possui sua própria configuração individual armazenada na tabela **`app_certidoes`**. O formulário referente a cada certidão fica na coluna **`campos`**.

> 🔍 Exemplo de certidões separadas por configuração:

![Configuração APP_CERTIDOES](/v3/captura_de_tela_2025-05-16_151455.png)

- Cada certidão pode ter seu próprio tema, perfil, formulário e JSON (form) específico.
- Os novos formulários devem ser criados separadamente para cada certidão dentro dessa nova estrutura.

<br>

### 🔗 Acesso ao Consulta Certidão

- A nova URL de acesso ao módulo é:


> 📎 Exemplo:  
[https://sigv3.geopixel.com.br/#/reportConsultation](https://sigv3.geopixel.com.br/#/reportConsultation)

![captura_de_tela_2025-05-16_153345.png](/v3/captura_de_tela_2025-05-16_153345.png)
