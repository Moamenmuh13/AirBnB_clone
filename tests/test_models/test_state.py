import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up a new State instance for testing."""
        self.state = State()

    def test_state_attributes(self):
        """Test if State instance has the expected attributes."""
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))


if __name__ == '__main__':
    unittest.main()
