import unittest

from cybox.common import String
from cybox.objects.address_object import Address, EmailAddress
from cybox.test import round_trip
from cybox.test.objects import ObjectTestCase


class TestAddress(unittest.TestCase, ObjectTestCase):
    object_type = "AddressObjectType"
    klass = Address

    def test_round_trip(self):
        v = String("test@example.com")
        c = Address.CAT_EMAIL

        a = Address()
        a.address_value = v
        a.category = c

        addr2 = round_trip(a, Address, output=False)

        self.assertEqual(addr2.address_value, v)
        self.assertEqual(addr2.category, c)

    def test_roundtrip2(self):
        addr_dict = {'address_value': "1.2.3.4",
                     'category': Address.CAT_IPV4,
                     'is_destination': True,
                     'is_source': False}
        addr_obj = Address.object_from_dict(addr_dict)
        addr_dict2 = Address.dict_from_object(addr_obj)
        self.assertEqual(addr_dict, addr_dict2)


class TestEmailAddress(unittest.TestCase):

    def test_create_email_address(self):
        a = "test@example.com"
        addr = EmailAddress(a)
        self.assertTrue(isinstance(addr, EmailAddress))
        self.assertTrue(isinstance(addr, Address))
        self.assertEqual(addr.to_dict(), {'address_value': a,
                                          'category': Address.CAT_EMAIL})

if __name__ == "__main__":
    unittest.main()
