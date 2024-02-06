import pytest
import builtins
from src.classes.get_data import GetDataFromUser


def test_initialization(mocker):
    # Test Case. Testing initialization
    mocker.patch.object(builtins, 'input', side_effect=['Python', '6'])
    get_data = GetDataFromUser()
    assert get_data.name_vacancy == 'Python'
    assert get_data.experience['name'] == 'Более 6 лет'


@pytest.mark.parametrize(
    'my_input,my_result',
    [(['Python Developer'], 'Python Developer'), (['Менеджер'], 'Менеджер'), ([''], None)]
)
def test_input_vacancy_name(my_input, my_result, mocker):
    # Test Case staticmethod 'input_vacancy_name' classes 'GetDataFromUser'
    mocker.patch.object(builtins, 'input', side_effect=my_input)
    result = GetDataFromUser.input_vacancy_name()
    assert result == my_result


@pytest.mark.parametrize(
    'my_input,my_result,my_print',
    [(['0'], 'Нет опыта', ''), (['1'], 'От 1 года до 3 лет', ''), (['4'], 'От 3 до 6 лет', ''),
     (['6'], 'Более 6 лет', ''), (['noExperience', '5'], 'От 3 до 6 лет', 'Вы ввели не корректный опыт\n'),
     (['noExperience', 'noExperience', '5'], 'От 3 до 6 лет', 'Вы ввели не корректный опыт\n' * 2)]
)
def test_input_experience1(my_input, my_result, my_print, mocker, capsys):
    # Test Case staticmethod 'input_experience()' classes 'GetDataFromUser' if return correct answer
    mocker.patch.object(builtins, 'input', side_effect=my_input)
    result = GetDataFromUser.input_experience()
    captured = capsys.readouterr()
    print(result)
    assert captured.out == my_print
    assert result['name'] == my_result


@pytest.mark.parametrize(
    'my_input,my_result,my_print',
    [([''], None, ''),
     (['Not', 'Not', 'Not'], None, 'Вы ввели не корректный опыт\n' * 3 +
     'Вы 3 раза ввели ваш опыт работы неверно. Поиск будет осуществлён без фильтра "Опыт работы".\n')]
)
def test_input_experience2(my_input, my_result, my_print, mocker, capsys):
    # Test Case staticmethod 'input_experience()' classes 'GetDataFromUser' if return None
    mocker.patch.object(builtins, 'input', side_effect=my_input)
    result = GetDataFromUser.input_experience()
    captured = capsys.readouterr()
    print(result)
    assert captured.out == my_print
    assert result is None
