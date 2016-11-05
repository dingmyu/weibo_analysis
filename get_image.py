#coding=utf-8
 
import urllib
import re
 
def downloadPage(url):
    h = urllib.urlopen(url)
    return h.read()
 
def downloadImg(content):
    pattern = r'src="(.+?\.jpg)" pic_ext'
    m = re.compile(pattern)
    urls = re.findall(m, content)
 
    for i, url in enumerate(urls):
        urllib.urlretrieve(url, "%s.jpg" % (i, ))
 
content = downloadPage("http://tieba.baidu.com/p/2460150866")
downloadImg(content)