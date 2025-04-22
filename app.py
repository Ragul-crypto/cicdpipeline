from flask import Flask

app = Flask(__name__)

@app.route("/favicon.ico")
def home():
    return "Hello from the Ragul to the World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
