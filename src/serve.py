from waitress import serve
import app
import TextGeneration
TextGeneration.LoadModel()
print("Model loaded")
serve(app.app, host='127.0.0.1', port=8080)