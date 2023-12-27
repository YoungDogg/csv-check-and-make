from unittest.mock import patch, mock_open
import unittest
import file_manager
from datetime import datetime

class FileManagerTest(unittest.TestCase):

    def test_find_files(self):
        with patch('os.walk') as mock_walk:
            mock_walk.return_value = [
                ('/path/to/files/2023/01/01', [], ['titles-original', 'otherfile.txt']),
                ('/path/to/files/2023/01/02', [], ['titles-original', 'anotherfile.txt']),
            ]

            result = file_manager.find_files('/path/to/files', 'titles-original')
            expected = ['/path/to/files/2023/01/01/titles-original', '/path/to/files/2023/01/02/titles-original']
            self.assertEqual(result, expected)

    def test_extract_date_from_path(self):
        path = '/path/to/files/2023/01/01/titles-original'
        result = file_manager.extract_date_from_path(path)
        expected = '2023-01-01'
        self.assertEqual(result, expected)

    def test_read_file(self):
        mock_data = "Title 1, Title 2"
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = file_manager.read_file("dummy/path")
            self.assertEqual(result, "Title 1, Title 2")

    def test_process_files(self):
        # This test needs to mock several functions used in process_files
        with patch('file_manager.find_files') as mock_find_files, \
             patch('file_manager.extract_date_from_path') as mock_extract_date, \
             patch('builtins.open', mock_open()) as mock_file, \
             patch('file_manager.read_file') as mock_read_file:

            mock_find_files.side_effect = [
                ['/path/to/files/2023/01/01/titles-original'], 
                ['/path/to/files/2023/01/01/titles-afterGPT']
            ]
            mock_extract_date.return_value = '2023-01-01'
            mock_read_file.side_effect = ['Original Title', 'AfterGPT Title']

            file_manager.process_files('/path/to/files')

            # Ensure the process_files function is calling the right functions
            mock_find_files.assert_called()
            mock_extract_date.assert_called()
            mock_read_file.assert_called()
            mock_file().write.assert_called()

if __name__ == '__main__':
    unittest.main()
