from abc import ABC, abstractmethod
from constant import DIR_PROJECT
import random
import requests
import os
import json


class Parser(ABC):
    """
    This is abstract class is parent class for class-children.
    This class realize basic functional for parsing information about vacancies with web-site.
    """

    # Abstract methods
    @abstractmethod
    def get_headers(self):
        """Abstract method that generates headers for a request to the site."""
        pass

    @abstractmethod
    def get_params(self):
        """Abstract method that generates parameters for a request to the site."""
        pass

    # Static method
    @staticmethod
    def get_response(basic_url: str, headers: dict, params: dict) -> dict or Exception:
        """
        This method sends a request to a specific site and returns a response in case of a positive response
        (response with status 200 or raises an exception in case of an error)
        :param basic_url: url website which the requests sent;
        :param headers: headers requests
        :param params: parameters requests
        :return: server response with list vacancies in format json or raise Exception
        """
        response = requests.get(basic_url, headers=headers, params=params)

        if bool(response):
            return response.json()
        else:
            raise requests.HTTPError('Ошибка. Запрос ответ не с кодом 200. Внутри get_response')

    @staticmethod
    def create_json(name_file):
        """This method create json-file for save information about vacancies."""
        file_ = os.path.join(DIR_PROJECT, 'data', f"{name_file}.json")
        with open(file_, 'w', encoding='UTF-8') as file:
            json.dump([], file, indent=4, ensure_ascii=False)


    @staticmethod
    def add_in_json(name_file, *args):
        """This method add information about vacancies in json-file."""
        file_ = os.path.join(DIR_PROJECT, 'data', f"{name_file}.json")
        with open(file_, "r+", encoding='UTF-8') as file:
            data = json.load(file)
            for arg in args:
                data.append(arg)
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def time_sleep():
        """This method forms random time for sleep between requests"""
        count_second = random.uniform(0.3, 0.5)
        return count_second
