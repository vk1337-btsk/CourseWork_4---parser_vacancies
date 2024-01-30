class GetDataFromUser:
    """This class collects information from the user about desired vacancies and form criteria for search"""


    def __init__(self):
        """
        Initialization attributes classes
        """
        self.name_vacancy = self.input_vacancy_name()

    # Static methods for getting search criteria
    @staticmethod
    def input_vacancy_name():
        """This method requests name vacancy from the user.
        :return: name vacancy or None
        """
        vacancy_name = input('Введите название вакансии для поиска или нажмите Enter, чтобы не искать по: ')
        if vacancy_name == "":
            return None
        return vacancy_name
