---
title: Configuração de acesso SSH
description: Criação de chave SSH e configuração de acesso SSH entre dois hosts
published: true
date: 2024-04-11T13:07:28.060Z
tags: 
editor: markdown
dateCreated: 2023-12-06T15:29:15.027Z
---

# Configuração de acesso SSH
Esse tutorial exemplificará como é configurada uma conexão SSH entre dois hosts.
A configuração demonstrada foi realizada entre os hosts do `GitLab (10.0.200.200)` e `Homologação (10.0.0.146)`, chamados de host de origem e host de destino, respectivamente.

A forma mais comum de estabelecer uma conexão SSH é através de uma chave SSH, neste modelo é gerada um `par de chaves` (chave pública e chave privada) para o host de origem.
A `chave privada` é armazenada no host de origem e **NÃO DEVE SER COMPARTILHADA**, já a `chave pública` terá de ser adicionada no host de destino, indicando que a conexão SSH desse par de chaves deve ser aceita.

Criação de chave SSH para o host de origem utilizando o algoritmo `ed25519`:
![1-criacao-chave-ssh-ed25519-hosta.png](/1-criacao-chave-ssh-ed25519-hosta.png)

Altere os parâmetros conforme necessidade:
> ssh-keygen -t ed25519 -f ~/.ssh/to_access_homolog_ed25519 -C "Chave SSH criada para acesso à máquina de homolog IP 10.0.0.146"

Parâmetros:
- **-t** - Algoritmo utilizado para geração do par de chaves SSH.
- **-f** - Caminho onde o par de chaves será armazenado.
- **-C** - Comentário opcional para adicionar uma anotação semântica às chaves.

PS.: O *passphrase* pode ser definido como vazio, como sugerido no prompt.

A chave pública deve ser copiada para ser adicionada no host de destino:
![2-chave-publica-copiada-hosta.png](/2-chave-publica-copiada-hosta.png)

Copie seu valor com o comando:
> cat ~/.ssh/to_access_homolog_ed25519.pub

No host destino, a chave pública deve ser adicionada ao arquivo `authorized_keys`, comumente localizado no diretório `.shh` do usuário utilizado.
Neste exemplo, o usuário `root` será utilizado na conexão, e o arquivo editado se encontrava em `/root/.ssh/authorized_keys`.
Basta copiar todo o conteúdo da chave pública para uma nova linha deste arquivo:
![3-copia--chave-publica-hostb.png](/3-copia--chave-publica-hostb.png)

Para abrir o arquivo para configuração, use:
> nano /root/.ssh/authorized_keys

O host de destino deve estar configurado para aceitar conexões SSH via chave pública, para isso basta especificar a chave-valor `PubkeyAuthentication yes`:
![4-config-permitir-acesso-chave-publica-hostb.png](/4-config-permitir-acesso-chave-publica-hostb.png)

Para abrir o arquivo para ajuste, use:
> nano /etc/ssh/sshd_config

Para que a nova configuração seja reconhecida, é necessário reiniciar o serviço SSH do host de destino, utilize o comando:
> service ssh restart

![5-restart-servico-ssh-hostb.png](/5-restart-servico-ssh-hostb.png)

Por fim, devemos fazer um teste de conexão SSH a partir do host de origem utilizando a chave SSH gerada e configurada para o host de destino.
Utilize o comando `ssh` de forma análoga a esta chamada:
> ssh -i ~/.ssh/to_access_homolog_ed25519 root@10.0.0.146

![6-acesso-ssh-chave-especifica-hosta.png](/6-acesso-ssh-chave-especifica-hosta.png)

Parâmetros:
- **-i** - Caminho da chave privada gerada configurada para a conexão.
- **\<usuario>@\<host-destino>** - Usuário do host de destino utilizado, seguido do IP do host de destino.

## Utilização da Chave SSH na Pipeline
A Pipeline do GitLab espera que a chave privada esteja na pasta */opt/docker-public* do host de origem, para conseguir utilizá-la na realização de uma conexão SSH.
Para isso, copie a chave privada gerada com o comando a seguir:
> cp ~/.ssh/to_access_homolog_ed25519 /opt/docker-public/