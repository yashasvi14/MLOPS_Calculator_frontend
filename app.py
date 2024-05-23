from flask import Flask 
from flask_restful import Api, Resource
from packages.helloworld import HelloWorld
from packages.calculator_page import CalculatorWebpage

app = Flask(__name__) 

api = Api(app) 

api.add_resource(HelloWorld, '/hello', '/')
api.add_resource(CalculatorWebpage, '/calculator')


if __name__=='__main__': 
	app.run(debug=False)
