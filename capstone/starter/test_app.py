import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import Movie , Actor ,setup_db ,db

class CapestoneTestCase(unittest.TestCase):
    """This class represents the capestone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capestone_test"
        self.database_path ='postgresql://postgres:password@localhost:5432/capestone_test'
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    
   #Actors endpoints test cases  
    #testing getting all actors 
    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_actors'])
        self.assertTrue(len(data['actors']))

    #Testing adding a new actor(successful trial )
    def test_add_actor(self):
        res = self.client().post('/actors',
        json={'name': ' fake actor',
              'age': '55',
              'gender': 'fake female'
              })
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_actors'])
        self.assertTrue(len(data['actors']))

    #test editing an actor (successful trial)
    def test_patch_actor(self):
        res = self.client().patch('actors/7',
        json={'name': 'dalia mahmoud ',
               'age': 20,
               'gender': 'female',
                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    #test editing an actor ( non-successful trial)
    def test_patch_actor_2(self):
        res = self.client().patch('actors/24',
        json={'name': 'sameh gaber karar ',
               'age': 44,
               'gender': 'male',
                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found ")
 

    #testing deleting an actor (successful trial)
    def test_delete_actor(self):
        res = self.client().delete('/actors/9')
        data =json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    #testing deleting a actor ( non-successful trial)
    def test_delete_actor_2(self):
        res = self.client().delete('/actors/102')
        data =json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], "resource not found ")



   #Movies endpoints test cases  

    
    #testing getting all movies 
    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_movies'])
        self.assertTrue(len(data['movies']))
      
    #Testing adding a new movie 
    def test_add_movie(self):
        res = self.client().post('/movies',
        json={'title': 'lacasa de papel',
              'release_date': '22nd april ',
              'actors': [7]
              })
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_movies'])
        self.assertTrue(len(data['movies']))

    #test editing a movie (successful trail)
    def test_patch_movie(self):
        res = self.client().patch('movies/8',
        json={'title': 'my second movie ',
               'release_date': 'a long ago',
               'actors': []

                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    #test editing a movie (non-successful trial)
    def test_patch_movie_2(self):
        res = self.client().patch('movies/22',
        json={'title': 'my movie ',
               'release_date': 'a long ago',
               'actors': [4,5]

                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "resource not found ")

    #testing deleting a movie (successful trial )
    def test_delete_movie(self):
        res = self.client().delete('/movies/9')
        data =json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)

    #testing deleting a movie (non-successful trial ))
    def test_delete_movie_2(self):
        res = self.client().delete('/movies/102')
        data =json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], "resource not found ")
    
   

    

    


    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()