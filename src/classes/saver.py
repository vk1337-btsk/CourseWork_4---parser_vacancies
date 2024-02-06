from abc import ABC
from constant import DIR_PROJECT
import os
import json


class Saver(ABC):
    """This class provides functionality for saving and reading files with vacancies"""

    @staticmethod
    def save_data_json(list_vacancies: list) -> None:
        """This method saves the list of vacancies in json"""
        file_ = os.path.join(DIR_PROJECT, 'data', "vacancies.json")
        with open(file_, 'w', encoding='UTF-8') as file:
            json.dump([*list_vacancies], file, indent=4, ensure_ascii=False)
