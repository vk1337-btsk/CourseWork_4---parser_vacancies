from src.classes.parser_vacancy_hh import ParserVacancyHH
from src.classes.parser_vacancy_sj import ParserVacancySJ


if __name__ == '__main__':

    hh = ParserVacancyHH()
    hh.get_all_vacancies()

    sj = ParserVacancySJ()
    sj.get_all_vacancies()
