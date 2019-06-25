import unittest
from app import create_app
from app.data import db
from app.data.models import models


class Test_User(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config='test')
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_init(self):
        u = models['User'](username='susan')
        db.session.add(u)
        db.session.commit()
        assertEquals(models['User'].query.all()[0], u)
        db.session.delete(u)

    def test_password_hashing(self):
        u = models['User'](username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_class_link(self):
        pass


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class StationTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class RollTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class ClassTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()