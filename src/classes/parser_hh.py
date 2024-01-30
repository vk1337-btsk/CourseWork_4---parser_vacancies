import requests
from config import API_CLIENT_ID, API_CLIENT_SECRET
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
        self.search_criteria = search_criteria
        self.headers = self.get_headers()
        self.params = self.get_params()

    def get_headers(self):
        """Method that generates headers for a request to the site.
        :return: headers for a request to the site
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/121.0.0.0 Safari/537.36'}
        return headers

    def get_params(self):
        """Method that generates parameters for a request to the site.
        :return: parameters for a request to the site
        """
        params = {
                # Parameters for parsing
                'page': 0,  # Number page site
                'per_page': 100,  # Number of requests on page
                # Parameters for search
                'text': self.search_criteria.name_vacancy  # Keyword for search (name vacancy or etc.)
        }

        for key, value in params.items():
            if value is None:
                del params[key]
        return params

    @staticmethod
    def formatting_vacancy(info_vacancy):
        """This method receives one dictionary with information about one job and reduces it to a template form."""
        return info_vacancy

    def get_all_vacancies(self):
        """This method requests job data from a site, retrieves it, transforms it, and stores it.
        This method returns nothing."""
        name_array = 'items'
        super().create_json(self.name_file)

        while True:
            try:
                response = super().get_response(basic_url=self.basic_url, headers=self.headers, params=self.params)
                list_vacancies = response[name_array]
                last_page = response['pages']
                self.params['page'] += 1
                super().time_sleep()
                for vacancy in list_vacancies:
                    super().add_in_json(self.name_file, self.formatting_vacancy(vacancy))

                if last_page == self.params['page']:
                    break
                break
            except requests.HTTPError:
                print('Прерываем работу из-за ошибки или из-за того, что мы достигли глубины пагинации')
                break
