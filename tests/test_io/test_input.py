import unittest
import pandas as pd
from app.io import input as input_module

class TestInput(unittest.TestCase):
    def setUp(self):
        with open('data/test_data.txt', 'w') as file:
            file.write('i am a cool programmer')

        with open('data/empty_file.txt', 'w') as file:
            file.write('')

        df = pd.DataFrame({'name': ['nastya', 'ilya'], 'age': [23, 20]})
        df.to_csv('data/test_data.csv', index=False)

        empty_df = pd.DataFrame()
        empty_df.to_csv('data/empty_file.csv', index=False)

    def tearDown(self):
        import os
        os.remove('data/test_data.txt')
        os.remove('data/empty_file.txt')
        os.remove('data/test_data.csv')
        os.remove('data/empty_file.csv')

    def test_read_from_file_non_empty(self):
        content = input_module.read_from_file('data/test_data.txt')
        self.assertEqual(content, 'i am a cool programmer')

    def test_read_from_file_empty(self):
        content = input_module.read_from_file('data/empty_file.txt')
        self.assertEqual(content, '')

    def test_read_from_file_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            input_module.read_from_file('data/nonexistent_file.txt')

    def test_read_from_file_pandas_non_empty(self):
        df = input_module.read_from_file_pandas('data/test_data.csv')
        expected_df = pd.DataFrame({'name': ['nastya', 'ilya'], 'age': [23, 20]})
        pd.testing.assert_frame_equal(df, expected_df)

    def test_read_from_file_pandas_empty(self):
        df = input_module.read_from_file_pandas('data/empty_file.csv')
        expected_df = pd.DataFrame()
        pd.testing.assert_frame_equal(df, expected_df)

    def test_read_from_file_pandas_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            input_module.read_from_file_pandas('data/nonexistent_file.csv')

if __name__ == '__main__':
    unittest.main()
