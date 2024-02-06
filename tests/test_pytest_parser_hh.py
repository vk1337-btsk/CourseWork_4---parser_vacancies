import pytest
import builtins
from src.classes.parser_hh import ParserVacancyHH
from src.classes.get_data import GetDataFromUser


# Initialization instance class ParserVacancyHH
@pytest.fixture()
def hh(mocker):
    mocker.patch.object(builtins, 'input', side_effect=['Python', '6'])
    get_data = GetDataFromUser()
    hh = ParserVacancyHH(get_data)
    return hh


def test_get_headers(hh):
    # Test Case. Testing method classes 'get_headers'
    assert (hh.get_headers() ==
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/121.0.0.0 Safari/537.36'})


def test_get_params(hh):
    # Test Case. Testing method classes 'get_params'
    assert (hh.get_params() == {'page': 0, 'per_page': 100, 'text': 'Python', 'experience': 'moreThan6'})


@pytest.mark.parametrize('currency_old,currency_new', [('RUR', 'RUB'), ('BYR', 'BYN')])
def test_formatting_vacancy(hh, currency_old, currency_new):
    # Test Case. Testing method classes 'formatting_vacancy'
    vacancy = {
        "name": "Инженер (Китай)", "salary": {"from": 400000, "to": 500000, "currency": currency_old}, "address": None,
        "alternate_url": "https://hh.ru/vacancy/...", "employment": {"id": "full", "name": "Полная занятость"},
        "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"}
    }

    assert (hh.formatting_vacancy(vacancy) ==
            {'name': "Инженер (Китай)", 'address': 'Не указан',
             'salary': {'from': 400000, 'to': 500000, 'currency': currency_new}, 'experience': 'От 1 года до 3 лет',
             'employment': 'Полная занятость', 'url': 'https://hh.ru/vacancy/...', 'Web-site': "HeadHunter"})
