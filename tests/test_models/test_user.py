#!/usr/bin/python3
"""
Unittest for the User class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_user.py
"""
import unittest
import pycodestyle
from os import path, remove
import datetime
import models
from models import user
from models.user import User
from models.engine.file_storage import FileStorage


class Test_User(unittest.TestCase):
    """ Declares TestUser class """

    def setUp(self):
        """
        Assigns an empty string to public class attributes of User ""
        Method called to prepare the test fixture.
        It gets called immediately before calling the test method
        """
        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def tearDown(self):
        """
        Deletes public class props from User
        Method called immediately after the test method is called
        """
        del User.email
        del User.password
        del User.first_name
        del User.last_name
        del FileStorage._FileStorage__file_path
        del FileStorage._FileStorage__objects
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8(self):
        """ Test that User conforms to PEP8 standards """
        pyco = pycodestyle.StyleGuide(quiet=True)
        result = pyco.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Errors (and warnings).")

    def test_class_method(self):
        """ Test that the User methods are defined """
        u = dir(User)
        self.assertIn('__init__', u)
        self.assertIn('to_dict', u)
        self.assertIn('save', u)
        self.assertIn('__str__', u)

    def test_class_attribute(self):
        """ Test that the User attributes are declared """
        u = dir(User)
        self.assertIn('email', u)
        self.assertIn('password', u)
        self.assertIn('first_name', u)
        self.assertIn('last_name', u)

    def test_instance_method(self):
        """Test that the User instance has the same methods"""
        u = dir(User())
        self.assertIn('__init__', u)
        self.assertIn('save', u)
        self.assertIn('to_dict', u)
        self.assertIn('__str__', u)

    def test_instance_attribute(self):
        """Test that the User instance attributes are declared"""
        u = dir(User())
        self.assertIn('id', u)
        self.assertIn('updated_at', u)
        self.assertIn('created_at', u)
        self.assertIn('__class__', u)
        self.assertIn('email', u)
        self.assertIn('password', u)
        self.assertIn('first_name', u)
        self.assertIn('last_name', u)

    def test_docstring(self):
        """Test that docstring is present
        in Module, Class, and methods"""
        self.assertIsNot(user.__doc__, None)
        self.assertIsNot(User.__doc__, None)
        self.assertIsNot(User.__init__.__doc__, None)
        self.assertIsNot(User.save.__doc__, None)
        self.assertIsNot(User.to_dict.__doc__, None)
        self.assertIsNot(User.__str__.__doc__, None)

    def test_instantiation(self):
        """Test correct instantiation of object of type User"""

        u = User()
        self.assertIsInstance(u, User)
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.created_at, datetime.datetime)
        self.assertIsInstance(u.updated_at, datetime.datetime)
        self.assertIsInstance(u.__class__, type)

        u.size = "Short"
        lu = dir(u)
        self.assertIn('size', lu)
        self.assertEqual(u.__dict__['size'], 'Short')

        u.size = 'Short'
        ll = dir(u)
        self.assertIn('size', ll)
        self.assertEqual(u.__dict__['size'], 'Short')

        u.age = 32
        l3 = dir(u)
        self.assertIn('age', l3)
        self.assertEqual(u.__dict__['age'], 32)

        u.age = 32.5
        l4 = dir(u)
        self.assertIn('age', l4)
        self.assertEqual(u.__dict__['age'], 32.5)

        u.age = None
        l5 = dir(u)
        self.assertIn('age', l5)
        self.assertEqual(u.__dict__['age'], None)

        us1 = User(**{})
        self.assertIsInstance(us1, User)
        self.assertIsInstance(us1.id, str)
        self.assertIsInstance(us1.created_at, datetime.datetime)
        self.assertIsInstance(us1.updated_at, datetime.datetime)
        self.assertIsInstance(us1.__class__, type)

        # us2 = User(**{"first_name": "Rachid", "age": 32})
        # l6 = dir(us2)
        # self.assertIn('first_name', l6)
        # self.assertIn('age', l6)
        # self.assertEqual(us2.__dict__['first_name'], 'Rachid')
        # self.assertEqual(us2.__dict__['age'], 32)

    def test_save(self):
        """Test save method"""

        us = User()
        temp = us.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        us.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(us.__dict__['updated_at'], temp)
        temp = us.__dict__['updated_at']
        models.storage.reload()
        self.assertEqual(us.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method call"""

        ins = User()
        ins.age = 32
        ins.size = "Short"
        for k, v in ins.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, ins.to_dict())
                self.assertEqual(v, ins.to_dict()[k])
        self.assertEqual(ins.to_dict()['__class__'], ins.__class__.__name__)
        self.assertEqual(ins.to_dict()['updated_at'],ins.updated_at.isoformat())
        self.assertEqual(ins.to_dict()['created_at'],ins.created_at.isoformat())
        self.assertEqual(ins.to_dict()['age'], 32)
        self.assertEqual(ins.to_dict()['size'], 'Short')
        self.assertIsInstance(ins.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        ins = User()
        string = '['+ins.__class__.__name__+']'+' ('+ins.id+') '+str(ins.__dict__)
        self.assertEqual(string, ins.__str__())