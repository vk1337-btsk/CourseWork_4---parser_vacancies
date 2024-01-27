from abc import ABC, abstractmethod
from constant import DIR_PROJECT
import random
import requests
import os
import json


class Engine(ABC):

    @abstractmethod
    def get_headers(self):
        pass

    @abstractmethod
    def get_params(self):
        pass

    @staticmethod
    def get_response(basic_url: str, headers: dict, params: dict) -> dict or Exception:
        """
        This function sends a request to a specific site and returns a response in case of a positive response
        (response with status 200 or raises an exception in case of an error)
        :param basic_url:
        :param headers:
        :param params:
        :return:
        """
        response = requests.get(basic_url, headers=headers, params=params)

        # Для отладки
        # print(response.url)
        # print(response.status_code)
        # print(response.json())

        if bool(response):
            return response.json()
        else:
            raise requests.HTTPError('Ошибка. Запрос ответ не с кодом 200. Внутри get_response')

    @staticmethod
    def create_json(name_file):
        """Метод для создания файла json с информацией о вакансиях"""
        file_ = os.path.join(DIR_PROJECT, 'data', f"{name_file}.json")
        with open(file_, 'w', encoding='UTF-8') as file:
            json.dump([], file, indent=4, ensure_ascii=False)

        # Для отладки
        print('Создали файл')

    @staticmethod
    def add_in_json(name_file, my_data):
        """Метод для добавления результатов парсинга в json"""
        file_ = os.path.join(DIR_PROJECT, 'data', f"{name_file}.json")
        with open(file_, "r+", encoding='UTF-8') as file:
            data = json.load(file)
            data.append(my_data)
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)

        # Для отладки
        print('Добавили инфу в файл')

    @staticmethod
    def input_name():
        name = 'Тестировщик'  # input('Введите название вакансии для поиска')
        return name

    @staticmethod
    def time_sleep():
        """Формируем рандомное время для сна между запросами"""
        count_second = random.uniform(0.3, 0.5)
        return count_second
