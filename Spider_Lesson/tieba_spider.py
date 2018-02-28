#-*- coding=utf-8 -*-
import urllib2

def load_page(url):
	'''
		网页加载的方法
	'''
	#定义 浏览器代理 ，模拟浏览器访问
	user_agent = "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;"
	#定义一个字典数据类型，作为请求的头部文件
	headers = {'User-Agent':user_agent}
	#建立请求，使用Request方法，输入URL和headers属性
	req = urllib2.Request(url,headers = headers)
	#打开请求，得到响应
	response = urllib2.urlopen(req)
	#读出 response响应
	html = response.read()
	#返回数据
	return html

def write_to_file(file_name,txt):
	'''
		将请求的内容TXT 写入到 file_name 文件中
	'''
	print(file_name +"正在存储...")
	#1: 打开文件，以w权限
	f = open(file_name,'w')
	#2：写入内容
	f.write(txt)
	#3:关闭文件
	f.close

def tieba_spider(url,begin_page,end_page):
	'''
		贴吧爬虫函数
	'''
	for i in range(begin_page,end_page+1):
		pn = 50 * (i - 1)
		myURL = url + str(pn)
		html = load_page(myURL)

		file_name = str(i)+".html"
		write_to_file(file_name,html)
		
#main
if __name__ == '__main__':
	#url = raw_input("请输入网址：\n")
	url = "http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="
	#begin_page = int(raw_input("请输入起始页码：\n"))
	#end_page = int(raw_input("请输入结束页码：\n"))

	begin_page = 1
	end_page = 2

	tieba_spider(url,begin_page,end_page)