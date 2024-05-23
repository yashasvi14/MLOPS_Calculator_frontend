from flask import render_template, request, make_response
from flask_restful import Resource
from .controller import CalculatorAPI

    
class CalculatorWebpage(Resource):
    "A simple calculations app"
    def get(self):
        
        print('GET request received')
        return make_response(render_template("calculations.html"))
    
    def post(self):

        var_1 = request.form.get("var_1", type=int, default=0)
        var_2 = request.form.get("var_2", type=int, default=0)
        operation = request.form.get("operation")

        cal = CalculatorAPI(var_1, var_2, operation)
        result = cal.calculate()

        return make_response(render_template("calculations.html", entry=result))