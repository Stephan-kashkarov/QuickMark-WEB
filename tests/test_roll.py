import unittest
from ../../app.data import db
from ../../app import create_app
from ../../app.data.models import models


class RollTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
