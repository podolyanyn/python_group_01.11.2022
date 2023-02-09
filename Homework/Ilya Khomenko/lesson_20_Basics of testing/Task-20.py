#Task-1
import unittest
def in_range(start, step=None, end=None):
    if step == None and end == None:
        start, step, end = 0, 1, start
        while start < end:
            yield start
            start += step
    elif end == None:
        start, step, end = start, 1, step
        while start < end:
            yield start
            start += step
    while start < end:
        yield start
        start += step

l = []
for i in in_range(1, 10, 200):
    l.append(i)

class Test(unittest.TestCase):
    def test_range(self):
        test1 = l
        self.assertEqual(test1,[1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191])

   
#Task-2

class Food(object):
   def __init__(self):
       self.consumed = False
   def consume(self):
       self.consumed = True


class Fruit(Food):
    def __init__(self):
        super(Fruit, self).__init__()
        self.been_cut = False

    def cut(self):
        print("cut the fruit")
        self.been_cut = True


class Consumer(object):
    def __init__(self):
        self.apple = Fruit()
        self.banana = Fruit()

    def consume_food(self):
        food = self.pick_food()
        food.cut()
        print("consuming the food")
        food.consume()

    def pick_food(self):
        return self.apple

class TestConsumer(unittest.TestCase):

    def test_consume_food_consumes_the_apple(self):
        c = Consumer()
        c.consume_food()
        self.assertTrue(c.apple.consumed,
                        "Expected apple to be consumed")

    def test_consume_food_cuts_the_food(self):
        c = Consumer()
        c.consume_food()
        self.assertTrue(c.apple.been_cut,
                        "Expected apple to be cut")

    def test_pick_food_always_selects_the_apple(self):
        c = Consumer()
        food = c.pick_food()
        self.assertEquals(c.apple, food,
                          "Expected apple to have been picked")




unittest.main()


