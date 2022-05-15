from utils import *
from config import FILE_NAME
from flask import Flask


def main():
    list_from_json = load_data(FILE_NAME)
    list_objects = get_objects_list(list_from_json)

    app = Flask(__name__)

    @app.route('/')
    def page_general():
        total_info_list = []
        for i in list_objects:
            total_info_list.append(f'{i.name_to_print}\n{i.position_to_print}\n{i.skills_to_print}\n')
        return '<pre>\n'+"\n".join(total_info_list)+'<pre>'

    @app.route('/candidates/<int:cand_id>')
    def page_candidates(cand_id):
        for i in list_objects:
            if cand_id == i.id:
                return (f'{i.picture}\n\n'
                        f'Имя кандидата - {i.name}\n'
                        f'Позиция кандидата - {i.position}\n'
                        f'Навыки - {i.skills}\n')
        return f'Кандидата с id {cand_id} нет в базе данных!'

    @app.route('/skills/<skill>')
    def page_skills(skill):
        cand_with_skill = []
        for i in list_objects:
            if skill.lower() in i.skills:
                cand_with_skill.append(f'Имя кандидата - {i.name}\n'
                                       f'Позиция кандидата - {i.position}\n'
                                       f'Навыки - {i.skills}\n')
        if not cand_with_skill:
            return f'Кандидата со скиллом  {skill} нет в базе данных!'

        return '\n'.join(cand_with_skill)

    app.run()


if __name__ == '__main__':
    main()
