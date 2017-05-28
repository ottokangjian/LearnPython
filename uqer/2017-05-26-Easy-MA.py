import numpy as np
import pandas as pd 
from pandas import DataFrame,Series
#回测设定
start='2014-01-01'
end='2015-12-30'
benchmark='HS300'
#选股策略
universe=StockScreener(Factor.PE.nsmall(10))+['600600.XSHG','600030.XSHG','600497.XSHG','600111.XSHG','600030.XSHG','600028.XSHG']
capital_base=500000
freq = 'd'
#择时策略:短期均线上穿买入，下穿卖出(5日大于10日，30日一定幅度，；10日大于30日一定幅度,且之前30个交易日内5日，10日，30日间距在固定值内（盘整），就买入50手；5日小30日，全部卖出)
def initialize(account):
    pass

def handle_data(account):
    #计算最近一段时间的均价
    hist=account.get_attribute_history('closePrice',60)
    hist=DataFrame(hist)#字典转为DF,0为前第60天收盘价，59为前一天收盘价）
    ma_list=[5,10,30]
    #计算当日5、10、30日均值
    for s in account.universe:
        ma=DataFrame()
        #计算股票s在当日的5、10、30日均值
        for  m in ma_list:
            ma['MA'+str(m)]=pd.rolling_mean(hist[s],m)
        #ma是一个列名为5、10、30日均值的由远及近的DataFrame
        
        a=0.25#盘整幅度参数
        b=0.04#突破幅度参数
        #突破买入条件：5日线突破10日线5%，突破30日线5%；前期较长盘整，过去30天，5，10，30日线之间的差距不超过a
        #Series没有-1的访问方法，所以必须转换成list
        break_condition_buy=((list(ma['MA5'])[-1]/list(ma['MA10'])[-1]-1>b) and (list(ma['MA5'])[-1]/list(ma['MA30'])[-1]-1>b))
        
        #盘整条件实现
        bool_list=[]
        for i in range(2,31):
            bool_list.append((abs(list(ma['MA5'])[-i]/list(ma['MA10'])[-i]-1)<a) and (abs(list(ma['MA5'])[-i]/list(ma['MA30'])[-i]-1)<a) and (abs(list(ma['MA10'])[-i]/list(ma['MA30'])[-i]-1)<a))
        #盘整条件
        arrange_condition=True
        for each in bool_list:
            if each==False:
                arrange_condition=False
                break
                
        #突破卖出条件:5日线跌破30日线
        c=0.04#有效突破条件参数
        break_condition_sell=( list(ma['MA5'])[-1]/list(ma['MA30'])[-1]-1<-c )
        
        #买入
        if break_condition_buy and arrange_condition:
            order(s,5000)
        #卖出
        if (s in account.valid_secpos) and break_condition_sell:
            order_to(s,0)
        
        
    




