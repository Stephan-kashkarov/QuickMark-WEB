import unittest
from ../../app import create_app
from ../../app.data import db


class Base_Model_test(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
