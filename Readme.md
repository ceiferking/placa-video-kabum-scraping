# Projeto scraping python + selenium + beautifulsoup4 site kabum.
# Python 3.10.5
## Extração dos dados: descrição, preço e URL do produto.
## Para funcionabilidade do codigo completa basta seguir os paços a seguir:
#### 1-Baixe todos os arquivos.
#### 2-Instale a versão adequada do Python onde que o código foi escrito.
#### 3-Baixe o WebDriver do Chome na versão correta do seu navegador.
#### 4-Coloque o arquivo executável do Webdriver na mesma pasta do código.
#### 5-Faça a instalação do requeriments.txt através do comando 'pip3 install -r requirements.txt' no terminal na pasta raiz do projeto.
#### 6-Execute o arquivo python 'seleniscripip.py' através do comando no terminal "python seleniscripip.py"

### Funções:

#### -Pede URL do tipo de produto que o usuário deseja extrair, Exemplo: 'https://www.kabum.com.br/hardware/placa-de-video-vga'
#### -Adiciona configurações ao navegador que crome que sera automatizado.
#### -Oculta navegador com a config: "opitions.add_argument('==headdless')"
#### -Aguarda o navegador carregar todo conteúdo.
#### -Puxa o conteúdo do site.
#### -Separa os conteúdos, descrição, preço e URL percorrendo todo o número pagináveis de produtos especificados.
#### -Adiciona ao dicionário criado.
#### -Cria e armazena todas essas informações extraídas para o arquivo CSV.