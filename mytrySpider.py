# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:20:55 2018

@author: kadar c
"""

import scrapy

scrapy.selector.SelectorList  

class mytrySpider(scrapy.Spider):
    name = "espncricinfo"
   # allowed_domains= ['www.espncricinfo.com/ci/content/']
   # start_urls=['http://www.espncricinfo.com/ci/content/site/cricket_squads_teams/index.html']
    def start_requests(self):
        urls = [
            'http://www.espncricinfo.com/ci/content/site/cricket_squads_teams/index.html',
            'http://www.espncricinfo.com/india/content/player/36084.html',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            #yield scrapy.MytryPipeline(url)
            
            
     
            
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'espncricinfo-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
        for espn in response.css('.pnl650M'):
            yield {
                    
                    'scraped1': espn.css('.link-text').extract(),
                   'scraped2': espn.css('.imgHldr').extract(),
                #'text': espn.css('span.text::text').extract(),
                #'author': espn.css('small.author::text').extract(),
               # 'tags': espn.css('div.tags a.tag::text').extract(),
            }
       
        for espn2 in response.css('#ciMainContainer'):
            yield {
                    
                    'scraped1': espn2.css('.pnl490M').extract(),
                    'scraped2': espn2.css('.pnl490M').extract(),
                
            }
        
        
        
        next_page = response.css('table.pnl650M a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)    

      #textLine

