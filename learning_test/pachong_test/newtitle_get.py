# _*_coding: UTF-8_*_
# 开发人员  : oini
# 开发时间  : 2020/3/2 17:09
# 文件名称  : newtitle_get.PY
# 开发工具  : PyCharm
import requests
from bs4 import BeautifulSoup
import re

# 告诉网站是合法的浏览器
from pip._internal.models import link

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

url1 = 'http://www.chinanews.com/'


# 获取网页中的标题
def craw1(url):
    response = requests.get(url, headers=headers)
    # 如果会出现乱码，一定要先查看网页的编码方式，上述网页的编码方式为utf-8，只需添加为web指定编码方式即可
    response.encoding = 'UTF-8'
    # 把页面全扒拉下来
    # print(response.text)

    # 把响应结果页面通过BeatufulSoup方法按照lxml格式优化
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)

    for href_title in soup.find_all('div', 'group'):
        # 打印div标签下，group组的内容
        # print(href_title)

        for title in href_title.find_all('a'):

            #   打印a标签中的内容
            # print(title)
            title = str(title)

            pattern = re.compile(r'<a href="//(.*?)">(.*?)</a>', re.S)
            results = re.findall(pattern, title)
            print(results)

                #     title = title.append('title')
                # print(title.get('href'))
        # print([title.get('title')
        #        for title in href_title.find_all('a') if title.get('title')])


craw1(url1)
