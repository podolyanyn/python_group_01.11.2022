print('> > > Task 1 - File Context Manager class\n')
# Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging.
# Pay special attention to the implementation of `__exit__` method,
# which has to cover all the requirements to context managers mentioned here:
# https://docs.python.org/3.7/library/stdtypes.html#typecontextmanager
# https://docs.python.org/3.7/reference/compound_stmts.html#with


class MyOpen:
    counter = 0

    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        MyOpen.counter += 1
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('counter:', MyOpen.counter)
        if exc_type:
            print(exc_val)
        self.file.close()
        return True

with MyOpen('test_file.txt', 'r') as my_open:
    print(my_open.readline())
    1/0

with MyOpen('test_file.txt', 'r') as my_open:
    print(my_open.readline())
    print(f'change counter from {MyOpen.counter} to 10:')
    MyOpen.counter = 10


print('> > > Task 2\n - Writing tests for context manager')
# Take your implementation of the context manager class from Task 1 and write tests for it.
# Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed.
# And also, write tests when your class raises errors, or you have errors in the runtime context suite.

import unittest


class TestMyOpen(unittest.TestCase):
    def test_open_existing_file(self):
        self.filename = 'test_file.txt'
        self.method = 'r'
        self.case = MyOpen(self.filename, self.method)
        with self.case as self.file:
            self.assertEqual(self.file.readline(), 'Hello world! 1\n')

    def test_open_empty_file(self):
        self.filename = 'test_empty.txt'
        self.method = 'r'
        self.case = MyOpen(self.filename, self.method)
        with self.case as self.file:
            self.assertNotEqual(self.file.readline(), 'Hello world! 1\n')

    def test_counter(self):
        self.filename = 'test_file.txt'
        self.method = 'r'
        self.case = MyOpen(self.filename, self.method)
        with self.case as self.file:
            self.file.counter = 50
            self.assertEqual(self.file.counter, 50)


if __name__ == '__main__':
    unittest.main()



