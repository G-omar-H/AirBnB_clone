#!/usr/bin/python3
"""
AirBnB cloning prototype protect Unittesting...
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        set up class...
        """
        cls.obj = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """
        tear down the class
        """
        pass


    def test_instance(self):
        """
        test class instance creation
        """
        self.assertTrue(self.obj.__class__)

    def test_collision(self):
        """
        test for potential collision
        """
        obj_2 = BaseModel()
        self.assertNotEqual(self.obj, obj_2)
        self.assertIsNot(self.obj, obj_2)
    
    def test_print_obj(self):
        """
        test string format on an object
        """
        obj_2 = BaseModel()
        self.assertEqual(str(self.obj), self.obj.__str__())
        self.assertIsNot(str(obj_2), self.obj)

    def test_id(self):
        """
        test id attribute of BaseModel
        """
        obj_2 = BaseModel()
        obj_3 = BaseModel()
        self.assertTrue(obj_2.id)
        self.assertTrue(obj_3.id)
        self.assertNotEqual(obj_2.id, self.obj.id)
        self.assertNotEqual(obj_3.id, obj_2)
        self.assertNotEqual(obj_3.id, self.obj)

    def test_updated_at(self):
        """
        test updated_at BaseModel attribute
        """
        
        obj_temp = BaseModel()
        self.assertTrue(obj_temp.created_at)
        self.assertEqual(obj_temp.updated_at, obj_temp.created_at)
        obj_temp.save()
        self.assertNotEqual(obj_temp.updated_at, obj_temp.created_at)

    def test_created_at(self):
        """
        test created_at BaseModel attribute
        """
        obj_temp = BaseModel()
        self.assertTrue(obj_temp.created_at)
        self.assertEqual(obj_temp.updated_at, obj_temp.created_at)
        obj_temp.save()
        self.assertNotEqual(obj_temp.updated_at, obj_temp.created_at)


if __name__ == "__main__":
    unittest.Test_BaseModel()
