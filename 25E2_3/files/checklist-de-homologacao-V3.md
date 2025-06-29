---
title: Checklist de Homologacao V3
description: Este documento visa elencar os pontos que devem ser checados para homologar a migração da V2 para a V3
published: true
date: 2023-11-17T14:11:50.423Z
tags: checklist, homologacao, v3, v2, migração, migrar
editor: markdown
dateCreated: 2023-11-09T11:13:39.670Z
---

# Checklist de Homologação V3

## Contexto 
A versão 3 do sistema Geopixel Cidades está perto de entrar em produção. Diante deste cenário, se faz necessária a criação de documentos que auxiliarão para que este processo de migração entre versões ocorra de maneira segura, rápida e com qualidade, mitigando boa parte dos riscos envolvidos no processo. Para execução deste checklist, pressupõe-se que o ambiente já está **implantado** e **operacional**, seguindo o processo de implantação da V3 (vide documento [neste link](https://wiki.flow.geopixel.com.br/pt-br/v3/ambiente/configuracao-publicacao-geocidades)).

## Objetivo
O propósito deste documento é assegurar uma transição suave entre as versões 2 e 3, de modo que, através de itens claros e detalhados de checagem, nos pontos críticos do sistema, seja possível homologar se a migração para a versão 3 ocorreu com o sucesso esperado.

## Instruções
O checklist será dividido em seções do sistema, podendo conter um ou mais itens de verificação para cada seção. Cada seção terá um parágrafo de contextualização. Cada item terá uma descrição detalhada, seguido de campos de validação, tais como: **Atende**, **Não atende** e **Observações**.

## Preâmbulo
Antes da execução do checklist, é de suma importância que sejam verificados alguns itens que garantirão a mitigação de possíveis riscos inerentes a qualquer migração.

### Item I - Backup do banco de dados
Antes da execução do checklist, é importante verificar se a configuração de backup, na máquina Oracle, está ativa. Isso nos permite retornar a um estado anterior a qualquer modificação introdozida pela versão 3. Diante deste cenário, só prossiga com a execução deste checklist após certificar-se que essa configuração está ativa.

## Seção I - Autenticação
### Contexto
A área de autenticação em um sistema desempenha um papel crucial ao verificar a identidade dos usuários que buscam acesso. Seu propósito fundamental é garantir a segurança, prevenindo acessos não autorizados por meio da validação de credenciais, como nomes de usuário e senhas. Além de proteger informações sensíveis, a autenticação contribui para a rastreabilidade das atividades do usuário, fortalecendo a integridade do sistema e assegurando que apenas usuários legítimos possam interagir com suas funcionalidades e dados.

### Itens de verificação

#### Item I - Criação e ativação de conta

**Valida:** O fluxo de cadastro de novas contas na aplicação, bem como o envio de e-mails pela aplicação.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Na tela de cadastro, preencha corretamente os campos (incluindo o aceite dos termos de uso) e clique no botão `Cadastrar`  | É esperado que seja enviado um e-mail de ativação para o e-mail inserido durante o cadastro | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
2 | Clique no link enviado ao e-mail, para ativação da conta | É esperado que a conta seja ativada com sucesso | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

#### Item II - Recuperação de senha

**Valida:** Se o fluxo de recuperação e reset de senhas está funcionando corretamente

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Na tela inicial, clique no link `Esqueceu sua senha?`, preencha o e-mail informado na hora do cadastro e clique no botão `Enviar` | É esperado que seja enviado um e-mail de recuperação de senhas, para o e-mail informado | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
2 | Atualize a senha a partir do link recebido no e-mail | É esperado que a senha seja atualizada com sucesso | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

#### Item III - Login na aplicação

**Valida:** O fluxo de login na aplicação, bem como seleção do perfil e acesso ao sistema no perfil público.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Na tela inicial, preencha os campos de login e senha conforme dados informados no momento do cadastro | É esperado que o usuário seja redirecionado para a tela de seleção de perfil | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
2 | Na tela de seleção de perfil, selecione um perfil e prossiga com o login clicando no botão com o logo do sistema `Geopixel Cidades` | É esperado que apareça, no mínimo, um perfil a ser selecionado e que o usuário ao clicar no botão com o logo do sistema `Geopixel Cidades` seja autenticado e redirecionado à tela principal da aplicação (mapa). | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
3 | Voltando a tela de login, clique no botão `Acesso público` | É esperado que o usuário seja redirecionado à tela principal da aplicação, com funções reduzidas e perfil anônimo | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

## Seção II - Visualização de feições
### Contexto
A capacidade de visualizar geometrias desempenha um papel essencial em nosso sistema, sendo fundamental para a compreensão e análise de dados espaciais. A visualização de geometrias permite que os usuários observem e interpretem mapas, camadas e informações geoespaciais de maneira intuitiva, facilitando a tomada de decisões informadas. Essa funcionalidade é crucial para diversos setores, como planejamento urbano, gestão ambiental e análise de recursos naturais. Ao proporcionar uma representação visual precisa do ambiente geográfico, a visualização de geometrias no `Geopixel Cidades` não apenas simplifica a interpretação de dados complexos, mas também permite a identificação de padrões, tendências e relações espaciais, contribuindo significativamente para o processo de análise e tomada de decisões estratégicas.

### Itens de verificação
#### Item I - Visualização de feições
**Valida:** Configuração do Geoserver, recuperação e apresentação de geometrias persistidas no banco de dados, seguindo os estilos definidos.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, percorra a barra lateral esquerda e clique no ícone que se refere à `Temas disponíveis`. Diante disso, ative todos os temas disponíveis, mudando o *checkbox* para a posição ativa. Após isso, na barra lateral esquerda, clique no ícone que se refere à `Mapas` e percorra a lista dos temas, ativando um a um. (Se necessário, ajustar o nível de zoom do mapa para que o tema fique visível) | É esperado que os temas sejam ativados e desativados com sucesso e que, para todos os temas, seja possível recuperar as feições persistidas no banco, podendo visualizá-las em tela. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

## Seção III - Persistência, recuperação, atualização e deleção de feições
### Contexto
A funcionalidade CRUD (Create, Read, Update, Delete) de geometrias no sistema `Geopixel Cidades` desempenha um papel crucial na gestão eficiente e dinâmica de dados espaciais. Permitindo a criação, leitura, atualização e exclusão de geometrias, essa capacidade oferece flexibilidade para a manipulação contínua de informações geográficas. Ao criar novas geometrias, os usuários podem incorporar dados atualizados ao sistema, refletindo mudanças no ambiente geográfico. A leitura facilita a visualização e análise dessas geometrias, enquanto a atualização possibilita ajustes precisos de informações. A capacidade de exclusão é essencial para manter a integridade dos dados, removendo geometrias obsoletas ou incorretas.

### Itens de verificação
#### Item I - Criação de feições
**Valida:** Geração de dados geométricos e tabulares, e persistência destes no banco de dados.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, ative o tema mais utilizado. Em seguida, defina-o como tema corrente ao clicar sobre o seu nome, no menu de `Mapas`. Com isso, na barra lateral direita, ative as ferramentas de edição (botão `Habilitar edição`, representado por um ícone de lápis). Prosseguindo, crie uma feição e a persista, clicando com o botão direito ao fim da edição. (Repite estes passos para os três temas mais utilizados no sistema) | É esperado que as feições sejam persistidas no banco de dados com sucesso. Uma mensagem de sucesso deverá ser retornada ao usuário. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

#### Item II - Recuperação e atualização de feições
**Valida:** Recuperação dos dados gerados no passo anterior, bem como atualização de suas informações.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, ative um dos temas utilizado no passo anterior. Em seguida, defina-o como tema corrente ao clicar sobre o seu nome, no menu de `Mapas`. Com isso, na barra lateral direita, ative a ferramenta de seleção (botão `Ferramenta de seleção`, representado por um ícone de cursor de *mouse*). Prosseguindo, clique na feição recém criada. | É esperado que a feição recém criada seja recuperada, e suas informações sejam mostradas em tela. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
2 | Prosseguindo, com a feição selecionada e a tela de detalhes aberta, clique no ícone de lápis para abrir a edição de seus atributos (ícone que está no escopo do componente de detalhes). Altere alguns atributos e clique em `Salvar alterações`. | É esperado que as informações tabulares sejam atualizadas com sucesso. Uma mensagem de sucesso deverá ser retornada ao usuário. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
3 | Ato contínuo, ainda com o tema habilitado como corrente, feche a tela de detalhes e habilite as ferramentas de edição no menu lateral direito (botão `Habilitar edição`, representado por um ícone de lápis). Faça alguma alteração na geometria da feição em questão, como curva, mover vértice, mover ponto etc (exceto deletar). | É esperado que a alteração na geometria seja concluída com sucesso e que uma mensagem de sucesso seja retornada ao usuário. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

**OBS.: Repetir os passos acima para os três temas mais utilizados no sistema.**

#### Item III - Deleção de feições
**Valida:** Expiração de feições no banco de dados.
Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, ative um dos temas utilizado no passo anterior. Em seguida, defina-o como tema corrente ao clicar sobre o seu nome, no menu de `Mapas`. Com isso, na barra lateral direita, ative a ferramenta de seleção (botão `Ferramenta de seleção`, representado por um ícone de cursor de *mouse*). Prosseguindo, clique na feição a ser deletada. Na tela de detalhes, clique no ícone de um lápis. Percorra a tela até o final e clique no botão `Deletar feição`. | É esperado que a feição seja expirada no banco e não fique mais disponível para futuras interações. Uma mensagem de sucesso na exclusão é esperada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

**OBS.: Repetir o passo acima para os três temas mais utilizados no sistema.**

## Seção IV - Formulários
### Contexto
Os formulários desempenham um papel crucial no contexto do sistema `Geopixel Cidades`, proporcionando uma maior flexibilidade e capacidade de modificação sem a necessidade imediata de implementar novas funcionalidades. Essa funcionalidade permite aos usuários adaptar e personalizar a interação com o sistema de acordo com as necessidades específicas, otimizando a experiência do usuário. Com os formulários, é possível coletar e processar dados de maneira eficiente, ajustando a entrada de informações de acordo com os requisitos em constante evolução. Isso não apenas simplifica a interação, mas também oferece uma abordagem ágil para aprimorar a usabilidade do sistema, atendendo às demandas dinâmicas sem a necessidade de extensas alterações de código. Em suma, os formulários no sistema `Geopixel Cidades` representam uma ferramenta fundamental para a adaptação contínua, promovendo uma maior agilidade e personalização sem comprometer a estabilidade do sistema.

#### Item I - CRUD em formulários
**Valida:** Se os formulários estão totalmente operacionais e se operações de CRUD através deles estão sendo realizadas com sucesso. Para este item, pressupõe-se que os formulários estejam corretamente cofigurados na tabela `app_form` e os botões na tabela `app_buttons`.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, se dirigir ao formulário para teste. Preencher as informações que o formulário precisa e em seguida, tentar persistí-las no banco. | É esperado que os dados informados sejam persistidos no banco de dados com sucesso | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

**OBS.: Repetir este passo para os três formulários mais utilizados no sistema.**

## Seção V - Busca rápida

### Contexto
A busca rápida no sistema `Geopixel Cidades` é essencial para a eficiência operacional, oferecendo aos usuários uma maneira ágil e intuitiva de localizar informações específicas. Com buscas em temas pré-definidos e formatação automática de valores na caixa de pesquisa através dos domínios, essa funcionalidade proporciona acesso rápido a dados relevantes, aprimorando a experiência do usuário em um ambiente dinâmico.

### Itens de verificação
#### Item I - Busca rápida simples
**Valida:** O mecanismo de busca rápida

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, localizar a barra de busca rápida. Ela lista os temas que são passíveis de busca, bem como ordena pelos temas mais utilizados. | É esperado que sejam retornados resultados para busca rápida, ou uma mensagem clara caso não houverem correspondências. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

#### Item II - Busca rápida com domínio
**Valida:** A aplicação de domínios durante a busca rápida

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, localizar a barra de busca rápida e selecionar um tema para realizar a busca. Verificar dentre os atributos que podem ser pesquisáveis, se há algum que se utiliza de domínios (normalmente CEP, CPF, CNPJ etc). Digitar um valor correspondente para determinado atributo e realizar a busca. | É esperado que durante a inserção dos dados no campo de busca, os dados sejam automaticamente formatados para determinado domínio, e que sejam retornados resultados para busca rápida, ou uma mensagem clara caso não houverem correspondências. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

**OBS.: Realizar o teste com os três temas mais pesquisados na busca rápida da cidade. Se um tema possuir mais de um domínio configurado, testar para todos os domínios disponíveis naquele tema.**

## Seção VI - Anexação e recuperação de documentos

### Contexto
A capacidade de anexar e recuperar documentos diversos no sistema `Geopixel Cidades` desempenha um papel crucial ao facilitar a organização e o acesso eficiente a informações relevantes a temas e feições. Essa funcionalidade permite aos usuários associar documentos específicos a feições, enriquecendo sua contextualização. Além disso, a recuperação fácil de documentos anexados simplifica a revisão de informações relacionadas, contribuindo para uma tomada de decisões informada.

### Itens de verificação

#### Item I - Anexar documentos

**Valida:** A anexação de documentos à feições do sistema.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, clique no ícone de `Mapas`, no menu lateral esquerdo, para listar os temas habilitados. Dentre os temas listados, clique com o botão **direito** sobre o nome de algum, e em seguida clique em `Ver tabela`. Serão listadas as feições correspondentes aquele tema, portanto selecione uma pelo checkbox e clique no botão `Detalhes` que se encontra no rodapé do componente de consulta. Será aberto o componente de detalhes da feição. Neste contexto, clique no ícone que é representado por um clipe de papel. Será aberta a tela de anexos de uma feição. Nesta tela, clique ou arraste o documento a ser anexado no campo designado. Selecione também o tipo do documento a ser anexado e em seguida clique em `Anexar arquivo` | É esperado que o documento seja anexado e vinculado aquela feição com sucesso. Uma mensagem de sucesso é esperada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

#### Item II - Recuperação e visualização de documentos

**Valida:** A recuperação e visualização de documentos vinculados à feições do sistema.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Ato contínuo, o documento recém anexado deve aparecer listado nesta mesma interface. Diante deste cenário, clique sobre o nome do documento. | É esperado que o documento seja aberto e que seja possível a sua visualização. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

## Seção VII - Importação e exportação

### Contexto
A capacidade de importar e exportar geometrias nos formatos DXF, DWG, KML e ShapeFile em nosso sistema `Geopixel Cidades` desempenha um papel essencial ao proporcionar uma interoperabilidade robusta e flexibilidade na manipulação de dados geoespaciais. Essa funcionalidade permite a integração eficiente com outras plataformas e ferramentas, promovendo uma colaboração mais ampla e facilitando a troca de informações entre diferentes sistemas. A importação de geometrias possibilita a incorporação de dados externos, enriquecendo a base de informações do sistema, enquanto a exportação oferece a capacidade de compartilhar dados de maneira padronizada e amplamente reconhecida.

### Itens de verificação

#### Item I - Exportação de arquivos

**Valida:** A exportação de arquivos através do sistema.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, acesse o ícone `Geral` na barra lateral esquerda. Dentre as opções disponíveis no menu que se abriu, selecione `Exportar`. Preencha as informações necessárias e clique em `Exportar` para exportar um arquivo `Shapefile`. | É esperado que seja exportado um arquivo `Shapefile` com sucesso, dados os inputs de entrada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
2 | Ato contínuo, siga os mesmos passos e exporte um arquivo no formato `DWG`. | É esperado que seja exportado um arquivo `DWG` com sucesso, dados os inputs de entrada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
3 | Ato contínuo, siga os mesmos passos e exporte um arquivo no formato `DXF`. | É esperado que seja exportado um arquivo `DXF` com sucesso, dados os inputs de entrada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
4 | Ato contínuo, siga os mesmos passos e exporte um arquivo no formato `KML`. | É esperado que seja exportado um arquivo `KML` com sucesso, dados os inputs de entrada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

#### Item II - Importação de arquivos

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, acesse o ícone `Geral` na barra lateral esquerda. Dentre as opções disponíveis no menu que se abriu, selecione `Importar`. Preencha as informações necessárias e importe um arquivo no formato `Shapefile`. Clique em `Importar`. | É esperado que seja importado um arquivo `Shapefile` com sucesso, criando assim feições a partir das informações contidas no arquivo de importação. Se espera uma mensagem de sucesso. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
2 | Ato contínuo, siga os mesmos passos e importe um arquivo no formato `DWG`. | É esperado que seja importado um arquivo `DWG` com sucesso, criando assim feições a partir das informações contidas no arquivo de importação. Se espera uma mensagem de sucesso. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
3 | Ato contínuo, siga os mesmos passos e importe um arquivo no formato `DXF`. | É esperado que seja importado um arquivo `DXF` com sucesso, criando assim feições a partir das informações contidas no arquivo de importação. Se espera uma mensagem de sucesso. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
4 | Ato contínuo, siga os mesmos passos e importe um arquivo no formato `KML`. | É esperado que seja importado um arquivo `KML` com sucesso, criando assim feições a partir das informações contidas no arquivo de importação. Se espera uma mensagem de sucesso. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |


## Seção VIII - Publicação de temas

### Contexto
A entidade formada por um mapa e uma tabela, que armazena as informações textuais, é chamada TEMA. A capacidade de publicar TEMAS, a partir de um arquivo TXT que segue padrões pré-determinados em nosso sistema é fundamental para a disseminação eficiente de dados geoespaciais. Essa funcionalidade permite a criação de conjuntos de informações estruturadas e padronizadas, facilitando a compartilhamento consistente de dados entre diferentes usuários e sistemas. Ao utilizar um formato de arquivo TXT seguindo padrões estabelecidos, promovemos a interoperabilidade e a integração de dados, garantindo que as informações sejam compreendidas de maneira consistente. A publicação de TEMAS não apenas simplifica o processo de disponibilização de dados geoespaciais, mas também contribui para a colaboração efetiva.

### Itens de verificação

#### Item I - Publicação de um tema

**Valida:** A publicação correta de temas, tabelas necessárias, atributos, mapas, permissões, parâmetros em nosso sistema.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, no menu lateral esquerdo, clique no ícone de `Publicar tema`, representado por um livro aberto, com uma página clara e outra escura. Arraste ou clique para importar o arquivo TXT que será utilizado na publicação do tema em questão, e em seguida clique em `Aplicar`. | É esperado que o tema seja publicado com sucesso. Se espera também uma mensagem de sucesso e que a página recarregue para que a lista de temas seja atualizada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
2 | Logado no sistema, na aba de busca rápida, procure dentre os temas disponíveis para busca. | É esperado que o tema recém importado esteja listado dentre os temas do sistema, bem como deve ser possível realizar uma busca rápida a partir de sua chave primária configurada no arquivo TXT. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |
3 | Logado no sistema, no menu lateral esquerdo, clique no ícone de `Temas disponíveis`. | É esperado que o tema esteja listado dentre os temas disponíveis do sistema. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

## Seção IX - Certidões e notificações

### Contexto
A geração automatizada de certidões municipais e notificações em PDF, com base em templates no formato JSON em nosso sistema, é essencial para fornecer informações certificadas de maneira eficiente e padronizada. Essa funcionalidade não apenas agiliza processos burocráticos, mas também assegura a conformidade com requisitos normativos, contribuindo para a transparência e confiabilidade das informações fornecidas pelo sistema.

### Itens de verificação

#### Item I - Emissão de certidões e impressão do mapa
**Valida:** Emissão de certidões no sistema

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, clique no ícone `Mapas` no menu lateral esquerdo. Dentre os temas disponíveis, selecione algum que possua certidões configuradas e clique com o botão direito sobre o nome do tema, em seguida clicando em `Ver tabela`. Selecione uma feição na lista, e clique no botão `Certidão`. Selecione uma certidão e em seguida clique no botão `Gerar`. | É esperado que seja gerada a certidão selecionada, com todas as informações que seu respectivo arquivo JSON estipula. O arquivo deve ser baixado pelo navegador no momento em que o usuário clicar em `Gerar` | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |


#### Item II - Emissão de notificações
**Valida:** Emissão de notificações através do sistema

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, clique no ícone `Geral` no menu lateral esquerdo. Dentre as opções disponíveis, clique no botão de `Notificações`. Preencha as informações necessárias e clique no botão `Gerar` | É esperado que seja gerada a(s) notificação(ões) com base nos parâmetros de entrada, contendo todas as informações que seu respectivo arquivo JSON estipula. O arquivo deve ser baixado pelo navegador no momento em que o usuário clicar em `Gerar`. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

## Seção X - Memorial descritivo

### Contexto
A capacidade do nosso sistema de gerar memoriais descritivos de lotes e glebas é de importância fundamental para a documentação precisa e legalmente válida de propriedades. Essa funcionalidade permite a criação automatizada de documentos detalhados que descrevem as características específicas de cada lote ou gleba, incluindo limites, dimensões, coordenadas, azimutes, elevação e outros elementos relevantes. Ao fornecer essa documentação de forma padronizada, contribuímos para a transparência e conformidade com normas legais e regulatórias. A emissão de memoriais descritivos não apenas simplifica processos administrativos, mas também fortalece a segurança jurídica das propriedades, garantindo que as informações estejam registradas de maneira clara e precisa.

### Itens de verificação

#### Item I - Emissão de memorial descritivo

**Valida:** A emissão de memoriais descritivos em nosso sistema

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, clique no ícone `Geral` no menu lateral esquerdo. Dentre as opções disponíveis, clique em `Memorial descritivo`. Preencha os campos necessários para geração do memorial. No tema principal, é interessante escolher um tema que faça alusão à lote, quadra ou glebas. No tema de logradouro, normalmente é atribuído Logradouro ou Vias como tema. E como tema auxiliar, escolher algum ao critério do usuário. Na interface principal de geração do memorial descritivo, marque todas as opções disponíveis em `Parâmetros` e após isso clique no botão `Gerar`. | É esperado que após o tempo de processamento, um arquivo referente ao memorial descritivo em questão seja baixado. Diante disto, analisar o arquivo gerado a fim de identificar se as informações de input correspondem ao que foi gerado no arquivo. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

## Seção XI - PGV

### Contexto
A capacidade do nosso sistema de realizar simulações de cálculos de impostos e gerar plantas genéricas de valores é de suma importância para fornecer aos usuários ferramentas poderosas na gestão financeira e planejamento tributário. Essa funcionalidade permite que os usuários avaliem antecipadamente o impacto fiscal de determinadas transações, contribuindo para a tomada de decisões informadas. Além disso, a geração de plantas genéricas de valores simplifica a visualização e análise de informações financeiras, facilitando a compreensão de dados complexos.

### Itens de verificação

#### Item I - Geração do cálculo PGV

**Valida:** Execução do cálculo da Planta Genérica de Valores pelo sistema

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, clique no ícone do módulo de `PGV`, no menu lateral esquerdo, representado por uma imagem de uma mão segurando um cifrão. Preencha os campos necessários ou recupere uma simulação já salva no sistema. Clique no botão `Executar`. | É esperado que seja realizado o cálculo da planta genérica de valores com sucesso. Uma mensagem de sucesso também é esperada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

## Seção XII - Temáticos

### Contexto
A capacidade do nosso sistema em gerar mapas temáticos, incluindo mapas de calor, de proximidade, agrupamento, etiquetas, entre outros, é de extrema importância para a visualização e interpretação eficaz de dados geoespaciais. Essa funcionalidade proporciona aos usuários uma ferramenta valiosa para representar padrões e tendências de forma intuitiva, facilitando a análise e compreensão de informações complexas. 

### Itens de verificação

#### Item I - Geração de mapas de calor

**Valida:** Geração de mapas de calor pelo nosso sistema.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, cliqe no ícone de `Temáticos` no menu lateral esquerdo, representado por uma imagem de um globo terrestre. Dentre as opções disponíveis, clique em `Mapa de calor`. Preencha com as informações necessárias à geração e por fim clique no botão `Gerar`. | É esperado que o mapa de calor seja gerado com sucesso e renderizado no mapa. Uma mensagem de sucesso também é esperada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

#### Item II - Geração de mapas de agrupamento

**Valida:** Geração de mapas de agrupamento pelo nosso sistema.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, cliqe no ícone de `Temáticos` no menu lateral esquerdo, representado por uma imagem de um globo terrestre. Dentre as opções disponíveis, clique em `Mapa de agrupamento`. Preencha com as informações necessárias à geração e por fim clique no botão `Gerar`. | É esperado que o mapa de agrupamento seja gerado com sucesso e renderizado no mapa. Uma mensagem de sucesso também é esperada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

#### Item III - Geração de mapas de seleção

**Valida:** Geração de mapas de seleção pelo nosso sistema.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, cliqe no ícone de `Temáticos` no menu lateral esquerdo, representado por uma imagem de um globo terrestre. Dentre as opções disponíveis, clique em `Seleção`. Preencha com as informações necessárias à geração e por fim clique no botão `Gerar`. | É esperado que o mapa de seleção seja gerado com sucesso e renderizado no mapa. Uma mensagem de sucesso também é esperada. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

## Seção XIII - Panorâmica e Street Viewer

### Contexto
A capacidade do nosso sistema em visualizar fotos panorâmicas de ruas e integrar-se ao Google Street View é fundamental para enriquecer a experiência do usuário e proporcionar uma compreensão mais abrangente do ambiente geográfico. Essa funcionalidade permite que os usuários explorem visualmente locais específicos, oferecendo uma representação virtual detalhada das ruas.

### Itens de verificação

#### Item I - Visualização de panorâmica

**Valida:** Apresentação e visualização de fotos panorâmicas no sistema

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, clique no ícone de `Temas disponíveis`, representado por um livro aberto com uma folha clara e outra escura, e dentre as opções, procure pelo tema de `Panorâmica`. Ative-o e clique no ícone de `Mapas`, representado por dois quadrados sobrepostos. Ative o tema de `Panorâmica` como corrente, bem como sua visualização. Agora, no menu lateral direito, clique no botão `Visão panorâmica`, representado por um ícone de uma imagem panorâmica. Em sequência, clique em um ponto no mapa em que haja uma feição do tema de panorâmica. | É esperado que seja carregada a imagem panorâmica do ponto clicado com sucesso. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

#### Item II - Visualização do Street Viewer

**Valida:** Integração com o Google Street Viewer

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema, clique no ícone de `Google Street View`, no menu lateral direito, representado por um boneco. Clique em uma via do mapa. | É esperado que seja carregada a visualização Street View do ponto clicado com sucesso. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |

## Apêndice

### Itens de verificação na V2

Tendo em vista que o processo de homologação da V3 altera estruturas de algumas tabelas, e que essas tabelas são compartilhadas entre as versões, levantam-se a seguir os itens que necessitarão serem verificados após a homologação da V3, a fim de se certificar que os mesmos continuam operacionais na V2.

#### Item I - Histórico de edição

**Valida:** Histórico de edição está funcional em ambas as versões.

Item | Descrição da ação | Resultado esperado | Atende | Não atende
- | - | - | - | -
1 | Logado no sistema (V2), ative a ferramenta de seleção com um dos temas utilizados na homologação da V3 habilitado como corrente, e selecione uma feição criada durante o teste das ferramentas de edição (vide seção III deste documento). Abra o histórico de edição dessa feição. | É esperado que a aplicação continue funcional e que o log de edição seja renderizado normalmente. | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> | <input type='checkbox' style='width: 100%; height: 100%; display: flex; justify-content: center; align-items: center;'></input> |