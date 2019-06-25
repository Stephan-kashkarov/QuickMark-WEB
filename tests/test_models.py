import unittest
from app import create_app
from app.data import db
from app.data.models import models


class Test_User(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config='test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_init(self):
        u = models['User'](username='susan')
        db.session.add(u)
        db.session.commit()
        self.assertEquals(models['User'].query.all()[0], u)
        db.session.delete(u)

    def test_password_hashing(self):
        u = models['User'](username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config='test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


class StationTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class RollTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config='test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


class ClassTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config='test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config='test')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_Access(self):
        u1 = models['User'](username='a')
        u2 = models['User'](username='b')
        u3 = models['User'](username='c')
        c1 = models['Class'](title='a', desc='aaa')
        c2 = models['Class'](title='a', desc='aaa')
        c3 = models['Class'](title='a', desc='aaa')
        a1 = models['Access'](user_id=u1.id, class_id=c1.id)
        a2 = models['Access'](user_id=u1.id, class_id=c2.id)
        a3 = models['Access'](user_id=u1.id, class_id=c3.id)
        a4 = models['Access'](user_id=u2.id, class_id=c2.id)
        a5 = models['Access'](user_id=u2.id, class_id=c3.id)
        q1 = [
                models['Class'].query.get(x.class_id)
                for x in
                models['Access'].query.filter_by(
                    user_id=u1.id
                ).all()
            ]
        q2 = [
                models['Class'].query.get(x.class_id)
                for x in
                models['Access'].query.filter_by(
                    user_id=u2.id
                ).all()
            ]
        q3 = [
                models['Class'].query.get(x.class_id)
                for x in
                models['Access'].query.filter_by(
                    user_id=u3.id
                ).all()
            ]
        print(models['Access'].query.filter_by(
                    user_id=u1.id
                ).all())
        self.assertEquals(q1, [c1, c2, c3])
        self.assertEquals(q2, [c2, c3])
        self.assertEquals(q3, [])