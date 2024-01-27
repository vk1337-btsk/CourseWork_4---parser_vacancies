from src.classes.parser import Engine
from src.classes.vacancy import Vacancy
import requests


class ParserVacancyHH(Engine):

    name_file = 'vacancy_from_hh'
    basic_url = 'https://api.hh.ru/vacancies'

    def __init__(self) -> None:

        self.name = super().input_name()
        self.headers = self.get_headers()
        self.params = self.get_params()

    def get_headers(self):
        headers = \
            {
                # 'User-Agent': 'MyApp/1.0 (my-app-feedback@example.com)'
            }
        return headers

    def get_params(self):
        params = \
            {
                'page': 0,  # Номер страницы
                'per_page': 1,  # Количество элементов на странице / в запросе
                'text': self.name,  # Название вакансии
                'only_with_salary': 'true',  # Показывать вакансии только с зарплатой
                'search_field': ['company_name', 'name', 'description']  # Области поиска
             }
        return params

    def get_all_vacancies(self):
        """Метод, в котором мы проходим по страницам и делаем запросы по вакансиям"""
        super().create_json(self.name_file)

        while True:
            if (self.params['page'] + 1) * self.params['per_page'] > 2000:
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
        name_array = 'items'
        data = super().get_response(basic_url=self.basic_url, headers=self.headers,
                                    params=self.params)
        return data[name_array]
