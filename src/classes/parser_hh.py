import requests
from constant import API_CLIENT_ID, API_CLIENT_SECRET
from src.classes.parser import Parser


class ParserVacancyHH(Parser):
    """
    This class realize parsing information about vacancies from the web-site HeadHunter.ru
    """

    # Attributes classes
    api_client_id = API_CLIENT_ID
    api_client_secret = API_CLIENT_SECRET
    name_file = 'vacancy_from_hh'
    basic_url = 'https://api.hh.ru/vacancies'

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
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/121.0.0.0 Safari/537.36'}
        return headers

    def get_params(self) -> dict:
        """Method that generates parameters for a request to the site.
        :return: parameters for a request to the site
        """
        criteria_name = self.search_criteria['name_vacancy']
        criteria_experience = None if self.search_criteria['experience'] is None \
            else self.search_criteria['experience']['hh']

        params_ = {
                # Parameters for parsing
                'page': 0,  # Number page site
                'per_page': 100,  # Number of requests on page
                # Parameters for search
                'text': criteria_name,  # Keyword for search (name vacancy or etc.)
                'experience': criteria_experience  # Experience work
        }

        params = {key: value for key, value in params_.items() if value is not None}

        return params

    @staticmethod
    def formatting_vacancy(info_vacancy: dict) -> dict:
        """This method receives one dictionary with information about one job and reduces it to a template form."""

        def choice_currency(currency):
            if currency == 'RUR':
                return 'RUB'
            elif currency == 'BYR':
                return 'BYN'
            return currency

        vacancy = \
            {
                'name': info_vacancy['name'],
                'address': ('Не указан' if not info_vacancy.get('address')
                            else info_vacancy['address'].get('raw', 'Не указан')),
                'salary':
                    {
                        'from': 0 if not info_vacancy.get('salary') else info_vacancy['salary'].get('from', 0),
                        'to': 0 if not info_vacancy.get('salary') else info_vacancy['salary'].get('to', 0),
                        'currency': 0 if not info_vacancy.get('salary') else
                        choice_currency(info_vacancy['salary'].get('currency', 0)),
                    },
                'experience': Parser.get_value_experience(info_vacancy['experience']['id']),
                'employment': Parser.get_value_employment(info_vacancy['employment']['id']),
                'url': info_vacancy['alternate_url'],
                'Web-site': "HeadHunter"
            }
        return vacancy

    def get_all_vacancies(self) -> list:
        """This method requests job data from a site, retrieves it, transforms it, and stores it.
        This method returns nothing."""
        name_array = 'items'
        list_vacancies = []
        print('Пожалуйста, подождите. Загружаем вакансии с сайта HeadHunter.ru')
        while True:
            try:
                response = super().get_response(basic_url=self.basic_url, headers=self.headers, params=self.params)
                response_list_vacancies = response[name_array]
                last_page = response['pages']
                self.params['page'] += 1
                super().get_time_for_sleep()
                for vacancy in response_list_vacancies:
                    list_vacancies.append(self.formatting_vacancy(vacancy))

                if last_page == self.params['page']:
                    break
            except requests.HTTPError:
                break

        return list_vacancies
