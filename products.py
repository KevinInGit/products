# -*- coding:utf-8 -*-
# 建立二维列表，即列表中一项中套着另一个列表

# 读取档案
products = []
with open('/Users/kevin/Desktop/products/products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,价格' in line:
            continue  # 继续
        #开始split切割
        name, price = line.strip().split(',')  # 用逗号作为分隔符
        products.append([name, price])
print(products)

# 使用者输入：用来存 商品名和价格
while True:
    name = input('请输入商品名称：')
    if name == 'q':
        break
    price = input('请输入商品价格：')
    price = int(price)  #注意 int类型的元素不能与字符串 用＋ 相连，因此下文需要对元素拼接部分进行修改
    # p = []
    # p.append(name)
    # p.append(price)
    # 上文三行等效于下文一行
    p = [name, price]
    products.append(p)
print(products)

# 印出所有商品购买记录
for p in products:
    print(p[0])

# 写入档案
# 注意对文档的 写入 与 读取 都要涉及编码问题
# 这里的with是python自带的功能，在with框架中，自动关闭close 文件
with open('/Users/kevin/Desktop/products/products.csv', 'w', encoding='utf-8') as f:  # 如果没有创建待写入的txt文档，会自动创建
    # csv用来存储专门的文件资料
    # encoding='utf-8'用来使得编码正确
    f.write('商品,价格\n')
    for p in products:
        #f.write(p[0] + ',' + p[1] + '\n')
        f.write(p[0] + ',' + str(p[1]) + '\n')
    # 该程序每执行一次会覆盖之前的products文件