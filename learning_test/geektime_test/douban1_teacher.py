import requests
from bs4 import BeautifulSoup as bs


# Python 使用def定义函数，myurl是函数的参数
def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {}
    ##这里如果不去定义header为字典直接使用是否会报错？
    header['user-agent'] = user_agent

    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')

    # Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
    ## 混合使用模块和for的功能，因为tags atag对象既能支持find_all又拥有迭代功能
    for tags in bs_info.find_all('div', attrs={'class': 'pl2'}):
        for atag in tags.find_all('a', ):
            # 获取所有链接
            print(atag.get('href'))
            # 获取图书名字
            print(atag.get('title'))


urls = tuple(f'https://book.douban.com/top250?start={page * 25}' for page in range(10))
## 推导式功能,相当于
## for page in range(10)：
##     astring = 'https://book.douban.com/top250?start={ page * 25}'
##     urls = tuple(astring)


from time import sleep

## autopep8 或者其他IDE 会自动调整import from 到文件最开头，
## 但是有的时候我们希望在某些对象实例化以后再去进行导入，
## 所以自动移动代码位置不一定每次都是正确的


## 单独执行python文件的一般入口
if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(5)
