from decouple import config
import requests
import argparse

parser = argparse.ArgumentParser(
    description='Сокращает ссылку или выдает количество переходов по сокращенной ссылке'
)
parser.add_argument('link', help='your_link')


def shorten_link(token, url):
    api_endpoint = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    long_url = {"long_url": url}
    response = requests.post(api_endpoint, headers=headers, json=long_url)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, bitlink):
    api_endpoint = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()
    total_clicks = response.json()['total_clicks']
    return total_clicks


def is_bitlink(token, url):
    api_endpoint = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(api_endpoint, headers=headers)
    return response.ok


if __name__ == "__main__":
    args = parser.parse_args()
    token = config('BITLY_AUTH_TOKEN')
    user_input = args.link
    try:
        if is_bitlink(token, user_input):
            sum_of_clicks = count_clicks(token, user_input)
            print('Количество кликов:', sum_of_clicks)
        else:
            bitlink = shorten_link(token, user_input)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print('Неверная ссылка')
