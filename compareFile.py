#coding:utf-8
import linecache
import sys
aPath =r''+str(sys.argv[1])
bPath =r''+str(sys.argv[2])
a=open(aPath,'r')
b=open(bPath,'r')
countA = len(a.readlines())
countB = len(b.readlines())
flag = True
flaseCount = 0
# print countA
# print countB
if countA!=countB:
    print "false:count"
    flag = False
else:
    for i in range(countA):
        if linecache.getline(aPath,i+1).replace(' ','') == linecache.getline(bPath,i+1).replace(' ',''):
            continue
        else:
            print "false:line:"+str(i+1)
            flag = False
            flaseCount=flaseCount+1
if flag: print "ok"
else: print "falseCount:"+str(flaseCount)
a.close()
b.close()

