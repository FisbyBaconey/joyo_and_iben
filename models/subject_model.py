class SubjectModel:
    # add def init
    def __init__(self,subject_id,name):
        self.__subject_id = subject_id
        self.__name = name

    def get_subject_id(self):
        return self.__subject_id

    def get_name(self):
        return self.__name