import json
from class_Candidate import Candidate


def load_data(path):
    '''
    This function to load json file
    '''
    with open(path, "r", encoding='utf-8') as file:
        file_ = json.load(file)
    return file_


def get_objects_list(added_list):
    '''
    This function to make Candidate class object and put in the list
    '''
    list_objects = []
    for i in added_list:
        list_objects.append(
            Candidate(i['id'], i['name'], i['picture'], i['position'], i['gender'], i['age'], i['skills']))
    return list_objects


def create_output(cand_object):
    '''
    This function to create f string with important information about particular candidate
    '''
    return (f'Имя кандидата - {cand_object.name}\n'
            f'Позиция кандидата - {cand_object.position}\n'
            f'Навыки - {cand_object.skills}\n')
