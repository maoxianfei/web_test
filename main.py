import web
urls=(
	'/','index',
	'/demo','demo',
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
