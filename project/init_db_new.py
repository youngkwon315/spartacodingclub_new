from selenium import webdriver
from bs4 import BeautifulSoup


url = 'https://www.jefit.com/exercises/bodypart.php?id=11&exercises=All'

driver = webdriver.Chrome(('./chromedriver'))
driver.implicitly_wait(3)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

workouts = soup.select("#hor-minimalist_3 > tbody > tr > td > table > tbody")

for workout in workouts:
    img = workout.select(
        'tr > td > a > img')
    title = workout.select(
        'tr > td > h4 > a')
    part = workout.select(
        'tr > td > p')

    for i in img:
        img_url = i['src']
        ex_title = title[i].text
        ex_part = part[i].text.strip()

        doc = {
            'workout_name': ex_title,
            'img_url': img_url,
            'workout_part': ex_part
        }
        print('완료!', title)
