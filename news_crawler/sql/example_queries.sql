-- TRUNCATE news_crawler.common CASCADE; -- deletes all data
-- ALTER SEQUENCE news_crawler."common_ID_seq" RESTART WITH 1;
-- ALTER SEQUENCE news_crawler."article_ID_seq" RESTART WITH 1;
SELECT * FROM news_crawler.common;
SELECT * FROM news_crawler."article";
SELECT * FROM news_crawler."page";
SELECT count(common."ID") FROM news_crawler.common GROUP BY common."Domain";