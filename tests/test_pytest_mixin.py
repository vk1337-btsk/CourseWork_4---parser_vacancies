from src.classes.mixin import Mixin


def test_get_exchange_rate1(mocker):
    # Test Case. Testing staticmethod 'get_exchange_rate'
    mocker_response = mocker.Mock()
    mocker_response.text = """
    <div class="table">
    <tr>...</tr>
    <tr>
       <td>10400</td>
       <td>GEL</td>
       <td>9999</td>
       <td>Манат</td>
       <td>45,6547</td>
    </tr>
    </div>
    """

    # Create a stub for the request.get
    mocker.patch("src.classes.mixin.requests.get", return_value=mocker_response)

    # Check
    assert Mixin.get_exchange_rate() == [
       {'digit_code': '10400', 'letter_code': 'GEL', 'quantity': '9999', 'currency': 'Манат', 'rate': '45,6547'}
    ]

    # Return the attribute value to None
    Mixin._exchange_rate = None
