select count(*) from newslist;

select count(*) from newscomments;

select count(*) from comics where '冒险' = ANY(comics.tags);


TRUNCATE TABLE newslist;
TRUNCATE TABLE newscomments;



CREATE TABLE newslist
(
    url TEXT PRIMARY KEY NOT NULL,
    pub_time TIMESTAMP NOT NULL,
    title TEXT NOT NULL,
    tags TEXT[],
    author TEXT,
    pub_name TEXT,
    pub_url TEXT,
    content JSONB NOT NULL,
    content_html TEXT NOT NULL,
    descr TEXT,
    img_num INTEGER DEFAULT 0 NOT NULL,
    docid TEXT NOT NULL,
    love INTEGER DEFAULT 0 NOT NULL,
    up INTEGER DEFAULT 0 NOT NULL,
    img_style INTEGER DEFAULT 0 NOT NULL,
    img_list TEXT[],
    insert_time TIMESTAMP NOT NULL DEFAULT now(),
    province VARCHAR(128) DEFAULT NULL ,
    city VARCHAR(128) DEFAULT NULL ,
    district VARCHAR(128) DEFAULT NULL
);

CREATE UNIQUE INDEX newslist_docid_key ON newslist (docid);


select count(*) from newslist;
select count(*) from monitor;
select count(*) from news;
select count(*) from newscomments;

select * from newslist ORDER BY insert_time DESC LIMIT 50;

TRUNCATE TABLE newslist;
TRUNCATE TABLE monitor;
TRUNCATE TABLE news;
TRUNCATE TABLE newscomments;


create table monitor(
  id serial primary key,
  crawl_url varchar not null,
  original_url varchar,
  crawl_source varchar,
  original_source varchar,
  channel varchar not null,
  error int not null,
  insert_time timestamp default now()
);
comment on column monitor.error is '错误类型: 1(暂时不支持), 2(解析失败)'


create table news
(
  key VARCHAR PRIMARY KEY ,
  title VARCHAR NOT NULL,
  tags VARCHAR[],
  summary VARCHAR,
  publish_time TIMESTAMP NOT NULL ,
  content JSONB NOT NULL ,
  province VARCHAR,
  city VARCHAR,
  district VARCHAR,
  love int DEFAULT 0,
  up int DEFAULT 0,
  down int DEFAULT 0,
  image_number int DEFAULT 0,
  docid VARCHAR NOT NULL ,
  channel VARCHAR,
  category VARCHAR,
  crawl_url VARCHAR UNIQUE ,
  original_url VARCHAR,
  crawl_source VARCHAR,
  original_source VARCHAR,
  insert_time TIMESTAMP DEFAULT now()
);















select * from newslist WHERE newslist.channel_id=3 ORDER BY newslist.insert_time DESC LIMIT 10;

SELECT * from ydzxcommentlist ORDER BY ydzxcommentlist.id DESC LIMIT 50;

select source_url from spidersourcelist;

select * from comiclist WHERE comic_url='http://m.dmzj.com/info/lhzy.html';

select count(*) from comiclist;

select count(*) from comicchapterlist;

select count(*) from comiccommentlist;

select * from comiclist, (select comic_url, count(*) as ct FROM comicchapterlist GROUP BY comic_url) cc WHERE comiclist.comic_url=cc.comic_url and comiclist.chapter_num!=cc.ct;

select * from comiclist WHERE comic_url='http://m.dmzj.com/info/wangzhezhijian.html';

delete from comiccommentlist WHERE comic_id=11274;

select project_name, count(*) from spiderqueuelist GROUP BY project_name;


select * from newslist limit 100 OFFSET 38700;

select count(*) from newslist;

select count(DISTINCT comicchapterlist.chapter_url) from comicchapterlist;

select count(*) from comicchapterlist WHERE comicchapterlist.id not in  (select min(comicchapterlist.id) from comicchapterlist GROUP BY chapter_url);


select count(*) from comicchapterlist a where a.ctid <> (select min(b.ctid) from comicchapterlist b where a.chapter_url=b.chapter_url);

INSERT INTO comicchapterlist_tmp select * from comicchapterlist WHERE id in (SELECT min(id) FROM comicchapterlist GROUP BY chapter_url);

SELECT count(*) from comicchapterlist_tmp;

CREATE TABLE comicchapterlist_tmp
(
    id INTEGER PRIMARY KEY NOT NULL,
    chapter_url TEXT NOT NULL UNIQUE,
    chapter_order INTEGER NOT NULL,
    comic_url TEXT NOT NULL,
    name TEXT NOT NULL,
    images TEXT[] NOT NULL
);

alter table comicchapterlist_tmp RENAME to comicchapterlist;

select * from newslist WHERE title LIKE '大众%';

select * from newslist LIMIT 50 OFFSET 37250;

SELECT count(*) from newslist WHERE insert_time BETWEEN '2016-01-20 11:00:00' AND '2016-01-20 12:00:00';


select count( DISTINCT docid ) from ydzxcommentlist;


select failed_list from spidermonitorlist WHERE failed_list is NOT NULL ORDER BY id DESC LIMIT 50;


select y,m,d,count(url) from (select url, extract(YEAR from insert_time) as y, extract(MONTH from insert_time) as m, extract(DAY from insert_time) as d from newslist WHERE insert_time BETWEEN '2016-01-01 00:00:00' AND '2016-02-01 00:00:00') newdata GROUP BY y,m,d;

select current_date, current_date + interval '1 month';

select count(*), date_trunc('hour', insert_time) from newslist WHERE insert_time BETWEEN DATE 'today' AND DATE 'tomorrow' GROUP BY 2 ORDER BY 2;

select count(DISTINCT (comment_id, docid, pid)) from ydzxcommentlist;

show DATESTYLE ;

select count(DISTINCT url) from newslist;
SELECT count(*) from newslist;



create table monitor(
  id serial primary key,
  crawl_url varchar not null,
  original_url varchar,
  crawl_source varchar,
  original_source varchar,
  channel varchar not null,
  error int not null,
  insert_time timestamp default now()
);
comment on column monitor.error is '错误类型: 1(暂时不支持), 2(解析失败)'

