# Projeto scraping python + selenium + beautifulsoup4 site kabum.
## extração dos dados: descrição, preço e URL do produto.

### Funções:

#### -Pede URL do tipo de produto que o usuário deseja extrair, Exemplo: 'https://www.kabum.com.br/hardware/placa-de-video-vga'
#### -adiciona configurações ao navegador que crome que sera automatizado.
#### -oculta navegador com a config: "opitions.add_argument('==headdless')"
#### -aguarda o navegador carregar todo conteúdo.
#### -puxa o conteúdo do site.
#### -separa os conteúdos, descrição, preço e URL percorrendo todo o número pagináveis de produtos especificados.
#### -adiciona ao dicionário criado.
#### -cria e armazena todas essas informações extraídas para o arquivo CSV.