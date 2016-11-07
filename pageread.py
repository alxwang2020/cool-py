from urllib import urlopen
html = urlopen("http://www.mm131.com/qingchun").read()

import re
r= r'src="(.*?\.jpg)"'
s = re.compile(r)
fhtml = re.findall(s,html)

from urllib import urlretrieve
i = 0
for x in fhtml:
    urlretrieve(x,'%s.jpg'%i )
    i= i + 1
    print i,'.jpg'

