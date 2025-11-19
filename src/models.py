class Task:
    def __init__(self, title, description, completed=False, id=None):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
