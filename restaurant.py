class Restaurant:
    '''模拟餐馆的练习题'''
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("the restaurant name is:"+self.restaurant_name+";the restaurant_type is:"+self.cuisine_type)

    def open_restaurant(self):
        print("Now our restaurant is open!")
