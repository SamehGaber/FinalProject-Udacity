import app.py from .
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
'''
app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

# TODO: connect to a local postgresql database
migrate = Migrate(app,db) # making an instance of Migrate Class and link it to the app and DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/fyyur'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db) # making an instance of Migrate Class and link it to the app and DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/capestone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
'''
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
# movie is the child and Actor is the parent 
class Movie(db.Model):
    __tablename__ = 'Movie'
    #__searchable__= ["name","city","state","address"]
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.String(120),nullable=False)
    Actor_id = db.Column(db.Integer ,db.ForeignKey('Actor.id'),nullable=False)
    te
class Actor(db.Model):
    __tablename__ = 'Actor'
    #__searchable__= ["name","city","state"]
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120),nullable=False )  
    shows_movie = db.relationship("Movie", backref="Actor")
    