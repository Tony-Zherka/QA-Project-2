from flask import Flask, jsonify
import random
app = Flask(__name__)


if __name__=='__main__': app.run(host = "0.0.0.0", port=5002, debug=True)