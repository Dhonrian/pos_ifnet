---
title: Componentes de cadastro imobiliário
description: Documento contendo o levantamento dos componentes que serão necessários serem implementados para o funcionamento do módulo de Cadastro Imobiliário
published: true
date: 2023-10-10T14:48:29.426Z
tags: cadastro imobiliário formulários
editor: markdown
dateCreated: 2023-10-10T14:48:27.465Z
---

## Levantamento de tags a serem implementadas no módulo de cadastro imobiliário

- Tag `"btn_update"`:
	- Necessário implementar os botões abaixo, que compõem a tag `btn_update`:
	- Botão `"changeGeom"`:
		- Reponsável por: O `changeGeom` é um botão que é configurado através da tag btn_update, porém que não é renderizado em tela, mas é responsável por aplicar algumas regras de negócio aos formulários. Neste caso, se o `changeGeom` estiver setado como `true`, significa que a geometria também será atualizada (neste caso a aplicação faz mais sentido para temas vesgos, onde pode se desejar, ou não, atualizar a geometria correspondente)
	- Botão `"expireDate"`:
		- Reponsável por: O `expireDate` é um botão que é configurado através da tag btn_update, porém que não é renderizado em tela, mas é responsável por aplicar algumas regras de negócio aos formulários. Neste caso, se o `expireDate` estiver setado como `true`, ao persistir a informação do formulário, a feição original será expirada e será gerado um novo ID para aquela feição. (Basicamente é o fluxo padrão da atualização de dados na v3. Na atualização, o dado antigo é expirado e é inserido um novo dado com as informações atualizadas)
	- Botão `"history"`:
		- Responsável por: O `history` é um botão que é configurado através da tag btn_update, porém que não é renderizado em tela, mas é responsável por aplicar algumas regras de negócio aos formulários. Neste caso, se o `history` estiver setado como `true`, ao persistir a informação do formulário, esta inserção/atualização/deleção será registrada na tabela `app_log`. (No nosso caso, todos estes fluxos já são registrados automaticamente, pois são disparados através dos métodos `insertData`, `updateData` e `deleteData` da classe `DataService.java`)
	- Botão `"buttonAssociar"`:
		- Responsável por: Associar determinado formulário a algum usuário cadastrado no sistema. Este botão existe no contexto de Manutenção de Sepulturas, Obras Públicas - Vistoria, etc. Na v2, é aberto um novo modal com um `selectList` solicitando que se escolha um usuário a ser associado. Após isto o modal é fechado e o usuário associado ao formulário original que está sendo preenchido.
- Tag `"log"`:
	- Necessária a implementação da tag `log`.
	- Reponsável por: Registar informações relevantes ao log de edição. Ela possui campos e inputs específicos e usados na persistência dos dados na tabela de log de edição. Estes campos deverão somente ser renderizados caso o botão `history` estiver setado como `true`
	- No formulário de Cadastro Imobiliário, a tag contém os componentes de input, selectlist, textarea, etc.
- Tag `"execute"`:
	- Necessária a implementação da tag `execute`
	- Responsável por: Executar códigos JavaScript que forem determinados dentro desta tag, como por exemplo:
	- ``` "execute": "(
		function() {
			if ($('#inscricao')[0].value.length<=0) {
					functionSpecific.creteSomePointByPopUp();
					functionSpecific.getDataByGeom(undefined,1018,'codigo,id,area,qdr_id','inscricao,lte_id,area_lote_geo,qdr_id');
					$('#inscricao').val($('#inscricao').val().substring(0,18)+'.9999');
			} else {
				functionSpecific.serchCEP($('#lte_id')[0].value,1018,'qdr_id,area','id','qdr_id:qdr_id/area_lote_geo:area');
				functionSpecific.serchCEP($('#inscricao')[0].value,2342,'area_desenho','inscricao','area_edif_geo:area_desenho');
				functionSpecific.serchCEP($('#inscricao')[0].value,2343,'area_desenho','inscricao','area_edif_comum_geo:area_desenho');
				$('#area_edif_privativa').val($('#area_edif_pref').val().replace('.','').replace(',','.')-$('#area_edif_comum_pref').val().replace('.','').replace(',','.'));
				$('#area_edif_privativa').val(parseFloat($('#area_edif_privativa').val()).toFixed(2).replace('.',','));
			}
			
			if ($('#bai_id')[0].value.length<=0) {
				functionSpecific.getDataByGeom(undefined,991,'nome,id','tmp_bairro,bai_id');
			} else {
				functionSpecific.serchCEP($('#bai_id')[0].value,991,'nome','id','tmp_bairro:nome');
			}
			
			if ($('#ltm_id')[0].value.length<=0) {
				functionSpecific.getDataByGeom(undefined,993,'nome,id','tmp_nome_loteamento,ltm_id');
			} else {
				functionSpecific.serchCEP($('#ltm_id')[0].value,993,'nome','id','tmp_nome_loteamento:nome');
			}
			
			if ($('#cnd_id')[0].value.length<=0) {
				functionSpecific.getDataByGeom(undefined,1000,'nome,id','tmp_nome_condominio,cnd_id');
			} else {
				functionSpecific.serchCEP($('#cnd_id')[0].value,1000,'nome','id','tmp_nome_condominio:nome');
			}
			
			if ($('#edificio_id')[0].value.length>0) {
				functionSpecific.serchCEP($('#edificio_id')[0].value,1789,'nome_edif','id','tmp_nome_edificio:nome_edif');
			}
				
			if ($('#corr_cnd_id')[0].value.length>0) {
				functionSpecific.serchCEP($('#corr_cnd_id')[0].value,1000,'nome','id','corr_condominio:nome');
			}
			
			if ($('#corr_edificio_id')[0].value.length>0) {
				functionSpecific.serchCEP($('#corr_edificio_id')[0].value,1789,'nome_edif','id','corr_edificio:nome_edif');
			}
			
			if ($('#log_id')[0].value.length>0) {
				functionSpecific.serchCEP($('#log_id')[0].value,285,'logradouro','id','tmp_logradouro:logradouro');
			}

			if ($('#log_id_principal')[0].value.length>0) {
				functionSpecific.serchCEP($('#log_id_principal')[0].value,285,'logradouro','id','logradouro_testada_principal:logradouro');
			}
			
			if ($('#log_id_secundario')[0].value.length>0) {
				functionSpecific.serchCEP($('#log_id_secundario')[0].value,285,'logradouro','id','logradouro_testada_secundaria:logradouro');
			}
			
			if ($('#log_id_curva')[0].value.length>0) {
				functionSpecific.serchCEP($('#log_id_curva')[0].value,285,'logradouro','id','logradouro_testada_curva:logradouro');
			}
			
			$('#area_lote_pref').val($('#area_lote_pref').val());
			$('#area_alodial').val($('#area_lote_pref').val().replace('.','').replace(',','.')-$('#area_marinha').val().replace('.','').replace(',','.'));
			$('#area_alodial').val(parseFloat($('#area_alodial').val()).toFixed(2).replace('.',','));
			
			if ($('#fracao_ideal').val().length<=0) {
				$('#fracao_ideal').val('1,000000')
			}
			
			if ($('#inscricao')[0].value=='.9999') {
				$('#inscricao')[0].value='';
				$('#id')[0].value=''
			}
			
			if ($('#area_marinha')[0].value.length<1) {
				$('#area_marinha')[0].value='0,00';
			}
			
			if ($('#area_edif_privativa')[0].value.length<1) {
				$('#area_edif_privativa')[0].value='0,00';
			}
			
			if ($('#area_edif_comum_pref')[0].value.length<1) {
				$('#area_edif_comum_pref')[0].value='0,00';
			}
			
			let a=document.getElementById('btn-group-popup').children;
			
			for (let a1=0;a1<a.length;a1++) {
				if (a[a1].textContent=='Atualizar') {
					if ( $('#inscricao').val().length>1) {
						$('#inscricao').prop( 'disabled', true );
					}
				}
			}
		}) ()", ```
	- Será necessário implementar jQuery no nosso projeto para garantir a compatibilização
	- A execução destes código se dá somente após a renderização dos componentes de formulário
- Tag `"divisions"`:
	- Dentro das divisions, será necessário implementar algumas tags que o módulo de Cadastro Imobiliário faz uso.
	- Tag `"meta"`:
		- Necessária a implementação da tag `meta`
		- Responsável por: Indicar o nome do formulário. Na v2 essa informação é representada no cabeçalho do modal.
	- Tag `"mask"`:
		- Necessário implementar a função `mask` nos inputs
		- Responsável pela aplicação de máscaras aos valores dos inputs. É possível aplicar máscaras pré-determinadas, ou criá-las via padrão passado como valor da tag.
			- Exemplo: `"mask": "create::0000.000.0000.0000.0000",`  ou `"mask": "set::real",`
		- Como foi desenvolvido na v2: O motor de aplicação de máscara na v2, no caso dos formulários, se encontra no arquivo `interpreter.js`. Verificar os métodos `__insertMask__`, `__createMask__` etc.
		- Padrões pré-definidos na v2: Os padrões pré-definidos que deverão também serem implementados na v3 se encontram dentro do `maskDictionary` , na classe `interpreter.js`
	- Implementar validação dos componentes `required` dentro do contexto dos formulários. Se houverem elementos que estão anotados como `required`, não permitir o envio do formulário, bem como explicitar quais campos faltaram preenchimento.
	- Implementar componente `checkbox`
		- Responsável por: Realizar a seleção de um ou mais itens listados dentro de um formulário.
		- Exemplo: 
		- ```{"checkbox": "Mesmo endereço do imóvel", "id": "check-userTerm", "attributes": [ "onclick=(function(){if($('#check-userTerm')[0].checked){functionSpecific.copyValueById(document.getElementById('corr_logradouro'),'tmp_logradouro');functionSpecific.copyValueById(document.getElementById('corr_log_id'),'log_id');functionSpecific.copyValueById(document.getElementById('corr_numero'),'imo_numero');functionSpecific.copyValueById(document.getElementById('corr_complemento'),'imo_complemento');functionSpecific.copyValueById(document.getElementById('corr_bloco'),'imo_bloco');functionSpecific.copyValueById(document.getElementById('corr_condominio'),'tmp_nome_condominio');functionSpecific.copyValueById(document.getElementById('corr_cnd_id'),'cnd_id');functionSpecific.copyValueById(document.getElementById('corr_edificio'),'tmp_nome_edificio');functionSpecific.copyValueById(document.getElementById('corr_edificio_id'),'edificio_id');functionSpecific.copyValueById(document.getElementById('corr_cep'),'imo_cep');functionSpecific.copyValueById(document.getElementById('corr_bairro'),'tmp_bairro');$('#corr_cidade').val('São Sebastião');$('#corr_uf').val('SP');$('#corr_pais').val('Brasil');}else{ $('#corr_logradouro').val('');$('#corr_log_id').val('');$('#corr_numero').val('');$('#corr_comlemento').val('');$('#corr_bloco').val('');$('#corr_condominio').val('');$('#corr_cnd_id').val('');$('#corr_edificio').val('');$('#corr_edificio_id').val('');$('#corr_cep').val('');$('#corr_bairro').val('');$('#corr_cidade').val('');$('#corr_uf').val('');$('#corr_pais').val('');$('#corr_complemento').val('');}})()"], "width": 100}```

## Levantamento dos botões a serem implementados no módulo de cadastro imobiliário

### Botões do tema de `Imóvel`
- Os botões abaixo referem-se ao tema de `imóvel` (que seria o core do módulo de Cadastro Imobiliário na cidade de São Sebastião). Diante disto, temos que garantir que todos estes botões estejam implementados e com seus comportamentos funcionais.

|id|tma_id|btn_id|btn_function|btn_hint|btn_image_path|btn_name|tela|chave|btn_class|visible|
|---|---|---|---|---|---|---|---|---|---|---|
|1742|1021|btn-updategeometry|`infoProperty.selectOperation(infoProperty.idModalNome,'update');`|upadate geometrias de edição||Atualizar|edição|update|btn btn-info|1|
|1744|1021|btn-savegeometry|`infoProperty.selectOperation(infoProperty.idModalNome,'insert');`|salvar geometrias de edição||Salvar|edição|insert|btn btn-success|1|
|1741|1021|btn-closePopUp|`closeModal(infoProperty.idModalNome);editor.setObservers(editor.typeTool);`|close popUp edição||Fechar|edição|close|btn btn-danger|0|
|1743|1021|btn-deletegeometry|`infoProperty.selectOperation(infoProperty.idModalNome,'delete');`|deletar geometrias de edição||Deletar|edição|delete|btn btn-warning|1|
|1747|1021|botao-view|`uploadFile.buildOptionModal('.pdf',true)`|Visualizar documentos anexados|image/glyphicons/glyphicons/png/glyphicons-63-paperclip.png|`<img src='image/glyphicons/glyphicons/png/glyphicons-63-paperclip.png' width='20' height='20'>`|popup||btn btn-light|14|
|1748|1021|botao-deletar|`uploadFile.buildDel()`|Deletar documentos anexados|image/glyphicons/glyphicons/png/glyphicons-418-disk-remove.png|`<img src='image/glyphicons/glyphicons/png/glyphicons-418-disk-remove.png' width='20' height='20'>`|popup||btn btn-light|17|
|1746|1021|botao-view|`uploadFile.buildOptionModal('.pdf',false)`|Baixar documentos anexados|image/glyphicons/glyphicons/png/glyphicons-415-disk-save.png|`<img src='image/glyphicons/glyphicons/png/glyphicons-415-disk-save.png' width='20' height='20'>`|popup||btn btn-light|15|
|2359|1021|btn-certidao|`certidao.buildModal('popup')`|Mostra certidões disponíveis|image/glyphicons/glyphicons/png/doc.png|`<img src='image/glyphicons/glyphicons/png/doc.png' width='20' height='20'>`|popup||btn btn-light|18|
|2415|1021|btn-resume-empreend|`functionSpecific.pushPoolForm();resume.callMe('1374','inscricao',infoProperty.dataPopup[0].inscricao,'','');`|Ver contribuintes associados a este imóvel|image/glyphicons/glyphicons/png/glyphicons-4-user.png|`<img src='image/glyphicons/glyphicons/png/glyphicons-4-user.png' width='20' height='20'>`|popup||btn btn-light|5|
|3651|1021|botao-calculate|`functionSpecific.calculateAreaByIncricao($('#inscricao').val())`|Ajustar áreas das edificações à área total do imóvel||Ajustar Áreas|popup||btn btn-success|17|
|1745|1021|botao-upload|`uploadFile.openModalUpload(this,'1','//opt//disco01//arquivos','1','','');`|Anexar um documento|image/glyphicons/glyphicons/png/glyphicons-416-disk-open.png|`<img src='image/glyphicons/glyphicons/png/glyphicons-416-disk-open.png' width='20' height='20'>`|popup||btn btn-light|16|
|2405|1021|botao-view|`vwers.getLocation(map.getLayersByName('tableFeatures')[0].features[map.getLayersByName('tableFeatures')[0].features.length-1].geometry.getCentroid())`|Foto fachada|image/glyphicons/glyphicons/png/glyphicons-12-camera.png|`<img src='image/glyphicons/glyphicons/png/glyphicons-12-camera.png' width='20' height='20'>`|popup||btn btn-light|7|
|4674|1021|btn-resume-empreend|`functionSpecific.pushPoolForm();resume.loadResume(1000)`|Cadastrar Condomínio|image/glyphicons/glyphicons/png/glyphicons-90-building.png|`<img src='image/glyphicons/glyphicons/png/glyphicons-90-building.png' width='20' height='20'>`|popup||btn btn-light|5|
|4808|1021|botao-naotem|`setTimeout(function(){$('#attr_log_button').remove()}, 500);`|Histórico||Histórico|popup||btn btn-link|6|
|5138|1021|btn-resume-empreend|`functionSpecific.pushPoolForm();resume.loadResume(1374)`|Cadastrar Contribuintes|image/glyphicons/glyphicons/png/glyphicons-44-group.png|`<img src='image/glyphicons/glyphicons/png/glyphicons-44-group.png' width='20' height='20'>`|popup||btn btn-light|5|
|1740|1021|botao-detalhe|`searchNav.showModalDetail();`|Exibe detalhes do item selecionado|image/glyphicons/glyphicons/png/glyphicons-115-list.png|Detalhe|resume|||2|
|1750|1021|botao-atualizar|`functionSpecific.auxLoadDataByMultiplyForm($('#resume-table').bootstrapTable('getSelections')[0].inscricao,1021,1021);`|Atualizar item selecionado|image/glyphicons/glyphicons/png/glyphicons-31-pencil.png|Atualizar|resume|||4|
|1835|1021|botao-mapa|`resume.loadFeatureOnMap(0);`|Navegar para feição selecionada (mapa)|image/glyphicons/glyphicons/png/glyphicons-503-map.png|Mapa|resume|||1|
|2423|1021|botao-novo_item|`functionSpecific.createNewObjectByResume(1021,false,'',true,false);$('#inscricao').val('');$('#id').val('');`|Inserir novo item|image/glyphicons/glyphicons/png/glyphicons-191-circle-plus.png|Inserir|resume|||3|
|4530|1021|botao-certidao|`certidao.buildModal('resume')`|Certidões|image/glyphicons/glyphicons/png/doc.png|Certidões|resume|||3|

- O form de cadastro imobiliário não possui temas aninhados, porém possui um botão de cadastro de contribuinte (vide tabela acima - id `5138`). Diante disso se faz necessário o desenvolvimento de uma estrutura que permita o cadastro de um novo contribuinte e eventual retorno ao formulário original (cadastro imobiliário)

### Botões do tema de `Contribuinte`
- Os botões abaixo referem-se ao tema de `contribuinte` (que faz conexão com o formulário de `Imóvel`). Diante disto, temos que garantir que todos estes botões estejam implementados e com seus comportamentos funcionais.

|id|tma_id|btn_id|btn_function|btn_hint|btn_image_path|btn_name|tela|chave|btn_class|visible|
|---|---|---|---|---|---|---|---|---|---|---|
|2412|1374|botao-detalhe|`searchNav.showModalDetail();`|Exibe Detalhe|image/glyphicons/glyphicons/png/glyphicons-158-show-thumbnails-with-lines.png|Detalhe|resume|||1|
|2910|1374|botao-remover|`(function(){setTimeout(function(){ if($('#btn-group-popup .btn-success'). text()=='Atualizar'){$('#btn-group-popup .btn-success')[0].remove() }},500);})()`|esconder|image/glyphicons/glyphicons/png/glyphicons-55-clock.png|remover botao atualizar|popup||btn btn-link|3|
|2911|1374|botao-detalhe|`functionSpecific.taxPayerHistory($('#resume-table').bootstrapTable('getSelections')[0].inscricao,'contribuinte_test')`|Historico Inscrição|image/glyphicons/glyphicons/png/glyphicons-55-clock.png|Historico Inscrição|resume|||4|
|2411|1374|botao-detalhe|`functionSpecific.auxLoadDataByMultiplyForm($('#resume-table').bootstrapTable('getSelections')[0].gid,1678,1678);(function(){ if($('#tipo_contribuinte').val()=='Proprietário'){functionSpecific.serchCEP($('#inscricao').val(),1374,'*','inscricao'); let result=window.functionSpecific.lastSearchCep; let removeButton=false; for(let a=0;a<result.length;a++){ if(result[a].tipo_contribuinte.contains('Secund')){ removeButton=true;} } if(removeButton){ document.querySelector('#btn-group-popup').querySelector('.btn-info').remove(); editorInfoTools.createPopUpInfomative('<center>Atenção <br> remova todos os Proprietário Secundário do imóvel! </center>','waring',5000)} }})()`|Deletar item selecionado|image/glyphicons/glyphicons/png/glyphicons-31-pencil.png|Deletar|resume|||3|
|2413|1374|botao-detalhe|`functionSpecific.createNewObjectByResume(1678,false,'',true,false);$( '#cpf_cnpj_pessoa' ).val( '');$( '#nome_pessoa_imovel' ).val( '');$( '#pes_id' ).val( '');`|Inserir novo item|image/glyphicons/glyphicons/png/glyphicons-191-circle-plus.png|Inserir|resume|||2|
|4655|1374|botao-inserir-pessoa|`functionSpecific.createNewObjectByResume(1373,false,'',true,false,true)`|Pessoa|image/glyphicons/glyphicons/png/glyphicons-191-circle-plus.png|Pessoa|resume|||5|