from flask_restful import Resource

class HelloWorld(Resource):
	"""
	A simple hello world app that shows how to use flask_restful
	"""
	def get(self):
		data= "Hello World"
		return data