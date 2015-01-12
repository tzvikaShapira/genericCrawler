# -*- coding: utf-8 -*-

# Scrapy settings for genericCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'genericCrawler'

SPIDER_MODULES = ['genericCrawler.spiders']
NEWSPIDER_MODULE = 'genericCrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'genericCrawler (+http://www.yourdomain.com)'
