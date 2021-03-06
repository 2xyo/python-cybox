import unittest
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.mutex_object_1_3 as mutex_binding
from cybox.objects.mutex_object import Mutex


class MutexTest(unittest.TestCase):
    def setUp(self):
        self.test_dict = {'named': True, 'name': {'value': 'test_name'}}
        self.mutex_obj = Mutex.object_from_dict(self.test_dict)
        self.mutex_dict = Mutex.dict_from_object(self.mutex_obj)

    def test_obj_from_dict(self):
        #Make sure it's an instance of the right class
        self.assertIsInstance(self.mutex_obj, mutex_binding.MutexObjectType)
        #Test the named attribute
        self.assertEqual(self.mutex_obj.get_named(), True)
        #Test the name element
        self.assertIsInstance(self.mutex_obj.get_Name(),
                common_types_binding.StringObjectAttributeType)
        self.assertEqual(self.mutex_obj.get_Name().get_valueOf_(), 'test_name')

    def test_dict_from_obj(self):
        #Make sure it's an instance of the right class
        self.assertIsInstance(self.mutex_dict, dict)
        #Test the dictionary values
        self.assertEqual(self.mutex_dict['named'], True)
        self.assertEqual(self.mutex_dict['name']['value'], 'test_name')

if __name__ == "__main__":
    unittest.main()
