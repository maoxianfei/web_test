# -*- coding: utf-8 -*-
# filename: main.py
import web
from weixin_server.handle import Handle
#url映射
urls=(
	'/hello','index',#根目录
	'/aa','index',
	'/wx', 'Handle',#微信公众号消息接收地址
	'/(.*)','demo',#演示程序
)
app=web.application(urls,globals())

class index(object):
	"""docstring for index"""
	def GET(self):
		return "hello"

class demo(object):
	"""docstring for demo"""
	def GET(self):
		# render=web.template.frender("demo1/index.html")
		return open(r'demo1/index.html','r').read()
		
if __name__ == '__main__':
	app.run()
