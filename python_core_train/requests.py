# Получает ссылку и возвращает битлинк, если уже создан, то возвращает количество кликов

import os
import requests
from urllib.parse import urlparse


def is_bitlink(user_link, headers):
    user_link = urlparse(user_link).netloc + urlparse(user_link).path
    info_url = f'https://api-ssl.bitly.com/v4/bitlinks/{user_link}'
    response = requests.get(info_url, headers=headers)
    return response.ok


def count_clicks(user_link, headers):
    user_link = urlparse(user_link).netloc + urlparse(user_link).path
    print(user_link)
    user_link = f'https://api-ssl.bitly.com/v4/bitlinks/{user_link}/clicks/summary'
    params = (
        ('unit', 'month'),
        ('units', '-1'),
    )
    response = requests.get(user_link, headers=headers, params=params)
    return response.json()['total_clicks']


def shorten_link(user_link, headers):
    short_url = 'https://api-ssl.bitly.com/v4/shorten'
    data = {"long_url": user_link, "domain": "bit.ly"}
    response_post = requests.post(short_url, headers=headers, json=data)
    response_post.raise_for_status()
    return response_post.json()["link"]


def main_run():
    token = os.environ['Bitly_Token']
    headers = {'Authorization': f'Bearer {token}'}
    user_link = input('Введите ссылку для сокращения: ')
    if is_bitlink(user_link, headers):
        try:
            counts = count_clicks(user_link, headers)
            print(f'Число кликов по ссылке: {counts}')
        except requests.exceptions.HTTPError as error:
            exit(f"Неправильная ссылка:\n{0}".format(error))
    else:
        try:
            user_link = shorten_link(user_link, headers)
            print(f'Битлинк {user_link}')
        except requests.exceptions.HTTPError as error:
            exit(f"Неправильная ссылка:\n{0}".format(error))


if __name__ == '__main__':
    main_run()
