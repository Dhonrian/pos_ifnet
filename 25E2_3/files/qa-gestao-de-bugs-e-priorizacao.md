---
title: Gestão de bugs, como reportar bugs e priorizá-los
description: 
published: true
date: 2023-08-24T14:27:17.044Z
tags: testes, qa, desenvolvimento, tecnologia, bugs, gestão, sistema, defeitos, falhas, erros, reporte, priorização
editor: markdown
dateCreated: 2023-08-17T17:08:06.471Z
---

A implementação de um sólido sistema de qualidade e gestão de bugs é fundamental para garantir a eficiência e confiabilidade de qualquer projeto. Neste artigo, exploraremos a importância desses sistemas, destacando como eles contribuem para a melhoria contínua, identificação precoce de problemas e entrega de produtos ou serviços de alta qualidade. Vamos adentrar nos principais pilares dessas práticas e como elas se interligam para criar um ambiente propício ao desenvolvimento de soluções robustas e livres de defeitos.

# Priorização de bugs

A Priorização eficaz de bugs é um aspecto crucial no processo de desenvolvimento de software, permitindo uma alocação estratégica de recursos para resolver problemas de maneira eficiente. Para atingir esse objetivo é comum categorizar os bugs em diferentes níveis de gravidade impacto, facilitando a tomada de decisões. Nesse contexto utilizamos ***quatro categorias principais de priorização*** que são:
- **Crítico - Impeditivo** 
![screenshot_2.png](/screenshot_2.png)
    Bugs classificados como "Crítico e Impeditivo" tem um impacto imediato e drástico na funcionalidade ou usabilidade do software. Podendo levar à interrupção completo do sistema ou impedir que os usuários executem tarefas essenciais. A resolução desses bugs rapidamente é essencial para mantes a integridade do produto e evitar perdas significativas.
    
    ### Para Bugs Impeditivos temos o Bombeiro
    
    ***Comunicação - Quem é o Bombeiro*** - O bombeiro é definido pelo gerente e comunicado antes do início de cada sprint e pode ser qualquer um dos Dev's, sendo 1 o suficiente.
    ***Alertas - Quem pode acionar o Bombeiro?*** - Qualquer membro do time pode alertar possíveis ***Bugs Impeditivos***, porém, o bombeiro só priorizará se for ***IMPEDITIVO***.
    ***Priorização - Estar atento aos alertas*** - Se um Bug Impeditivo for identificado, o bombeiro deve priorizá-lo na frente de qualquer atividade da sprint.
    ***Eficiência - Apagar incêndio*** - Entender o problema e ser cirúrgico. Resolver rapidamente, sem grandes mudanças. Garantir que o problema não volte ou gere mais bugs.
    ***Trabalho em Equipe - Já entrou?*** - Bombeiro e Scrum Master devem cobrar prioridade no CR, Testes e Deploy. Termina quando o problema está resolvido no cliente.
    ***Aprendizados - Registra a ocorrência!*** - Escreve POST-MORTEM simples que resume o problema, causa, consequência, solução e aprendizado para evitar que se repita.
    ***Paz - O que fazer sem alertas?*** - O bombeiro volta para as atividades priorizadas da sprint enquanto não aparecem IMPEDITIVOS.
    
- **Alto - Funcional**
![screenshot_1.png](/screenshot_1.png)
    Bugs classificados como "Alto e Funcional" referem-se a problemas que afetam a funcionalidade principal do software, mas não são tão prejudiciais quanto os críticos. Embora não causem interrupções graves, esses bugs podem prejudicar a experiência do usuário ou impedir realização de tarefas essenciais. Resolver esses problemas é importante para garantir um software confiável e utilizável.
    
- **Médio - Melhorias**
![screenshot_3.png](/screenshot_3.png)
    Bugs classificados como "Médio - Melhoria" são bugs que não possuem impacto imediato na funcionalidade principal, mas podem afetar a eficiência, desempenho ou experiência do usuário. Priorizar e resolver esses bugs contribui para aperfeiçoar o produto a longo prazo e aumentar a satisfação do cliente.
    
- **Baixo - Acabamento**
![screenshot_4.png](/screenshot_4.png)
    Bugs classificados como "Baixo - Acabamento" são problemas menores que não tem impacto significativo na funcionalidade ou experiência geral do usuário, eles estão relacionados a questões estéticas, pequenas melhorias ou ajustes cosméticos. Embora não sejam prioridades imediatas, resolver esses bugs contribui para aprimorar a qualidade percebida do software
    
# Como funciona o processo de reporte de bugs?

Para fazer o reporte de um bug devemos utilizar um metodologia clara e objetiva mostrando os pontos principais do erro encontrado exemplo:
    ***Título curto e Objetivo:***
    Um breve resumo do problema.
    ![titulo.png](/titulo.png)
    ***Descrição mais detalhada no corpo do bug:***
    O problema precisa ser entendido com poucas palavras porém com todas as informações pertinentes, evitando redações e prolixidade.
    ![descrição.png](/descrição.png)
    ***Passo a passo para reprodução:***
    Passo a passo de como reproduzir a inconsistência, levando em consideração todo o contexto que o usuário faria para reproduzir.
    ![passo_a_passo.png](/passo_a_passo.png)
    ***Evidência:***
     São importantes para comprovar a existência do bug e geralmente são anexadas ao "bug report". Podem ser prints de tela, gravações, mensagens no console do navegador ou IDEs, logs,banco de dados, etc.
    ![evidência.png](/evidência.png)
    ***Classificar de acordo com sua priorização:***
    Impeditivo, funcional, melhoria ou acabamento
    ![classificação.png](/classificação.png)
    