# _*_coding: UTF-8_*_
# 开发人员  : Jayo
# 开发时间  : 2020/3/6 21:13
# 文件名称  : pachong_douban.PY
# 开发工具  : PyCharm
# 作业内容：
# 安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评
# 并以 UTF-8 字符集保存到 csv 格式的文件中。
# code思路：定义2个函数，函数1:get_mv_info()，函数2:get_my_url()，通过函数2 获取豆瓣子页面的链接，
# 以及电影名称，并将这两个作为参数传给函数1，在函数1中get电影的评分、短评数量和前5条热门短评，传入list中，
# 并return给函数2，函数2再将所有电影信息传入一个大list中，return给调用方，最后将list转为to_csv格式。

import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
from time import sleep
import pandas as pd

header = {}
header['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
    'Chrome/78.0.3904.108 Safari/537.36 '

#url = tuple(f'https://movie.douban.com/top250?start={page * 25}'for page in range(10))
url = 'https://movie.douban.com/top250?start=0'


def get_mv_info(url):
    movie_info = []
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    # 获取电影名字
    movie_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
    movie_info.append(movie_name[0])
    # 获取电影评分
    rating_num = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
    movie_info.append(rating_num[0])
    # 获取电影评价条数
    rating_pepple = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span[@property="v:votes"]/text()')
    movie_info.append(rating_pepple[0])
    # 获取电影前五条短评
    hot_comments = selector.xpath('//*[@id="hot-comments"]//div[@class="comment"]/p/span/text()')
    for hot_comment in hot_comments[:5]:
        movie_info.append(hot_comment)
    return movie_info



def get_my_url(url):
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    movie_infos = []
    # movie_names = selector.xpath(
    #     '//*[@id="content"]//div[@class="hd"]/a/span[1]/text()')
    hrefs = selector.xpath('//*[@id="content"]//div[@class="hd"]/a/@href')
    # print(href)
    for href in hrefs[:2]:
        movie_info = get_mv_info(href)
        sleep(1)
        movie_infos.append(movie_info)

    return movie_infos


if __name__ == '__main__':

    results = get_my_url(url)
    cs_column = ['电影名称', '电影评分', '电影评价条数', '热评1', '热评2', '热评3', '热评4', '热评5']
    movie_info = pd.DataFrame(columns=cs_column, data = results)
    print(movie_info)
    movie_info.to_csv('/Users/jayoxie/Documents/GitHub/Pythontest/learning_test/geektime_task/movie_info.csv', encoding='utf-8')
