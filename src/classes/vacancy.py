from src.classes.mixin import Mixin


class Vacancy(Mixin):
    """This class represent information about one vacancy and provides functionality for working with it """

    # Initialization attributes
    def __init__(self, dict_info_vacancy: dict) -> None:
        """Initialization attributes
        :param dict_info_vacancy - dict with information about vacancy"""
        self.exchange_rate = Mixin.get_exchange_rate()

        self.info_vacancy = dict_info_vacancy
        self.__name = self.info_vacancy['name']
        self.__address = self.info_vacancy['address']
        self.__salary_from = 0 if self.info_vacancy['salary']['from'] is None else self.info_vacancy['salary']['from']
        self.__salary_to = 0 if self.info_vacancy['salary']['to'] is None else self.info_vacancy['salary']['to']
        self.__salary_currency = (0 if self.info_vacancy['salary']['currency'] is None
                                  else self.info_vacancy['salary']['currency'])
        self.__experience = self.info_vacancy['experience']
        self.__employment = self.info_vacancy['employment']
        self.__url = self.info_vacancy['url']
        self.__web_site = self.info_vacancy['Web-site']

    # Magic methods str and repr
    def __str__(self) -> str:
        """Shows information for user"""
        if all(map(lambda x: x == 0, [self.__salary_from, self.__salary_to, self.__salary_currency])):
            return f'Вакансия: {self.__name}, зарплата не указана. Ссылка на вакансию: {self.__url}'
        return (f'Вакансия: {self.__name}, зарплата {self.__salary_from}-{self.__salary_to} {self.__salary_currency}. '
                f'Ссылка на вакансию: {self.__url}')

    def __repr__(self) -> str:
        """Shows information for developer"""
        return (f'Экземпляр класса: {self.__class__.__name__}\n'
                f'С аргументами: {self.__name=}, {self.__address=}, {self.__salary_from=}, {self.__salary_to=},'
                f'{self.__salary_currency=}, {self.__experience=}, {self.__employment=}, {self.__url=}, '
                f'{self.__web_site=}.')

    # Magic methods comparison
    def prepare_comparison_data(self, other: object) -> tuple[str, int, int, str, int, int]:
        """This method prepares data for comparisons vacancies."""
        self_name = self.__name
        self_from = self.__salary_from
        self_to = self.__salary_to
        self_currency = self.__salary_currency

        other_name = other.info_vacancy['name']
        other_from = other.info_vacancy['salary']['from']
        other_to = other.info_vacancy['salary']['to']
        other_currency = other.info_vacancy['salary']['currency']

        if self_currency != 'RUB':
            self_from = self.convert_currency(self_from, self_currency)
            self_to = self.convert_currency(self_to, self_currency)

        if other_currency != 'RUB':
            other_from = self.convert_currency(other_from, other_currency)
            other_to = self.convert_currency(other_to, other_currency)

        return self_name, self_from, self_to, other_name, other_from, other_to

    def __gt__(self, other: object) -> bool:
        """This method defines the class behavior for the more operator '>' """
        self_name, self_from, self_to, other_name, other_from, other_to = self.prepare_comparison_data(other)

        # If salaries FROM and TO are indicated or NOT indicated
        if (all(map(lambda x: x == 0, [self_from, self_to, other_from, other_to])) or
                (self_from == other_from and self_to == other_to)):
            return self_name < other_name
        elif all(map(lambda x: x != 0, [self_from, self_to, other_from, other_to])):
            return (self_from + self_to) / 2 > (other_from + other_to) / 2

        # If salaries are indicated BEFORE and salaries FROM are NOT indicated or vice versa
        elif self_from == 0 and self_to != 0 and other_from == 0 and other_to != 0:
            return self_to > other_to
        elif self_from != 0 and self_to == 0 and other_from != 0 and other_to == 0:
            return self_from > other_from

        # If salaries FROM and TO of another class are indicated, but in our class only FROM or TO is indicated
        elif self_from != 0 and self_to == 0 and other_from != 0 and other_to != 0:
            return self_from > other_from
        elif self_from == 0 and self_to != 0 and other_from != 0 and other_to != 0:
            return self_to > other_to

        # If salaries FROM and TO our class are indicated, but in another class only FROM or TO is indicated
        elif self_from != 0 and self_to != 0 and other_from == 0 and other_to != 0:
            return self_to > other_to
        elif self_from != 0 and self_to != 0 and other_from != 0 and other_to == 0:
            return self_from > other_from

    def __eq__(self, other: object) -> bool:
        """This method defines the class behavior for the more operator '=' """
        self_name, self_from, self_to, other_name, other_from, other_to = self.prepare_comparison_data(other)

        # If salary FROM, salary TO and job title are equal
        return self_from == other_from and self_to == other_to and self_name == other_name

    # Methods classes
    def vacancy_to_dict(self) -> dict:
        """This method returns a dictionary with job information"""
        dict_vacancy = \
            {'name': self.__name, 'address': self.__address,
             'salary': {'from': self.__salary_from, 'to': self.__salary_to, 'currency': self.__salary_currency},
             'experience': self.__experience, 'employment': self.__employment, 'url': self.__url,
             'Web-site': self.__web_site}
        return dict_vacancy

    def convert_currency(self, salary: float or int, currency: str) -> float or int:
        """This method converts salary from foreign currency into rubles."""
        for dict_ in self.exchange_rate:
            if dict_['letter_code'] == currency:
                my_dict = dict_
                new_salary = salary * float(my_dict['rate'].replace(',', '.')) / int(my_dict['quantity'])
                return new_salary
