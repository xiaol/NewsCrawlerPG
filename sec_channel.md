## 二级频道改动方案

#### 数据库改动
##### 1.添加secondchannel表,字段包括id, scname, cid(关联至channellist_v2表id字段), cname(关联至channellist_v2表cname字段), state, des
##### 2.修改newslist_v2表,添加scid字段,外键关联至secondchannel的id字段,可以为空

#### API改动
##### 1.添加根据scid与游戏名称检索新闻接口,查到对应数据并返回

#### 爬虫对接改动
##### redis中的新闻数据增加scid字段,如果有该字段则新闻数据进入postgre时对应填写scid字段