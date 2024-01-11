from flask  import Flask

api = Flask(__name__)

@api.route("/",methods=["GET"])
def hello():
    return "helloworld"
# @api.route("/add", methods=["GET"])
# def add():
#     num1 = int(request.args.get("num1", 0))
#     num2 = int(request.args.get("num2", 0))
#     result = num1 + num2
#     return jsonify({'result': result})

if __name__ == "__main__":
    api.run(host="0.0.0.0")
