# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:20:55 2018

@author: kadar c
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "espncricinfo"

    def start_requests(self):
        urls = [
            'http://www.espncricinfo.com/ci/content/site/cricket_squads_teams/index.html',
            'http://www.espncricinfo.com/india/content/player/36084.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)