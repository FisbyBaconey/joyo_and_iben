class Student:
    def __init__(self, assistant_id, name):
        self.__assistant_id = assistant_id
        self.__name = name

    # added def get atr
    def get_assistant_id(self):
        return self.__assistant_id

    def get_name(self):
        return self.__name