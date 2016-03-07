# coding: utf-8

import sys
import requests
from News.extractor import BaseExtractor
from News.extractor.news163 import News163Extractor, NewsExtractor


def get_document(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.content
    else:
        print("get document error: %s" % r.status_code)
        return ""


def test_news163_extractor():
    body = '''<p>苏州今天早上最低气温-8.3℃，刷新了苏州本世纪的低温纪录!这是要冻死宝宝吗?!</p> <div class="img"> <a><img src="http://easyread.ph.126.net/KE0hpIfejBS6I0wF6WtK7w==/7917110441618980351.gif" size="100*100" alt="" /></a> </div> <p>这个周末无论你是顶着严寒拍着雪景，还是在家里的被窝四季如春。都要注意啦!</p> <p>因为，24～26日将出现严重冰冻天气!预计周一(25日)上班日的极端最低气温仍将达零下8度!</p> <div class="img"> <a><img src="http://easyread.ph.126.net/tShSP_kJH89Tlb-wBHazIw==/7916545292641531497.jpg" size="400*400" alt="" /></a> </div> <p>恰逢周一上班的你是不是感觉将要被床封印了!预计25日气温零下8度到0度，26日零下5度到4度。要注意防范道路结冰、低温冰冻和大风。</p> <p>周一的上班路上，这些事情要特别注意。</p> <p>开车上班的亲们出发前，首先要检查一下爱车在特殊天气中的状况，要知道这些事都是有可能发生的：</p> <div class="img"> <a><img src="http://easyread.ph.126.net/T7ZUSc2BEPDelasxiMxayA==/7916849857361121993.gif" size="145*145" alt="" /></a> </div> <p>打不开车门怎么办?</p> <div class="img"> <a><img src="http://easyread.ph.126.net/pzvcv7-qu66ISoIdWgKi5g==/7916728911083370565.jpg" size="365*220" alt="" /></a> </div> <p>出现这种情况不要用力去拧钥匙或打车门。如果用力去拧钥匙或打车门可能会适得其反，钥匙或许会受到损坏。而如果强打车门，车漆也会受到损伤。建议从家中灌制一瓶温水(热水可能会使玻璃炸裂)浇到结冰处。</p> <p>预防招数：可事先向车门锁孔内注入少许润滑油，并在车门四周的密封条上抹一层薄薄的油脂。</p> <p>雨刮器被冻住!</p> <div class="img"> <a><img src="http://easyread.ph.126.net/GVkWpRe4O61gDBh9HCThgg==/7916833364688009406.jpg" size="253*189" alt="" /></a> </div> <p>如果类似的情况，千万别心急，因为这时候如果强行使用雨刮器的话，可能会损伤车辆多个部件，也千万别用浇热水来化雪。最好的办法是，车辆点火预热，再打开空调向玻璃吹热气，用空调的热量将雨刮器上的雪化开后再使用。</p> <p>出发前汽车发动不着了!</p> <p>这种情况很有可能是水箱被冻住。这样会发动汽车，会导致发动机因温度过高而烧坏，一定记得要更换一下防冻液。</p> <div class="img"> <a><img src="http://easyread.ph.126.net/T5hT3blVDiIDVGiNKeHi7w==/7916885041734519346.jpg" size="328*219" alt="" /></a> </div> <p>驾驶注意：</p> <div class="img"> <a><img src="http://easyread.ph.126.net/7ZFgW2ARBwlb9pC4-giS-Q==/7916885041734519348.jpg" size="397*334" alt="" /></a> </div> <p>行车时两大危险路段要小心。高架、桥梁两种类型道路容易结冰，要特别小心。特别是高架上下匝道、互通转弯处，保持好安全距离，尽量匀速驾驶，不急打方向、猛减速、急转弯。</p> <p>如果你选择骑车出行</p> <div class="img"> <a><img src="http://easyread.ph.126.net/4qlufQwCrezoL_rpYwoKpQ==/7916688229153142950.jpg" size="344*220" alt="" /></a> </div> <p>一定要提前检查车辆车闸。遇到结冰路段，下车推行。注意要减速慢行，不要急刹车，避免急转弯。</p> <div class="img"> <a><img src="http://easyread.ph.126.net/4ouOBfPr-Tpr3Eag0aiosA==/7916689328664770720.jpg" size="300*200" alt="" /></a> </div> <p>而步行上班的筒子们要注意：遇到冰冻路面，步伐要小，横过马路时要仔细观察，走人行道。</p> <p>最后，气象专家提醒，因为有严重冰冻，建议大家最好还是选择不要开车。</p> <div class="img"> <img src="http://easyread.ph.126.net/QCfLanEnUNczLq-EPaJdrg==/7916951012430624996.gif" size="80*80" alt="" /> </div> <p>这场寒潮给苏城的周末带来了闪亮的阳光和优质的空气，雪中大苏州和寒潮中的景区们也显得格外有强调。</p> <div class="img"> <a><img src="http://easyread.ph.126.net/65LWjp6DxJaEWzZhbAbg6w==/7916882842711263819.jpg" size="439*319" alt="" /></a> </div> <p>但气温真的是太低了!!!这么冷的天气何时是个头呢?</p> <div class="img"> <img src="http://easyread.ph.126.net/R0QijGR0JY3e9dgaI6dS_w==/7916944415361231125.gif" size="80*80" alt="" /> </div> <p>根据苏州市气象台的预报，下周开始气温将逐日回升，周三开始基本维持在4度以上，周四最高温度也将达到7度。</p> <div class="img"> <a><img src="http://easyread.ph.126.net/fjXie284tMwD4_wtx2qfbQ==/7916689328664770724.jpg" size="472*271" alt="" /></a> </div> <p>小鱼提醒广大小伙伴们，最近几天，一定要勤加减衣物，注意保暖哦!</p> <div class="img"> <a><img src="http://easyread.ph.126.net/eZ6w1PjKjsLmU3RSEQ_7ZQ==/7916669537454240126.gif" size="100*100" alt="" /></a> </div> '''
    extractor = News163Extractor(body)
    contents, count = extractor.extract()
    print contents
    print count


def test_base_extractor(string):
    extractor = BaseExtractor(string)
    tag = extractor.soup.find(id="js_content")
    contents, count = extractor.extract(tag)
    extractor._show(contents)


def main(url):
    string = get_document(url)
    test_base_extractor(string)


if __name__ == '__main__':
    main(sys.argv[1])


