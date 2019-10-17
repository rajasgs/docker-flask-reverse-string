# app.py - a minimal flask api using flask_restful
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {
            'hello': 'world',
            'one' : 'two',
            'three' : 'four'
            }

api.add_resource(HelloWorld, '/')

@app.route("/reverse")
def hello():

    name = request.args.get('name', default='Aloha')

    reverse_name = name[::-1]

    return reverse_name

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
