from flask import url_for
from flask_testing import TestCase
from app import app, perk_two, gun_effect
import random

class TestPerkTwo(TestCase):
    def create_app(self):
        return app

class TestPerkTwo(TestPerkTwo):
    def test_perk_two(self):
        response = self.client.get(url_for('get_perk2'))
        self.assertEqual(response.status_code, 405)
        

    def test_perk_two(self):
        perk_one = random.choice(list(perk_two))
        gun = random.choice(list(gun_effect))
        generate = {'gun': gun, 'perk_one': perk_one}
        response = self.client.post(url_for('get_perk2'), json=generate)
        self.assertEqual(response.status_code, 200)
        self.assertIn(gun, response.json['gun'])
        self.assertIn(perk_one, response.json['perk_one'])
        
        