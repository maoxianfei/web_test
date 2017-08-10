# -*- coding: utf-8 -*-
# filename: main.py
import web
from weixin_server.handle import Handle
#url映射
urls=(
	'/zhihu','demo2',#根目录
	'/love','demo3',
	'/wx', 'Handle',#微信公众号消息接收地址
	'/(.*)','demo1',#匹配的内容回会传入到函数里
)
app=web.application(urls,globals())

class index(object):
	"""docstring for index"""
	def GET(self):
		return "Hello,World"

class demo1(object):
	"""docstring for demo"""
	def GET(self,name):
		# render=web.template.frender("demo1/index.html")
		return open(r'demo1/index.html','r').read()
class demo2(object):
	"""docstring for demo"""
	def GET(self):
		# render=web.template.frender("demo1/index.html")
		return open(r'demo1/index2.html','r').read()
class demo3(object):
	"""docstring for demo"""
	def GET(self):
		# render=web.template.frender("demo1/index.html")
		return open(r'demo1/heart.html','r').read()
		
if __name__ == '__main__':
	app.run()
