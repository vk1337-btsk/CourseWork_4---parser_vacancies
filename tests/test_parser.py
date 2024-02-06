import pytest
from src.classes.parser_hh import ParserVacancyHH
from src.classes.parser import Parser


# Initialization instance classes ParserHH
@pytest.fixture()
def test_parser():
    parser = ParserVacancyHH
    return parser


@pytest.mark.parametrize('key,result', [('noExperience', 'Нет опыта'), ('between1And3', 'От 1 года до 3 лет'),
                                        ('between3And6', 'От 3 до 6 лет'), ('moreThan6', 'Более 6 лет'),
                                        ('1', 'Нет опыта'), ('2', 'От 1 года до 3 лет'),
                                        ('3', 'От 3 до 6 лет'), ('4', 'Более 6 лет'), (None, None)])
def test_get_value_experience(test_parser, key, result):
    # Test Case. Testing method 'get_value_experience'
    assert test_parser.get_value_experience(key) == result


def test_get_value_employment(test_parser):
    # Test Case. Testing method 'get_value_employment'
    key = None
    assert test_parser.get_value_employment(key) is None


def test_get_time_for_sleep():
    # Test Case. Testing method 'get_time_for_sleep'
    result = Parser.get_time_for_sleep()
    assert 0.3 <= result <= 0.5
