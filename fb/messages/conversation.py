import json
from pathlib import Path
import pprint

class conversation:
    def __init__(self, folder_path):

        self.__messages_json = None
        self.__thread_path = None

        self.__messages_per_participants = None
        self.__characters_per_participant = None
        self.__total_messages = None


        messages_files = folder_path.glob("message_*.json")
        for mf in messages_files:
            self.__load_message_json(mf)



        self.__messages = self.__messages_json['messages']
        self.__participants = self.__messages_json['participants']



    def __str__(self):
        return f"Title: {self.__messages_json['title']}"

    def __load_message_json(self, json_path: Path):
        j = json.load(open(json_path, 'r'))
        if self.__thread_path is None:
            self.__thread_path = j['thread_path']
        elif self.__thread_path != j['thread_path']:
            print("Warning or something")

        if self.__messages_json is not None:
            print("Loading more messages from " + str(json_path))
            self.__messages_json['messages'] += j['messages']
        else:
            self.__messages_json = j


    def get_messages_per_participants(self):
        if self.__messages_per_participants is  None:
            self.__messages_per_participants = {}
            for p in self.__participants:
                self.__messages_per_participants[p["name"]] = 0

            msg_types = ['Generic']
            for m in self.__messages:
                if m['type'] in msg_types:
                    if m['sender_name'] in self.__messages_per_participants:
                        self.__messages_per_participants[m['sender_name']] += 1
                    else:
                        self.__messages_per_participants[m['sender_name']] = 1

        return self.__messages_per_participants

    def get_characters_per_participant(self):
        if self.__characters_per_participant is  None:
            self.__characters_per_participant = {}
            for p in self.__participants:
                self.__characters_per_participant[p['name']] = 0

            msg_types = ['Generic']
            for m in self.__messages:
                if m['type'] in msg_types and 'content' in m:
                    if m['sender_name'] in self.__characters_per_participant:
                        self.__characters_per_participant[m['sender_name']] += len(m['content'])
                    else:
                        self.__characters_per_participant[m['sender_name']] = 1

        return self.__characters_per_participant

    def getTotalMessages(self):
        msgs_per_person = self.get_messages_per_participants()
        total_msgs = 0
        for p in msgs_per_person:
            total_msgs += msgs_per_person[p]
        self.__total_messages = total_msgs
        return total_msgs

    def getTitle(self):
        return self.__messages_json['title']

    def getMessages(self):
        return self.__messages
