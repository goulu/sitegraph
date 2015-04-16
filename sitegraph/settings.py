# -*- coding: utf-8 -*-

# Scrapy settings for sitegraph project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sitegraph'

SPIDER_MODULES = ['sitegraph.spiders']
NEWSPIDER_MODULE = 'sitegraph.spiders'

FEED_FORMAT="jsonlines"
FEED_URI="file:///tmp/sitegraph.json"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sitegraph (+http://www.yourdomain.com)'
