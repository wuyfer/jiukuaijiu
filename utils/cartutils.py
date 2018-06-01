#coding=utf-8
from  cart.models import *
class CartManager(object):
    def add_cart_item(self,goodsid,colorid,sizeid,count,*args,**kwargs):
        pass
    def delete_cart_item(self,goodsid,colorid,sizeid,count,*args,**kwargs):
        pass
    def get_all_cart_items(self,*args,**kwargs):
        pass
# 第一个问题session（request）
# session认为字典的字典发生改变，
class SessionCartManager(CartManager):

    # 小心session为空
    def __init__(self,session):
        self.session = session
    # 浏览器发送的数据都是字符串
    def add_cart_item(self, goodsid, colorid, sizeid, count,*args,**kwargs):
        #[{"key":CatItem}]  /[{'key':key,'value':CartItem}]
        count=int(count)
        cart = self.session.get('cart',[])
        key = self.__gen_key(goodsid,colorid,sizeid)
        if self.is_exist(cart,key):
                cartitem = self.get_cart_item(cart,key)
                if cartitem.count+count<1:
                    raise Exception('数量不能小于1')
                cartitem.count+=count
        else:
            cart.append({key:CartItem(goodsid=goodsid,colorid=colorid,sizeid=sizeid,count=count)})
        self.session['cart']=cart


    def delete_cart_item(self, goodsid, colorid, sizeid, count,*args,**kwargs):
        pass

    def get_all_cart_items(self,*args,**kwargs):
        #[{'10101',CatriItems},{}]
        cart= self.session.get('cart')
        if cart == None:
            return []
        else:
            cartiems = []
            for cartitem in cart:
                cartiems.extend(cartitem.values())
            return cartiems

    def __gen_key(self,goodsid,colorid,sizeid):
        return str(goodsid)+":"+str(colorid)+":"+str(sizeid)
    def is_exist(self,cart,key):
        isExist = False
        for cartitem in cart:
            if list(cartitem.keys())[0] == key:
                isExist = True
                break
        return isExist
    def get_cart_item(self,cart,key):
        for cartitem in cart:
            if list(cartitem.keys())[0] == key:
                return cartitem[key]
        return None