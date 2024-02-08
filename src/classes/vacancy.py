from src.classes.mixin import Mixin


class Vacancy(Mixin):
    """This class represent information about one vacancy and provides functionality for working with it """

    # Initialization attributes
    def __init__(self, dict_info_vacancy: dict) -> None:
        """Initialization attributes
        :param dict_info_vacancy - dict with information about vacancy"""
        self.exchange_rate = Mixin.get_exchange_rate()

        self.info_vacancy = dict_info_vacancy
        self.name = self.info_vacancy['name']
        self.address = self.info_vacancy['address']
        self.salary_from = 0 if self.info_vacancy['salary']['from'] is None else self.info_vacancy['salary']['from']
        self.salary_to = 0 if self.info_vacancy['salary']['to'] is None else self.info_vacancy['salary']['to']
        self.salary_currency = (0 if self.info_vacancy['salary']['currency'] is None
                                  else self.info_vacancy['salary']['currency'])
        self.experience = self.info_vacancy['experience']
        self.employment = self.info_vacancy['employment']
        self.url = self.info_vacancy['url']
        self.web_site = self.info_vacancy['Web-site']

    # Magic methods str and repr
    def __str__(self) -> str:
        """Shows information for user"""
        if all(map(lambda x: x == 0, [self.salary_from, self.salary_to, self.salary_currency])):
            return f'Вакансия: {self.name}, зарплата не указана. Ссылка на вакансию: {self.url}'
        return (f'Вакансия: {self.name}, зарплата {self.salary_from}-{self.salary_to} {self.salary_currency}. '
                f'Ссылка на вакансию: {self.url}')

    def __repr__(self) -> str:
        """Shows information for developer"""
        return (f'Экземпляр класса: {self.__class__.__name__}\n'
                f'С аргументами: {self.name=}, {self.address=}, {self.salary_from=}, {self.salary_to=},'
                f'{self.salary_currency=}, {self.experience=}, {self.employment=}, {self.url=}, '
                f'{self.web_site=}.')

    # Magic methods comparison
    def prepare_comparison_data(self, other: object) -> tuple[str, int, int, str, int, int]:
        """This method prepares data for comparisons vacancies."""
        self_name = self.name
        self_from = self.salary_from
        self_to = self.salary_to
        self_currency = self.salary_currency

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
            {'name': self.name, 'address': self.address,
             'salary': {'from': self.salary_from, 'to': self.salary_to, 'currency': self.salary_currency},
             'experience': self.experience, 'employment': self.employment, 'url': self.url,
             'Web-site': self.web_site}
        return dict_vacancy

    def convert_currency(self, salary: float or int, currency: str) -> float or int:
        """This method converts salary from foreign currency into rubles."""
        for dict_ in self.exchange_rate:
            if dict_['letter_code'] == currency:
                my_dict = dict_
                new_salary = salary * float(my_dict['rate'].replace(',', '.')) / int(my_dict['quantity'])
                return new_salary
