# -*- encoding: utf-8 -*-
'''
@File    :   money_4.py
@Time    :   2022/11/07 20:24:58
@Author  :   xiangyujie
@Version :   1.0
@Desc    :   面值组合，采用动态规划的算法
'''

import os

all_money = [1, 5, 10, 20, 50, 100]
def calc(target : int):
    '''计算小于该面值，最大的个数，如5，只能是1元与2元，5元'''
    zuhuo = [x for x in all_money if x <= target]
    num_max_list=list()
   
    for i in zuhuo:
        #取整操作有：//, round（四舍五入）, int（去掉浮点数）, ceil（向上）, floor(与//一样，向下)
        n= target // i
        # print(i, '===',n)
        num_max_list.append((i,n))
       
    return num_max_list

def combin(target:int):
    '''求取有几种组合情况，采用动态规划算法'''
    m = [1, 2, 5, 10, 20, 50, 100]
    dp = [1] * (target + 1) # 初始化dp
    for i in range(1, 6):
        for j in range(1,target+1):
            if j >= m[i]:
                dp[j] += dp[j - m[i]]
                print(j,',dp=',dp[j])
    return dp[-1]

def combin_v2(target:int):
    '''求取有几种组合情况，采用动态规划算法'''
    m = [1, 2, 5, 10, 20, 50, 100]
    dp = [1] * (target + 1) # 初始化dp
    result=[]
    tmp=0
    for i in range(1, 6):
        for j in range(1,target+1):
            
                

# print('v=',combin(5))
combin_v2(5)



