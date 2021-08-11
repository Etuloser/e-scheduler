import unittest

from flask import url_for

from config import create_app, db


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def get_api_headers(self):
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_user_path(self):
        response = self.client.get('/user')
        self.assertEqual(response.json['code'], 10200)

    def test_status_path(self):
        response = self.client.get('/status/')
        self.assertEqual(response.json['code'], 10200)
    