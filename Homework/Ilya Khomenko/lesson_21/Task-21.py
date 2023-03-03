import unittest
import pytest
import re
#Task-1
class File:
    def __init__(self, file_name, method):
        try:
            self.file_obj = open(file_name, method)
        except FileNotFoundError:
            print("file not found")

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
        print(f"{exc_val}")
        return True








#Task-2
class Test(unittest.TestCase):
    def test_load(self):
        with File('log.txt', 'r') as f:
            text = f.read()
        self.assertEquals(text,text)

    def test_invalid_load(self):
        inp_u =  input('Enter a name of json file: ')
        self.assertEqual(inp_u,'phonebook.json')

    def test_write(self):
        with File('log.txt', 'w') as f:
            text = input('Enter name: ')
            x = f.write(text)
        self.assertEqual(text[0].isupper(),True)
unittest.main()
#Task-3
@pytest.fixture
def test(file_obj):
    file_obj = File('log.txt','r')
    with file_obj:
        file_obj.read()

    return file_obj



@pytest.fixture
def first_elem(first_entry):
    return [first_entry]


def test_string(order):

    # Assert
    assert order == ["Invalid"]


