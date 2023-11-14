# News_crawler project
## Run this project with Docker Compose
### Start the app
- Start the containers with this command: ```docker compose up```
    - You can connect to the postgres server using pgAdmin on http://localhost:8888/ 
        - Email: In docker-compose.yml
        - Password: In docker-compose.yml
            - Register a new server
                - Add a name to it (doesn't matter how you name it)
                - Connection settings
                    - Host: postgres
                    - Port: 5432
                    - Maintenance database: postgres
                    - username: In docker-compose.yml
                    - password: In docker-compose.yml
### Stop the app
- Stop the containers with this command: ```docker compose down```
---
---
## Run this project locally
## Prerequisites
- Have a local postgres server and it is configured with the news_crawler/sql/1.sql file
- Change news_crawler/news_crawler/settings.py DATABASES settings for local usage
    ```
    DATABASES = {
    'default': {
        'NAME': 'postgres',
        'USER': 'admin_spider',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',  # Default PostgreSQL port
    }
    ```
## Run
- start.ps1 powershell script
    - Works only on Windows
---
## Docker Compose command helper
- Start with rebuilding the Dockerfiles: ```docker-compose up --build```
- Stop and delete volume: ```docker compose down -v```
- Execute commands in postgres_container and check if the 1.sql file is exists there
    - ```docker exec -it postgres_container /bin/bash```
    - ```ls -la /docker-entrypoint-initdb.d/```
---
## Scrapy command helper
- Start a new scrapy project: ```scrapy startproject <project_name>```
- Run a spider: ```scrapy crawl <spider_name>```
