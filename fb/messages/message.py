from datetime import datetime
import fb.user
import fb.messages.conversation


class message:
    def __init__(self, text, timestamp_ms, sender: fb.user, conversation: fb.messages.conversation, attachments = None):
        self.__text = text
        self.__time = datetime.fromtimestamp(timestamp_ms)
        self.__sender = sender
        self.__type = type
        self.__conversation = conversation



