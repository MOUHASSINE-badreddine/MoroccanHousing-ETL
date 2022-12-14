from urllib import response
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import HousingpipelineItem
Locators = {}
def getLocation(ville):
    global Locators
    global geolocator
    if ville in Locators.keys():
        return Locators[ville]
    else:
        locator = geolocator.geocode(ville)
        Locators[ville] = locator
        return locator
def get_other_features(response):
        ans=[]
        generalDiv=response.xpath('//*[@id="__next"]/div/main/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[5]/div/div')
        for div in generalDiv.xpath('.//div'):
            componentContent=div.xpath('.//span/text()').get()
            if componentContent!=None:
                ans.append(componentContent)
        return ';'.join(ans)
def get_secondaryInformations(response):
    l=[]
    ans={
        'Secteur':None,
        'Etage':None,
        'Salons':None
    }
    generalDiv=response.xpath('//*[@id="__next"]/div/main/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/ol')
    for component in generalDiv.xpath('.//li/span/text()'):
        l.append(component.extract())
    for k in ans.keys():
        if k in l:
            ans[k]=l[l.index(k)+1]
        else: 
            pass
    return ans

class avitoSpider(CrawlSpider):
    name = 'avitoSpider'
    allowed_domains = ['avito.ma']
    start_urls = ['https://www.avito.ma/fr/maroc/appartements-%C3%A0_louer']
    base_url = 'https://www.avito.ma/fr/maroc/appartements-%C3%A0_louer'
    rules = [
             Rule(LinkExtractor(allow='appartements'),
                  callback='parse_filter', follow=True)
             ]

    def parse_filter(self, response):
        #item = HousingpipelineItem()
        ville = response.xpath(
            '//*[@id="__next"]/div/main/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/span[1]/text()'
            ).get()

        SecondInfos=get_secondaryInformations(response)

        secteur,etage,salons=SecondInfos['Secteur'],SecondInfos['Etage'],SecondInfos['Salons']
        Equipements=get_other_features(response)
        if 'Meubl??' in Equipements:
            MeubleBool=1
        else:
            MeubleBool=0
        try:
            items=HousingpipelineItem(
                Surface= int(response.xpath(
                    '//*[@id="__next"]/div/main/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/div/span/text()'
                    ).get().replace(
                    " m??", "")),
                Prix= int(response.xpath(
                    '//*[@id="__next"]/div/main/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/p/text()'
                    ).get().replace("\u202f", "").split()[0]),
                Nombre_Chambres=int(response.xpath(
                    '//*[@id="__next"]/div/main/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div/span/text()'
                ).get()),
                Ville=ville,
                Secteur=secteur,
                Etage=etage,
                Salons=salons,
                Meuble=MeubleBool,
                Equipements=Equipements

            )
            yield items
        except:
            pass