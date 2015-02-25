from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from mp_data_scrapper.items import MpDataScrapperItem

class MininovaSpider(CrawlSpider):

    name = 'mp'
    allowed_domains = ['india.gov.in']
    start_urls = ['http://india.gov.in/my-government/indian-parliament/lok-sabha',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=1',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=2',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=3',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=4',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=5',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=6',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=7',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=8',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=9',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=10',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=11',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=12',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=13',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=14',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=15',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=16',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=17',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=18',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=19',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=20',
                  'http://india.gov.in/my-government/indian-parliament/lok-sabha?page=21',
                 ]
    rules = [Rule(SgmlLinkExtractor(allow=['/my-government/indian-parliament/[^?]+'], deny=['my-government/indian-parliament/lok-sabha', 'my-government/indian-parliament/rajya-sabha'], unique=True), process_links='process_links', callback='parse_mp', follow=True)]

    def parse_mp(self, response):
        mp = MpDataScrapperItem()
	try:
                mp['name'] = response.xpath("//h1/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['constituency'] = response.xpath("//span[@class='views-label views-label-field-const-name-value']/following::span[1]/text()").extract()[0]
                #mp['constituency'] = response.xpath("//span[contains(concat(' ',normalize-space(@class),' '),' views-label-field-const-name-value ')]/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['party'] = response.xpath("//span[@class='views-label views-label-field-party-fname-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['father'] = response.xpath("//span[@class='views-label views-label-field-father-name-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['mother'] = response.xpath("//span[@class='views-label views-label-field-mother-name-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['dob'] = response.xpath("//span[@class='views-label views-label-field-dob-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['birth_place'] = response.xpath("//span[@class='views-label views-label-field-birth-place-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['marital_status'] = response.xpath("//span[@class='views-label views-label-field-marital-status-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['spouse_name'] = response.xpath("//span[@class='views-label views-label-field-spouse-name-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['num_sons'] = response.xpath("//span[@class='views-label views-label-field-sons-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['num_daughters'] = response.xpath("//span[@class='views-label views-label-field-daughters-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['state'] = response.xpath("//span[@class='views-label views-label-field-state-name-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['permanent_address'] = response.xpath("//span[@class='views-label views-label-phpcode-1']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['present_address'] = response.xpath("//span[@class='views-label views-label-phpcode-2']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['email'] = response.xpath("//span[@class='views-label views-label-field-email-value']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['education'] = response.xpath("//span[@class='views-label views-label-phpcode-5']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['positions_held'] = response.xpath("//span[@class='views-label views-label-phpcode']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['social_cultural_activities'] = response.xpath("//span[@class='views-label views-label-phpcode-7']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['sports_clubs'] = response.xpath("//span[@class='views-label views-label-phpcode-8']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['pastimes_recreation'] = response.xpath("//span[@class='views-label views-label-phpcode-9']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['countries_visited'] = response.xpath("//span[@class='views-label views-label-phpcode-4']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['other_info'] = response.xpath("//span[@class='views-label views-label-phpcode-3']/following::span[1]/text()").extract()[0]
	except IndexError:
	        pass
	try:
                mp['photo'] = 'http://india.gov.in' + response.xpath("//div[@class='views-field views-field-phpcode-10']/child::span[1]/child::img[1]/@src").extract()[0]
	except IndexError:
	        pass
        return mp

    def process_links(self,links):
        for i, w in enumerate(links):
            print w.url
            #w.url = w.url.replace("http://india.gov.in/my-government/indian-parliament/lok-sabha", "http://india.gov.in")
            links[i] = w
        return links
