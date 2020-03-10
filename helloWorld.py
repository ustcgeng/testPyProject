import json

i=10
print(i)
print("您好，世界！")

str=b'{"event_rep":"","channel":"market_vdsusdt_ticker","data":null,"tick":{"amount":"2767846.184860351209","close":"0.8905","high":"1.2222","low":"0.8","open":"1.1089","rose":"-0.1969519343","vol":"2745985.74256389"},"ts":1582707974000,"status":"ok"}'

#print(str);
mesJSON = json.loads(str)
#print("222")
#print(mesJSON)

if('channel' in mesJSON):
    #print(mesJSON['channel'])
    pass
else:
    #print("00000000")
    pass
#print(mesJSON['event_rep'])

x=[3,5,7]
print(x[-1::-1])

s="language"
print(s[-8:-1].lower())

#键盘输入10个数字组成数列，并显示，在除掉负数再次显示
i=0
a=[1,-1,4,-6,7,-6]
a=a+[5]
print(a)