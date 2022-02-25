#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup


def get_name_list():
    # 如果不加headers，会回复状态码418。用了requests库，没有添加请求头等信息，被反爬程序识别了，再次请求添加了header的User-Agent信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    film_name_list = []
    # comments_list = []
    for page in range(0, 10):
        r = requests.get(url='https://movie.douban.com/top250?start=' + str(page * 25) + '&filter=', headers=headers)
        if r.status_code == 200:
            html = r.content  # 字节的方式显示获取到的内容
        else:
            raise RuntimeError('status code is %s' % r.status_code)
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.find_all('span'):
            try:
                if link.get('class')[0] == 'title':
                    if '/' in link.string:
                        continue
                    film_name_list.append(link.string)
            except:
                pass
    return film_name_list


film_name_list = get_name_list()
rank_list = [str(rank) for rank in range(1, 251)]
json_dict = list(zip(rank_list, film_name_list))
print(json_dict)
