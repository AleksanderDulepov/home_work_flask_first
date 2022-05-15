class Candidate:
    def __init__(self, id, name, picture, position, gender, age, skills):
        self.id = id
        self.name = name
        self.picture = picture
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills.lower()

        self.name_to_print = f'Имя кандидата - {self.name}'
        self.position_to_print = f'Позиция кандидата - {self.position}'
        self.skills_to_print = f'Навыки - {self.skills}'

    def __repr__(self):
        return f'This is a Candidate class object {self.name}'
