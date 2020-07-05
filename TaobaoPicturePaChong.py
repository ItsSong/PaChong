import urllib.request
import re
import urllib.parse

# 第一步：浏览器伪装
headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                        ' (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36') # 获取报头信息
opener = urllib.request.build_opener()  # 创建一个opener对象（添加报头信息使用）
opener.addheaders = [headers]    # 添加报头信息
urllib.request.install_opener(opener) # 添加为全局

# # 登录自己的淘宝
# address = "https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F" # 淘宝网登录页面网址
# myInfo = urllib.parse.urlencode({       # 在登录页面找用户名和密码的位置，填写自己的账号
#     "TPL_username":"songzhuo8883",
#     "TPL_password":"songzhuo0813-+"
# })
# request1 = urllib.request.Request(address,myInfo)   # 强myInfo发送到address


# 第二步：给要爬取的图片名编码
keyname = "连衣裙"
key = urllib.request.quote(keyname)

# 第三步：爬取淘宝网连衣裙前10页的高清图片（注意：不要缩略图）
for i in range(10):
    url = "https://s.taobao.com/search?q="+key\
          +"&imgfile=&commend=all&ssid=s5-e&search_type=item" \
           "&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1" \
           "&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3" \
           "&p4ppushleft=1%2C48&s="+str(i*44) # 分析网址得规律
    data = urllib.request.urlopen(url).read().decode("utf-8","ignore")             # 获取对应网址
    # print(len(data))

    pat = '"pic_url":"//(.*?)"'                  # 分析每一张图片地址在网页源代码中的位置，编写正则式
    imgurl = re.compile(pat).findall(data)       # 图片网址的结果赋给imgurl
    print(len(imgurl))
    #
    # for j in range(0,len(imgurl)):               # 循环爬取每一页中图片，并存储在本地
    #     thisimg = imgurl[j]
    #     thisimg1 = "http://"+thisimg
    #     file = "C:/D_pan/python_exer/2019年11月学习python_爬虫_数据分析/爬虫/TaobaoJieGuo/"+str(i)+str(j)+".jpg" # 存储位置设置
    #     urllib.request.urlretrieve(thisimg1,filename=file)  # 获取图片并下载到本地




