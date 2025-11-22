from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def slow():
    time.sleep(10)  # simulate slow backend
    return "Hello! This is the SLOW app — it waited 10 seconds.\n"

if __name__ == "__main__":
    app.run()
