import requests
from pprint import pprint
def create_dir(token, dir_name):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params={'path': dir_name}, headers=headers)
    return response

# status_code = create_dir('AQAAAAAfkNmRAADLWyZzDnjg1Ecos34Spfj_fUM').status_code

def get_all_info(token, dir_name):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    response = requests.get('https://cloud-api.yandex.net/v1/disk/resources', params={'path': dir_name}, headers=headers)
    return response

print('test1' in get_all_info('AQAAAAAfkNmRAADLWyZzDnjg1Ecos34Spfj_fUM', 'test1').json()['_embedded']['path'])


