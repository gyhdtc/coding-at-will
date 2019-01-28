import urllib.request
page = urllib.request.urlopen('https://www.bing.com/?mkt=zh-CN&mkt=zh-CN').read()
print (page)
fhandle = open("./1.txt","wb")    #将爬取的网页保存在本地
fhandle.write(page)
fhandle.close()