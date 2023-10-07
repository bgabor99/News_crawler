-- -- DROP DATABASE IF EXISTS news_crawler;
-- CREATE DATABASE news_crawler;
-- DROP SCHEMA IF EXISTS news_crawler news_crawler;
CREATE SCHEMA IF NOT EXISTS news_crawler;

-- DROP TABLE IF EXISTS news_crawler.article CASCADE;
CREATE TABLE news_crawler.article (
	"ID" serial NOT NULL,
	"Article_ID" text NOT NULL,
	"Processed_Date" timestamp NOT NULL,
	"Article_Body" text NOT NULL,
	CONSTRAINT article_pk PRIMARY KEY ("ID"),
	CONSTRAINT "Unique_Article_ID" UNIQUE ("Article_ID")
);
-- ddl-end --
-- ALTER TABLE news_crawler.article OWNER TO postgres;
-- ddl-end --

-- DROP TABLE IF EXISTS news_crawler."Latest_news" CASCADE;
CREATE TABLE news_crawler."Latest_news" (
	"ID" serial NOT NULL,
	"Article_ID" text NOT NULL,
	"Title" text NOT NULL,
	CONSTRAINT "Latest_news_pk" PRIMARY KEY ("ID")
);
-- ddl-end --
-- ALTER TABLE news_crawler."Latest_news" OWNER TO postgres;
-- ddl-end --

-- ddl-end --
-- object: "Latest_news_FK" | type: CONSTRAINT --
-- ALTER TABLE news_crawler."Latest_news" DROP CONSTRAINT IF EXISTS "Latest_news_FK" CASCADE;
ALTER TABLE news_crawler."Latest_news" ADD CONSTRAINT "Latest_news_FK" FOREIGN KEY ("Article_ID")
REFERENCES news_crawler.article ("Article_ID") MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --
