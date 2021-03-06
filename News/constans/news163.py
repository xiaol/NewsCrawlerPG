# coding: utf-8

from urllib import urlencode

SPIDER_NAME = "spider:news:news163"
COMMENT_SPIDER_NAME = "spider:news:comment:news163"
CRAWL_SOURCE = u"网易新闻"
ARTICLE_URL_TEMPLATE = "http://j.news.163.com/hy/doc.s?" \
                       "info=2&type=10&hash=&docid={docid}"
COMMENT_URL_TEMPLATE = "http://comment.news.163.com/api/v1" \
                       "/products/a2869674571f77b5a0867c3d71db5856/" \
                       "threads/{docid}/comments/newList?" \
                       "offset={offset}&limit={count_per_page}"
DOMAIN = "http://j.news.163.com"
START_URL_PREFIX = "http://j.news.163.com/hy/newshot.s?"
CHANNELS = {
    2: {"channel": 3},  # 娱乐
    3: {"channel": 6},  # 体育
    4: {"channel": 7},  # 财经
    5: {"channel": 4},  # 科技
    6: {"channel": 5},  # 汽车
    7: {"channel": "女人"},   # 女人
    8: {"channel": 21},     # 搞笑
    9: {"channel": 26},     # 美女
    11: {"channel": "LOFTER"},  # LOFTER
    14: {"channel": "交友"},  # 交友
    16: {"channel": "星座"},  # 星座
    17: {"channel": 12},    # 旅游
    18: {"channel": 15},    # 美食
    19: {"channel": "数码"},  # 数码
    20: {"channel": "房产"},  # 房产
    21: {"channel": "家居"},  # 家居
    22: {"channel": "人文"},  # 人文
    23: {"channel": "亲子"},  # 亲子
    24: {"channel": 11},    # 游戏
    25: {"channel": "减肥"},  # 减肥
    26: {"channel": "手机"},  # 手机
    28: {"channel": "生活"},  # 生活
    29: {"channel": "动漫"},  # 动漫
    30: {"channel": 17},    # 养生
    31: {"channel": "教育"},  # 教育
    32: {"channel": "历史"},    # 13
    66: {"channel": "图集"},  # 图集
    98: {"channel": "专题"},  # 专题
}

LOCAL_CHANNEL = 10  # 本地
LOCAL_CHANNEL_VALUE = {"channel": 28}
CITIES = u"中卫,七台河,巫山,红河,三明,崇明,白城,池州,西沙,莆田,忠县,大连,定西," \
         u"莱芜,和田,贵阳,钦州,赣州,大足,昭通,郑州,黑河,汉中,衡水,雅安,滨州,阳泉," \
         u"通辽,澄迈,深圳,邯郸,台州,潮州,张家界,大港,延吉,九江,保亭,塔城,云浮,汕尾," \
         u"商洛,常州,库尔勒,梧州,延庆,运城,奉贤,綦江,石嘴山,襄樊,哈尔滨,新乡,宁波," \
         u"西安,天水,怒江,盘锦,阿勒泰,金昌,万盛,汤河口,彭水,武汉,阿里,平凉,林芝,巫溪," \
         u"驻马店,固原,石河子,黔阳,河池,金华,齐齐哈尔,广州,苏州,仙桃,济南,沙坪坝," \
         u"伊宁,江门,三亚,郴州,内江,长春,都匀,佛山,儋州,舟山,文昌,惠州,哈密,商丘," \
         u"益阳,大庆,昆明,洛阳,石柱,佳木斯,清远,铜仁,通化,邵阳,顺义,荆门,本溪," \
         u"阿拉善左旗,天津,兴义,玉林,廊坊,白沙,锡林浩特,宜宾,亳州,无锡,铜陵,怀柔," \
         u"泰州,抚州,海西,海南,百色,恩施,巴南,杭州,黄南,酒泉,临高,北京,自贡,晋城," \
         u"济源,大同,广元,西青,肇庆,抚顺,荆州,宁德,浦东,高雄,五指山,巢湖,怀化,秦皇岛," \
         u"沧州,晋江,南通,武都,芜湖,青岛,中山,漳州,平谷,铜梁,开封,泸州,喀什,毕节," \
         u"贺州,玉树,菏泽,蚌埠,株洲,阜阳,景德镇,达州,大理,漯河,黄冈,琼海,呼伦贝尔," \
         u"宿州,北辰,上海,秀山,鞍山,湛江,永川,永州,静海,房山,斋堂,鹤岗,丽江,朔州," \
         u"四平,阿拉尔,鄂尔多斯,海东,六安,伊春,湘潭,庆阳,连云港,梅州,津南,南京,潼南," \
         u"张家口,承德,咸阳,合川,榆林,昌平,南昌,天门,咸宁,琼中,克拉玛依,万宁,上饶," \
         u"松江,威海,大兴安岭,泉州,南汇,大兴,唐山,遂宁,铁岭,万州龙宝,台中,资阳,武隆," \
         u"鹰潭,银川,荣昌,防城港,镇江,延安,济宁,潜江,香格里拉,宜春,临汾,宝坻,梁平," \
         u"日照,马鞍山,安顺,宜昌,垫江,锦州,丰都,潍坊,海北,濮阳,淮安,普洱,乐山,阿图什," \
         u"山南,渭南,信阳,茂名,赤峰,青浦,南阳,烟台,徐州,南平,甘孜,德宏,昌江,武威,湖州," \
         u"吉安,吉林,阳江,北碚,乌鲁木齐,淮北,双鸭山,葫芦岛,蓟县,盐城,南宁,汉沽,合作," \
         u"来宾,渝北,许昌,丰台,楚雄,琼山,文山,阿坝,黔江,绵阳,铜川,宝鸡,集宁,广安," \
         u"通州,白银,临沂,塘沽,衢州,嘉定,白山,晋中,临河,武清,宣城,临沧,温州,西宁," \
         u"衡阳,宿迁,辽源,东方,遵义,阜新,安阳,凉山,北海,沈阳,兰州,汕头,长沙,吐鲁番," \
         u"娄底,阿克苏,辽阳,绥化,韶关,龙岩,福州,泰安,河源,淮南,成都,太原,随州,果洛," \
         u"忻州,城口,滁州,东营,景洪,拉萨,保定,长治,鸡西,海口,台北县,崇左,包头,绍兴," \
         u"聊城,巴中,松原,鹤壁,金山,吉首,厦门,宁河,德阳,新余,乐东,吕梁,淄博,鄂州,营口," \
         u"丽水,丹东,嘉峪关,攀枝花,石家庄,珠海,合肥,东莞,枣庄,南川,江津,酉阳,重庆," \
         u"宝山,焦作,凯里,博乐,霞云岭,屯昌,牡丹江,乌海,黄石,呼和浩特,三门峡,神农架," \
         u"长寿,扬州,南沙岛,桂林,昌都,十堰,张掖,云阳,开县,玉溪,日喀则,常德,临夏,陵水," \
         u"邢台,乌兰浩特,德州,平顶山,嘉兴,柳州,眉山,昌吉,定安,东丽,黄山,周口,岳阳," \
         u"揭阳,南充,保山,贵港,萍乡,六盘水,安康,涪陵,奉节,孝感,那曲,安庆,吴忠,璧山,曲靖"

_URL_TEMPLATE = "http://j.news.163.com/hy/newshot.s?newchannel=news&limit=100&channel={0}&offset=0"
CATEGORIES = {
    u"娱乐": (_URL_TEMPLATE.format(2), 3, 30),
    u"体育": (_URL_TEMPLATE.format(3), 6, 30),
    u"财经": (_URL_TEMPLATE.format(4), 7, 30),
    u"科技": (_URL_TEMPLATE.format(5), 4, 30),
    u"汽车": (_URL_TEMPLATE.format(6), 5, 30),
    u"女人": (_URL_TEMPLATE.format(7), None),
    u"搞笑": (_URL_TEMPLATE.format(8), 21, 30),
    u"美女": (_URL_TEMPLATE.format(9), 26, 30),
    u"LOFTER": (_URL_TEMPLATE.format(11), None),
    u"交友": (_URL_TEMPLATE.format(14), None),
    u"星座": (_URL_TEMPLATE.format(16), None),
    u"旅游": (_URL_TEMPLATE.format(17), 12, 30),
    u"美食": (_URL_TEMPLATE.format(18), 15, 30),
    u"数码": (_URL_TEMPLATE.format(19), None),
    u"房产": (_URL_TEMPLATE.format(20), None),
    u"家居": (_URL_TEMPLATE.format(21), None),
    u"人文": (_URL_TEMPLATE.format(22), None),
    u"亲子": (_URL_TEMPLATE.format(23), None),
    u"游戏": (_URL_TEMPLATE.format(24), 11, 30),
    u"减肥": (_URL_TEMPLATE.format(25), None),
    u"手机": (_URL_TEMPLATE.format(26), None),
    u"生活": (_URL_TEMPLATE.format(28), None),
    u"动漫": (_URL_TEMPLATE.format(29), None),
    u"养生": (_URL_TEMPLATE.format(30), 17, 30),
    u"教育": (_URL_TEMPLATE.format(31), None),
    u"图集": (_URL_TEMPLATE.format(66), None),
    u"最具争议": (_URL_TEMPLATE.format(97), None),
    u"专题": (_URL_TEMPLATE.format(98), None),
    u"本地": {

    }
}

__URL_LOCAL = "http://j.news.163.com/hy/newshot.s?newchannel=news&limit=100&channel=10&offset=0&"
for city in CITIES.split(","):
    params = {"city": city.encode("utf-8")}
    CATEGORIES[u"本地"][city] = (__URL_LOCAL+urlencode(params), 28, 60)


