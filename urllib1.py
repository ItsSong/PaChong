import re
import urllib.request
url=urllib.request.urlopen("https://read.douban.com/provider/all").read()
url = url.decode("utf-8")
data = '<div class="cm-body"><div class="name">(.*?)</div>'
result = re.compile(data).findall(url)
print(result)   # 结果显示在一个列表里

# 将结果写入一个文本文件
a = open("C:/D_pan/python_exer/NiuKe/urllib.txt",'w')
for i in range(0,len(result)):
    a.write(result[i]+'\n')
a.close()