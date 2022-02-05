import unittest
from ya import folder_check, folder_create

class TestYa(unittest.TestCase):
    def test_create_folder(self):
        self.assertEqual(201, folder_create('test'), 'Папку не создали')

    def test_check_folder(self):
        self.assertEqual(200, folder_check('test'), 'Папки нет')

if __name__ == '__main__':
    unittest.main()