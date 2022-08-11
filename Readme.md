# Projeto scraping python + selenium + beautifulsoup4 site kabum.
# Python 3.10.5
## Extração dos dados: descrição, preço e URL do produto.

### Funções:

#### -Pede URL do tipo de produto que o usuário deseja extrair, Exemplo: 'https://www.kabum.com.br/hardware/placa-de-video-vga'
#### -Adiciona configurações ao navegador que crome que sera automatizado.
#### -Oculta navegador com a config: "opitions.add_argument('==headdless')"
#### -Aguarda o navegador carregar todo conteúdo.
#### -Puxa o conteúdo do site.
#### -Separa os conteúdos, descrição, preço e URL percorrendo todo o número pagináveis de produtos especificados.
#### -Adiciona ao dicionário criado.
#### -Cria e armazena todas essas informações extraídas para o arquivo CSV.