---
title: Integrações
description: 
published: true
date: 2023-11-28T12:35:11.176Z
tags: 
editor: markdown
dateCreated: 2023-11-27T16:23:14.221Z
---

# Integrações: Documentação - BETHA
- Objetivo
- Introdução
- Acesso aos dados legados
- Acesso aos dados através de Web Services
- Integração
- Atualização de dados
- Princiapis Problemas encontrados
- Ferramentas importantes

## Objetivo

Este documento tem como objetivo, trazer orientações para realização da integração entre sistemas legados, em particular o sistema Tributário da Betha, com o sistema Geopixel Cidades. 

## Introdução

A integração entre o Geopixel Cidades e o sistema Tributário de uma prefeitura é um item previsto em contrato, que prevê a integração com o sistema legado, garantindo assim a operacionalização plena do sistema. 

Para atender a integração a Geopixel desenvolveu ferramentas que permitem ao Geopixel Cidades acessar vistas do banco de dados legado, independente do Sistema Gerenciador de Banco de Dados (SGBD) utilizado. Estão homologadas a integração com sistemas legados em Postgres 9.4 ou superior, SQL Server 12.0 ou superior, Oracle 12.0 ou superior, Firebird 2.5, MariaDB 10 ou superior. 

Para que a integração seja realizada é necessário a liberação de acesso ao servidor onde reside o banco de dados. Este acesso é liberado apenas para dois IPs específicos (Rede da Geopixel para suporte e Rede do servidor de aplicação do Geopixel Cidades), para acesso a uma ou mais “views” que permitam a consulta às informações de interesse da prefeitura, utilizando autenticação disponibilizada pelo fornecedor de dados. 

O acesso é realizado pelo servidor de aplicação do Geopixel Cidades, que atende aos requisitos de segurança preconizados pelo OWASP, sendo submetido a um “Pen test”, por certificador independente, a cada liberação de nova versão. As informações de IP, SGDB utilizado, Nome do Banco, Usuário, Senha, Nome da View são criptografados utilizando o padrão AES e chave aleatória. 

## Acesso aos dados legados

O acesso aos dados legados para a visualização de consultas, geração de mapas temáticos, estatísticas e infográficos (dashboard) exigem vistas liberadas apenas para leitura.  

De um modo geral é fundamental que o portal possa acessar as informações básicas relacionadas ao cadastro imobiliário. 

Normalmente os cadastros tributários são estruturados em uma ou mais tabelas que integram as informações básicas que caracterizam completamente uma unidade imobiliária. Normalmente existem tabelas que agrupam os dados relativos aos imóveis, aos logradouros e aos contribuintes, e tabelas adicionais e de domínios. 

Em razão das informações que a prefeitura deseja utilizar em consultas, mapas temáticos, estatísticas e gráficos será necessário liberar o acesso a várias tabelas através de “views” especificas ou criar uma única “view” que agrupe os dados necessários. 

A seguir relacionamos os dados normalmente utilizados no processo de integração, caso existam, e que vão permitir que a Prefeitura realize inúmeras análises levando em conta os aspectos espaciais: 

**Dados do Imóvel:** 

- Matrícula da unidade imobiliária, número único que identifica a unidade imobiliária; 

- Inscrição da unidade imobiliária, código estruturado composto normalmente pelo número do distrito, setor, quadra, lote e unidade. Existem variantes desta codificação, é comum também a inscrição ser composta pelo número da quadricula, posição na quadricula, número da quadra, lote e unidade imobiliária; 

- Código do logradouro, Nome do logradouro, Número Predial e Complemento, ou somente o Código do Logradouro, no caso de ser liberada a tabela de logradouros; 

- CEP do imóvel; 

- Bairro; 

- Loteamento, nome do loteamento aprovado na época da incorporação; 

- Quadra no Loteamento, designativo da quadra no mapa do loteamento; 

- Lote no loteamento, designativo do lote na planta do loteamento; 

- Nome do proprietário, CPF/CNPJ do proprietário e código do contribuinte, ou apenas o código contribuinte, no caso da tabela de contribuintes ser liberada; 

- Número do Registro no Cartório de Imóveis; 

- Cartório de Imóveis – identificação do cartório; 

- Área do Terreno 

- Área Construída Total, ou Área da Edificação Principal caso a prefeitura adote o controle de áreas de edícula e piscina; 

- Área da Edícula, caso exista; 

- Área da Piscina caso exista; 

- Testada Principal; 

- Valor Venal do Imóvel; 

- Valor Venal Predial; 

- Valor Venal do Terreno; 

- Preço Unitário do Terreno; 

- Padrão construtivo; 


**Logradouro:** 

- Código do Logradouro 

- Nome do Logradouro, em alguns casos o nome do logradouro pode estar estruturado por Tipo, Título, Preposição e Nome ou apenas alguns destes elementos; 

- Nome antigo, caso exista 

- Bairro, caso seja usado em razão de alguns sistemas criarem códigos diferentes para o logradouro em função do bairro onde se encontra aquele trecho do logradouro. 

- Lei, número e descrição da lei que designou o logradouro caso exista; 

 
**Contribuintes:** 

- Código do Contribuinte; 

- Nome do Contribuinte; 

- CPF/CNPJ do contribuinte, pessoa física ou jurídica; 

- Endereço de notificação, caso exista, como campo único ou estruturado; 

## Acesso aos dados através de Web Services

