class Candidate:
    def __init__(self, id, name, picture, position, gender, age, skills):
        self.id = id
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills.lower()

    def __repr__(self):
        return f'This is a Candidate class object {self.name}'
