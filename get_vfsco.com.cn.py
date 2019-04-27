# -*- coding: utf-8 -*-
import os
import requests
from lxml import html

headers = {
    'Host': 'www.vfsco.net.cn',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}

def save(text, filename='temp', path='download'):
    fpath = os.path.join(path, filename)
    with open(fpath, 'w') as f:
        print('output:', fpath)
        f.write(text)

def save_image(image_url):
    resp = requests.get(image_url)
    page = resp.content
    filename = image_url.split('vfsco.com.cn/')[-1]
    save(page, filename)

def crawl(url):
    resp = requests.get(url, headers=headers)
    page = resp.content
    root = html.fromstring(page)
    image_urls = root.xpath('//img[@data-original]/@data-original')
    for image_url in image_urls:
        save_image(image_url)

if __name__ == '__main__':
    # ensure there's one subfolder called 'download' in same path, to store the image downloaded
    url = 'http://www.vfsco.com.cn'
    crawl(url)