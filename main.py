# -*- coding: utf-8 -*-
# filename: main.py
import web
from weixin_server.handle import Handle
import time
import base64
import hashlib
#url映射
urls=(
	'/zhihu','demo2',#根目录
	'/love','demo3',
	'/wx', 'Handle',#微信公众号消息接收地址
	'/time','timer',#时间记录
	'/test','index',
	# '/(.*)','demo1',#匹配的内容回会传入到函数里

)
app=web.application(urls,globals())

class index(object):
	"""page"""
	def GET(self):
		render=web.template.render('./')
		return render.first()

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
class timer(object):
	"""docstring for demo"""
	def GET(self):
		# render=web.template.frender("demo1/index.html")
		a=time.asctime(time.localtime(time.time()))
		b=str(time.time())
		c=a+'\n'+b
		return c
		
if __name__ == '__main__':
	app.run()
	# print base64.b64encode('')
	# print base64.b64decode('96e79218965eb72c92a549dd5a330112')
	# m=hashlib.md5()
	# m.update('111111')
	# print m.hexdigest()

