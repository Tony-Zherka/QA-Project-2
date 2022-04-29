from flask import render_template
from sqlalchemy import desc
import requests
from application import app, db



if __name__=='__main__': app.run(host = "0.0.0.0",port=5000, debug=True)