import requests
from token_47 import token


def create_folder(folder_name: str):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    params = {'path': folder_name}
    response = requests.put(url, headers=headers, params=params)

    return response.status_code
