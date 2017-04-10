# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
import re
# url = []
headers ={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#开始爬取的网页地址，通过该地址获取其他url
start_url = 'http://www.runoob.com/docker/docker-tutorial.html'

# print(start_html.text)
# pattern = re.compile('',re.s)
# url.append(start_url)
start_html = requests.get(start_url,headers=headers)
soup = BeautifulSoup(start_html.text,'lxml')
content = soup.find(class_='article-body').get_text()
urls = soup.find(class_='design').find_all('a')
# url.append(url)
# title = start_url[29:-5]
# print(content)
# print(urls)
# print(os.path.abspath('.'))
# print(os.path.join('Users/Yufog Chan/Desktop', 'testdir'))
if os.path.exists(os.path.join("D:", "docker")):
    print("文件夹",os.path.join("D:", "docker"),"已经存在。")
    os.chdir("D:"+"docker")
else:
    print("创建了",os.path.join("D:", "docker"),"的文件夹。")
    os.makedirs(os.path.join("D:", "docker"))
    #切换到上面创建的文件夹
    os.chdir("D:"+"docker")
count = 1
for a in urls:
    print(a.text.strip())
    filename = a.text.strip()
    if a['href'][0:1] == '/':
        # html = requests.get('http://www.runoob.com' + a['href'], headers=headers)
        # print('http://www.runoob.com' + a['href'])
        req = 'http://www.runoob.com' + a['href']
    else:
        # html = requests.get('http://www.runoob.com/' + a['href'], headers=headers)
        # print('http://www.runoob.com/' + a['href'])
        # print('http://www.runoob.com/' + a['href'])
        req = 'http://www.runoob.com/' + a['href']
    html = requests.get(req,headers = headers)
    soup = BeautifulSoup(html.text,'lxml')
    content = soup.find(class_='article-body').get_text()
    print(content)
    with open(str(count)+filename+'.txt','w',encoding='utf-8') as f:
        f.write(content)
    print(req)
    count+=1
print("已完成。")