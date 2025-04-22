from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the Ragul to the World!"

@app.route("/<path:path>")
def catch_all(path):
    return f"Hello from Ragul — you requested: /{path}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
