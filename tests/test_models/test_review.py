import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up a new Review instance for testing."""
        self.review = Review()

    def test_review_attributes(self):
        """Test if Review instance has the expected attributes."""
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_string_representation(self):
        """Test the string representation of the Review object."""
        expected_str = f"[Review] ({self.review.id}) ({self.review.__dict__})"
        self.assertEqual(str(self.review), expected_str)


if __name__ == '__main__':
    unittest.main()
