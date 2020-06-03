import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.fitlogdb


def get_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://www.bodybuilding.com/exercises/finder', headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    workouts = soup.select(
        '#js-ex-category-body > div.ExCategory-results > div')

    for workout in workouts:
        img = workout.select_one(
            '#js-ex-category-body > div.ExCategory-results > div:nth-child(2) > div:nth-child(1) > img')
        test = workout.select_one(
            'div.ExResult-cell.ExResult-cell--nameEtc > h3')
        part = workout.select_one(
            'div.ExResult-cell.ExResult-cell--nameEtc > div > a')

        if test is not None:
            image = img['src']
            title = test.text.strip()
            part = part.text.strip()
            print(image, title, part)


get_urls()
