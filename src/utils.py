from src.classes.parser_hh import ParserVacancyHH
from src.classes.parser_sj import ParserVacancySJ
from src.classes.get_data import GetDataFromUser
from src.classes.saverreader import SaverReader
from src.classes.vacancy import Vacancy


def load_new_vacancies() -> None:
    # User input '1', load new vacancies
    criteria = GetDataFromUser()

    list_vacancies = []
    for parser in [ParserVacancyHH(criteria), ParserVacancySJ(criteria)]:
        list_vacancies.extend(parser.get_all_vacancies())

    list_vacancies = [Vacancy(vacancy) for vacancy in list_vacancies]

    print(*list_vacancies, sep='\n')
    list_vacancies = [v.vacancy_to_dict() for v in list_vacancies]
    SaverReader.save_data_json(list_vacancies)


def only_read_vacancies():
    list_vacancies = [Vacancy(vacancy) for vacancy in SaverReader.read_data_json()]
    print(*list_vacancies, sep='\n')


def filter_vacancies():
    list_vacancies = [Vacancy(vacancy) for vacancy in SaverReader.read_data_json()]

    criteria_filter = input(str('Введите критерий, по которому желаете отфильтровать вакансии.\n'
                                '1 - по названию\n'
                                '2 - по адресу\n'
                                '-> '))

    if criteria_filter == '1':
        key_word = input('Введите ключевое слово: ')
        list_vacancies = list(filter(lambda x: key_word.lower() in x.name.lower(), list_vacancies))
        print(*list_vacancies, sep='\n')

    elif criteria_filter == '2':
        key_word = input('Введите ключевое слово: ')
        list_vacancies = list(filter(lambda x: (key_word.lower() in x.address.lower() if x.address else False),
                                     list_vacancies))
        print(*list_vacancies, sep='\n')
