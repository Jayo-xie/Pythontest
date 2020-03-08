# _*_coding: UTF-8_*_
# 开发人员  : oini
# 开发时间  : 2020/2/29 21:04
# 文件名称  : douban2.PY
# 开发工具  : PyCharm
# _*_coding: UTF-8_*_
# 开发人员  : oini
# 开发时间  : 2020/2/29 21:04
# 文件名称  : douban2.PY
# 开发工具  : PyCharm
from bs4 import BeautifulSoup as bs
import requests

myurl = 'https://book.douban.com/top250?start=0'

# 如果是豆瓣电影呢？
# myurl = 'https://movie.douban.com/top250?start=0'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {}
header['user-agent'] = user_agent

response = requests.get(myurl, headers=header)
# print(response.text)


# 另一种导入包的方法

bs_info = bs(response.text, 'html.parser')

print(bs_info.find_all('div', attrs={'class': 'pl2'}))

# 豆瓣电影，取第一个
# print(bs_info.find_all('div', attrs={'class': 'hd'})[0])
