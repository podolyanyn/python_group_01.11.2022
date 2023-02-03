from les20_TV import TVController
import unittest


class TestTVController(unittest.TestCase):
    tv = TVController(["BBC", "Discovery", "TV1000"])

    def test_first_channel(self):
        self.assertEqual(TestTVController.tv.first_channel(), "BBC")

    def test_last_channel(self):
        self.assertEqual(TestTVController.tv.last_channel(), "TV1000")

    def test_previous_channel(self):
        TestTVController.tv.first_channel()
        self.assertEqual(TestTVController.tv.previous_channel(), "TV1000")

    def test_current_channel(self):
        self.assertEqual(TestTVController.tv.current_channel(), "BBC")

    def test_next_channel(self):
        TestTVController.tv.last_channel()
        self.assertEqual(TestTVController.tv.next_channel(), "BBC")

    def test_turn_channel(self):
        self.assertEqual(TestTVController.tv.turn_channel(1), "BBC")

    def test_is_exist(self):
        self.assertEqual(TestTVController.tv.is_exist('BBC'), 'Yes')


if __name__ == '__main__':
    unittest.main()
