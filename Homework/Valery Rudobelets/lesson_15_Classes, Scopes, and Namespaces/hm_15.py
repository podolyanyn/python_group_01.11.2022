# task_1

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old")


person_1 = Person("Normal", "Guy", 21)
person_2 = Person("Average", "Man", 43)

person_1.talk()
person_2.talk()


# task_2

class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.age_factor * self.dog_age


age_1 = Dog(1)
age_2 = Dog(4)
age_3 = Dog(16)

print(age_1.human_age())
print(age_2.human_age())
print(age_3.human_age())

# task_3

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    current = 0

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, channel):
        self.channel = channel
        self.current = channel
        if self.channel <= len(CHANNELS):
            return self.channels[self.channel-1]
        else:
            return "There are not that many channels"

    def next_channel(self):
        if self.current < len(CHANNELS):
            return self.channels[self.current]
        else:
            self.current = self.channel % len(CHANNELS)
            return self.channels[self.current]

    def previous_channel(self):
        if self.current < len(CHANNELS):
            return self.channels[self.current-2]
        else:
            self.current = self.channel % len(CHANNELS)
            return self.channels[self.current+1]

    def current_channel(self):
        return self.channels[self.current]

    def is_exist(self, name):
        if name in CHANNELS:
            return "Yes"
        elif name in range(len(CHANNELS)):
            return "Yes"
        else:
            return "No"


controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(2))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
print(controller.is_exist("BBC"))
