# _*_coding: UTF-8_*_
# 开发人员  : oini
# 开发时间  : 2020/2/29 20:17
# 文件名称  : douban1.PY
# 开发工具  : PyCharm

#   F12调试模式分析网页源代码
#   用requests爬取网页全部内容
#   用Beautiful Soup 解析网页提取关键信息：pip install bs4
#   用csv文件存储书籍名字和评分


# 请求翻页：https://book.douban.com/top250?start=25
# 定义一个函数

# 标准库定义：安装好工具，系统已经集成好的库，可以直接使用，不需要另外安装，可以直接通过import导库
# 第三方库：需要通过不同的安装方法进行安装，大部分的第三方工具都可以通过pip进行安装

import requests  # 第三方库
from bs4 import BeautifulSoup as bs # 解析html，使用bs4的优点：

url = 'https://book.douban.com/top250?start=0'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# 伪装，反爬虫，引入请求头
header = {'user-agent': user_agent}

response = requests.get(url, headers=header)
print(response.status_code)

bs_info = bs(response.text, 'html.parser')
print(bs_info.find_all('div', attrs={'class', 'pl2'})[0])