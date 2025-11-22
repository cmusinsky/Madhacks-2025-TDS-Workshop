from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def fast():
    return "Hello! This is the FAST app — response is instantaneous.\n"

if __name__ == "__main__":
    app.run()
