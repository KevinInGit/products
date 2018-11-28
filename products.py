# -*- coding:utf-8 -*-
# 建立二维列表，即列表中一项中套着另一个列表

# 用来存：商品名和价格
products = []
while True:
    name = input('请输入商品名称：')
    if name == 'q':
        break
    price = input('请输入商品价格：')
    # p = []
    # p.append(name)
    # p.append(price)
    # 上文三行等效于下文一行
    p = price[name, price]
    products.append(p)
print(products)