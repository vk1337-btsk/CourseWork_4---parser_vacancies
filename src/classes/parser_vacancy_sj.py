from config import API_KEY_SJ
from src.classes.parser import Engine
import requests


class ParserVacancySJ(Engine):
    api_key = API_KEY_SJ
    name_file = 'vacancy_from_sj'
    basic_url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self) -> None:
        self.name = super().input_name()
        self.headers = self.get_headers()
        self.params = self.get_params()

    def get_headers(self):
        headers = \
            {
                'X-Api-App-Id': self.api_key
            }
        return headers

    def get_params(self):
        params = \
            {'page': 0,  # Номер страницы запроса
             'count': 1,  # Количество запросов в одной странице
             'keyword': 'Python'}
        return params

    def get_all_vacancies(self):
        """Метод, в котором мы проходим по страницам и делаем запросы по вакансиям"""
        super().create_json(self.name_file)

        while True:
            if (self.params['page'] + 1) * self.params['count'] > 500:
                break

            try:
                obj = self.get_vacancies()
                self.params['page'] += 1
                super().time_sleep()
                super().add_in_json(self.name_file, obj)
            except requests.HTTPError:
                print('Прерываем работу из-за ошибки или из-за того, что мы достигли глубины пагинации')
                break
            break

    def get_vacancies(self):
        name_array = 'objects'
        data = super().get_response(basic_url=self.basic_url, headers=self.headers,
                                    params=self.params)
        return data[name_array]
