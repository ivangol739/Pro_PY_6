import requests


TOKEN_YA = 'AQAAAAA3RXiVAADLW8Te5tpGPUMmuKtKHjr-QgI'
url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {
            'Content-Type': 'application/json',
            'Authorization': TOKEN_YA
        }

def folder_create(folder):
    params = {
        'path': folder
    }
    response = requests.put(url=url, headers=headers, params=params)
    return response.status_code

def folder_check(folder):
    params = {
        'path': folder
    }
    response = requests.get(url=url, headers=headers, params=params)
    return response.status_code

folder_create('test')
folder_check('test')

