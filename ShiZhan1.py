import urllib.error
import urllib.request
import re

# 第一步：先通过正则表达式获取首页新闻的链接
data = urllib.request.urlopen("https://news.sina.com.cn/").read()  # 获取网址
data = data.decode("utf-8","ignore")
pat = 'href="(https://news.sina.com.cn/.*?)">'  # 新闻所在网页的位置
allurl = re.compile(pat).findall(data)

# 第二步：循环获取所有的新闻，并存在本地
for i in range(0,len(allurl)):
    try:
        print("第"+str(i)+"次爬取")
        thisurl = allurl[i]
        file="C:/D_pan/python_exer/2019年11月学习python_爬虫_数据分析/爬虫/ShiZhanJieGuo/"+str(i)+".html"  #存储位置
        urllib.request.urlretrieve(thisurl,file)   # 爬取网页，存储在本地
        print("-------爬取成功------")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)




