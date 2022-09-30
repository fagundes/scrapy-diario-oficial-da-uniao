# -*- encoding: utf-8 -*-
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor

import loggerConfig

from crawlDou import crawlDou
from writeResult import writeResult
import os.path

# create a crawler process with the specified settings
runner  = CrawlerRunner(
    {
        'USER_AGENT': 'Sinayra-meuCrawlerComScrapy/1.1 (sinayra@hotmail.com)',
        'LOG_STDOUT': True,
        'LOG_ENABLED': False,
        'ROBOTSTXT_OBEY' : False,
        'RANDOMIZE_DOWNLOAD_DELAY': True,
        'CONCURRENT_REQUESTS': 5,
        'RETRY_TIMES' : 5,
        'AUTOTHROTTLE_ENABLED' : True,
        'HTTPCACHE_ENABLED': True,  # for development
        'FEEDS':{
            'items.jl': {
                'format': 'jsonlines',
                'encoding': 'utf8'
            }   
        },
    }
)

data = "14-09-2022"

crawlDou(runner, data, "dou2")
reactor.run()  # the script will block here until the last crawl call is finished

if (os.path.exists("items.jl")):
    writeResult("result" + data + ".json", "items.jl")
else:
    raise FileNotFoundError("Required files not found. Try again later")
