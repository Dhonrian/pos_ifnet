---
title: Certidões
description: Artefato para implantação de certidões
published: true
date: 2025-05-19T13:57:09.462Z
tags: implantação, artefato, artefatos, certidões, certidão, negócios
editor: markdown
dateCreated: 2023-11-07T13:48:13.383Z
---

# Artefato para certidões

Esse artigo será utilizado para referenciar o padrão de artefato que deverá ser utilizado ao solicitar a implantação de uma certidão para a Implantação Técnica.

<blockquote class="is-info">
<p>Deverão ser enviados sempre 2 arquivos em PDF: 1 arquivo sem nenhum comentário ou marcação e um arquivo com os devidos comentários e as devidas marcações.</p>
</blockquote>


## Passo a passo para produção do artefato

O arquivo poderá ser criado em qualquer ferramenta de texto (Word online, LibreOffice, etc.), pois o envio do arquivo como PDF garante que ele seja aberto e visualizado da mesma maneira para todos. Após criar sua certidão, **sem grifar ou fazer comentários** salve em formato PDF, certifique-se que o arquivo ficou salvo na forma que você deseja, verifique a quantidade de páginas, alinhamentos etc. Após revisão, esse será o primeiro arquivo a ser enviado para a implantação. Esse envio garante um PDF limpo de distorões entre um arquivo e outro, ou com interferência dos comentários atravessando os textos. A seguir um exemplo de Elias Fausto de como o PDF limpo deve vir:

![image_55723890331695753104494.png](/image_55723890331695753104494.png)

Após gerar o PDF, esse será o primeiro arquivo anexo no formulário de solicitação da implantação de certidão. O segundo documento enviado será o PDF grifado e comentado. Para fazer essas marcações iremos utilizar o PDF no **Edge**, pois não precisa de instalação, é fácil de utilizar, atende as necessidades e conseguimos padronizamos a forma como o dado será visualizado. Assim, utilizaremos a cor **AZUL** para informações que virão de forma automática e **AMARELO** para atributos que serão preenchíveis. Como na imagem a seguir:

![image_72753443721699440512143.png](/image_72753443721699440512143.png)

Após as marcações, deverão ser inseridos os comentário. Clicando com o botão direito do mousse a caixa de diálogo abrirá a opção de criar um comentário, assim como é feito nos documentos de texto. 

<blockquote class="is-info">
<p>Para o atributo automático, o texto do comentário deverá conter: o tema, do qual o atributo deverá ser puxado; o atributo em si; qualquer observação pertinente, conforme será exemplificado abaixo.</p>
</blockquote>

![image_96641347531699441055148.png](/image_96641347531699441055148.png)
![image_77307008041699441129447.png](/image_77307008041699441129447.png)


Para o atributo preenchível deverá ser inserido o nome que o campo deve ter na caixa de geração da certidão e o tipo que ele será. No caso de uma informação manual ele poderá ser do tipo texto (que engloba números também) **ou** selectlist. No caso do selectlist, deverão ser indicadas as opções de seleção, conforme imagem abaixo:

![image_98433461951699441275920.png](/image_98433461951699441275920.png)

Após comentar e grifar todos os campos necessários, salve o documento. Após salvar, o documento deverá ser anexo à solicitação de implantação da certidão.

Para solicitação da certidão deverá ser utilizado o [Formulário de Implantação](https://geopixel.movidesk.com/kb/form/7529/), definindo o serviço como SIGWeb e a categoria como Certidão.

![imagetools0.png](/imagetools0.png)

Na descrição do chamado deverão ser incluídas as seguintes informações **obrigatórias**, sem as quais **o card não será executado** na sprint: Perfil, Tema, Botão, Observações. Um exemplo do texto que deverá ser utilizado para solicitar a certidão:

**Perfil:** Administrador
**Tema:** Cadastro Imobiliário
**Botão:** Pop-up e resumo
**Observações:** Fonte principal Verdana, tamanho geral 12. Campo logradouro justificado. Inserir a marca d'agua anexa.

![image_77050151291695756229538.png](/image_77050151291695756229538.png)

> Em caso de marca d'água, um arquivo em formato png ou jpeg deverá ser anexo **separadamente**, no mesmo card.
{.is-warning}

## Checklist de anexos

- [x] Arquivo em PDF em branco e sem comentários;
- [x] Arquivo em PDF, **editado no Edge**, com grifos e comentários;
- [x] Texto informativo com perfil, tema, botão e observação, a ser inserido no campo "Descrição" do Formulário de Implantação;
- [x] Arquivo JPEG ou PNG, caso haja marca d'água.


