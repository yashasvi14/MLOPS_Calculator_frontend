from .constants import BASE_URL
import requests

class CalculatorAPI():
    def __init__(self, var_1, var_2, operation):
        self.operation = operation
        self.params = {'num1': var_1, 'num2': var_2}
    
    def calculate(self):
        result = 0
        match self.operation:
            case 'Addition':
                result = requests.get(BASE_URL + '/add', params=self.params).json()['result']
                print(result)
            case 'Subtraction':
                result = requests.get(BASE_URL + '/subtract', params=self.params).json()['result']
            case 'Multiplication':
                result = requests.get(BASE_URL + '/multiply', params=self.params).json()['result']
            case 'Division':
                result = requests.get(BASE_URL + '/divide', params=self.params).json()['result']
        return result