from flask import url_for
from flask_testing import TestCase

from app import app, perk_one

class TestPerkOne(TestCase):
    def create_app(self):
        return app

class TestPerkOne(TestPerkOne):
    def test_perk_one(self):
        response = self.client.get(url_for('get_perk1'))
        self.assertIn(response.json, perk_one)