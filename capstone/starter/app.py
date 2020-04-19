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

  
  #testing end point
  
  @app.route('/hello', methods=['GET'])
  def test_api():
    return jsonify({
      'success': True ,
      'hello' : "hello there "
    })

  #list all the actors 
  @app.route('/actors', methods=['GET'])
  def get_actors():
    
    actors = Actor.query.all()
    formatted_actors = [actor.format() for actor in actors]
    if len(formatted_actors) == 0:
        abort(404)

    return jsonify({
      'success': True ,
      'actors' : formatted_actors ,
      'total_actors' : len(formatted_actors)
    })
   
  # adding a new actor 
  @app.route('/actors', methods=['post'])
  def add_new_actor(): 
    body = request.get_json()
    name= body.get('name', None)
    age= body.get('age', None)
    gender= body.get('gender', None)
    
    
    actor = Actor(name=name, age=age , gender=gender)
    actor.insert()
    actors = Actor.query.all()
    formatted_actors = [actor.format() for actor in actors]

    return jsonify ({
      'success': True ,
      'actors' : formatted_actors ,
      'total_actors' : len(formatted_actors) ,
      'created' : actor.id 
      })
  
  # updating  a specifc actor 
  @app.route('/actors/<int:id>', methods=['PATCH'])
  def update_actor(id):
    actor = Actor.query.filter(Actor.id == id).one_or_none()
    body = request.get_json()
    actor.name = body.get('name', actor.name)
    actor.age = body.get('age', actor.age)
    actor.gender = body.get('gender', actor.gender)
    actor.update()
    actors = Actor.query.all()
    formatted_actors = [actor.format() for actor in actors]

    return jsonify ({
      'success': True ,
      'actors' : formatted_actors ,
      'modified_actor' : id 
      })
  # deleting a specifc actor 
  @app.route('/actors/<int:id>', methods=['DELETE'])
  def delete_actor(id):
    selected_actor=Actor.query.get(id)
    selected_actor.delete()

    if selected_actor is None:
      abort(404)

    return jsonify ({
        'success': True ,
        'deleted' : id 
      })

  

  #Error Handeling 
  @app.errorhandler(404)
  def unprocessable(error):
     return jsonify({
       "success" : False,
       "error" : 404 ,
       "message" : "resource not found "
     }) ,404








    



  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)