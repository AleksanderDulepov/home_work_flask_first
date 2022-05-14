from utils import *
from config import PATH
from flask import Flask


def main():
    list_from_json = load_data(PATH)
    list_objects = get_objects_list(list_from_json)

    app = Flask(__name__)

    @app.route('/')
    def page_general():
        total_info_list = []
        for i in list_objects:
            total_info_list.append(f'Имя кандидата - {i.name}\n'
                                   f'Позиция кандидата - {i.position}\n'
                                   f'Навыки - {i.skills}\n')
        return '\n'.join(total_info_list)
    app.run()


if __name__ == '__main__':
    main()
