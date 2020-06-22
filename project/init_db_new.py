import requests
from selenium import webdriver
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.fitlogdb


def getUrls():

    for page_no in range(1, 11):
        url = 'https://terms.naver.com/list.nhn?cid=51001&categoryId=51001&page=' + \
            str(page_no)
        # url = 'https://terms.naver.com/list.nhn?cid=51001&categoryId=51001'

        driver = webdriver.Chrome(('./chromedriver'))
        driver.implicitly_wait(3)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        workouts = soup.select('#content > div.list_wrap > ul')

        for workout in workouts:
            img = workout.select('div.thumb_area > div > a > img')
            title = workout.select(
                'div.info_area > div.subject > strong > a:nth-child(1)')
            desc = workout.select('div.info_area > p')
            difficulty = workout.select(
                'div.info_area > div:nth-child(3) > div > span:nth-child(1)')
            part = workout.select(
                'div.info_area > div:nth-child(3) > div > span:nth-child(2) > em')
            main_part = workout.select(
                'div.info_area > div:nth-child(3) > div > span:nth-child(3) > em')

            for item in zip(img, title, desc, difficulty, part, main_part):
                workout_set = {
                    '사진': item[0]['src'],
                    '운동명': item[1].text,
                    '운동설명': item[2].text.strip(),
                    '운동난이도': item[3].text,
                    '운동부위': item[4].text,
                    '주요운동부위': item[5].text
                }
                db.fitlogdb.insert_one(workout_set)
            print('완료!')


getUrls()
