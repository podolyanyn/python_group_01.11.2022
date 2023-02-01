import unittest
import hm_19
from phonebookClass import *
import types

# task_1


class WithIndexTest(unittest.TestCase):

    def test_with_index(self):
        example = hm_19.in_range(1, 10)
        self.assertIsInstance(example, types.GeneratorType)
        self.assertIsNotNone(example)
        self.assertTrue(example)


if __name__ == "__main__":
    unittest.main()

# task_2

class PhonebookClassTest(unittest.TestCase):

    def test_phonebook(self):

        phonebook = Phonebook()
        phonebook.new_user("Valery", "Rudobelets", "+380955048230", "Dnipro")
        phonebook.new_user("Jiri", "Krutsky", "+392234934923", "Prague")
        phonebook.new_user("Bartosz", "Grzyb", "+563453534543", "Warsaw")
        phonebook.new_user("Lee", "San", "+123453546453", "Toronto")
        phonebook.new_user("Asuka", "Langley", "+233242432233", "Osaka")
        phonebook.change_name(100001, "Valerie Rudobelec")
        valery = phonebook.users_accounts[0]
        self.assertIsInstance(phonebook.users_accounts[0], User)
        self.assertEqual(valery.first_name, "Valerie")
        self.assertNotEqual(valery.first_name, "Valery")

if __name__ == "__main__":
    unittest.main()
