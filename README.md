# News_crawler project
## Run this project with Docker Compose
### Prerequisites
- Create a .env file in the app root folder
    - It must contain these env variables
        - POSTGRES_USER, POSTGRES_PASSWORD, PGADMIN_DEFAULT_EMAIL, PGADMIN_DEFAULT_PASSWORD, POSTGRES_CRAWL_USER, POSTGRES_CRAWL_PASSWORD
            - Pay attention to POSTGRES_CRAWL_USER and POSTGRES_CRAWL_PASSWORD, because these have to be the same which user and pwd is defined in 1.sql file!
    - Example of an .env file
        ```
        POSTGRES_USER=postgres
        POSTGRES_PASSWORD=password
        PGADMIN_DEFAULT_EMAIL=admin@admin.com
        PGADMIN_DEFAULT_PASSWORD=admin
        POSTGRES_CRAWL_USER=admin_spider
        POSTGRES_CRAWL_PASSWORD=password
        ```
### Start the app
- Start the containers with this command: ```docker compose --env-file .env up```
    - You can connect to the postgres server using pgAdmin on http://localhost:8888/ 
        - Email: In .env file: PGADMIN_DEFAULT_EMAIL
        - Password: In .env file: PGADMIN_DEFAULT_PASSWORD
            - Register a new server
                - Add a name to it (doesn't matter how you name it)
                - Connection settings
                    - Host: postgres
                    - Port: 5432
                    - Maintenance database: postgres
                    - username: In .env file: POSTGRES_USER
                    - password: In .env file: POSTGRES_PASSWORD
    - After connecting you can check the datas under Databases -> postgres -> Schemas -> news_crawler
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
- Start with rebuilding the Dockerfiles: ```docker compose --env-file .env up --build```
- Stop and delete volume: ```docker compose down -v```
- Execute commands in postgres_container and check if the 1.sql file is exists there
    - ```docker exec -it postgres_container /bin/bash```
    - ```ls -la /docker-entrypoint-initdb.d/```
---
## Scrapy command helper
- Start a new scrapy project: ```scrapy startproject <project_name>```
- Run a spider: ```scrapy crawl <spider_name>```
