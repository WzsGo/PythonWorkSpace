#-*- coding=utf-8 -*-
import urllib2
import re

#定义爬虫类，集成常用方法
class spider:
	'''
		爬虫类
	'''
	def __init__(self):
		'''
			初始化函数
		'''
		self.enable = True

		self.page = 2

	def write_to_file(self,txt):
		'''
			将所有数据写到一个文件中
		'''
		file_name = "duanzi.txt"


		f = open(file_name,'a')

		#f.write('----------------------------------------------------')

		f.write(txt)

		f.close() 

	def deal_onepage(self,item_list,page):
		'''
			处理每一页的数据
		'''
		print("***第%d页 正在存储...***") %(page)
		for item in item_list:
			item.replace("&amp","").replace("hellip","")
			self.write_to_file(item)
			self.write_to_file("\n----------------------------\n")
		print("***第%d页 存储完毕...***") %(page)

	def load_page(self,page):
		'''
			加载网页方法：发送请求并返回response
		'''
	
		'''
			step1:获取网站全部内容，根据指定范围
		'''
		#需要爬取的网站
		url = "http://www.neihanpa.com/article/index_"+str(page)+".html"
		#print url 
		#模拟代理浏览器 IE9.0
		uesr_agent = "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"
		#生成同步文件数据-字典类型数据
		headers = {"User-Agent":uesr_agent}
		#利用Request将连接URL和headers 封装成 seq请求，
		req = urllib2.Request(url,headers = headers)
		#利用urlopen方法打开req请求，得到响应
		response = urllib2.urlopen(req)
		#读出响应
		html = response.read()
		#以上内容得到的网页的全部内容
		'''
			step2:对网页的原始数据，通过正则表达式进行筛选，得到我们关注的内容
		'''
		#定义 正则表达式对象 
		patter = re.compile(r'<div.*?class="desc">(.*?)</div>',re.S)
		#进行匹配，得到结果
		item_result=patter.findall(html)
		'''
			step3:返回数据
		'''
		return item_result
	def do_work(self):
		'''
			循环工作函数
			通过Enter是的爬虫持续工作或者停止
		'''
		while self.enable:
			print("按Enter键继续\n输入quit退出")
			command = raw_input()
			if (command == "quit"):
				self.enable = False
				break;
			#
			item_list = self.load_page(self.page)
			#
			self.deal_onepage(item_list,self.page)
			#
			self.page +=1



#main
if __name__ == '__main__':
	my_spider = spider()
	my_spider.do_work()
