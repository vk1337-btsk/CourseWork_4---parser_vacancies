from config import API_KEY_SJ
from src.classes.parser import Parser
import requests


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
        self.search_criteria = search_criteria
        self.headers = self.get_headers()
        self.params = self.get_params()

    def get_headers(self):
        """Method that generates headers for a request to the site.
        :return: headers for a request to the site
        """
        headers = {'X-Api-App-Id': self.api_key}
        return headers

    def get_params(self):
        """Method that generates parameters for a request to the site.
        :return: parameters for a request to the site
        """
        params = \
            {
                # Parameters for parsing
                'page': 0,  # Number page site
                'count': 20,  # Number of requests on page
                # Parameters for search
                'keyword':  self.search_criteria.name_vacancy  # Keyword for search (name vacancy or etc.)
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
        name_array = 'objects'
        super().create_json(self.name_file)

        while True:
            try:
                response = super().get_response(basic_url=self.basic_url, headers=self.headers, params=self.params)
                list_vacancies = response[name_array]
                flag_more = response['more']
                self.params['page'] += 1
                super().time_sleep()
                for vacancy in list_vacancies:
                    super().add_in_json(self.name_file, self.formatting_vacancy(vacancy))

                if not flag_more:
                    break
                break
            except requests.HTTPError:
                print('Прерываем работу из-за ошибки или из-за того, что мы достигли глубины пагинации')
                break
