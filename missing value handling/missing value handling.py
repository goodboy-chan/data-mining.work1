import numpy
# import cvxopt
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.ensemble import RandomForestRegressor
# from fancyimpute import KNN

# 以Wine Reviews为例，Consumer & Visitor Insights For Neighborhoods数据集更改下路径和列名称即可

def loader():   #读取数据
    filepath ="winemag-data_first150k.csv" #使用的数据集文件地址
    df = pd.read_csv(filepath, header=0, usecols = [3, 4, 7])
    return df

def fun1(data1):    #将缺失部分剔除
    Data1 = data1.dropna(axis = 0)
    # 绘制直方图
    hist = Data1.hist(bins=100)  # 显示在100个bins中
    # 绘制盒图
    Data1.plot.box()
    plt.show()

def fun2(data2):    #用最高频率值来填补缺失值
    Data2 = data2.fillna(data2.mode()) #填充众数
    # 绘制直方图
    hist2 = Data2.hist(bins=100)  # 显示在100个bins中
    # 绘制盒图
    Data2.plot.box()
    plt.show()
'''
def fun3(data3):    #通过属性的相关关系来填补缺失值
    #随机森林填充

    known = data3[data3.notnull()].values
    uknown = data3[data3.isnull()].values
    X = known[:, 1:]
    y = known[:, 1:]
    rf = RandomForestRegressor(random_state=0, n_estimators=200, max_depth=3, n_jobs=-1)
    rf.fit(X, y)
    predicted = rf.predict(uknown[:, 1:])
    Data3 = data3.loc[(data3.c.isnull()), 'c'] = predicted
    # 绘制直方图
    hist = Data3.hist(bins=100)  # 显示在100个bins中
    # 绘制盒图
    Data3.plot.box()
    plt.show()

def fun4(data4):    #通过数据对象之间的相似性来填补缺失值
    #KNN算法填充
    fill_knn = KNN(k=3).fit_transform(data4)
    Data4 = pd.DataFrame(fill_knn)
    # 绘制直方图
    hist = Data4.hist(bins=100)  # 显示在100个bins中
    # 绘制盒图
    Data4.plot.box()
    plt.show()
'''


if __name__ == "__main__":
    df = loader()
    fun1(df)
    fun2(df)
    # fun3(df)
    # fun4(df)