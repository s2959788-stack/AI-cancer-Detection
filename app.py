from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    if file:
        return "File uploaded successfully!"

    return "No file selected"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
