from models.student import Student

class AssistantModel(Student):
    # added def init
    def __init__(self, assistant_id, name):
        super().__init__(assistant_id, name)
