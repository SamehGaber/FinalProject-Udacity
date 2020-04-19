#import app.py from .
#import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
#import json
from flask_migrate import Migrate
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

database_path ='postgresql://postgres:password@localhost:5432/capestone'
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config.from_object('config')
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app,db)
    with app.app_context():
      db.create_all()


    
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
# movie is the child and Actor is the parent 
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.String(120),nullable=False)
    Actors =db.relationship("helper_table", backref="movie")
   
   
class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120),nullable=False )  
    Movies = db.relationship("helper_table", backref="actor")

class helper_table(db.Model):
    __tablename__ = 'helper_table'
    Actor_id = db.Column(db.Integer ,db.ForeignKey('actor.id'),primary_key=True)
    Movie_id = db.Column(db.Integer ,db.ForeignKey('movie.id'),primary_key=True)

    

#db.create_all()