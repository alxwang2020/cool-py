import re
import urllib

def getHTML(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html
def geturl(html):
    r= r'src="(.*?\.jpg)"'
    s = re.compile(r)
    fhtml = re.findall(s,html)
    i = 0
    for x in fhtml:
    	urllib.urlretrieve(x,'%s.jpg'%i)
    	i= i+1
        print i,'.jpg'
html = getHTML('http://www.mm131.com/xinggan')
geturl(html)
