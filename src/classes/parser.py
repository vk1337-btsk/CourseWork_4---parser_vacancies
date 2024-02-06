from abc import ABC, abstractmethod
import random
import requests


class Parser(ABC):
    """
    This is abstract class is parent class for class-children.
    This class realize basic functional for parsing information about vacancies with web-site.
    """

    # Abstract methods
    @abstractmethod
    def get_headers(self) -> None:
        """Abstract method that generates headers for a request to the site."""
        pass

    @abstractmethod
    def get_params(self) -> None:
        """Abstract method that generates parameters for a request to the site."""
        pass

    # Static method
    @staticmethod
    def get_time_for_sleep() -> float:
        """This method forms random time for sleep between requests"""
        count_second = random.uniform(0.3, 0.5)
        return count_second

    @staticmethod
    def get_response(basic_url: str, headers: dict, params: dict) -> dict or Exception:
        """This method sends a request to a specific site and returns a response in case of a positive response
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
    def get_value_experience(obj: str) -> str or None:
        """This method takes a string and checks whether it exists or not. If it is not equal to None,
        then it returns the work experience value from the dictionary, otherwise it returns None:
        :param obj - string with information about experience or None
        :return None or string template"""
        list_experience = \
            [
                {"hh": "noExperience", 'sj': '1', "name": "Нет опыта"},
                {"hh": "between1And3", 'sj': '2', "name": "От 1 года до 3 лет"},
                {"hh": "between3And6", 'sj': '3', "name": "От 3 до 6 лет"},
                {"hh": "moreThan6", 'sj': '4', "name": "Более 6 лет"}
            ]
        if obj is None:
            return None
        else:
            for dict_ in list_experience:
                if str(obj) in dict_.values():
                    return list(dict_.values())[-1]

    @staticmethod
    def get_value_employment(obj: str or None) -> str or None:
        """This method takes a string and checks whether it exists or not. If it is not equal to None,
        then it returns the work employment value from the dictionary, otherwise it returns None:
        :param obj - string with information about employment or None
        :return None or string template"""
        list_employment = \
            [
                {'hh': 'full', 'sj': '6', 'name': 'Полная занятость'},
                {'sj': '10', 'name': 'Неполный день'},
                {'sj': '12', 'name': 'Сменный график'},
                {'hh': 'part', 'sj': '13', 'name': 'Частичная занятость'},
                {'sj': '7', 'name': 'Временная работа'},
                {'sj': '9', 'name': 'Вахтовый метод'},
                {'hh': 'project', 'name': 'Проектная работа'},
                {'hh': 'volunteer', 'name': 'Волонтерство'},
                {'hh': 'probation', 'name': 'Стажировка'},
            ]
        if obj is None:
            return None
        else:
            for dict_ in list_employment:
                if str(obj) in dict_.values():
                    return list(dict_.values())[-1]
