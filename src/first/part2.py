import math
from datetime import datetime

def premeCountLessThan(n):
    '''求质数的个数'''
    if n < 2:
        return 0
    preme_count=1
    lst=[2]   # 最小质数为2
    for x in range(3,n+1,2):
        preme=True
        # 判断它是否能被小于它开根后的所有数整除
        for y in range(3,int(math.sqrt(x))+1):
            if x % y == 0:
                preme = False
        if preme:
            preme_count +=1
            lst.append(x)
    return preme_count

class CreditCard:
    '''A consumer credit card.
    根据消费额度限制支付，但不收取利息或滞纳金
    '''
    def __init__(self,customer,bank,acnt,limit):
        '''客户、银行、账户、信用额度和余额信息'''
        self._customer=customer
        self._bank=bank
        self._account=acnt
        self._limit=limit # 信用额度
        self._balance=0
    
    def get_curstomer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit

    def get_blance(self):
        return self._balance
    
    def set_blance(self,value):
        self._balance = value
    

    def charge(self,price):
        '''Charge given price to the card.assuming sufficient credit _limit.'''
        if price+ self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self,amount):
        self._balance -= amount

class PredatoryCreditCard(CreditCard):
    OVERLIMIT_FEE=5
    def __init__(self, customer, bank, acnt, limit,apr):
        '''
        :param apr: 年利率
        '''
        super().__init__(customer, bank, acnt, limit)
        self._apr=apr

    def charge(self, price):
        '''收费'''
        success = super().charge(price)
        # 收费由于超过信用卡额度被拒绝时，会收取5元的费用
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE # access penalty
        return success
     
    def process_month(self):
        # 对未清余额按月收取利息的机制
        if self._balance > 0:
            monthly_factor = pow(1+ self._apr,1/12)
            self._balance *= monthly_factor

class PredatoryCreditCardV2(CreditCard):
    OVERLIMIT_FEE=5
    def __init__(self, customer, bank, acnt, limit,apr):
        '''
        :param apr: 年利率
        '''
        super().__init__(customer, bank, acnt, limit)
        self._apr=apr
        self.__monthcalls = [self.__get_month(), 0]
        self._lowst_money= 0
        self._pre_pay=0
    @property
    def lowst_pay_money(self):
        '''最低付款额'''
        return self._lowst_money
    @lowst_pay_money.setter
    def lowst_pay_money(self, money):
        self.lowst_pay_money = money

    def __get_month(self):
        return datetime().month

    
    def charge(self, price):
        '''收费'''       
        has_delay=False
        if self._pre_pay <= self.lowst_pay_money:
            # 什么是连续？第二次仍是最低付款额度
            has_delay=True                  

        self._pre_pay=price
        if has_delay:
            # 有延迟，需要增加延迟费用
            price += 1
        success = super().charge(price)
        # 收费由于超过信用卡额度被拒绝时，会收取5元的费用
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE # access penalty
        return success
    def check_month_call(self,month):
        if self.__monthcalls[0] == month:
           self.__monthcalls[1] += 1
        else:
            self.__monthcalls[0] = month
            self.__monthcalls[1] = 1 
        return self.__monthcalls[1]

    def process_month(self):
        m=self.__get_month()
        if self.check_month_call(m) > 10:
            # 
            self.set_blance(self.get_blance() + 1)
        # 对未清余额按月收取利息的机制
        if self.get_blance() > 0:
            monthly_factor = pow(1+ self._apr,1/12)
            self.set_blance(self.get_blance() * monthly_factor) 
if __name__ == '__main__':
    print(premeCountLessThan(100))
   
