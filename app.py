# app.py - a minimal flask api using flask_restful
from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api
import os

application = Flask(__name__)
api = Api(application)

class HelloWorld(Resource):
    
    def get(self):
        return {
            "name" : "John",
            "city" : "Toronto",
            "country" : "Canada"
            }

# api.add_resource(HelloWorld, '/')

@application.route("/reverse")
def hello():

    name = request.args.get('name', default='Aloha')
    reverse_name = name[::-1]

    return reverse_name

def reverse_name(name):

    reverse_name = name[::-1]
    return reverse_name

@application.route('/env', methods=['GET'])
def show_env():

    env =  os.environ.get('app-env', "base")

    response = jsonify({'env': env})
    response.status_code = 200
    return response

@application.route('/', methods=['GET', 'POST'])
def home():

    if(request.method == 'GET'):
        return render_template('index.html')

    # Post
    name  = request.form.get('name')
    
    r_name = reverse_name(name)
    
    result = {
        'name' : name,
        'r_name' : r_name
    }
    
    #return content
    return render_template('index.html', result=result)

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
