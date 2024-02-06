from src.classes.parser_hh import ParserVacancyHH
from src.classes.parser_sj import ParserVacancySJ
from src.classes.get_data import GetDataFromUser
from src.classes.saver import Saver
from src.classes.vacancy import Vacancy


if __name__ == '__main__':

    criteria = GetDataFromUser()

    list_vacancies = []
    for parser in [ParserVacancyHH(criteria), ParserVacancySJ(criteria)]:
        list_vacancies.extend(parser.get_all_vacancies())

    list_vacancies = [Vacancy(vacancy) for vacancy in list_vacancies]

    print(*list_vacancies, sep='\n')
    list_vacancies = [v.vacancy_to_dict() for v in list_vacancies]
    Saver.save_data_json(list_vacancies)
