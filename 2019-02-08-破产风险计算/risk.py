import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

p = 0.5   #获胜的概率
a = 2   #获胜的净回报
b = 1  #失败的净损失

randomNum = 10000 #随机样本数

randomSample = [1 if np.random.random_sample() < p else 0 for i in range(randomNum)] #

def isWin(i):
    global randomSample
    return randomSample[i] == 1

#根据样本模拟投机， 并计算所有投机完成后的最后资产
def calc_return(p, a, b, position, times):
    result = 1
    for i in range(times):
        #根据样本计算赌博之后的资产
        result = result * (1 - position) + result * position * ((1 + a) if isWin(i) else (1 - b))
        
    return result

#返回字典数组， [{仓位: postion， 回报率: rate},]
def monte_carlo_calc(p, a, b):
    
    result = []
    
    #穷举仓位， 并计算对应的回报率
    for x in range(101):
        position = x * 0.01
        total = calc_return(p, a, b, position, randomNum)
        rate = math.pow(total, 1.0/randomNum) - 1
        # print "仓位 = %.2f 复利 = %.3f" % (position, d)
        result.append({"position" : position, "rate" : rate})
        
    return result


results = monte_carlo_calc(p, a, b)

maxRate = -1
bestPostion = 0

for result in results:
    print "仓位 = %.2f 复利 = %.3f" % (result["position"], result["rate"])
    if result["rate"] > maxRate:
        maxRate = result["rate"]
        bestPostion = result["position"]

print "\r\n最佳仓位 = %.2f%% 复利 = %.2f%%" % (bestPostion*100, maxRate*100)


