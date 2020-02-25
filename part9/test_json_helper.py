import unittest
import os
import json_helper


class JsonHelperTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._json_stubs = [
            {
                'name': 'Mario',
                'neutral_special': 'Fireball',
                'side_special': 'Cape',
                'up_special': 'Super Jump Punch',
                'down_special': 'F.L.U.D.D.',
                'final_smash': 'Mario Finale'
            },
            {
                'name': 'Link',
                'neutral_special': 'Bow and Arrows',
                'side_special': ' Boomerang',
                'up_special': ' Spin Attack',
                'down_special': 'Remote Bomb',
                'final_smash': 'Ancient Bow and Arrow'
            }
        ]

    def test_read_json(self):
        expected = self._json_stubs[0]
        file_path = os.path.join('./', 'data', 'super_smash_bros', 'mario.json')
        actual = json_helper.read_json(file_path)
        self.assertEqual(expected, actual)

    def test_read_all_json_files(self):
        expected = self._json_stubs
        file_path = os.path.join('./', 'data', 'super_smash_bros')
        actual = json_helper.read_all_json_files(file_path)
        self.assertEqual(expected, actual)

