import unittest
from user import User
from admin import Admin

class TestAdminUser(unittest.TestCase):
    def setUp(self):
        self.adminUser = Admin('Jane Smith','jane.smith@company.com','itssecret')
    def test_init(self):
        self.assertEqual(self.adminUser.name, "Jane Smith")
        self.assertEqual(self.adminUser.email, "jane.smith@company.com")
        self.assertEqual(self.adminUser.password,"itssecret")
    def test_delete(self):
        self.assertEqual(self.adminUser.delete(), "this is an admin delete message for Jane Smith")
    def test_getters(self):
        self.assertEqual(self.adminUser.getUserFirstName(),'Jane')
        self.assertEqual(self.adminUser.getUserLastName(),'Smith')
if __name__ == '__main__':
    unittest.main()