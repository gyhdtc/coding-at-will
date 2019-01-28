from bs4 import BeautifulSoup
import urllib.request
import sys

# 获取图片url
try:
    Page = urllib.request.urlopen('https://www.bing.com/?mkt=zh-CN&mkt=zh-CN').read()
    Soup = BeautifulSoup(Page,"lxml")
except:
    print ("Error")
    sys.exit()
Temp = Soup.link.attrs['href']
Image_Url = "https://cn.bing.com" + Temp
print (Image_Url)

# 保存图片
## 名字就用 /az/hprichbg/rb/###.jpg 中的 ###.jpg 来命名吧
name = Temp.split('/')[4]
print (name)
urllib.request.urlretrieve(Image_Url, name)

# log日志记录