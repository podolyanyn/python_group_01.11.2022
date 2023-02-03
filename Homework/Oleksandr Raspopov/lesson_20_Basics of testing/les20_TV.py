class TVController:
    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.channel_index = 0

    def first_channel(self):  # turns on the first channel from the list.
        self.channel_index = 0
        return TVController.current_channel(self)

    def last_channel(self):  # turns on the last channel from the list.
        self.channel_index = len(self.channel_list) - 1
        return TVController.current_channel(self)

    def turn_channel(self, num):  # turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
        self.channel_index = num-1
        return TVController.current_channel(self)

    def next_channel(self):  # turns on the next channel. If the current channel is the last one, turns on the first channel.
        if self.channel_index + 1 == len(self.channel_list):
            return TVController.first_channel(self)
        self.channel_index = self.channel_index + 1
        return TVController.current_channel(self)

    def previous_channel(self):  # turns on the previous channel. If the current channel is the first one, turns on the last channel.
        if self.channel_index - 1 < 0:
            return TVController.last_channel(self)
        self.channel_index = self.channel_index - 1
        return TVController.current_channel(self)

    def current_channel(self):  # returns the name of the current channel.
        return self.channel_list[self.channel_index]

    def is_exist(self, find):  # gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
        if find in range(1, len(self.channel_list)+1) or str(find) in self.channel_list:
            return 'Yes'
        return 'No'


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)
