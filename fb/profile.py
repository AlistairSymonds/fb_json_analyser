from pathlib import Path
import json
import pprint
from . import user

class Profile:
    def __init__(self, profile_path: Path):
        profile_fp = open(profile_path / 'profile_information.json')
        self.__raw_data = json.load(profile_fp)
        pprint.pprint(self.__raw_data["profile"]["name"])
        self.__user = user.user(self.__raw_data["profile"]["name"])
        print(self.__user.getFullName())