from decouple import config

import requests
from urllib.parse import urlparse


def shorten_link(token, url):
    shortening_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    long_url = url
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {"long_url": long_url}
    response = requests.post(shortening_url, headers=headers, json=data)
    response.raise_for_status()
    bitlink = response.json()['link'].split('//')[-1]
    return bitlink


def count_clicks(token, bitlink):
    summary_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(summary_url, headers=headers)
    response.raise_for_status()
    total_clicks = response.json()['total_clicks']
    return total_clicks


def is_bitlink(url):
    parsed = urlparse(url)
    it_is_bitlink = True
    if parsed.scheme != '':
        it_is_bitlink = False
    return it_is_bitlink


if __name__ == "__main__":
    token = config('TOKEN')
    user_input = input()
    try:
        if is_bitlink(user_input):
            sum_of_clicks = count_clicks(token, user_input)
            print('Количество кликов:', sum_of_clicks)
        else:
            bitlink = shorten_link(token, user_input)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print('Неверная ссылка')
