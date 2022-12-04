import unittest
from ddt import ddt,data,unpack

def duplicateCount_1(lst_data):
    '''输出重复值的个数，重复次数独立计算,暴力解法'''    
    dic_1 = {}    
    for i in lst_data:
        if i in dic_1:
            dic_1[i] += 1   #重复次数            
        else:
            dic_1[i]=1
    # 重复个数
    lst_repeat = [x for x in dic_1.values() if x>1]
    return len(lst_repeat)

from collections import Counter

def duplicateCount_2(lst_data:list):
    '''输出重复值的个数,排序解法'''    
    #求数组中每个数字出现了几次
    repeat_tuple = Counter(lst_data) 
     # 重复个数
    lst_repeat = [x for x in repeat_tuple.values() if x>1]  
    return len(lst_repeat) 

def duplicateCount_3(lst_data:list):
    '''输出重复值的个数,利用列表'''    
    #求数组中每个数字出现了几次
    myset = set(lst_data)
    repeat_n = 0 
    for x in myset:
        n = lst_data.count(x)
        print('x=',x,',found x repeat count=', n)
        if n > 1:
            repeat_n += 1   
    # 重复个数
    return repeat_n    
  

def frogJump(n):
    '''可以选择一次跳1-2阶，跳到顶端有多少种方式'''
    if n <= 2:
        return n
    tmp1,tmp2=1,2
    while n > 2:
        tmp = tmp1 + tmp2
        tmp1,tmp2 = tmp2,tmp
        n -= 1
    return tmp
   

def longgetSubstring(str_value):
    '''返回不包含重复字符的最长字符'''
    lst_result = []
    stmp = ''    
    for x in str_value:      
        if x not in stmp:
            stmp += x          
        else:
            # 有重复字符
            if stmp not in lst_result:
                lst_result.append(stmp)                
            n = stmp.find(x)             
            t = stmp[n+1:] + x
            stmp = t            
       
        if str_value[-1] == x and len(stmp) > 1:
            lst_result.append(stmp)

    lst_result.sort(key=lambda x:len(x), reverse=True)
    return lst_result[0]

@ddt
class PartThreeTestCase(unittest.TestCase):

    def test_longgetSubstring_01(self):
        '''验证有多个相同的最长字符'''
        s_value = longgetSubstring('cdcdafcdaa')       
        lst_v=['cdaf','dafc','fcda']
        self.assertIn(s_value, lst_v)


    # 单个重复字符；最长字符在前面；在中间；在后面
    @data(('bbbb','b'),('dvdf','vdf'),('aaabacddd','bacd'),('abababcd','abcd'),('abab','ab'),('abefgefgbefg','abefg'))  
    @unpack
    def test_longgetSubstring(self, sdata, exect_value):
        '''参数化，获取最长字符'''
        s_value = longgetSubstring(sdata)
        self.assertEqual(s_value, exect_value)

    @data(([1,1,1,3],1),([1,2,3,4],0),([1,1,2,2],2),([1,2,3,1],1))
    @unpack
    def test_duplicateCount_01(self,lst_data,exect_count):
        '''重复值计数'''
        count = duplicateCount_1(lst_data)
        self.assertEqual(exect_count, count)

    @data(([1,1,1,3],1),([1,2,3,4],0),([1,1,2,2],2),([1,2,3,1],1))
    @unpack
    def test_duplicateCount_02(self,lst_data,exect_count):
        '''重复值计数2'''
        count = duplicateCount_3(lst_data)
        self.assertEqual(exect_count, count)

    @data((4,5),(3,3),(2,2),(1,1))
    @unpack
    def test_frogJump(self, step_count, exect_value):
        '''青蛙跳台阶'''
        n = frogJump(step_count)
        self.assertEqual(exect_value, n)

# ababc,bbbb,abcab,ffaa
if __name__ == '__main__':
    unittest.main()   

