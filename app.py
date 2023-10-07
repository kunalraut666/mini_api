from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def dataChecker(data, functionName):
    if functionName == "add" or functionName == "multi" or functionName == "sub":
        if "x" not in data or "y" not in data:
            return 301
        else:
            return 200
    
    if functionName == "div":
        if "x" not in data or "y" not in data:
            return 301
        elif data['y'] == 0:
            return 302     
        else:
            return 200

class Add(Resource):
    def post(self):
        dataPosted = request.get_json()
        validation_code = dataChecker(dataPosted, "add")

        if validation_code!=200:
            retJson = {
                "Message": "Required parameters are missing",
                "status code": 301
            }

            return jsonify(retJson)

        x = int(dataPosted['x'])
        y = int(dataPosted['y'])

        ret = x+y

        retMap = {
            "Message": ret,
            "Status code": 200 
        }
        return jsonify(retMap)


class Multiply(Resource):
    def post(self):
        dataPosted = request.get_json()
        validation_code = dataChecker(dataPosted, "multi")

        if validation_code!=200:
            retJson = {
                "Message": "Required parameters are missing",
                "status code": 301
            }

            return jsonify(retJson)
        
        x = int(dataPosted['x'])
        y = int(dataPosted['y'])

        ret = x*y

        retMap = {
            "Message": ret,
            "Status code": 200 
        }
        return jsonify(retMap)

class Subtraction(Resource):
    def post(self):
        dataPosted = request.get_json()
        validation_code = dataChecker(dataPosted, "sub")

        if validation_code!=200:
            retJson = {
                "Message": "Required parameters are missing",
                "status code": 301
            }

            return jsonify(retJson)
        
        x = int(dataPosted['x'])
        y = int(dataPosted['y'])

        ret = x-y

        retMap = {
            "Message": ret,
            "Status code": 200 
        }
        return jsonify(retMap)

class Division(Resource):
    def post(self):
        dataPosted = request.get_json()
        validation_code = dataChecker(dataPosted, "div")

        if validation_code==301:
            retJson = {
                "Message": "Required parameters are missing",
                "status code": 301
            }

            return jsonify(retJson)
        
        if validation_code==302:
            retJson = {
                "Message": "Cannot divide by zero",
                "status code": 302
            }

            return jsonify(retJson)
        
        else:
            x = int(dataPosted['x'])
            y = int(dataPosted['y'])

            ret = x/y

            retMap = {
                "Message": ret,
                "Status code": 200 
            }
            return jsonify(retMap)

api.add_resource(Add, "/add")
api.add_resource(Multiply, "/multi")
api.add_resource(Subtraction, "/sub")
api.add_resource(Division, "/div")

@app.route("/add/two/num", methods=["POST"])
def add_num():
    dataDict = request.get_json()
    x = dataDict['x'];
    y = dataDict['y'];

    return jsonify(x+y)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')