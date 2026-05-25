from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
  return"AI Cancer Detection Project Runing Successfully"
if __name__ == "__main__": 
  app.run(debug=True)
