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