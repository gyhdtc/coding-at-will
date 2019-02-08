from bs4 import BeautifulSoup
import urllib.request
import sys
import os
# log日志记录
def log(flag, Image_path, Image_Url):
    print ("文件网址 ：", Image_Url)
    print ("文件路径 ：", Image_path)
    if flag == 2:
        print ("Successful")
    else:
        print ("Unsuccessful")
        
flag = int(0)
# 文件所在目录
path = os.path.split( os.path.realpath( sys.argv[0] ) )[0]

# 获取图片url
try:
    Page = urllib.request.urlopen('https://www.bing.com/?mkt=zh-CN&mkt=zh-CN').read()
    Soup = BeautifulSoup(Page,"lxml")
    flag = 1
except:
    print ("Url Error")
Temp = Soup.link.attrs['href']
Image_Url = "https://cn.bing.com" + Temp
# 保存图片
name = Temp.split('/')[4]   # 名字就用 /az/hprichbg/rb/###.jpg 中的 ###.jpg 来命名吧
# urllib.request.urlretrieve(Image_Url, name)
response = urllib.request.urlopen(Image_Url)
htmldata = response.read()
Image_path = path + '\\' + name
try:
    fileOb = open(Image_path, 'wb')     #打开一个文件，没有就新建一个
    fileOb.write(htmldata)
    fileOb.close()
    flag = 2
except:
    print ("Save Error")

log(flag, Image_path, Image_Url)