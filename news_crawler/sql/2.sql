-- DROP TABLE IF EXISTS news_crawler.page CASCADE;
CREATE TABLE news_crawler."page" (
	"ID" serial NOT NULL,
	"Page_ID" text NOT NULL,
	"Page" text,
	CONSTRAINT "Page_pk" PRIMARY KEY ("ID")
);
-- ddl-end --
-- ALTER TABLE news_crawler."page" OWNER TO postgres;
-- ddl-end --

-- ddl-end --
-- object: "Page_FK" | type: CONSTRAINT --
-- ALTER TABLE news_crawler."page" DROP CONSTRAINT IF EXISTS "Page_FK" CASCADE;
ALTER TABLE news_crawler."page" ADD CONSTRAINT "Page_FK" FOREIGN KEY ("Page_ID")
REFERENCES news_crawler.common ("Page_ID") MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --
