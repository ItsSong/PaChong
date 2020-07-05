import re
import urllib.request
url=urllib.request.urlopen("http://data.stats.gov.cn/easyquery.htm?cn=C01").read()
url = url.decode("utf-8")
data = '"出租汽车（辆）"</td><td align="right" class>(.*?)</td>'
result = re.compile(data).findall(url)
print(result)   # 结果显示在一个列表里

# 将结果写入一个文本文件
a = open("C:/D_pan/python_exer/NiuKe/PaChong.txt",'w')
for i in range(0,len(result)):
    a.write(result[i]+'\n')
a.close()