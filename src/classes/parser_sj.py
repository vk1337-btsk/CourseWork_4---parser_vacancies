import requests

from constant import API_KEY_SJ
from src.classes.parser import Parser


class ParserVacancySJ(Parser):
    """
    This class realize parsing information about vacancies from the web-site SuperJob.ru
    """

    # Attributes classes
    api_key = API_KEY_SJ
    name_file = 'vacancy_from_sj'
    basic_url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self, search_criteria: object) -> None:
        """Initialization attributes classes
        :param search_criteria: criteria for search vacancies.
        """
        self.search_criteria = search_criteria.__dict__

        self.headers = self.get_headers()
        self.params = self.get_params()

    def get_headers(self) -> dict:
        """Method that generates headers for a request to the site.
        :return: headers for a request to the site
        """
        headers = {'Host': 'api.superjob.ru', 'X-Api-App-Id': self.api_key}
        return headers

    def get_params(self) -> dict:
        """Method that generates parameters for a request to the site.
        :return: parameters for a request to the site
        """
        criteria_name = self.search_criteria['name_vacancy']
        criteria_experience = None if self.search_criteria['experience'] is None \
            else self.search_criteria['experience']['sj']
        params_ = \
            {
                # Parameters for parsing
                'page': 0,  # Number page site
                'count': 50,  # Number of requests on page
                # Parameters for search
                'keyword':  criteria_name,  # Keyword for search (name vacancy or etc.)
                'experience': criteria_experience  # Experience work
            }

        params = {key: value for key, value in params_.items() if value is not None}

        return params

    @staticmethod
    def formatting_vacancy(info_vacancy: dict) -> dict:
        """This method receives one dictionary with information about one job and reduces it to a template form."""
        vacancy = \
            {
                'name': info_vacancy['profession'],
                'address': 'Не указан' if not info_vacancy.get('address') else info_vacancy.get('address'),
                'salary':
                    {
                        'from': info_vacancy['payment_from'],
                        'to': info_vacancy['payment_to'],
                        'currency': info_vacancy['currency'].upper(),
                    },
                'employment': Parser.get_value_employment(info_vacancy['type_of_work']['id']),
                'experience': Parser.get_value_experience(info_vacancy['experience']['id']),
                'url': info_vacancy['link'],
                'Web-site': "SuperJob"
            }
        return vacancy

    def get_all_vacancies(self) -> list:
        """This method requests job data from a site, retrieves it, transforms it, and stores it.
        This method returns nothing."""
        name_array = 'objects'
        list_vacancies = []
        print('Пожалуйста, подождите. Загружаем вакансии с сайта SuperJob.ru')

        while True:
            try:
                response = super().get_response(basic_url=self.basic_url, headers=self.headers, params=self.params)
                response_list_vacancies = response[name_array]
                flag_more = response['more']
                self.params['page'] += 1
                super().get_time_for_sleep()
                for vacancy in response_list_vacancies:
                    list_vacancies.append(self.formatting_vacancy(vacancy))

                if not flag_more:
                    break

            except requests.HTTPError:
                break

        return list_vacancies
