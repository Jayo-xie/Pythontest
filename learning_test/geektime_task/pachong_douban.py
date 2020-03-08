# _*_coding: UTF-8_*_
# 开发人员  : Jayo
# 开发时间  : 2020/3/6 21:13
# 文件名称  : pachong_douban.PY
# 开发工具  : PyCharm
# 作业内容：
# 1.安装并使用 requests、bs4 库，爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评，并以 UTF-8 字符集保存到 csv 格式的文件中。
# 2.使用 requests 库对 http://httpbin.org/ 分别用 get 和 post 方式访问，并将返回信息转换为 JSON。

import requests
from bs4 import BeautifulSoup as bs
from time import sleep


# 爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评
def get_my_url(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/78.0.3904.108 Safari/537.36 '
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    # 查看响应状态码
    # print(response.status_code)
    # 通过html语法解析器，对获取的内容进行解析
    bs_info = bs(response.text, 'html.parser')
    # print(bs_info)

    # 爬取豆瓣电影 Top250 的电影名称、评分
    # 找到豆瓣电影的电影名称
    n = 0
    for tags in bs_info.find_all('div', attrs={'class': 'info'}):
        n += 1
        print(f'第{n}个电影 ', end='\n')
        # 爬取电影名称
        for hd_tags in tags.find_all('div', attrs={'class': 'hd'}):
            # print(tags)

            for a_tag in hd_tags.find_all('a'):
                # print(tag)
                part_of_name = []

                for res in a_tag.find_all('span'):
                    # pass
                    part_of_name.append(res.get_text())
                    # print(f'电影名称为：{res.get_text()}')
                print('电影名称为 : ' + ''.join(part_of_name))

        # 爬取电影评分、短评数量
        for bd_tag in tags.find_all('div', attrs={'class': 'bd'}):
            # print(bd_tag)

            for star_tag in bd_tag.find_all('div', attrs={'class': 'star'}):
                # print(star_tag)
                # part_of_name = []
                for res1 in star_tag.find_all('span', attrs={'class': 'rating_num'}):
                    # pass
                    # part_of_name.append(res.get_text())
                    # print(f'电影名称为：{res.get_text()}')
                    print(f'电影评分为 : {res1.get_text()}')

                # for res2 in star_tag.find_all('span',attrs={}):
                #                  #    print(f'有{res2.get_text()}')


# 遍历豆瓣top250每一页
urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

# 通过name属性=main方法，主动调用get_my_url()方法，传入url
if __name__ == '__main__':
    # for url in urls:
    #     get_my_url(url)
    #     sleep(10)
    get_my_url(urls[0])
