'''
This is a program to determine whether a sequence is a Graph sequence or not.
If it is a graph sequence, draw it.
Copyright by KinoLogic(Xu Yuetonghui)
Date: 12th. Mar, 2020
UESTC
Version 2.0 ：修复了绘图的bug
'''

import numpy as np
num = [int(n) for n in input("Please input your sequence(splitted with space)").split()]
print("Your input is",num)
#输出乱序输入后的正序输入
num.sort(reverse=True)
print("The sequence order is as follow:",num)
#将输入转化为np数组
d = np.array(num)
n = d.size     #获取数组大小，n为数组大小
n_fixed = n    #锁定初始的矩阵长度
print("There are",n,"elements in your sequence.")
#生成一个nxn的邻接矩阵，用来存放结果
matrix_d = np.zeros((n,n))
matrix_result = np.array([d])   #初始化存储结果矩阵
print("matrix result",matrix_result)
j = 0

#每一次循环是执行了一步
while ((d < 0).any()==False)&((d == 0).all()==False):

    j = j+1
    print("This is after the",j,"turn")
    d = np.sort(-d)
    d = (-d)

    if (d[0]+1) >= n:
        for i in range(0,n):
            d[i]=d[i]-1;
            #print(d);
    else:
        for i in range(0,d[0]+1):
            d[i]=d[i]-1;
            #print(d);

    d = np.delete(d,0)

    n = n-1

    print(d)
    d_inst = np.pad(d,(j,0),'constant',constant_values=(0,0))
    matrix_result = np.insert(matrix_result,j,values=d_inst,axis=0)
    #print(matrix_result)
    #print(d_inst)
    print("There are",d.size,"elements left")

#循环结束，判断是否是全0还是有负数
if ((d<0).any()==True):
    print("It's not a Graph sequence");
elif ((d==0).all()==True):
    print("It's a Graph sequence,the total turn is",j);

    print(matrix_result)

    #当可以是图序列的时候，将暂存在matrix结果中的数值写进邻接矩阵
    for i in range(j-1,-1,-1): #行遍历
        for k in range(i+1,n_fixed,1): #列遍历
            matrix_d[i:i+1,k:k+1] = matrix_result[i:i+1,k:k+1] - matrix_result[i+1:i+2,k:k+1]
            matrix_d[k:k+1,i:i+1] = matrix_result[i:i+1,k:k+1] - matrix_result[i+1:i+2,k:k+1]

    print(matrix_d)

    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    Matrix =matrix_d

    #print(Matrix)

    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if Matrix[i, j]!= 0:
              G.add_edge(i, j)

    nx.draw(G,with_labels=True,font_weight='bold')
    plt.show()
