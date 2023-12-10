import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up a new City instance for testing."""
        self.city = City()

    def test_city_attributes(self):
        """Test if City instance has the expected attributes."""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_string_representation(self):
        """Test the string representation of the City object."""
        expected_str = f"[City] ({self.city.id}) ({self.city.__dict__})"
        self.assertEqual(str(self.city), expected_str)


if __name__ == '__main__':
    unittest.main()
