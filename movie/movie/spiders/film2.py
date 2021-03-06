# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import MovieItem

class Film2Spider(CrawlSpider):
    name = 'film2'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/oumei/list_7_3.html']

    link_extractor = LinkExtractor(restrict_xpaths=('//table[@bgcolor="#F6F6F6"]//a'))
    rules = (
        # Rule(LinkExtractor(restrict_xpaths=('//div[@class="x"]/a'), callback='parse', follow=False)),
        Rule(link_extractor, callback='parse', follow=False),
    )


    def parse(self, response):

        tables = response.xpath('//table[@class="tbspan"]')
        print('---------------------------------',len(tables))

        '''<table width="100%" border="0" cellspacing="0" cellpadding="0" class="tbspan" style="margin-top:6px">
<tbody><tr> 
<td height="1" colspan="2" background="/templets/img/dot_hor.gif"></td>
</tr>
<tr> 
<td width="5%" height="26" align="center"><img src="/templets/img/item.gif" width="18" height="17"></td>
<td height="26">
	<b>
		<a class="ulink" href="/html/gndy/jddy/index.html">[综合电影]</a>
		<a href="/html/gndy/jddy/20180705/57066.html" class="ulink">2015年剧情《一切都会好的》BD中文字幕</a>
	</b>
</td>
</tr>
<tr> 
<td height="20" style="padding-left:3px">&nbsp;</td>
<td style="padding-left:3px">
				<font color="#8F8C89">日期：2018-07-04 01:32:39 
点击：0 </font>

				</td>
</tr>
<tr> 
<td colspan="2" style="padding-left:3px">[07.04][欧美][一切都会好的][BD-RMVB.720p.中字][2015年剧情] ◎译 名 一切都会好的/一切都会好/一切安好/拥抱遗忘的过去(台) ◎片 名 Every Thing Will Be Fine ◎年 代 2015 ◎国 家 德国/加拿大/法国/瑞典/挪威 ◎类 别 剧情 ◎语 言 英语 ◎字 幕 中文 ◎IMDb评分</td>
</tr>
</tbody></table>'''
        for table in tables:
            try:
                item = MovieItem()
                film_type = table.xpath('.//b/a/text()').extract()[0]
                film_name = table.xpath('.//b/a/text()').extract()[1]
                film_info = table.xpath('.//tr[last()]/td/text()').extract_first()
                item['film_type'] = film_type
                item['film_name'] = film_name
                item['film_info'] = film_info
                yield item
            except Exception as e:
                print('----------------------------------++++++++++++++++++++',e)
                pass
