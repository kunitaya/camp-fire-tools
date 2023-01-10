#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_binary

driver = webdriver.Chrome()


cf_IDs = [
    36682,
    92999,
    127236,
    371104,
    524004
]
result = []


for cf_ID in cf_IDs:
    # Chromeを開いてcamp-fireの支援者ページにアクセスする
    driver.get('https://camp-fire.jp/projects/' + str(cf_ID) + '/backers')

    # 5秒待機する
    time.sleep(5)

    str_projectName = driver.find_element(By.CLASS_NAME, "project-name").text

    while True:
        main_element = driver.find_element(By.ID, "main")
        body_elms = main_element.find_elements(By.CLASS_NAME, 'body')
        for body_element in body_elms:
            backer = {}
            str_displayUserName = body_element.text.split('\n')[0]
            a_element = body_element.find_element(By.TAG_NAME, 'a')
            str_href = a_element.get_attribute('href')
            str_time = body_element.find_element(By.CLASS_NAME, 'time').text
            str_comment = body_element.find_element(
                By.CLASS_NAME, 'readmore').text

            backer['project'] = str(cf_ID)
            backer['projectName'] = str_projectName
            backer['displayUserName'] = str_displayUserName
            backer['url'] = str_href
            backer['time'] = str_time
            backer['comment'] = str_comment
            result.append(backer)

        pagination_element = main_element.find_element(
            By.CLASS_NAME, 'pagination')
        href_elms = pagination_element.find_elements(By.TAG_NAME, 'a')
        next_elms = list(
            filter(lambda x: x.accessible_name == '次のページ >', href_elms))
        if next_elms:
            next_url = next_elms[0].get_attribute('href')
            driver.get(next_url)
            time.sleep(5)
        else:
            break

# 画面を閉じる
driver.quit()

with open('result.json', 'w', encoding='UTF-8') as f:
    json.dump(result, f, ensure_ascii=False)
