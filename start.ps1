python3 -m venv env
.\env\Scripts\activate
pip3 install -r requirements.txt
cd news_crawler\news_crawler\spiders\
scrapy crawl latestnewsspider
scrapy crawl threatnewsspider
scrapy crawl cyberattacknewsspider
scrapy crawl vulnerabilitynewsspider
scrapy crawl zerodaynewsspider
scrapy crawl databreachesnewsspider
scrapy crawl cyberainewsspider
scrapy crawl whatisnewsspider
cd ..\..\..
deactivate
