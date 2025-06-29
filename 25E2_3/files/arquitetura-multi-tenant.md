---
title: Arquitetura Multi Tenant
description: Breve tour pelos conceitos e implementação da arquitetura multi tenant.
published: true
date: 2024-04-29T14:59:37.391Z
tags: geocidades, v3, multi-tenant, tenant, multitenant, multi tenant, multi, cidades, server, client
editor: markdown
dateCreated: 2024-04-24T14:18:03.672Z
---

# O que é e Como Implementamos o Multi Tenant

Breve tour pela nossa implementação da arquitetura multi tenant.

## O que é Arquitetura Multi Tenant

Multi tenant é uma arquitetura de software que permite que uma única instância de software atenda vários clientes. Em outras palavras, um único desenvolvimento de código pode atender vários usuários, separando informações confidenciais de cada um e deixando-as apenas visíveis para eles.

Assim, cada cliente do serviço é considerado um inquilino. Isso permite o cliente personalizar e configurar o software de acordo com suas necessidades específicas, mas o código em si se manterá o mesmo.

Algo que é importante destacar nesta arquitetura é que um cliente não é necessariamente um único usuário, podendo se tratar de um grupo de usuários. Alguns serviços, por exemplo, trabalham com equipes ou grupos em que um cliente pode ter um subdomínio para entrar no aplicativo e ter vários usuários com acesso a essas informações.

> Mais informações podem ser obtidas no artigo [Diferença entre Single Tenant e Multi Tenant](https://medium.com/@edytarcio/arquitetura-multi-tenancy-bb7b47d7ba).
{.is-info}

## Como Implementamos o Multi Tenant

Há muitas maneiras de se implementar a arquitetura multi tenant, variando em maneiras de reservar o espaço do tenant, de separar os dados e arquivos do tenant, etc.

Nós optamos por definir o espaço do tenant a partir do subdomínio, separando seus dados em bancos de dados próprio e armazenando seus arquivos em um espaço próprio também, seja esse espaço em disco ou em um serviço de storage em cloud.

### Identificando o Tenant

A partir do momento em que passamos a ter uma única aplicação para atender a muitos clientes, criamos um problema: como saberemos para qual tenant se direciona uma requisição?

Para lidar com esse problema, precisamos interceptar cada uma das requisições, identificar, a partir do subdomínio, o tenant a qual ela se refere e então adequar a aplicação para responder à requisição utilizando as configurações, dados e assets pertencentes ao tenent requerente.

Para interceptarmos as requisições, utilizamos Filters do Servlet, e para identificarmos o tenant, extraímos o subdomínio da URL de origem da requisição e comparamos com uma lista de tenants configurados em nosso enumerador de tenants.

Então na classe `PrefectureTenantFilter`, interceptamos a requição com o médoto `doFilter` (linha 6) e extraímos da requisição o nome do tenant através da chamada do método `resolveTenant` (linha 15):

```java
// src/main/java/br/com/geopixel/platform/model/filters/PrefectureTenantFilter.java
public class PrefectureTenantFilter implements Filter {
		...

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        HttpServletRequest httpRequest = (HttpServletRequest) request;
        HttpServletResponse httpResponse = (HttpServletResponse) response;

        Optional<PrefectureTenant> optionalTenant = Optional.empty();
        EnvOrRequest envOrRequest = new EnvOrRequest(httpRequest, environment);

        for (ITenantResolver<EnvOrRequest> tenantResolver : tenantResolvers) {
            optionalTenant = tenantResolver.resolveTenant(envOrRequest);
            
            if (optionalTenant.isPresent())
                break;
        }
        
        ...
    }
}
```

Neste trecho de código, notamos que é feita uma iteração por alguns resolvers, dentre eles haverá o implementado pela classe `SubDomainTenantResolver`, responsável por obter da requisição o nome do tenant que está acessando a aplicação.

Então, no método `resolveTenant` (linha 5) da classe `SubDomainTenantResolver`, extraímos dos headers da requisição a URL de origem (linha 11) e então extraímos da URL de origem o primeiro subdomínio (linhas 16 a 25). Obtido o subdomínio, verificamos se este subdomínio refer-se a um de nossos tenants configurados `PrefectureTenant.byNameIgnoreCase(subdomain)` (linha 33) e assim obtivemos nosso tenant a partir da requisição.

```java
// src/main/java/br/com/geopixel/platform/model/filters/tenantResolver/SubDomainTenantResolver.java
public class SubDomainTenantResolver implements ITenantResolver<EnvOrRequest> {
    ...

    @Override
    public Optional<PrefectureTenant> resolveTenant(EnvOrRequest envOrRequest) {
        String subdomain = "";

        try {
            HttpServletRequest request = envOrRequest.getRequest();
            Optional<String> originOptional = Optional.ofNullable(request.getHeader(HttpHeaders.REFERER));
            if (!originOptional.isPresent())
                return Optional.empty();

            String origin = originOptional.get();
            if (originOptional.isPresent() && !origin.isEmpty()) {
                // Resolver to subdomain
                URL url = new URL(origin);
                String host = url.getHost().replaceAll("^www\\.", "");
                String[] hostChunks = host.split("\\.");
                

                if (hostChunks.length > 0) {
                    subdomain = hostChunks[0];
                }
            }
        } catch (MalformedURLException ex) {
            ex.printStackTrace();
        }

        Optional<PrefectureTenant> customSubdomainPrefectureTenant = this.searchCustomSubdomain(subdomain);
        Optional<PrefectureTenant> prefectureTenant = 
            customSubdomainPrefectureTenant.isPresent() ? customSubdomainPrefectureTenant : PrefectureTenant.byNameIgnoreCase(subdomain);

        return prefectureTenant;
    }
    
    ...
}
```

Uma vez identificado o tenant, o atribuímos ao contexto da aplicação, assim todas as operações serão realizadas considerando este tenant. Com isso garantimos que as configurações, o banco e os assets acessados são pertencentes ao tenant definido no contexto. Então atribuímos o tenent ao contexto (linha 10), liberamos a requisição interceptada (linha 20) e por fim removemos o tenant do contexto (linha 21) para que as próximas requisições seja realizadas em seus contextos próprios.

```java
// src/main/java/br/com/geopixel/platform/model/filters/PrefectureTenantFilter.java
public class PrefectureTenantFilter implements Filter {
    ...

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        ...

        PrefectureTenant tenant = optionalTenant.get();
        PrefectureTenantContextHolder.set(tenant);

        try {
            this.dataSourceTenantManager.manage();
        } catch (SettingsException 
            | ConfigurationException 
            | ResourceNotFoundException ex) {
            throw new ServletException(ex); 
        }

        chain.doFilter(httpRequest, httpResponse);
        PrefectureTenantContextHolder.clear();
    }
}
```

### Encontrando o Banco do Tenant

Uma vez que o tenant é identificado, precisamos carregar suas configurações e seu banco de dados para responder a sua requisição. Sua conexão com banco de dados é realizada imediatamente na etapa de indentificação do tenant, ainda no método `doFilter` da classe `PrefectureTenantFilter` realizamos a chamada para `dataSourceTenantManager.manage` (linha 10).

```java
// src/main/java/br/com/geopixel/platform/model/filters/PrefectureTenantFilter.java
public class PrefectureTenantFilter implements Filter {
    ...

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        ...

        try {
            this.dataSourceTenantManager.manage();
        } catch (SettingsException 
            | ConfigurationException 
            | ResourceNotFoundException ex) {
            throw new ServletException(ex); 
        }

        ...
    }
}
```

Este método nos leva até a classe `DataSourceTenantManager` e em seu método `manage` obtemos o tenant do contexto da requisição (linha 6), carregamos as informações de acesso ao banco de dados do tenant através da chamada de `dataSourceTenantLoader.tenantDatabasePropertyConnection` (linha 14) e em seguida criamos o datasource para o banco do tenant (linha 15), por fim atribuímos ao router do Spring o mapa de tenant-datasource (linhas 19 a 21).

```java
// src/main/java/br/com/geopixel/platform/config/multitenant/DataSourceTenantManager.java
public class DataSourceTenantManager {
    ...

    public void manage() 
        throws ConfigurationException, ResourceNotFoundException, IOException, SettingsException {
        PrefectureTenant tenant = PrefectureTenantContextHolder.get();
        DataSourceRouter dataSourceRouter = ((DataSourceRouter) dataSource);
        Map<Object, Object> datasourceMap = new HashMap<>(dataSourceRouter.getResolvedDataSources());

        if (datasourceMap.containsKey(tenant))
            return;

        DatabasePropertyConnection dbPropertyConn;
        dbPropertyConn = this.dataSourceTenantLoader.tenantDatabasePropertyConnection(tenant);
        DataSource dataSource = dbPropertyConn.buildDataSource();

        this.executeMigrations(dbPropertyConn);

        datasourceMap.put(tenant, dataSource);
        dataSourceRouter.setTargetDataSources(datasourceMap);
        dataSourceRouter.afterPropertiesSet();
    }

    ...
}
```

Com o mapa de datasources configurado no Spring, temos de garantir que, quando for feita uma consulta ao banco de dados, seja direcionada ao banco correto, para isto fizemos uma implementação própria do datasource router do spring e configuramos que sempre utilize o tenant do contexto atual para definir para qual banco será roteado (linhas 5 à 7).

```java
// src/main/java/br/com/geopixel/platform/config/multitenant/DataSourceRouter.java
public class DataSourceRouter extends AbstractRoutingDataSource {

    @Override
    protected Object determineCurrentLookupKey() {
        return PrefectureTenantContextHolder.get();
    }
    
}
```

### Encontrando os Assets do Tenant

Além de banco de dados próprios, os tenants também possuem seus próprios documentos, imagens, entre outros tipos de arquivos e assets. Para garantir o consumo correto dos recursos de um tenant espeícifo, criamos alguns gerenciadores de arquivos para lidar com os diferentes tipos de arquivos utilizados pela aplicação. Classificamos os arquivos da aplicação em 3 tipos: configuração, dados e temporários. Organizamos essas classes de arquivos em caminhos diferentes em nosso storage, e para cada um deles também criamos um gerenciador específico somado de um genérico que pode ser utilizado para carregar arquivos de qualquer caminho. Esses gerenciadores são `ServerFolderStorageService` para arquivos de configuração, `DataFolderStorageService` para arquivos de dados, `TemporaryFolderStorageService` para os arquivos temporários e `LocalStorageService` para caminhos de arquivos genéricos.

Todos esses gerenciadores são implementações da interface `StorageManager` que dispõe de métodos para carregar, salvar de deletar arquivos (linhas 4, 8 e 11).

```java
// src/main/java/br/com/geopixel/platform/model/infra/storage/StorageManager.java
public interface StorageManager {
    ...
    public InputStream loadFile(String filePath)
            throws IOException, EnvironmentVariableNotFoundException, ConfigurationException, ResourceNotFoundException;

    ...
    public void saveFile(String path, InputStream data) throws IOException;

    ...
    public void deleteFile(String path) throws IOException, ForbiddenException;
}
```

Sendo assim, a diferença entre eles se baseia na classe de arquivos em que atuam e assim devem ser utilizadas: `ServerFolderStorageService` para arquivos de configuração, `DataFolderStorageService` para arquivos de dados, `TemporaryFolderStorageService` para os arquivos temporários e `LocalStorageService` para caminhos de arquivos genéricos.

Por exemplo, quando vamos carregar os arquivos de configuração da aplicação de do banco de dados, fazemos a requisição para o nosso storage na classe `ApplicationSettings` (linhas 16 e 21). Neste caso, basta passar o tenant e o caminho relativo para um arquivo de configuração, por exemplo `config/application.json` ou `config/database.json`, como exposto no trecho abaixo. Quanto às outras classes de arquivos, dados e temporários, a lógica é a mesma.

> Note na linha 5 que o tipo do gerenciador é **ServerFolderStorageService**, importante que seja exatamente do tipo do gerenciador que pretende usar. As outras variações são **DataFolderStorageService** e **TemporaryFolderStorageService**.
{.is-info}

> A única excessão à regra acima é para o **LocalStorageService**, pois quando pretendemos utilizar o gerenciador de arquivos genérico é importante que seu tipo seja o da interface **StorageManager**. Isto é necessário, pois o **LocalStorageService** faz o carregamento em disco, no entanto em algum momento podemos alterar a estratégia para consumir arquivos a partir de uma API de uma cloud qualquer e utilizando a interface **StorageManager** para que a manutenção seja facilitada.
{.is-warning}


```java
// src/main/java/br/com/geopixel/platform/model/config/ApplicationSettings.java
public class ApplicationSettings {
    ...

    private ServerFolderStorageService serverStorageManager;

    ...

    public void loadTenantConfigurations(PrefectureTenant prefectureTenant)
        throws EnvironmentVariableNotFoundException, ConfigurationException, IOException, 
        ApplicationSettingNotFoundException, ResourceNotFoundException {
        ...

        try (
                InputStream databaseConfigStream = 
                    serverStorageManager.loadFile(prefectureTenant, this.getConfigFilePath(databaseConfigFile));
                InputStreamReader databaseConfigReader = new InputStreamReader(databaseConfigStream);
                JsonReader databaseConfigJsonReader = new JsonReader(databaseConfigReader);

                InputStream applicationConfigStream = 
                    serverStorageManager.loadFile(prefectureTenant, this.getConfigFilePath(APPLICATION_CONFIGURATIONS_FILE_NAME));
                InputStreamReader applicationConfigReader = new InputStreamReader(applicationConfigStream);
                JsonReader applicationConfigJsonReader = new JsonReader(applicationConfigReader);
            ) {
            ...
        }
    }

    ...
}
```

