from flask import Flask

app = Flask(__name__)

# Catch root path
@app.route("/")
def index():
    return "Hello from the Ragul to the World!"

# Catch all other paths
@app.route("/<path:dummy>")
def catch_all(dummy):
    return f"Hello from the Ragul to the World! (You hit /{dummy})"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
