import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up a new User instance for testing."""
        self.user = User()

    def test_user_attributes(self):
        """Test if User instance has the expected attributes."""
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))


if __name__ == '__main__':
    unittest.main()
