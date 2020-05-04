import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 以Wine Reviews为例，Consumer & Visitor Insights For Neighborhoods数据集更改下路径和列名称即可
def loader():   #读取数据
    filepath ="winemag-data_first150k.csv" #使用的数据集文件地址
    data = pd.read_csv(filepath, header=0) #导出数值数据
    return data

def PLOT1(str1,dt1): #绘制直方图
    hist = dt1[str1].hist(bins= 100) #显示在100个bins中
    plt.show()

def PLOT2(str2,dt2):    #绘制盒图
    dt2[str2].plot.box()
    plt.show()

if __name__ == "__main__":
    data = loader()
    PLOT1("points",data)
    PLOT1("price",data)
    PLOT2("points", data)
    PLOT2("price", data)





