import numpy as np
import pandas as pd
from pandas import DataFrame

# 以Wine Reviews为例，Consumer & Visitor Insights For Neighborhoods数据集更改下路径和列名称即可

def loader():   #读取数据
    filepath ="winemag-data_first150k.csv" #使用的数据集文件地址
    df = pd.read_csv(filepath, header=0)
    return df

def count(str1,data1): #输出标称数据频数
    print(data1[str1].value_counts())

def fiveNumberandnull(str2,data2): #输出数值数据5数概括及缺失值的个数
    nums = data2[str2]
    nullnum = nums.isnull().sum()
    print("null:%d"%(nullnum))
    # 五数概括 Minimum（最小值）、Q1、Median（中位数、）、Q3、Maximum（最大值）
    nums = nums.dropna(axis = 0) #删除NaN值
    Minimum = min(nums)
    Maximum = max(nums)
    Q1 = np.percentile(nums, 25)
    Median = np.median(nums)
    Q3 = np.percentile(nums, 75)
    print("Minimum:%d; Q1:%d; Median:%d; Q3:%d; Maximum:%d;"%(Minimum , Q1 , Median , Q3 , Maximum)) #都为整数



if __name__ == "__main__":
    df = loader()

    #输出标称数据的每个可能的频数
    print("country频数：")
    count("country",df)
    print("designation频数：")
    count("designation",df)
    print("province频数：")
    count("province",df)
    print("region_1频数：")
    count("region_1",df)
    print("region_2频数：")
    count("region_2",df)
    print("variety频数：")
    count("variety",df)
    print("winery频数：")
    count("winery",df)

    #输出数值数据5数概括及缺失值的个数
    print("points数概括及缺失值的个数:")
    fiveNumberandnull("points",df)
    print("price数概括及缺失值的个数:")
    fiveNumberandnull("price",df)
