'''
Created on 2017年9月3日

@author: liutao
'''
# /bin/bash

from Excel import excel
import requests
from bs4 import BeautifulSoup

file = "刘涛5.xlsx"
ex = excel(file)
ids = ex.readExcel()

#开始爬取网站用户图片总量
nums_data = []  #存储对应的照片数量
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    ,'accept-language': 'zh-CN,zh;q=0.8'
    ,'accept-encoding': 'gzip, deflate, br'
    }

for i in range(0, len(ids)):
    url = r'https://www.flickr.com/photos/'+ids[i]
    print(str(i)+':'+url)
    try:
        r = requests.get(url, timeout=15, headers=headers)
    except requests.RequestException as e:
        print(e)
        #如果发生异常，设置照片数为0 
        nums_data.append([ids[i],0])
    except requests.ReadTimeout as t:
        print(t+'连接超时。。')
        nums_data.append([ids[i],0])
    else:    
        html = r.text
        #提取返回数据中的照片数
        soup = BeautifulSoup(html,"html.parser")
        tags = soup.find('p',attrs={'class':'metadata-item photo-count'})
        num = tags.string
        nums_data.append([ids[i],num])
        

ex.writeExcel(nums_data)
    
    