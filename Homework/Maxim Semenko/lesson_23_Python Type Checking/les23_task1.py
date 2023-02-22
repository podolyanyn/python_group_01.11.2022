from typing import List, Union


class TVController:

    def __init__(self, list_of_channels: List[str]) -> None:
        self.channels = list_of_channels
        self.counter = 0

    def first_channel(self) -> str:
        self.counter = 0
        return self.channels[0]

    def last_channel(self) -> str:
        self.counter = len(self.channels) - 1
        return self.channels[self.counter]

    def turn_channel(self, number: int) -> str:
        return self.channels[number-1]

    def next_channel(self) -> str:
        if self.channels[self.counter] == self.channels[-1]:
            self.counter = 0
        else:
            self.counter += 1
        return self.channels[self.counter]

    def previous_channel(self) -> str:
        if self.channels[self.counter] == self.channels[0]:
            self.counter = len(self.channels) - 1
        else:
            self.counter -= 1
        return self.channels[self.counter]

    def current_channel(self) -> str:
        return self.channels[self.counter]

    def is_exist(self, name: Union[int, str]) -> str:
        if type(name) == int:
            if name <= len(self.channels):
                return 'Yes'
            return 'No'
        elif type(name) == str:
            if name in self.channels:
                return 'Yes'
            return 'No'
        return 'Wrong input type, please try again'
