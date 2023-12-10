import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertEqual(self.file_storage.all(), {})

    def test_new(self):
        obj = BaseModel()
        self.file_storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.file_storage.all())
        self.assertEqual(self.file_storage.all()[key], obj)

    def test_classes(self):
        classes = self.file_storage.classes()
        self.assertEqual(len(classes), 7)  # Assuming you have 7 classes
        self.assertIn("BaseModel", classes)
        self.assertIn("User", classes)
        # Add more assertions for other classes

    def test_save_and_reload(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)
        self.file_storage.save()

        # Create a new instance of FileStorage for reloading
        new_file_storage = FileStorage()
        new_file_storage._FileStorage__file_path = self.file_path
        new_file_storage.reload()

        key1 = f"{obj1.__class__.__name__}.{obj1.id}"
        key2 = f"{obj2.__class__.__name__}.{obj2.id}"

        self.assertIn(key1, new_file_storage.all())
        self.assertIn(key2, new_file_storage.all())
        self.assertEqual(new_file_storage.all()[key1].to_dict(),
                         obj1.to_dict())
        self.assertEqual(new_file_storage.all()[key2].to_dict(),
                         obj2.to_dict())


if __name__ == '__main__':
    unittest.main()
