---
title: Configuração tomcat de acordo com a OWASP
description: Aqui serão listadas algumas configurações pertinentes para submeter o sistema ao OWASP.
published: true
date: 2023-08-30T13:17:50.697Z
tags: segurança, seguranca, owasp
editor: markdown
dateCreated: 2023-08-30T12:50:40.177Z
---

# Configurações do tomcat
- Esconder resposta de erros do tomcat:
> Adicionar a tag dentro do arquivo Server.xml: 
`<Valve className="org.apache.catalina.valves.ErrorReportValve" showReport="false" showServerInfo="false"/>`

- Renomear e remover pastas de documentação:
> /docs (remover)
	/examples (renover)
  /ROOT/index.jsp (remover)
  /manager (renomear, nome atual: /geopixel2023manager)
  /host-manager (renomear, nome atual: /geopixel2023host-manager)
  **Existe uma documentação nesse link**
http://20.0.0.191/geopixel/documentation/-/wikis/seguranca#configurações-do-servidor

- Adequar o tomcat para somente responder em HTTPS:
> Adicionar as tags dentro do arquivo web.xml:
`<security-constraint>
<web-resource-collection>
<web-resource-name>Entire Application</web-resource-name>
<url-pattern>/*</url-pattern>
</web-resource-collection>
<user-data-constraint>
<transport-guarantee>CONFIDENTIAL</transport-guarantee>
</user-data-constraint>
</security-constraint>`

- Aplicar medidas de segurança no cabeçalho do tomcat:
> Aplicar as seguintes tags no arquivo web.xml:
`<filter>
        <filter-name>httpHeaderSecurity</filter-name>
        <filter-class>org.apache.catalina.filters.HttpHeaderSecurityFilter</filter-class>
        <async-supported>true</async-supported>
        <init-param>
        <param-name>hstsEnabled</param-name>
        <param-value>true</param-value>
        </init-param>
        <init-param>
        <param-name>hstsMaxAgeSeconds</param-name>
        <param-value>31556927</param-value>
        </init-param>
        <init-param>
        <param-name>hstsIncludeSubDomains</param-name>
        <param-value>true</param-value>
        </init-param>
    </filter>`
    -----------------------------------------------------------------------------------------------------------------------------------------------   `<filter-mapping>
        <filter-name>httpHeaderSecurity</filter-name>
        <url-pattern>/*</url-pattern>
        <dispatcher>REQUEST</dispatcher>
    </filter-mapping>`
    
- Atualização da versão do tomcat:
> Atualizar o tomcat para 9.0.78 (Sem vunerabilidades conhecidas)



- Ajuste a nível de codígo (Fora do tomcat) para bloqueio de IP e conta:
> 1 - Filtro de conta por erro na autenticação (bloqueia conta por X segundos se o usuário errar a senha N vezes num intervalo de Y segundos)
2 - Filtro de IP para usuários não autenticados (bloqueia o IP se o usuário chamar N vezes os endoints de públicos de senha num intervalo de Y segundos). Número de requisições por intervalo deve ser menor
3 - Filtro de IP para usuários autenticados (bloqueia o IP se o usuário chamar N vezes os endoints de privados de senha num intervalo de Y segundos). Número de requisições por intervalo deve ser maior
**Filtro de RateLimit**
com token: 1000
sem token: 10
**Bloqueio de conta:**
5 tentativas erradas 
30 minutos

- Ajuste a nível de código (Fora do tomcat) Adicionar criptografia no trasporte de senha:
> Foi criada uma criptografia assimétrica para transportar todas as comunicações de senha. Para que o cliente tenha acesso a chave pública, foi criado um endpoint para requisição.


