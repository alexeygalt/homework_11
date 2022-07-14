import json


def load_candidates(file) -> list:
    """Загружает студентов из файла в список"""
    with open(file, 'r') as file:
        key = file.read()
        json_list = json.loads(key)
    return json_list


def get_by_pk(key_list: list, pk: int) -> dict:
    '''Сортировка кандидата по pk'''
    for item in key_list:
        if item['pk'] == pk:
            return item


def get_by_skill(key_list: list, skill_name: str) -> list:
    result = [item for item in key_list if skill_name in item['skills'].lower().split(', ')]
    return result


def get_candidates_by_name(key_list: list, candidate_name: str) -> list:
    result_list = []
    for item in key_list:

        if candidate_name.lower() == (item['name'].split()[0].lower()):
            result_list.append(item)

    return result_list
