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
comment on column monitor.error is '错误类型: 1(暂时不支持), 2(解析失败)';


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


CREATE TABLE newscomments
(
    id INTEGER PRIMARY KEY NOT NULL,
    comment_id VARCHAR(128),
    content TEXT,
    nickname VARCHAR(128),
    love INTEGER DEFAULT 0 NOT NULL,
    create_time TIMESTAMP,
    profile TEXT,
    docid VARCHAR(128),
    pid VARCHAR(128)
);


