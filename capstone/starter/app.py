import os
from flask import Flask, request, abort, jsonify , render_template, Response, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from models import Movie , Actor ,setup_db ,db
# app configuration # 
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  moment = Moment(app)
  setup_db(app)

  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Contro-Allow-Headers','Content-Type ,Authorization')
    response.headers.add('Access-Contro-Allow-Headers','GET, POST ,PATCH , DELETE ,OPTIONS')
    response.headers.add('Access-Control-Allow-Origin' ,  'http://localhost:5000')
    return response 

  '''
  testing end point
  '''
  @app.route('/hello', methods=['GET'])
  def test_api():
    return jsonify({
      'success': True ,
      'hello' : "hello there "
    })
  

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)