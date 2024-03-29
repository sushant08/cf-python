#!/usr/bin/env python
import unittest
from app import app
from flask import Flask, url_for

class FlaskBookshelfTests(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the response data
        self.assertEqual(result.data, "Welcome")

    def test_articles_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/articles') 

        # assert the response data
        self.assertEqual(result.data, "List of /articles")

    def test_articles_test_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/articles/test') 

        # assert the response data
        self.assertEqual(result.data, "You are reading test")
if __name__ == "__main__":
    unittest.main()
