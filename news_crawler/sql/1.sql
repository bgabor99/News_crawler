-- -- DROP DATABASE IF EXISTS news_crawler;
-- CREATE DATABASE news_crawler;
-- DROP SCHEMA IF EXISTS news_crawler CASCADE;
CREATE SCHEMA IF NOT EXISTS news_crawler;

-- REASSIGN OWNED BY admin_spider TO postgres;  -- or some other trusted role
-- DROP OWNED BY admin_spider;
-- DROP USER IF EXISTS admin_spider;
-- CREATE USER admin_spider WITH ENCRYPTED PASSWORD 'password'; -- set your password
-- ALTER USER admin_spider WITH PASSWORD 'password'; -- password can be changaed with this query
-- GRANT ALL PRIVILEGES ON DATABASE "news_crawler" to admin_spider;
-- GRANT ALL PRIVILEGES ON SCHEMA "news_crawler" to admin_spider;
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA "news_crawler" to admin_spider; -- if tables already exist
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA news_crawler TO admin_spider;

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


-- DROP TABLE IF EXISTS news_crawler."Threat_news" CASCADE;
CREATE TABLE news_crawler."Threat_news" (
	"ID" serial NOT NULL,
	"Article_ID" text NOT NULL,
	"Title" text NOT NULL,
	CONSTRAINT "Threat_news_pk" PRIMARY KEY ("ID")
);
-- ddl-end --
-- ALTER TABLE news_crawler."Threat_news" OWNER TO postgres;
-- ddl-end --

-- ddl-end --
-- object: "Threat_news_FK" | type: CONSTRAINT --
-- ALTER TABLE news_crawler."Threat_news" DROP CONSTRAINT IF EXISTS "Threat_news_FK" CASCADE;
ALTER TABLE news_crawler."Threat_news" ADD CONSTRAINT "Threat_news_FK" FOREIGN KEY ("Article_ID")
REFERENCES news_crawler.article ("Article_ID") MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --
