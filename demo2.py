from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Demo 2 complete !"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
