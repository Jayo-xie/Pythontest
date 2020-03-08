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
import re


# 爬取豆瓣电影 Top250 的电影名称、评分、短评数量和前 5 条热门短评
def get_mv_info(url):
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

    # 通过给n赋值，提示现在是第几页
    n = 0
    for tags in bs_info.find_all('div', attrs={'class': 'info'}):
        n += 1
        print(f'第{n}个电影 ', end='\n')
        # 爬取电影名称
        for hd_tags in tags.find_all('div', attrs={'class': 'hd'}):
            # print(tags)
            
            # 定义子页面的链接，获取热门短评
            link_page_url = ''
            for a_tag in hd_tags.find_all('a'):
                # print(tag)
                link_page_url = a_tag.get('href')

                part_of_name = []

                for res in a_tag.find_all('span'):
                    # pass
                    part_of_name.append(res.get_text())
                    # print(f'电影名称为：{res.get_text()}')
                print('电影名称为 : ' + ''.join(part_of_name))
            hot_comments = get_hot_comment(link_page_url)

            i = 0
            for comment in hot_comments:
                i = i+1
                print(f'第{i}条热门短评：{comment}')

        # 爬取电影评分、短评数量
        for bd_tag in tags.find_all('div', attrs={'class': 'bd'}):
            # print(bd_tag)

            for star_tag in bd_tag.find_all('div', attrs={'class': 'star'}):
                # print(star_tag)

                # 通过正则比较获取span中的评价条数
                p = re.compile(r'<span>(.*?)人评价</span>', re.S)
                results = re.findall(p, str(star_tag))
                print(f'一共有{results[0]}条评价')

                for res1 in star_tag.find_all('span', attrs={'class': 'rating_num'}):
                    print(f'电影评分为 : {res1.get_text()}')



def get_hot_comment(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 '
    header = {'user-agent': user_agent}
    response2 = requests.get(url, headers=header)
    # bs_info2 = bs(response2.text, 'html.parser')
    p2 = re.compile('<span class="short">(.*?)</span>', re.S)
    results2 = re.findall(p2, response2.text)
    print('查看前五条热门短评：')
    # i = 0
    # for result in results2[:5]:
    #     i = i+1
    #     print(f'第{i}条热门短评：{result}')

    return results2[:5]

    
                
                    


# 遍历豆瓣top250每一页
urls = tuple(f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

# 通过name属性=main方法，主动调用get_my_url()方法，传入url
if __name__ == '__main__':
    # for url in urls:
    #     get_mv_info(url)
    #     sleep(10)
    get_mv_info(urls[0])
