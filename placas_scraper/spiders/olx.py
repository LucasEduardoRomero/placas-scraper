import scrapy

from ..items import PlacasScraperItem


class OlxSpider(scrapy.Spider):
    name = "olx"

    def start_requests(self):
        urls = [
            'https://www.olx.com.br/brasil?q=placa%20de%20video'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # xpath do cartão do produto na lista
        xpath_li = '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div[7]/div/div/div/div[9]/div/div/div/ul//li'
        lista = response.xpath(xpath_li)

        # classe presente em cada atributo (seletor css)
        #.xpath("//span[@class='sc-1n4y6ur-1 gSZxaa sc-ifAKCX eUXUWN']")
        numr_fotos_class = 'sc-1n4y6ur-1 gSZxaa sc-ifAKCX eUXUWN'
        preco_class = 'sc-ifAKCX eoKYee'
        datahora_class = 'wlwg1t-1 fsgKJO sc-ifAKCX eLPYJb'

        for item in lista:
            # se tem link dentro, é um item útil, guardar dados
            if(len(item.xpath('.//a')) > 0):
                numr_fotos = item.xpath(f"//span[@class='{numr_fotos_class}']/text()").get()
                url_img = item.xpath('.//img/@src').get()
                descricao = item.xpath('.//h2/text()').get()
                preco = item.xpath(f".//span[@class='{preco_class}']/text()").get()
                # datahora_pub arr no formato [data, hora]
                datahora_pub = item.xpath(f".//span[@class='{datahora_class}']/text()").getall()
                # pegar imagem, descricao, preço e data
                # todo-> determinar coisas importantes a guardar: preço, nome foto etc
                # produto = PlacasScraperItem()
                #produto['produto'].append = descricao
                #produto["numr_de_fotos"].append = numr_fotos
                #produto["preco"].append = preco
                #produto["url_img"].append == url_img
                #produto["datahora_pub"].append = datahora_pub
                # produto_tempo = {
                yield {
                    'produto': descricao,
                    'numr_de_fotos': numr_fotos,
                    'preco': preco,
                    'url_img': url_img,
                    'datahora_pub': datahora_pub
                }
                #print(produto_tempo)
                # yield produto
                
            else:
                print('NÃO ACHOU LINK')
        # proxima pagina
        # response.xpath(".//span[text()='Próxima pagina']")

        next_btn = response.xpath("//a[@data-lurker-detail='next_page']")
        if(len(next_btn) > 0):
            next_btn = next_btn[0]
            yield response.follow(next_btn, self.parse)
            