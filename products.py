# -*- coding:utf-8 -*-
# 建立二维列表，即列表中一项中套着另一个列表

import os

# 读取文档
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,价格' in line:
                continue  # 继续
            name, price = line.strip().split(',')  # 用逗号作为分隔符
            products.append([name, price])
    return products

# 使用者输入：用来存 商品名和价格
def user_input(products):
    while True:
        name = input('请输入商品名称：')
        if name == 'q':
            break
        price = input('请输入商品价格：')
        price = int(price)  #注意 int类型的元素不能与字符串 用＋ 相连，因此下文需要对元素拼接部分进行修改
        p = [name, price]
        products.append(p)
    print(products)
    return products

# 印出所有商品购买记录
def print_products(products):
    for p in products:
        print(p[0])

# 写入档案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:  #  这里的with是python自带的功能，在with框架中，自动关闭close 文件；如果没有创建待写入的txt文档，会自动创建
        f.write('商品,价格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = '/Users/kevin/Desktop/products/products.csv'
    if os.path.isfile(filename): # 检查文档是否存在
        print('存在')
        products = read_file(filename)
    else:
        print('不存在')

    products = user_input(products)
    print_products(products)
    write_file('/Users/kevin/Desktop/products/products.csv', products)

main()