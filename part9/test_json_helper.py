import unittest
import os
import json_helper


class JsonHelperTest(unittest.TestCase):

    def test_read_json(self):
        expected = {
            'name': 'Mario',
            'neutral_special': 'Fireball',
            'side_special': 'Cape',
            'up_special': 'Super Jump Punch',
            'down_special': 'F.L.U.D.D.',
            'final_smash': 'Mario Finale'
        }
        file_path = os.path.join('./', 'data', 'super_smash_bros', 'mario.json')
        actual = json_helper.read_json(file_path)
        self.assertEqual(expected, actual)
