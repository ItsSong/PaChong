import re
import requests
import time
import os

# 函数1：获取一个页面的html并返回
def get_one_html(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                        ' (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r.text
    except Exception as er:
        print(er)


# 函数2：用正则提取每一页的关键信息并返回
def get_pic_url(html):
    pic_urls = re.findall('"pic_url":"(.*?)"', html,re.S)    # 对应网页源代码，找到图片对应的正则
    img_url = []                                             # 创建空列表，装每一页的所有图片的链接
    for one_pic_url in pic_urls:
        img_url.append('http:' + one_pic_url)
    return img_url                                           # 返回图片的链接的列表


# 函数3: 写入文件（下载）
def write_to_file(page, img_urls):
    i = page                                                 # 利用页码，防止后面的写入会覆盖之前的
    n = 0
    for pic_url in img_urls:
        pic = requests.get(pic_url)
        with open('C:/D_pan/python_exer/2019年11月学习python_爬虫_数据分析/爬虫/TaobaoJieGuo/' + str(i) + str(n) + '.jpg', 'wb') as f:
            f.write(pic.content)
        print('---第{}页第{}张图下载成功---'.format(str(i), str(n)))
        n += 1

# 调用函数1、2、3
def main(keyword, page_num, url):
    html = get_one_html(url)          # 调用函数得到该页的hml
    img_urls = get_pic_url(html)      # 调用函数得到该页的所有图片的链接
    write_to_file(page, img_urls)     # 调用函数，写入即下载图片


if __name__ == '__main__':
    keyword = input('请输入关键词：')
    page_num = eval(input('请输入要爬取的页数：'))
    try:
        os.mkdir('C:/D_pan/python_exer/2019年11月学习python_爬虫_数据分析/爬虫/TaobaoJieGuo/')
        for page in range(0, page_num):
            url = 'http://s.taobao.com/search?q=' + keyword + '&s=' + str(page)
          #   url = "https://s.taobao.com/search?q="+keyword\
          # +"&imgfile=&commend=all&ssid=s5-e&search_type=item" \
          #  "&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1" \
          #  "&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3" \
          #  "&p4ppushleft=1%2C48&s="+str(page*44) # 分析网址得规律
            main(keyword, page_num, url)
            if page % 2 == 0:
                time.sleep(10)  # 每爬取2页停留10秒
    except Exception as err:
        print(err)