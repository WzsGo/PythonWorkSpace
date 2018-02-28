#-*- coding=utf-8 -*-
#导入第三方URL库文件
import urllib2
#定义url对象
url = "http://www.baidu.com"
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
#打印数据
print html