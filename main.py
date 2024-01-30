from src.classes.parser_hh import ParserVacancyHH
from src.classes.parser_sj import ParserVacancySJ
from src.classes.get_data import GetDataFromUser


if __name__ == '__main__':

    criteria = GetDataFromUser()
    hh = ParserVacancyHH(criteria)
    hh.get_all_vacancies()

    sj = ParserVacancySJ(criteria)
    sj.get_all_vacancies()
