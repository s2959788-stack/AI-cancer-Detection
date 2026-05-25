from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
  return "AI Cancer Detection Project Running Successfully"
if __name__ == "__main__": 
   app.run(debug=False,use_reloader=False)
