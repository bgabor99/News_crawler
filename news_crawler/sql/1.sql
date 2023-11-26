-- DROP SCHEMA IF EXISTS news_crawler CASCADE;
CREATE SCHEMA IF NOT EXISTS news_crawler; --in postgres database

-- DROP TABLE IF EXISTS news_crawler.common CASCADE;
CREATE TABLE news_crawler.common (
	"ID" serial NOT NULL,
	"Domain" text NOT NULL,
	"Page_ID" text NOT NULL,
	"Processed_Date" timestamp NOT NULL,
	CONSTRAINT article_pk PRIMARY KEY ("ID"),
	CONSTRAINT "Unique_Page_ID" UNIQUE ("Page_ID")
);
-- ddl-end --
-- ALTER TABLE news_crawler.common OWNER TO postgres;
-- ddl-end --

-- DROP TABLE IF EXISTS news_crawler."article" CASCADE;
CREATE TABLE news_crawler."article" (
	"ID" serial NOT NULL,
	"Page_ID" text NOT NULL,
	"Title" text,
	"Body" text,
	"Content" text,
	"Author" text,
	"Date" text,
	CONSTRAINT "Article_pk" PRIMARY KEY ("ID")
);
-- ddl-end --
-- ALTER TABLE news_crawler."article" OWNER TO postgres;
-- ddl-end --

-- ddl-end --
-- object: "Article_FK" | type: CONSTRAINT --
-- ALTER TABLE news_crawler."article" DROP CONSTRAINT IF EXISTS "Article_FK" CASCADE;
ALTER TABLE news_crawler."article" ADD CONSTRAINT "Article_FK" FOREIGN KEY ("Page_ID")
REFERENCES news_crawler.common ("Page_ID") MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- REASSIGN OWNED BY admin_spider TO postgres;  -- or some other trusted role
-- DROP OWNED BY admin_spider;
DROP USER IF EXISTS admin_spider;
CREATE USER admin_spider WITH ENCRYPTED PASSWORD 'password'; -- set your password
-- ALTER USER admin_spider WITH PASSWORD 'password'; -- password can be changaed with this query
GRANT ALL PRIVILEGES ON DATABASE "postgres" to admin_spider;
GRANT ALL PRIVILEGES ON SCHEMA "news_crawler" to admin_spider;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA "news_crawler" to admin_spider; -- if tables are already exist
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA news_crawler to admin_spider;