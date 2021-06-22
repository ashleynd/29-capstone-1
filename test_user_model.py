"""User model tests."""

# run these tests like:
#
#    python3 -m unittest test_user_model.py


import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Post

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///picslink-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for posts."""

    def setUp(self):
        """Create test client, add sample data."""
        db.drop_all()
        db.create_all()

        u1 = User.register("test_username", "password", "test_first_name", "test_last_name")
        uid1 = 1111
        u1.id = uid1

        u2 = User.register("test_username", "password", "test_first_name", "test_last_name")
        uid2 = 2222
        u2.id = uid2

        db.session.commit()

        u1 = User.query.get(uid1)
        u2 = User.query.get(uid2)

        self.u1 = u1
        self.uid1 = uid1

        self.u2 = u2
        self.uid2 = uid2

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res


    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            username="testuser",
            password="HASHED_PASSWORD",
            first_name="user_first_name",
            last_name="user_last_name",
        )

        db.session.add(u)
        db.session.commit()

        # User should have no posts
        self.assertEqual(len(u.posts), 0)

    ####
    #
    # Signup Tests
    #
    ####
    def test_valid_register(self):
        u_test = User.register("TestUser", "password", "test_first", "test_last")
        uid = 99999
        db.session.commit()

        self.assertIsNotNone(u_test)
        self.assertEqual(u_test.username, "TestUser")
        self.assertNotEqual(u_test.password, "password")
        self.assertEqual(u_test.first_name, "test_first")
        self.assertEqual(u_test.last_name, "test_last")
        # Bcrypt strings should start with $2b$
        self.assertTrue(u_test.password.startswith("$2b$"))


    ####
    #
    # Authentication Tests
    #
    ####
    def test_valid_username(self):
        self.assertFalse(User.authenticate("TestUser", "password"))

    def test_invalid_username(self):
        self.assertFalse(User.authenticate("wrongusername", "password"))

    def test_valid_password(self):
        self.assertFalse(User.authenticate("TestUser", "password"))

    def test_invalid_password(self):
        self.assertFalse(User.authenticate("TestUser", "wrongpassword"))

