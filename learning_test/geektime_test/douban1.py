# _*_coding: UTF-8_*_
# 开发人员  : oini
# 开发时间  : 2020/2/29 20:17
# 文件名称  : douban1.PY
# 开发工具  : PyCharm

#   F12调试模式分析网页源代码
#   用requests爬取网页全部内容
#   用Beautiful Soup 解析网页提取关键信息：pip install bs4
#   用csv文件存储书籍名字和评分


import requests  # 实现http协议
from bs4 import BeautifulSoup as bs  # 分析内容


# 请求翻页：https://book.douban.com/top250?start=25
# 定义一个函数

def get_url_name(myurl):
    # 设置user_agent，header [反爬虫技巧]
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {'user-agent': user_agent}

    url = 'https://book.douban.com/top250?start=0'
    response = requests.get(url, headers=header)
    print(response)
    print(response.text)
    bs(response.text, 'html.parser')
    # 'lxml'#  速度最快，兼容性容错比html强
    bs_info = bs(response.text, 'html.parser')

    # 可以不用正则表达式，就找到指定的位置
    # bs_info.find_all()
    bs_info = bs(response.text, 'html.parser')

    # 取出第一本书，切片操作
    # print(bs_info.find_all('div', attrs={'class': 'pl2'})[0])

    # type(bs_info.find_all('div', attrs={'class': 'pl2'}))

    # 遍历
    for tags in bs_info.find_all('div', attrs={'class': 'p12'}):
        # 获取a标签
        # a_tag = tags.contents[1]
        # print(a_tag)
        for atag in tags.find_all('a', ):
            # 获取所有链接
            print(atag.get('href'))
            # 获取图书名字
            print(atag.get('title'))


urls = tuple(f'https://book.douban.com/top250?start={page * 25}' for page in range(10))
from time import sleep


for page in urls:
    get_url_name(page)
    sleep(5)