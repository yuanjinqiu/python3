import urllib3
from datetime import *
import time
def Process(url,n):
  minSpan = 10.0
  maxSpan = 0.0
  sumSpan= 0.0
  over1s = 0
  for i in range(n):
    startTime = datetime.now()
    try:
      res = urllib3.urlopen(url,timeout=10)
    except:
      pass
    endTime = datetime.now()
    span = (endTime-startTime).total_seconds()
    sumSpan = sumSpan + span
    if span < minSpan:
      minSpan = span
    if span > maxSpan:
      maxSpan = span
    #超过一秒的
    if span>1:
      over1s=over1s + 1
    print(u'%s Spent :%s seconds'%(url,int(span)))
  print(u'requested:%s times,Total Spent:%s seconds,avg:%s seconds, max:%s seconds,min:%s seconds,over 1 secnod:%s times'%(n,sumSpan,sumSpan/n,maxSpan,minSpan,over1s))
  print('\n')
if __name__=='__main__':
  Process('http:// http://www.baiyihulian.com:31329',30)