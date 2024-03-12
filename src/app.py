from flask import Flask, Response, request
app = Flask(__name__)
@app.route("/", methods=["POST"])
def main():
    print(request.get_json())
    return Response("HELLOWORLD", 200)
