import json

from restaurant import Restaurant

#i=10
# print(i)
# print("您好，世界！")

#str=b'{"event_rep":"","channel":"market_vdsusdt_ticker","data":null,"tick":{"amount":"2767846.184860351209","close":"0.8905","high":"1.2222","low":"0.8","open":"1.1089","rose":"-0.1969519343","vol":"2745985.74256389"},"ts":1582707974000,"status":"ok"}'

#print(str);
#mesJSON = json.loads(str)
#print("222")
#print(mesJSON)

# if('channel' in mesJSON):
#     #print(mesJSON['channel'])
#     pass
# else:
#     #print("00000000")
#     pass
#print(mesJSON['event_rep'])


# restaurant_XCY = Restaurant("XIAO CAI YUAN","Chinese")
# print(restaurant_XCY.cuisine_type)
# print(restaurant_XCY.restaurant_name)
# restaurant_XCY.open_restaurant()
# restaurant_XCY.describe_restaurant()

class ChineseRestaurant(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.mycook =1
    def describe_restaurant(self):
        print("the restaurant name is:" + self.restaurant_name + ";the restaurant_type is:"\
              + self.cuisine_type + ";the cook=" + str(self.mycook))

cr = ChineseRestaurant("HAI DI LAO","Chinese")
cr.mycook = 3
print(cr.cuisine_type)
print(cr.restaurant_name)
cr.open_restaurant()
cr.describe_restaurant()