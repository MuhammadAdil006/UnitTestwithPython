

import unittest
from phoneBook import PhoneBook
from contact import Contact

class Test_module(unittest.TestCase):
    
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.phonebook=PhoneBook()
        a=Contact('adil',123)
        b=Contact('bassam',1231)
        c=Contact('dar',123)
        self.phonebook.add(a)
        self.phonebook.add(b)
        self.phonebook.add(c)

    def test_consistency(self):
        self.assertTrue(self.phonebook.consistentOrNot(),True)
    # def test_equal(self):
    #     # self.assertEqual(5+5,10)
    #     self.assertNotEqual(5,1)
    # def test_conditions(self):
    #     self.assertTrue(4>3)
    #     self.assertFalse(3>4)
    # def test_conditions(self):
    #     self.assertTrue(4>3)
    #     self.assertFalse(3>4)
    # def test_isobjectOrNot(self):
    #     #Test that first and second are (or are not) the same object.
    #     self.assertIs(5,'5')
    #     self.assertIsNot(5,'5')
    # def test_isNoneOrNot(self):
    #     #test that expr is (or is not) None.
    #     self.assertIsNone(None)
    #     self.assertIsNotNone(None)
    # def test_isInstance(self):
    #     self.assertIsInstance(5,[1,2,5])
    #     self.assertNotIsInstance(5,[1,3,5])
    # def test_almostEqual(self):
    #     self.assertAlmostEqual(1.113,1.123,2)
    # def test_assertListEqual(self):
    #     self.assertListEqual([1,2],[2,1])
    # def test_regex(self):
    #     self.assertRegex("1234hellow","^\d*hellow$")


if __name__=='__main__':
    unittest.main()