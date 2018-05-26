# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:20:55 2018

@author: kadar c
"""

import scrapy


class mytrySpiderSpider(scrapy.Spider):
    name = "espncricinfo"

    def start_requests(self):
        urls = [
            'http://www.espncricinfo.com/ci/content/site/cricket_squads_teams/index.html',
            'http://www.espncricinfo.com/india/content/player/36084.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
            
            
    
    def parse_items(self, response):
        content = Selector(response=response).xpath('//body')
        for nodes in content:

            img_urls = nodes.xpath('//img/@src').extract()

            item = mytryItem()
            item['page_heading'] = nodes.xpath("//title").extract()
            item["page_title"] = nodes.xpath("//h1/text()").extract()
            
            item["page_link"] = response.url
            item["page_content"] = nodes.xpath('//div[@class="CategoryDescription"]').extract()
            item['image_url'] = img_urls 
            item['image'] = ['http://www.espncricinfo.com/ci/content/site/cricket_squads_teams/index.html ' + img for img in img_urls]

            yield item

    
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
        for quote in response.css('textLine'):
            yield {
                'text': quote.css('span.text::text').extract(),
                'author': quote.css('small.author::text').extract(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        next_page = response.css('table.teamList a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)    
        