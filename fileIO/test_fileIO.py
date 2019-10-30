import fileIO
import unittest
from unittest.mock import mock_open

class TestFileIO(unittest.TestCase):
    def test_getFileContents_Invalid_File_Path(self):
        self.assertRaises(FileNotFoundError, fileIO.getFileContents("INVALID_FILE"))

if __name__ == '__main__':
    unittest.main()