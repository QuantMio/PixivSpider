
import sys
import urllib
import urllib2
import cookielib
import re
import time
import httplib
import getpass
import random
from urllib2 import Request, urlopen, URLError, HTTPError

print 'Please enter your Pixiv ID',
username=raw_input()
password = getpass.getpass('Please enter your password ')

url="https://www.secure.pixiv.net/login.php"
#Process the cookie
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#POST data to Pixiv
values={'mode':'login','pixiv_id':username,'pass':password,'skip':'1'}
data=urllib.urlencode(values)
req=urllib2.Request(url,data)
#ERRORS
try:    
    
    response = opener.open(req,timeout=10)    
    
except URLError, e:    
  
    if hasattr(e, 'code'):    
    
        print 'The server couldn\'t fulfill the request.'    
    
        print 'Error code: ', e.code    
  
    elif hasattr(e, 'reason'):    
    
        print 'We failed to reach a server.'    
    
        print 'Reason: ', e.reason    

else:    
    print 'No exception was raised.' 

res=opener.open('http://www.pixiv.net/ranking.php?mode=daily&content=illust')	
html = res.read()
pattern = r'(?<=\bdata-id=")\d+(?=")'
m=re.search(pattern,html)
pattern=re.compile(r'(?<=\bdata-id=")\d+(?=")')
start=0
i=0
m=pattern.search(html,start)
target=open("save.txt",'w')
target.truncate()

while(m!=None):
     start=m.end()
     line = m.group()
     target.write(line)
     target.write("\n")
     m=pattern.search(html,start)
target.close()

target = open("save.txt",'r') 
lines = len(target.readlines())

i=1  
for line in open("save.txt"):
   id = line.strip('\n')
   patternself='http://i\d*\.pixiv\.net/img-original/img/\d*/\d*/\d*/\d*/\d*/\d*/%s\_p\d*\.(jpg|png)' %(id)
   str(patternself) 
   p=re.compile(patternself)
   illustURL='http://www.pixiv.net/member_illust.php?mode=medium&illust_id=%s'% (id)
   str(illustURL)
   resself=opener.open(illustURL)
   poi=resself.read()
   mself=re.search(p,poi)
   exname1=re.compile('\.jpg')
   exname2=re.compile('\.png')
   if(mself!=None):
       d=mself.group()
       h=re.compile('i\d*\.pixiv\.net(?=/img-original/img/\d*/\d*/\d*/\d*/\d*/\d*/%s\_p\d*\.(jpg|png))'%(id))
       host=re.search(h,d).group()
       r=re.compile('/img-original/img/\d*/\d*/\d*/\d*/\d*/\d*/%s\_p\d*\.(jpg|png)' %(id))
       reqline=re.search(h,d).group()
       httplib.HTTPConnection.debuglevel = 1
       
       print 'Downloading Illust Pixiv ID %s'% (id)
       header={'Host':host,
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
       'Accept':'image/png,image/*;q=0.8,*/*;q=0.5',
       'Accept-Language':'en-US,en;q=0.5',
       'Accept-Encoding':'gzip, deflate',
       'Referer':'http://www.pixiv.net/'}
       request = urllib2.Request(d,headers=header)
       response = urllib2.urlopen(url = request).read()
       if(re.search(exname1,d)!=None):
           filename="%s.jpg" %(id)
           f = file(filename,"wb") 
           f.write(response)  
           f.close() 
           print 'Success.'
       else:
           filename="%s.png"%(id)
           f = file(filename,"wb") 
           f.write(response)  
           f.close() 
           print 'Success.'
   else:
       print "ERROR"
   
   
   delay=random.randint(2, 6)
   time.sleep(delay)
     
