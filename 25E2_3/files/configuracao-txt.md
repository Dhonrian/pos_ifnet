---
title: Parâmetros do arquivo de configuração
description: Aqui estarão descritos os parâmetros do arquivo de configuração do servidor para o sistema de fluxo
published: true
date: 2024-05-08T17:17:15.155Z
tags: configuração, alvara, fluxo, documentação fluxo, servidor, funcionamento
editor: markdown
dateCreated: 2024-05-02T22:14:28.907Z
---

# Parâmetros de configuração (WIP)
Esta seção oferece uma explicação concisa de cada item no arquivo de configuração, acompanhada de exemplos para alguns deles, demonstrando como devem ser configurados. A página será atualizada conforme novos parâmetros forem incluídos

## Emails de administrador
Esses parâmetros se referem ao email que é enviado ao administrador sempre que um novo usuário entra no sistema. As `tags` são substituídas  automaticamente pelo código.

## configuracao email {.tabset}
### bodyAdmin
O bodyAdmin é usado como corpo do email ao ser criado um novo usuário no sistema. Sendo enviado para o administrador. 

- **bodyAdmin**: Prezado(a) Administrador,`<n>` Um novo usuário do Portal do Geoprocessamento Corporativo `<n>` foi cadastrado no sistema e aguarda liberação de seu perfil.`<n>` Seguem as informações do usuário:`<n><n>` Nome: `<nome><n>` Login: `<login><n>` E-mail: `<email>`


### subjectAdmin 
 Assunto do e-mail enviado para o administrador notificando sobre um novo usuário cadastrado no sistema.
- **subjectAdmin**:Novo Usuário - Portal Geoprocessamento Corporativo - Prefeitura

### bodyInternalUser
  Esta mensagem é enviada para um usuário interno informando que seu perfil de acesso precisa ser definido pelo administrador para concluir o acesso ao sistema. No caso do fluxo não é utilizado
  - **bodyInternalUser**:Prezado(a) `<nome>` Por motivo de segurança um perfil de acesso precisa ser definido pelo administrador do portal `<n>` para que seu acesso seja concluído, logo você receberá um e-mail com a confirmação de acesso,`<n>` em caso de dúvida basta entrar em contato com o suporte@geopx.com.br para mais informações. `<n>` Suas informações:`<n><n>` Nome: `<nome><n>` Login: `<login><n>` E-mail: `<email><n><n>` Atenciosamente, `<n>` Geoprocessamento Corporativo.

### subjectInternalUser
  Assunto do e-mail enviado para o usuário interno informando sobre a necessidade de definição de perfil de acesso pelo administrador.
  
 - **subjectInternalUser**:Cadastro - Portal Geoprocessamento Coporativo - Prefeitura
  
### bodyUser
  Mensagem enviada para um usuário externo para concluir o processo de cadastro. Inclui um link para verificar a conta de e-mail e informações de contato para suporte. No caso do fluxo também não é utilizado já que os perfis externos sempre vão ser Publicos.
  - **bodyUser**:Prezado(a) `<nome>`,`<n>` Para terminar o cadastro, favor clicar no link para verificar a conta de e-mail`<n>` Em caso de duvida basta entrar em contato com o suporte@geopx.com.br para mais informacoes.`<n>` Dados cadastrados:`<n><n>` Nome: `<nome><n>` Login: `<login><n>` E-mail: `<email><n><n>` Verificacao de E-mail : https://homolog.flow.geopixel.com.br/alvara/activateAccount.html?login=`<link><n>` Atenciosamente, `<n>`Geoprocessamento Corporativo.
  
  ### subjectUser
  Assunto do e-mail enviado para o usuário externo para concluir o processo de cadastro.
  - **subjectUser**:Cadastro - Portal Geoprocessamento Corporativo - Prefeitura
  
### bodyRecuve
  Esta mensagem é enviada para um usuário que solicitou recuperação de senha. Inclui informações de login e um link para redefinir a senha
  - **bodyRecuve**:Prezado(a) `<nome>`,`<n>` Seguem suas informações de acesso :`<n><n>` Login: `<login><n>` Verificacao de E-mail : https://homolog.flow.geopixel.com.br/alvara/recover_password.html?login=`<link><n><n>` Atenciosamente,`<n>` Geoprocessamento Corporativo

 ### subjectRecuve
 Assunto do e-mail enviado para o usuário durante o processo de recuperação de senha.
 - **subjectRecuve**:Recuperação de Senha - Portal Geoprocessamento Corporativo - Prefeitura

### administratorEmail
Email de administrador da prefeitura

 ## Caminhos para salvar
Todos as configurações de caminho por padrão apontam para a pasta `/opt/anexos`. 
- As configurações são: **savepath**, **documentsPath**, **emp_pathUpload** e **emp_pathUploadLaudos**

## Configurações Servidor de Email
As configurações do servidor de email são informações fixas para o servidor de email da Geopixel. 
- As configurações são: **server_email_username**, **server_email_password**, **server_smtp_host**, **server_smtp_port**, **server_smtp_config**

## Autenticação tabela PDF
Tabela de autenticação de PDF para validar documentos.

- **pdf_authentication_table**:gpx_file_auth

## emp_isHomolog
Valor `true|false` que diz se a aplicação é ou não Homologação.
- **emp_isHomolog**: true

## Conexão ao banco
As configurações de conexão ao banco ditam qual o host, porta, usuário e banco a qual a aplicação se conectará.
 - Os parâmetros são: **dbHost**, **dbName**, **dbPass**, **dbPort**, **dbUser** 
>  **emp_dbUrl**, **emp_dbUser**, **emp_dbPass** e **emp_driver** Também são parâmetros de conexão no banco. Hoje não são mais usados.
{.is-warning}

## Parâmetros para Prefeitura
Aqui seguem alguns parâmetros cruciais para indicar ao sistema pasta de certidões e textos da tela inicial
## prefeitura {.tabset}
### emp_city
Nome da cidade. Esse parâmetro também indica qual pasta usar na raiz do sistema para buscar informações da certidão ao ser concatenada com `resources_`
 - **emp_city**:gpx_homolog
### emp_mayorName
Nome do prefeito
 - **emp_mayorName**:Eric Carreiro

### emp_logo
Brasão da cidade
- **emp_logo**:geopixel.png

### emp_logoDescription
Descrição do logo
- **emp_logoDescription**:Brasão da Prefeitura Municipal de Geopixel

### emp_prefeituraAddress
Endereço da Prefeitura 
- **emp_prefeituraAddress**:Rua José Cláudio Alves Santos,585

### emp_cityName
Nome da Cidade
- **emp_cityName**:Geopixel

### emp_prefeituraCNPJ
CNPJ da Prefeitura
- **emp_prefeituraCNPJ**:67.995.027/0001-32

## Parâmetros Tela Inicial
Aqui são configurados alguns parâmetros da tela de login e da tela inicial do sistema 
## portal {.tabset}

### emp_portalName
Nome do portal 
- **emp_portalName**:Aprovação Digital de Alvará de Obras

### emp_portalDescricao
Descrição da usabilidade da aplicação
 - **emp_portalDescricao**: Este portal permite que sejam realizadas e acompanhadas todas as ações relativas à obtenção de um alvará de construção, reforma ou demolição, permitindo o acompanhamento dos processos em andamento e atendimento às exigências legais. `/n`Este portal foi desenvolvido para atender engenheiros, arquitetos e empresas de engenharia `/n`E necessário possuir uma conta na rede da Prefeitura para acessar os processos digitalmente. Utilize o mesmo código de usuário e senha. Após o primeiro acesso, aguarde a comunicação do administrador do sistema indicando seu perfil de permissões.

### emp_portalTitle
Título do Portal
- **emp_portalTitle**: Prefeitura Municipal

### emp_portalSubtitle
Subtitulo do Portal
- **emp_portalSubtitle**: Secretaria de Planejamento Urbano e Gestão Estratégica


### emp_portalTheme
Texto abaixo do subtítulo

- **emp_portalTheme**: 


## Parâmetros GovBR
Existem diversos parâmetros para configuração do GovBr tanto de maneira para integração quanto para configurações do próprio sistema.

### 


## Descrição Parâmetros

- Abaixo seguem os parâmetros que ainda não foram formatados
---
emp_portalZoningSearch: Esse parametro é específico de hortolandia que possui uma integração. O parametro diz se a integração deve ou nem ser utilizada. Nas demais cidades sempre é false

emp_portaldocsignatures: Se tem ou não assinatura com govbr

emp_portaldownloadTicket: Esse parametro também é voltado para hortolandia. Ele dita se deve ou não ter o botão de baixar boleto e se as verificações de taxas devem ser feitas

emp_pageGovbr: Qual tela vai ter os botões de govbr, login ou aprovacao

emp_pageLogoutGovbr: qual pagina é a de logout do govbr

emp_pageLogin: a página de login normal

emp_dispatchDocType: id do documento de parecer na tabela doctypes

emp_isRegistrable: se é possível ou não se cadastrar pelo sistema

emp_themeGenerateSequence: Tema da tabela generate_search_sequence

emp_themeSearchSequence: Tema da search_sequence para procurar os habite-se e alvarás emitidos

emp_generateSequence: Mapeia a sequencia de habite-se e alvarás para buscar

emp_integrationTheme: Tema e perfil do mobiliário separado por |

emp_updateInformationMobTheme: Tema para atualizar o imobiliario. Separado por | 

emp_supportChannel: informação de suporte para o requerente entrar em contato

emp_buttonsForProfilesOutOfProcess: Botões para os processos fora de seus perfis. Para o perfil Administrador e Consulta. Os perfis são separados por '#', os botões por ',' e para processos encerrados usa-se o '|'

emp_profilesThatCanViewReport: Perfis que podem ver a opção de relatório no menu

emp_themeGenerateReport: Tema do relatório

emp_showInternalUserExternalTable: Mostra para o usuário público, quem está atuando no seu processo.

emp_isHomolog: Se a aplicação é homologação ou não

emp_themeImobiliario: Tema do Imobiliário para integração

emp_hasGovBr: Se a aplicação possui integração com o govbr

emp_integrationFiorilliTheme: Tema de integração com a Fiorilli

emp_sendMailNextStep: Indica se um email deve ser enviado a cada tramitação do processo ao requerente.

emp_typeOfFilter: Tipo de filtro a ser exibido para obras ou empreendedor

emp_daysToArchive: Dias de um processo parado para arquivar

serproPathToken, serproPathCPF, serproPathCNPJ, serproClientId, serproClientSecret: São parametros de integração com o serviço SerPro da Receita Federal

hortTokenProduction, hortTokenDevelopment, hortCNDURL, hortCNDToken, hortViability, taxPathCreate, taxPathVerifyPayment: São parametros especificos de hortolandia para integração com o serviço de Taxa e a hortCNDToken

billetId: Qual chave usar para pegar o link de boleto em hortolandia

publicProfileId: ID do perfil Publico 

managerProfileId: Id dos perfis ou usuários que são considerados "gerentes" ou administradores.

isLDAP: Se o login é feito através do protocolo LDAP

ldapURL, ldapDomain, ldapUser, ldapPass: Parametros para o login através do LDAP

autoActivateProfileId: Id do perfil que o usuário é associado quando o usuário não precisa ativar o perfil. Por enquanto utilizado apenas no LDAP

keystore, keystorePassword: Caminho e senha da chave para assinatura caso não seja utilizado a do govbr

govBrResponseType, govBrUrlProviderLogin, govBrUrlService, govBrScopes, govBrCodeChallengeMethod, govBrCodeChallenge, govBrUrlSignature, govBrImagePath, govBrUrlProviderSignature, govBrScopeSignature, govBrRedirectUriSignature, govBrClientIdSignature, govBrClientSecret, govBrRedirectUriLogin, govBrClientIdLogin, govBrSecret: Parametros de integração com o GOVBR

softPlanBodyCredentialsRequestToken, softPlanUrlRequestToken, softPlanAuthorizationRequestToken, softPlanUrlRequestProtocol: Parametros de integração com os serviços da softplan

bookDocType: ID do caderno de documentos na tabela doctypes

processPrefix: Prefixo para um processo

## Configurações da integração Via Rápida
Os parâmetros descritos aqui se referem à implementação e correto funcionamento da integração com a JUCESP - Via Rápida.
Ressaltando que a integração possuí dois ambientes junto à JUCESP, homologação e produção, e o chaveamento para saber qual dos ambientes a aplicação irá acessar é baseada no valor do parâmetro ***emp_isHomolog***.

## Configuração Via Rápida {.tabset}
### viaRapidaIntegration
Um valor booleano ***(true/false)*** que define se o cliente possuí integração com o Via Rápida.
- Caso **true**, indica que a aplicação possuí integração com o Via Rápida e deverá ter os outros parâmetros configurados corretamente. Neste caso, o cliente poderá acessar às interfaces da integração.
- Caso **false**, indica que a aplicação ***NÃO*** possuí, e não há necessidade das outras nos outros parâmetros estarem configurados. Neste caso, o cliente não possuíra acesso às interfaces da integração.
- Exemplos:
  - viaRapidaIntegration:true
  - viaRapidaIntegration:false
  
### viaRapidaAlwaysHighRisk
Um valor booleano ***(true/false)*** que define se as solicitações de Licenciamento sempre deverão ser de alto risco. Esse parâmetro tem relação com o parâmetro **viaRapidaAlwaysHighRiskQuestionId**.
- Caso **true**, indica que todos as solicitações de Licenciamento serão categorizadas e informadas ao Via Rápida que é uma solicitação de Alto Risco. Neste caso, o parâmetro **viaRapidaAlwaysHighRiskQuestionId** deve ser informado corretamente.
- Caso **false**, indica que todas as solicitações de Licenciamento serão corretamente avaliadas e categorizadas em seu nível de risco correto. Neste caso, o banco de dados deverá estar coerente a relação de CNAEs no schema *via_rapida*
- Exemplos:
  - viaRapidaAlwaysHighRisk:true
  - viaRapidaAlwaysHighRisk:false
  
### viaRapidaAlwaysHighRiskQuestionId
Um valor inteiro ***(número)*** que aponta para o ID da questão *default* na tabela via_rapida.question. Este parâmetro é obrigatório quando o valor do parâmetro **viaRapidaAlwaysHighRisk** for **true**.
- Exemplo:
  - viaRapidaAlwaysHighRiskQuestionId:1
  
### viaRapidaSendRequesterEmail
Um valor booleano ***(true/false)*** que define se um e-mail deverá ser enviado ao solicitante da solicitação do Licenciamento. Este parâmetro não deve ser ***true*** para ambientes de homologação, pois o usuário de homologação do Via Rápida possuí o e-mail de um administrador da JUCESP.
Para ambientes de produção, é recomendado que o valor seja ***true***, para que o usuário solicitante seja notificado quando um processo interno for criado para a avaliação da solicitação de Licenciamento.
- Caso **true**, indica que um e-mail será enviado para o usuário que está solicitando o Licenciamento quando um processo interno for criado para a avaliação da solicitação.
- Caso **false**, indica que um e-mail ***NÃO*** será enviado para o usuário que está solicitando o Licenciamento quando um processo interno for criado para a avaliação da solicitação.
- Exemplos:
  - viaRapidaSendRequesterEmail:true
  - viaRapidaSendRequesterEmail:false

## Configuração Via Rápida 2 {.tabset}
### viaRapidaSoapUser
Um valor de texto para definir o usuário da prefeitura fornecido pela JUCESP para acesso aos serviços SOAP.
- Exemplo:
  - viaRapidaSoapUser:prefeitura.redesim

### viaRapidaSoapPassword
Um valor de texto para definir a senha do usuário da prefeitura fornecido pela JUCESP para acesso aos serviços SOAP.
- Exemplo:
  - viaRapidaSoapPassword:123abc
 
### viaRapidaSoapProxyUser
Um valor de texto para definir a usuário do proxy da prefeitura fornecido pela JUCESP para acesso aos serviços SOAP.
- Exemplo:
  - viaRapidaSoapProxyUser:prefeitura.redesim
 
### viaRapidaSoapProxyPassword
Um valor de texto para definir a senha do usuário do proxy da prefeitura fornecido pela JUCESP para acesso aos serviços SOAP.
- Exemplo:
  - viaRapidaSoapProxyPassword:abc123
 
 
## Configuração Via Rápida 3 {.tabset}
### viaRapidaRestUser
Um valor de texto para definir o usuário da prefeitura fornecido pela JUCESP para acesso aos serviços REST.
- Exemplo:
  - viaRapidaRestUser:prefeitura.redesim

### viaRapidaRestPassword
Um valor de texto para definir o usuário da prefeitura fornecido pela JUCESP para acesso aos serviços REST.
- Exemplo:
  - viaRapidaRestPassword:1ab2c3
  
### viaRapidaGeopixelRestUser
Um valor de texto para definir o usuário da prefeitura que é fornecido pela ***GEOPIXEL à JUCESP*** no momento da implantação da funcionalidade do Via Rápida na prefeitura, para que a JUCESP possa acessar os serviços implementados pela Geopixel.
Este valor pode ser arbitrário, mas recomenda-se que evite repeti-lo entre prefeituras, por segurança, e que o mesmo seja alinhado com o cliente.
***ATENÇÃO*** *: Este valor, uma vez definido e fornecido à JUCESP, não deve ser alterado sem informar o novo valor à eles*
- Exemplo:
  - viaRapidaGeopixelRestUser:prefeituraABC
  
### viaRapidaGeopixelRestPassword
Um valor de texto para definir a senha do usuário da prefeitura que é fornecido pela ***GEOPIXEL à JUCESP*** no momento da implantação da funcionalidade do Via Rápida na prefeitura, para que a JUCESP possa acessar os serviços implementados pela Geopixel.
Este valor pode ser arbitrário, mas recomenda-se que evite repeti-lo entre prefeituras, por segurança, e que o mesmo seja alinhado com o cliente.
***ATENÇÃO*** *: Este valor, uma vez definido e fornecido à JUCESP, não deve ser alterado sem informar o novo valor à eles*
- Exemplo:
  - viaRapidaGeopixelRestPassword:senhaPrefeituraABC
  
## Configuração Via Rápida 4 {.tabset}
### viaRapidaLicensingProcessTask
Um valor inteiro ***(número)*** que aponta para a coluna *task* da tabela *tab_process_flow* do tipo do fluxo a ser executado para um processo de análise interno de Licenciamento pela prefeitura.
- Exemplo:
  - viaRapidaLicensingProcessTask:20

### viaRapidaLicensingProcessTaskGroup
Um valor inteiro ***(número)*** que aponta para a coluna *task_group* da tabela *tab_process_flow* do tipo do fluxo a ser executado para um processo de análise interno de Licenciamento pela prefeitura.
- Exemplo:
  - viaRapidaLicensingProcessTaskGroup:20

### viaRapidaMunicipalInscriptionProcessTask
Um valor inteiro ***(número)*** que aponta para a coluna *task* da tabela *tab_process_flow* do tipo do fluxo a ser executado para um processo de análise interno de Inscrição Municipal pela prefeitura.
- Exemplo:
  - viaRapidaMunicipalInscriptionProcessTask:1

### viaRapidaMunicipalInscriptionProcessTaskGroup
Um valor inteiro ***(número)*** que aponta para a coluna *task_group* da tabela *tab_process_flow* do tipo do fluxo a ser executado para um processo de análise interno de Inscrição Municipal pela prefeitura.
- Exemplo:
  - viaRapidaMunicipalInscriptionProcessTaskGroup:20


## Exemplo de Arquivo de Configuração
Um arquivo de configuração completo geralmente segue este formato 
```
postgres
5432
postgres
Postgres!1@2#3
postgres
bodyAdmin:Prezado(a) Administrador,<n> Um novo usuário do Portal do Geoprocessamento Corporativo<n> foi cadastrado no sistema e aguarda liberação de seu perfil.<n> Seguem as informações do usuário:<n><n> Nome: <nome><n> Login: <login><n> E-mail: <email>
subjectAdmin:Novo Usuário - Portal Geoprocessamento Corporativo - Prefeitura
bodyInternalUser:Prezado(a) <nome>Por motivo de segurança um perfil de acesso precisa ser definido pelo administrador do portal <n> para que seu acesso seja concluído, logo você receberá um e-mail com a confirmação de acesso,<n> em caso de dúvida basta entrar em contato com o suporte@geopx.com.br para mais informações. <n> Suas informações:<n><n> Nome: <nome><n> Login: <login><n> E-mail: <email><n><n>Atenciosamente, <n>Geoprocessamento Corporativo.
subjectInternalUser:Cadastro - Portal Geoprocessamento Coporativo - Prefeitura
bodyUser:Prezado(a) <nome>,<n> Para terminar o cadastro, favor clicar no link para verificar a conta de e-mail<n> Em caso de duvida basta entrar em contato com o suporte@geopx.com.br para mais informacoes.<n> Dados cadastrados:<n><n> Nome: <nome><n> Login: <login><n> E-mail: <email><n><n> Verificacao de E-mail : https://homolog.flow.geopixel.com.br/alvara/activateAccount.html?login=<link><n> Atenciosamente, <n>Geoprocessamento Corporativo.
subjectUser:Cadastro - Portal Geoprocessamento Corporativo - Prefeitura
bodyRecuve:Prezado(a) <nome>,<n> Seguem suas informações de acesso :<n><n> Login: <login><n> Verificacao de E-mail : https://homolog.flow.geopixel.com.br/alvara/recover_password.html?login=<link><n><n> Atenciosamente,<n> Geoprocessamento Corporativo
subjectRecuve:Recuperação de Senha - Portal Geoprocessamento Corporativo - Prefeitura
bodyFeed:Prezado(a) <nome>,<n> Sua ocorrência foi registrada e está em análise<n> Obrigrado pelo contato.<n><n> Segue descrição da ocorrência: <n><n> <desc><n><n> Atenciosamente,<n> Geoprocessamento Corporativo
subjectFeed:Aviso de ocorrência aberta - Portal Geoprocessamento Corporativo - Prefeitura
bodyFeedEnd:Prezado(a) <nome>,<n> Sua ocorrência foi encerrada pelo Administrador do Sistema :<n><n> Segue descrição da ocorrência: <n><n> <desc><n><n> Atenciosamente,<n> Geoprocessamento Corporativo
subjectFeedEnd:Ocorrência encerrada - Portal Geoprocessamento Corporativo - Prefeitura
bodyFeedEndAdm:Prezado(a) Administrador,<n> O usuário <nome> foi notificado sobre o encerramento de sua ocorrencia.<n> Segue descrição da ocorrência: <n><n> <desc><n><n> Atenciosamente,<n> Geoprocessamento Corporativo
subjectFeedEndAdm:Aviso de ocorrência encerrada - Portal Geoprocessamento Corporativo - Prefeitura
savepath:/app/data/anexos
elevation:
geocoding:
viwerpath:
utmsirgas:31983
notificationPrivateKey:
notificationPublicKey:
panoramic:
pgv_files:
python_path:python3.7
pgv_pesquisa_id:
formPublic:920
formEmployee:921
formEntidade:
administratorEmail:sistema@geopx.com.br

server_email_username:sistema@geopixel.com.br
server_email_password:y,oV3BeWzq!1
server_smtp_host:smtp.office365.com
server_smtp_port:587
server_smtp_config:mail.smtp.starttls.enable=true

pdf_authentication_table:gpx_file_auth
domain:https://homolog.flow.geopixel.com.br/alvara_server/rest
pdfResources:/app/data/
documentsPath:/app/data/anexos

dbHost:postgres
dbName:postgres
dbPass:Postgres!1@2#3
dbPort:5432
dbUser:postgres

emp_city:gpx_homolog
emp_dbUrl:jdbc:postgresql://postgres:5432/postgres
emp_dbUser:postgres
emp_dbPass:Postgres!1@2#3
emp_driver:org.postgresql.Driver
emp_mayorName:Eric Carreiro
emp_logo:geopixel.png
emp_logoDescription:Brasão da Prefeitura Municipal de Geopixel
emp_cityName:Geopixel
emp_prefeituraAddress:Rua José Cláudio Alves Santos,585
emp_prefeituraCNPJ:67.995.027/0001-32
emp_urlClient:/alvara
emp_urlServer:/alvara
emp_pathUpload:/app/data/anexos
emp_pathUploadLaudos:/app/data/anexos
emp_portalName:Aprovação Digital de Alvará de Obras
emp_portalDescricao: Este portal permite que sejam realizadas e acompanhadas todas as ações relativas à obtenção de um alvará de construção, reforma ou demolição, permitindo o acompanhamento dos processos em andamento e atendimento às exigências legais. /nEste portal foi desenvolvido para atender engenheiros, arquitetos e empresas de engenharia /nE necessário possuir uma conta na rede da Prefeitura para acessar os processos digitalmente. Utilize o mesmo código de usuário e senha. Após o primeiro acesso, aguarde a comunicação do administrador do sistema indicando seu perfil de permissões.
emp_portalTitle: Prefeitura Municipal
emp_portalSubtitle: Secretaria de Planejamento Urbano e Gestão Estratégica
emp_portalTheme:
emp_portalZoningSearch:false
emp_portaldocsignatures:false
emp_portaldownloadTicket:false
emp_pageGovbr:aprovacao
emp_pageLogoutGovbr:logout
emp_pageLogin:login.html
emp_dispatchDocType:996
emp_isRegistrable:false
emp_themeGenerateSequence:1020
emp_themeSearchSequence:1021
emp_generateSequence:ESPELHO DE ALVARÁ|seq_number_alvara,ESPELHO DE HABITE-SE|seq_number_habitese
emp_integrationTheme:1023|56
emp_updateInformationMobTheme:1022
emp_supportChannel:suporte@geopixel.sp.gov.br,Telefone: (19) 99999-9999,Ramal: 8000/8000
emp_buttonsForProfilesOutOfProcess:Administrador|<i style="cursor:pointer" title="Informação Adicional" class="info-add acao material-icons">info</i>,<i style="cursor:pointer" title="Histórico do Processo" class="view-history acao material-icons">history</i>,<button type="button" class="btn btn-info btnSmall view-requerimento acao" title="Ver Requerimento">Ver Requerimento</button>,<button type="button" class="btn btn-changeColor btnSmall documentos acao" title="Documentos"> textChange </button>|,<button type="button" class="btn btn-success btnSmall changeResponsible acao" id="assign-user" title="Delegar Processo">Alterar Responsável</button>#Consulta|<i style="cursor:pointer" title="Informação Adicional" class="info-add acao material-icons">info</i>,<i style="cursor:pointer" title="Histórico do Processo" class="view-history acao material-icons">history</i>,<button type="button" class="btn btn-info btnSmall view-requerimento acao" title="Ver Requerimento">Ver Requerimento</button>,<button type="button" class="btn btn-changeColor btnSmall documentos acao" title="Documentos"> textChange </button>,<button type="button" class="btn btn-info btnSmall onlineHistory" title="Histórico Online" style="margin-left:16px;margin-right:10px"><img class="rounded" src="image/ajax-loader.gif" style="max-width: 18px;margin-right:5px;display:none;">Histórico Online</button>
emp_profilesThatCanViewReport:1,39,40
emp_themeGenerateReport:927
emp_showInternalUserExternalTable:true
emp_isHomolog:true
emp_themeImobiliario:976
emp_hasGovBr:false
emp_integrationFiorilliTheme:1200
emp_sendMailNextStep:false
emp_typeOfFilter:obras
emp_daysToArchive:90
serproPathToken:https://gateway.apiserpro.serpro.gov.br/token
serproPathCPF:https://gateway.apiserpro.serpro.gov.br/consulta-cpf/v1/cpf/
serproPathCNPJ:https://gateway.apiserpro.serpro.gov.br/consulta-cnpj-df/v2/qsa/
serproClientId:AvBkrQ2EnaEbkmoOlC20hcjynRMa
serproClientSecret:kjmJ5fnIEZ3nk5CH1_9FECcjo8wa
hortTokenProduction:b3ba81a5-6b6c-4fd3-88ce-3af4569def42
hortTokenDevelopment:274d1d56-11a4-48a6-bd40-e790a839e8d0
hortCNDURL:https://api.hortolandia.sp.gov.br/api/debitos/v1/certidao/IMO
hortCNDToken:b3ba81a5-6b6c-4fd3-88ce-3af4569def42
hortViability:https://api.hortolandia.sp.gov.br/api/geo/viabilidade/v1/get/x
taxPathCreate:https://api.hortolandia.sp.gov.br/api/boleto/v1/create
taxPathVerifyPayment:https://api.stage.hortolandia.sp.gov.br/api/boleto/v1/{number}/status
publicProfileId:16
managerProfileId:[1,155,154,153,137,70,1,40,175,51]
isLDAP:true
ldapURL:ldap://10.0.0.10:389/
ldapDomain:DC=geopixel,DC=local
ldapUser:int_geocidades
ldapPass:Geopixel@2024
autoActivateProfileId:0
hortToken:274d1d56-11a4-48a6-bd40-e790a839e8d0
keystore:/app/data/resources/certificate-pkcs12.p12
keystorePassword:geopixel@qwert
govBrResponseType:code
govBrUrlProviderLogin:https://sso.staging.acesso.gov.br
govBrUrlService:https://api.staging.acesso.gov.br
govBrScopes:openid+(email/phone)+profile+govbr_confiabilidades
govBrCodeChallengeMethod:S256
govBrCodeChallenge:UnautpKdBWtJKPMMmGpLowoEGl3JksnSe0mvak2xELk=
govBrUrlSignature:https://assinatura-api.staging.iti.br/externo/v2
govBrImagePath:/app/data/resources/imagens/logo-govbr-com-contorno_245x100px.png
govBrUrlProviderSignature:https://cas.staging.iti.br/oauth2.0
govBrScopeSignature:sign
govBrRedirectUriSignature:https://alvara.hortolandia.sp.gov.br/alvara_hortolandia/aftersignature
govBrClientIdSignature:prefeiturahortolandia
govBrClientSecret:RotGMfDPNXPYYFOPOkxB
govBrRedirectUriLogin:https://alvara.hortolandia.sp.gov.br/alvara_hortolandia/afterlogin
govBrClientIdLogin:hortolandia.facil.test
govBrSecret:AOZS3eX8YLM31PlW4bfjeUBrTDXqgaO7_G3fj61DZO5IRQgWE4hohHx-MJNm75kbxW-I1h3Ew2V0PcCG7g6pBeI
govBrRedirectUriLogout:
softPlanBodyCredentialsRequestToken:grant_type=client_credentials&cdUsuario=SOFTPLAN
softPlanUrlRequestToken:https://pmitapevi-services-hml:46281f9f-f1f8-450e-97b9-dee7772cc94b-hml@itapevi-hml.solarbpm.softplan.com.br/ungp-server-oauth/oauth/token
softPlanAuthorizationRequestToken:Basic cG1pdGFwZXZpLXNlcnZpY2VzLWhtbDo0NjI4MWY5Zi1mMWY4LTQ1MGUtOTdiOS1kZWU3NzcyY2M5NGItaG1s
softPlanUrlRequestProtocol:https://itapevi-hml.solarbpm.softplan.com.br/solarbpm-integracao/processo
pathDocType:999
bookDocType:997
billetId:id_boleto
processPrefix:e
emp_sendMailNextStep:true
emp_integrationTheme:4,1025|

viaRapidaIntegration:true

viaRapidaLicensingProcessTask:1
viaRapidaLicensingProcessTaskGroup:20
viaRapidaMunicipalInscriptionProcessTask:2
viaRapidaMunicipalInscriptionProcessTaskGroup:20

viaRapidaSoapUser:prefeitura.redesim
viaRapidaSoapPassword:123

viaRapidaSoapProxyUser:prefeitura.redesim
viaRapidaSoapProxyPassword:@#PREFEITURA#@

viaRapidaRestUser:prefeitura.redesim
viaRapidaRestPassword:123

viaRapidaGeopixelRestUser:usuarioPrefeitura
viaRapidaGeopixelRestPassword:senhaPrefeitura

viaRapidaSendRequesterEmail:false

viaRapidaAlwaysHighRisk:true

viaRapidaAlwaysHighRiskQuestionId:1
```

