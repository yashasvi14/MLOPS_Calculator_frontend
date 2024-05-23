import os

SPRING_HOST_NAME = os.getenv('SPRING_HOST_NAME', '127.0.0.1')
SPRING_HOST_PORT = os.getenv('SPRING_HOST_PORT', '8080')
BASE_URL = 'http://' + SPRING_HOST_NAME + ':' + SPRING_HOST_PORT + '/api/calculator'