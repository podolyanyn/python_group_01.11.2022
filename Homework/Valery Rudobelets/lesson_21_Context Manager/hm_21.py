from contextlib import contextmanager
import unittest
import pytest

# task_1.1


class Open:
    counter = 0

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        Open.counter += 1

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"We entered {Open.counter} times")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("We exited")
        self.file.close()


# if __name__ == "__main__":
#     with Open("pytext.txt", "w") as file:
#         file.write("That's pytext")
#
#     with Open("pytext.txt", "w") as file:
#         file.write("That's another pytext")


# task_1.2

@contextmanager
def better_open(file, mode, counter=[0]):
    counter[0] += 1
    try:
        f = open(file, mode)
        print(f"The file is opened {counter[0]} times")
        yield f
    finally:
        f.close()
        print("The file is closed")
#
#
# if __name__ == "__main__":
#     with better_open("pytext.txt", "w") as file:
#         file.write("That's pytext again")
#
#     with better_open("pytext.txt", "w") as file:
#         file.write("That's another pytext again")

# task_2

# class OpenTest(unittest.TestCase):
#
#     def test_counter(self):
#
#         with Open("pytext.txt", "w") as file:
#             file.write("Ablablablabla")
#
#         with Open("pytext.txt", "w") as file:
#             file.write("Ablablablabla")
#
#         with Open("pytext.txt", "w") as file:
#             file.write("Ablablablabla")
#
#         with Open("pytext.txt", "w") as file:
#             file.write("Ablablablabla")
#
#         self.assertEqual(Open.counter, 4)
#         self.assertTrue(file.closed)
#
#     def test_exception(self):
#         with self.assertRaises(ValueError):
#             with Open("pytext.txt", "i") as file:
#                 file.write("Something")
#
#
# if __name__ == "__main__":
#     unittest.main()

# task_3

# @contextmanager
def new_func(file, one_letter, another_letter):
    try:
        f = open(file)
        yield f
        print(f.read().replace(one_letter, another_letter))
    finally:
        f.close()
        print("The file is closed")
#
#
# with new_func("the_text.txt", "t", "a") as the_file:
#     print("Done")


def testing_one():
    with new_func("the_text.txt", "q", "a") as the_file:
        print("Done")
    assert "q" in the_file.read()

