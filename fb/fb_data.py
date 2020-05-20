import fb.profile
from pathlib import Path
from . messages import conversation
class fb_data:
    def __init__(self, directory_to_fb_data: Path):

        #set up owner info
        self.__owner = fb.profile.Profile(directory_to_fb_data / 'profile_information')

        #load all messages


        self.__inbox = []

        for t in (directory_to_fb_data / 'messages' / 'inbox').iterdir():
            print(t)
            msg_thread = conversation.conversation(t)
            self.__inbox.append(msg_thread)
        print(len(self.__inbox))

    def get_messages(self):
        return self.__inbox

    def get_owner(self):
        return self.__owner