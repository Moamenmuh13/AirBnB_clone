import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Set up a new Amenity instance for testing."""
        self.amenity = Amenity()

    def test_amenity_attributes(self):
        """Test if Amenity instance has the expected attributes."""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))


if __name__ == '__main__':
    unittest.main()
