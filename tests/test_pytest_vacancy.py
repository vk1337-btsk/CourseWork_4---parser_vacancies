import pytest
from src.classes.vacancy import Vacancy


@pytest.fixture()
def vacancy():
    # Create an instance of the class Vacancy
    my_vacancy = Vacancy(
        {'name': 'Менеджер', 'address': 'Не указан', 'salary': {'from': 30000, 'to': 44000, 'currency': 'RUB'},
         'experience': 'Нет опыта', 'employment': 'Полная занятость', 'url': 'https://hh.ru/vacancy/....',
         'Web-site': 'HeadHunter'}
    )
    return my_vacancy


def test_str_and_repr_classes_vacancy(vacancy):
    # Test Case. Testing magic methods 'str' and 'repr' class Vacancy
    assert str(vacancy) == ("Вакансия: Менеджер, зарплата 30000-44000 RUB. "
                            "Ссылка на вакансию: https://hh.ru/vacancy/....")

    assert repr(vacancy) == ("Экземпляр класса: Vacancy\n"
                             "С аргументами: self.__name='Менеджер', self.__address='Не указан', "
                             "self.__salary_from=30000, self.__salary_to=44000,self.__salary_currency='RUB', "
                             "self.__experience='Нет опыта', self.__employment='Полная занятость', "
                             "self.__url='https://hh.ru/vacancy/....', self.__web_site='HeadHunter'.")


@pytest.mark.parametrize(
    'self_salary_from,self_salary_to,self_salary_currency,other_salary_from,other_salary_to,other_salary_currency',
    [(40000, 50000, 'RUB', 30000, 40000, 'RUB'), (0, 50000, 'RUB', 0, 40000, 'RUB'),
     (40000, 0, 'RUB', 30000, 0, 'RUB'), (0, 50000, 'RUB', 30000, 40000, 'RUB'),
     (40000, 0, 'RUB', 30000, 40000, 'RUB'), (40000, 50000, 'RUB', 0, 40000, 'RUB'),
     (40000, 50000, 'RUB', 30000, 0, 'RUB'), (1000, 1100, 'GEL', 20000, 0, 'RUB'),
     (40000, 50000, 'RUB', 1000, 1100, 'GEL'), (40000, 40000, 'RUB', 40000, 40000, 'RUB'),
     (0, 0, 'RUB', 0, 0, 'RUB')]
)
def test_comparison_of_vacancies_gt(self_salary_from, self_salary_to, self_salary_currency,
                                    other_salary_from, other_salary_to, other_salary_currency):
    # Test Case. Testing magic method 'gt' class Vacancy
    vacancy1 = Vacancy(
        {"name": "Автоинспектор", "address": "Не указан",
         "salary": {"from": self_salary_from, "to": self_salary_to, "currency": self_salary_currency},
         "experience": "От 1 года до 3 лет", "employment": "Полная занятость", "url": "https://hh.ru/vacancy/....",
         "Web-site": "HeadHunter"})
    vacancy2 = Vacancy(
        {"name": "Инженер (Япония)", "address": "Не указан",
         "salary": {"from": other_salary_from, "to": other_salary_to, "currency": other_salary_currency},
         "experience": "От 1 года до 3 лет", "employment": "Полная занятость", "url": "https://hh.ru/vacancy/....",
         "Web-site": "HeadHunter"})
    assert vacancy1 > vacancy2


@pytest.mark.parametrize(
    'self_salary_from,self_salary_to,self_salary_currency,other_salary_from,other_salary_to,other_salary_currency',
    [(40000, 50000, 'RUB', 40000, 50000, 'RUB')])
def test_comparison_of_vacancies_eq(self_salary_from, self_salary_to, self_salary_currency,
                                    other_salary_from, other_salary_to, other_salary_currency):
    # Test Case. Testing magic method 'eq' class Vacancy
    vacancy1 = Vacancy(
        {"name": "Уборщик", "address": "Не указан",
         "salary": {"from": self_salary_from, "to": self_salary_to, "currency": self_salary_currency},
         "experience": "От 1 года до 3 лет", "employment": "Полная занятость", "url": "https://hh.ru/vacancy/....",
         "Web-site": "HeadHunter"})
    vacancy2 = Vacancy(
        {"name": "Уборщик", "address": "Не указан",
         "salary": {"from": other_salary_from, "to": other_salary_to, "currency": other_salary_currency},
         "experience": "От 1 года до 3 лет", "employment": "Полная занятость", "url": "https://hh.ru/vacancy/....",
         "Web-site": "HeadHunter"})
    assert vacancy1 == vacancy2


def test_vacancy_to_dict(vacancy):
    # Test Case. Testing method class 'vacancy_to_dict'
    assert vacancy.vacancy_to_dict() == {'name': 'Менеджер', 'address': 'Не указан',
                                         'salary': {'from': 30000, 'to': 44000, 'currency': 'RUB'},
                                         'experience': 'Нет опыта', 'employment': 'Полная занятость',
                                         'url': 'https://hh.ru/vacancy/....', 'Web-site': 'HeadHunter'}
