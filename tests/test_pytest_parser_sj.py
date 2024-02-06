import pytest
import builtins
from constant import API_KEY_SJ
from src.classes.parser_sj import ParserVacancySJ
from src.classes.get_data import GetDataFromUser


# Initialization instance class ParserVacancySJ
@pytest.fixture()
def sj(mocker):
    mocker.patch.object(builtins, 'input', side_effect=['Python', '6'])
    get_data = GetDataFromUser()
    sj = ParserVacancySJ(get_data)
    return sj


def test_get_headers(sj):
    # Test Case. Testing method classes 'get_headers'
    assert (sj.get_headers() == {'Host': 'api.superjob.ru', 'X-Api-App-Id': API_KEY_SJ})


def test_get_params(sj):
    # Test Case. Testing method classes 'get_params'
    assert (sj.get_params() == {'page': 0, 'count': 50, 'keyword': 'Python', 'experience': '4'})


def test_formatting_vacancy(sj):
    # Test Case. Testing method classes 'formatting_vacancy'
    vacancy = {
        "profession": "Инженер", "payment_from": 400000, "payment_to": 500000, "currency": 'rub',
        "address": None,  "link": "https://sj.ru/vacancy/...", "type_of_work": {"id": "6", "name": "Полная занятость"},
        "experience": {"id": "4", "name": "От 1 года до 3 лет"}
    }

    assert (sj.formatting_vacancy(vacancy) ==
            {'name': "Инженер", 'address': 'Не указан',
             'salary': {'from': 400000, 'to': 500000, 'currency': 'RUB'}, 'experience': 'Более 6 лет',
             'employment': 'Полная занятость', 'url': 'https://sj.ru/vacancy/...', 'Web-site': "SuperJob"})
