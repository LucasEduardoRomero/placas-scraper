# Placas Scraper
Um Projeto para capturar informações sobre placas de vídeos em site de vendas. No momento na versão inicial, temos a spider __OlxSpider__ que captura dados da olx

## Instalação

* Necessário pipenv 2020 pra cima e python 3.x

1. git clone __repo__

2. Crie o ambiente virtual  
    `pipenv shell`

3. Instale as dependências  
    `pipenv install`

## Comandos

4. Rodar script para coletar pesquisa de placa de video pesquisa na olx  
    `scrapy crawl olx -O placas.jl --logfile placas_olx.jl

