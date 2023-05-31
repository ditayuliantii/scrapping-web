import scrapy
# import requests

class UnivIndo(scrapy.Spider):
    name = "univ"
    start_urls = [
        'https://www.webometrics.info/en/asia/indonesia%20?page={}'.format(i) for i in range(0,3)
        # 'https://www.webometrics.info/en/asia/indonesia%20?page=0',
        # 'https://www.webometrics.info/en/asia/indonesia%20?page=1'
    ]

    def parse(self, response):
         for universitas in response.css('tbody > tr'):
            #block-system-main > div > table.sticky-enabled.tableheader-processed.sticky-table > tbody > tr:nth-child(1) > td:nth-child(1) > center
            #block-system-main > div > table.sticky-enabled.tableheader-processed.sticky-table > tbody > tr:nth-child(1) > td:nth-child(2) > center
            #block-system-main > div > table.sticky-enabled.tableheader-processed.sticky-table > tbody > tr:nth-child(1) > td:nth-child(3) > a

            rank = universitas.css('td:nth-child(1) > center::text').extract_first()
            world_rank = universitas.css('td:nth-child(2) > center::text').extract_first()
            nama_univ = universitas.css('td:nth-child(3) > a::text').extract_first()
            impact_rank = universitas.css('td:nth-child(5) > center::text').extract_first()
            openness_rank = universitas.css('td:nth-child(6) > center::text').extract_first()
            excellence_rank = universitas.css('td:nth-child(7) > center::text').extract_first()
            
            yield{
                'Ranking' : rank,
                'World Rank' : world_rank,
                'Nama Universitas' : nama_univ,
                'Impact Rank' : impact_rank,
                'Openness Rank' : openness_rank,
                'Excellence Rank' : excellence_rank
            }
              
              
         