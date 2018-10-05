import unittest
from user import User
from normal_user import NormalUser

class TestNormalUser(unittest.TestCase):
    def setUp(self):
        self.normalUser = NormalUser('Jane Smith','jane.smith@company.com','itssecret')
    def test_init(self):
        self.assertEqual(self.normalUser.name, "Jane Smith")
        self.assertEqual(self.normalUser.email, "jane.smith@company.com")
        self.assertEqual(self.normalUser.password,"itssecret")
    def test_delete(self):
        self.assertEqual(self.normalUser.delete(), "this is a normal user delete message for Jane Smith")
    def test_getters(self):
        self.assertEqual(self.normalUser.getUserFirstName(),'Jane')
        self.assertEqual(self.normalUser.getUserLastName(),'Smith')

if __name__ == '__main__':
    unittest.main()
        