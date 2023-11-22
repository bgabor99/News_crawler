python3 -m venv env # Developed in python 3.11
.\env\Scripts\activate
pip3 install -r requirements.txt
cd news_crawler\news_crawler\spiders\
scrapy crawl cybersecuritynewsspider
scrapy crawl thehackernewsspider
cd ..\..\..
deactivate