class user:
    def __init__(self, names_dict):
        self.__names_dict = names_dict


    def getFullName(self):
        return self.__names_dict["full_name"]