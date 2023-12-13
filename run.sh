#!/bin/bash

while true; do

    # crawl
    cd news_crawler/news_crawler/spiders/
    scrapy crawl cybersecuritynewsspider
    scrapy crawl thehackernewsspider

    # Sleep for 30 minutes
    sleep 1800
done