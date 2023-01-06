import pytest
import requests
from ya_create_folder import create_folder
from token_47 import token


fixtures = [
    ('test_folder', 201),
    ('test_folder', 409),
    ('test_folder_2', 201)
]

fixtures_2 = ['test_folder', 'test_folder_2']


@pytest.mark.parametrize('name_f, status_code', fixtures)
def test_create_folder_1(name_f: str, status_code: int):
    assert create_folder(name_f) == status_code


@pytest.mark.parametrize('name_f', fixtures_2)
def test_create_folder_2(name_f: str):
    list_folder = list()
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    params = {'path': '/'}
    response = requests.get(url, headers=headers, params=params)

    for item in response.json()['_embedded']['items']:
        if item['type'] == 'dir':
            list_folder.append(item['name'])

    assert name_f in list_folder


@pytest.mark.parametrize('name_f', fixtures_2)
def test_create_folder_3(name_f: str):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    params = {'path': name_f}
    response = requests.delete(url, headers=headers, params=params)

    assert response.status_code == 204