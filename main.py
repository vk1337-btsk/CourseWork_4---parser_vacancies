from src.utils import load_new_vacancies, only_read_vacancies, filter_vacancies


if __name__ == '__main__':
    count = 0

    while True:
        answer = input(str(
            'Здравствуйте! Это программа для просмотра вакансий. '
            'Желаете загрузить новые вакансии с сайтов HeadHunter и SuperJob или просмотреть уже загруженные?\n'
            'Введите 1, если хотите загрузить новые вакансии и нажмите 2, чтобы просмотреть уже загруженные.'
            'Если хотите выйти - нажмите 3.\n'
            '-> '))

        if answer == '1':
            load_new_vacancies()

        elif answer == '2':
            # User input '2', reading already saved vacancies
            count_ = 0

            while True:

                answer_ = input(str(
                    'Вы желаете вывести все вакансии или отфильтровать их?\n'
                    'Введите 1, если хотите вывести все вакансии или введите 2, если желаете их отфильтровать.\n'
                    'Введите 3, чтобы выйти.\n'
                    '-> '))

                if answer_ == '1':
                    only_read_vacancies()
                    count = 3
                    break

                elif answer_ == '2':
                    filter_vacancies()
                    count = 3
                    break

                elif answer_ == '3':
                    # User input '3', exit from program
                    print('Вы ввели "3" - выходим из программы')
                    count = 3
                    break

                count_ += 1
                if count_ == 3:
                    print('Вы трижды ввели некорректный запрос. Выхожу из программы...')
                    break

        elif answer == '3':
            # User input '3', exit from program
            print('Вы ввели "3" - выходим из программы')
            break

        count += 1
        if count >= 3:
            print('Выходим из программы')
            break
