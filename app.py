from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the Ragul to the World!"

# Catch-all route for anything else
@app.route("/<path:path>")
def catch_all(path):
    return f"Catch-all hit! Path: /{path} — Hello from Ragul!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
