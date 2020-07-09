# app.py - a minimal flask api using flask_restful
from flask import Flask, request
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)

class HelloWorld(Resource):
    
    def get(self):
        return {
            "name" : "John",
            "city" : "Toronto",
            "country" : "Canada"
            }

api.add_resource(HelloWorld, '/')

@application.route("/reverse")
def hello():

    name = request.args.get('name', default='Aloha')
    reverse_name = name[::-1]

    return reverse_name

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
