# -*- encoding: utf-8 -*-
'''
@File    :   one.py
@Time    :   2022/11/17 18:54:51
@Author  :   xiangyujie
@Version :   1.0
@Desc    :   None
'''


def foo(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n//k
        k += 1
        if k % k == n:
            yield k


def fibonacci(n):
    '''斐波拉契数列'''
    a = 0
    b = 1
    while b <= n:
        yield b
        f = b + a
        a = b
        b = f


def fibonacci2(int_n : int):
    '''斐波拉契数列，利用同时分配，简化写法'''
    n_a, n_b = 0, 1
    while n_b <= int_n:
        yield n_b
        n_a, n_b = n_b, n_b + n_a

def one_chapter_11():
    '''1.11 生成列表[0,2,4,8,16,32,64,128,256]''' 
    start=1    
    result = []
    result.append(0)
    for i in range(0,8):
        result.append(start * 2)
        start = start * 2
    print(result)
def one_chapter_11_v2():
    '''生成列表[0,2,4,8,16,32,64,128,256]''' 
    result = [pow(2,x) for x in range(0,9)]
    return result

def one_chapter_14():  
    '''判断一段序列中是否存在一对乘积是奇数的互相不同的数'''
    '''如果存在有2个基数，结果必然会存在乘积为基数的数'''  
    input_nums= list(map(int,input('input mulit nums:').split()))
    lst_result=[]
    for i in input_nums:
        if i % 2 == 0:
            continue
        if len(lst_result) == 0:
            lst_result.append(i)
        elif  lst_result[-1] != i:
            lst_result.append(i)

    return len(lst_result) >= 2 
         
def one_chapter_18(): 
    '''列表解析语法来产生列表[0,2,6, 12,20,30,42,56,72,90]'''
    result = [ n*(n+1) for n in range(0,10)]
    return result

def one_chapter_22(a, b):  
    '''两个整型数组a和b并返回数组a和b的点积''' 
    n = len(a)
    c = []
    if n != len(b):
        raise ValueError('2个数组的长度必须一致')
    for i in range(0,n):
       c.append(a[i] * b[i])
    return c
'''
1.28 在n维空间定义一个向量v=(v1,v2,……vn)的p范数
有几个数学概念：
范数：
欧几里得算法：https://blog.csdn.net/ltrbless/article/details/86770606，https://www.sohu.com/a/314655845_250298
幂：https://baike.baidu.com/item/%E5%B9%82%E8%BF%90%E7%AE%97/2727621?fr=aladdin
'''
def norm(tuple_v, int_p:int=2):
    '''
    :param tuple_v:向量
    :param int_p:范数
    :return 返回向量v的p范数值
    '''
    sum = 0
    for n in tuple_v:
        sum += pow(n, int_p)
    result =pow(sum,1/int_p)
    return result

def calc_div2_count(n):
    '''1.30 商小于2为止的次数'''
    count = 1
    while True:
        n = n//2       
        if n < 2:
            break              
        else:
            count +=1           
    print(f"##END# count={count}")
    return count

def get_samllchange(pay_money, give_money):
    '''1.31 找零'''
    if pay_money == give_money:
        return 0
    elif pay_money > give_money:
        raise ValueError('支付金额不足')
    elif pay_money is float or give_money is float:
        raise ValueError('暂不支持小面金额（角），只支持整数')
    change_money = give_money - pay_money
    # 只设计纸币
    all_money = [1, 5, 10, 20, 50, 100]
    # 余额
    balance=change_money
    result={x:0 for x in all_money}
    idx = -1
    ncount = len(all_money)
    # 返回尽可能少的纸币
    while True:
        if abs(idx) > ncount: 
            break
        if all_money[idx] > balance:
            idx = idx - 1
        elif balance - all_money[idx] >= 0:
            # 余额 - 面值大于等于0，表明足够
            balance = balance - all_money[idx]
            result[all_money[idx]] += 1       
        elif balance == 0:
            break
     # 只返回有面值的纸币   
    objdic = dict((key,value) for key,value in result.items() if value > 0)
    print('#1.31 result=',objdic)
    return objdic
   


if __name__ == '__main__':  
    # 生成器练习 
    # obj = foo(10)
    # print('type=', type(obj)) # type= <class 'generator'> 
    # obj = fibonacci2(20)
    # for i in obj:
    #     print('f=', i)
    # # 1.28 向量
    # print('result=',norm((4,3),2))
    # calc_div2_count(250)
    # 1.31 找零
    # get_samllchange(5,20)
    # one_chapter_18()
    # print('Has?',one_chapter_14())
    one_chapter_22([1,3,4,5,2], [2,3,3,1,5])
