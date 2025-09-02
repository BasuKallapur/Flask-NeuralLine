from flask import Flask, request

app= Flask(__name__)

@app.route('/')
def index():
    return "Hello Basavaraj"

# @app.route('/hello', methods= ['GET', 'POST'])
# def hello():
#     if request.method == 'GET':
#         return 'you made a GET request \n'
#     elif request.method == 'POST':
#         return 'you made a GET request \n'
#     return "you will never see this messege \n"   
     
@app.route('/hello')
def hello():
    return 'hello world!', 201      

@app.route('/greet/<name>')
def greet(name):
    return f'Hello {name} bro'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f'sum of {num1} + {num2} is {num1 + num2}'

@app.route('/handle_url_params')
def handle_params():
    greeting= request.args['greeting']
    name= request.args['name']
    return f'{greeting}, {name}'

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=True)

