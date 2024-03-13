from flask import Flask, Response, request, redirect
from TextGeneration import GenerateText, GenerateModelInput
app = Flask(__name__)
Generating = False
@app.route("/", methods=["GET","POST"])
def main():
    if request.method == "GET":
        return redirect("https://www.youtube.com/watch?v=xvFZjo5PgG0")
    global Generating
    if not(Generating):
        Generating = True
        AIResponse = GenerateText(GenerateModelInput(request.get_json()))
        Generating = False
        return Response(AIResponse, 200)
    else:
        return Response("Generating Right now", 501)
    return Response("Unknown error", 503)