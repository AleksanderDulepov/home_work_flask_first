from utils import *
from config import FILE_NAME
from flask import Flask


def main():
    list_from_json = load_data(FILE_NAME)
    list_objects = get_objects_list(list_from_json)

    app = Flask(__name__)

    @app.route('/')
    def page_general(list_=list_objects):
        total_info_list = []
        for i in list_:
            total_info_list.append(create_output(i))
        return '<pre>\n' + "\n".join(total_info_list) + '</pre>'

    @app.route('/candidates/<int:cand_id>')
    def page_candidates(cand_id, list_=list_objects):
        for i in list_:
            if cand_id == i.id:
                return (f'<img src={i.picture}>\n\n'
                        f'<pre>\n'
                        f'{create_output(i)}'
                        f'</pre>')
        return f'Кандидата с id {cand_id} нет в базе данных!'

    @app.route('/skills/<skill>')
    def page_skills(skill, list_=list_objects):
        cand_with_skill = []
        for i in list_:
            if skill.lower() in i.get_skills_list():
                cand_with_skill.append(create_output(i))
        if not cand_with_skill:
            return f'Кандидата со скиллом  {skill} нет в базе данных!'

        return '<pre>\n' + "\n".join(cand_with_skill) + '</pre>'

    app.run()


if __name__ == '__main__':
    main()
