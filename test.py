import pytest
from main import get_cat_photo


def test_get_cat_photo_success(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'url': 'https://cdn2.thecatapi.com/images/abcd1234.jpg'
    }
    photo = get_cat_photo()
    assert photo == {'url':'https://cdn2.thecatapi.com/images/abcd1234.jpg'}


def test_get_cat_photo_unsuccess(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    photo = get_cat_photo()
    assert photo is None
    