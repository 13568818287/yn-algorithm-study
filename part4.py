import unittest

from ddt import ddt,data,unpack





def arrage_money(n):
    '''
    要兑换n块钱，n是任意正整数。已知固定货币种类[1,2,5,10,25],有多少种不同兑换方式。
    这个题还没有理解
    排列，当N=3,[1,1,1],[1,2],[2,1] .
    当n=4,[1,1,1,1],[1,1,2],[2,1,1],[1,2,1],[2,2]
    当n=5,[1,1,1,1,1],[1,1,1,2],[1,1,2,1],[1,2,1,1],[2,1,1,1],[2,2,1],[1,2,2],[2,1,2],[5]   
    '''  
    # dp[x] 表示金额之和等于x的组合数，目标是求 dp[n]。
    # 空间复杂度：O(n),时间复杂度：O(n×n)
    all_money = (1,2,5,10,25)      
    dp=[0 for x in range(n+1)]
    dp[0] = 1    
    for itm in all_money:# 遍历数组 各种面值 的值
        for j in range(itm,n+1):    # 遍历不同的金额之和
            dp[j] += dp[j - itm] # 计算 dp[i]的值时，可以确保金额之和等于 itm 的面额的顺序，由于顺序确定，因此不会重复计算不同的排列。
    print('result=',dp[n])
    return dp[n]     
          
# def DP_Com(moneylist,num):
#     an=[1]+[0]*num
#     for i in moneylist :
#         for j in range(i,num+1):
#             an[j]+=an[j-i]

#     return an[num]
    
  

def frogJump(n):
    if n <= 2:
        return n
    return frogJump(n-1) + frogJump(n-2)

def frogJump_1(n, tmplst):
    if n <= 2:
        return n

    if tmplst[n-1] == 0:
        tmplst[n-1] = frogJump_1(n-1,tmplst)      
    
    if tmplst[n-2] == 0:
        tmplst[n-2] = frogJump_1(n-2,tmplst)      

    return tmplst[n-1] + tmplst[n-2]
   

def frogJump_4(n):
    '''可以选择一次跳1-2阶，跳到顶端有多少种方式'''
    if n <= 2:
        return n
    tmp1,tmp2=1,2
    while n > 2:
        tmp = tmp1 + tmp2
        tmp1,tmp2 = tmp2,tmp
        n -= 1
    return tmp

@ddt
class PartFourTest(unittest.TestCase):

    # @data((3,3),(50,3546),(150,39831),(250,177456))
    @data((3,2))
    @unpack
    def test_arrage_moeny(self,n,expect_v):
        # tmplst=[0 for i in range(len(all_money))]
        count=arrage_money(n)
       
        self.assertEqual(count,expect_v)
        
        
    
    @data((4,5),(100,573147844013817084101))
    @unpack
    def test_frogJump(self, n, expect_v):
        tmplst=[0 for i in range(n)]
        a = frogJump_1(n,tmplst)
        self.assertEqual(a,expect_v)


if __name__ == '__main__':
    unittest.main()   
   
