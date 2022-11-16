# Devman-Bitly

This program, when the user enters a full link, displays its shortened version on the console. And when a user enters a shortened link, the program displays the number of clicks on this link to the console.
## Environment

### Requirements

Python3 should be already installed. Then use pip3 to install dependencies:

```bash
pip3 install -r requirements.txt
```

### Environment variables

- BITLY_AUTH_TOKEN

1. Put `.env` file near `main.py`.
2. `.env` contains text data without quotes.

For example, if you print `.env` content, you will see:

```bash
$ cat .env
BITLY_AUTH_TOKEN=2d7e51f838b66c3d28d1d2607a92e77e2ggeba30
```
#### How to get

* Register an application [API bitly](https://app.bitly.com/) and get the `Access Token` in [settings](https://app.bitly.com/settings/api/)


## Run

Launch on Linux(Python 3) or Windows:

```bash

$ python3 main.py ВАША_ССЫЛКА

```

You will see:

```
Битлинк bit.ly/3En2LWy
```
or
```
Количество кликов: 3
```
