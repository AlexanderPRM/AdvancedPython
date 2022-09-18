import requests
from pprint import pprint

def create_dir(token, dir_name):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params={'path': dir_name}, headers=headers)
    return response


def get_all_info(token, dir_name):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    response = requests.get('https://cloud-api.yandex.net/v1/disk/resources', params={'path': dir_name}, headers=headers)
    return response



