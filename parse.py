import requests
from bs4 import BeautifulSoup
import os
import datetime

url = 'https://koronavirusinfo.az/az/page/statistika/azerbaycanda-cari-veziyyet'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
           "Accept-Encoding": "*", "Connection": "keep-alive"}


def req():
    return BeautifulSoup(requests.get(url, headers=headers).text, 'lxml').find_all('div', class_='flex_container')[1]


def genecov():
    return f"""{req().find_all('div', class_='gray_little_statistic')[0].find('strong').text}"""


def recovered():
    return f"""{req().find_all('div', class_='gray_little_statistic')[1].find('strong').text}"""


def new():
    return f"""{req().find_all('div', class_='gray_little_statistic')[2].find('strong').text}"""


def active():
    return f"""{req().find_all('div', class_='gray_little_statistic')[3].find('strong').text}"""


def deaths():
    return f"""{req().find_all('div', class_='gray_little_statistic')[4].find('strong').text}"""


def tests():
    return f"""{req().find_all('div', class_='gray_little_statistic')[5].find('strong').text}"""
