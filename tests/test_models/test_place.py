import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up a new Place instance for testing."""
        self.place = Place()

    def test_place_attributes(self):
        """Test if Place instance has the expected attributes."""
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_string_representation(self):
        """Test the string representation of the Place object."""
        expected_str = f"[Place] ({self.place.id}) ({self.place.__dict__})"
        self.assertEqual(str(self.place), expected_str)


if __name__ == '__main__':
    unittest.main()
