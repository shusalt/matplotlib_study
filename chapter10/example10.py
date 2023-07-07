import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
'''直方图'''

if __name__ == '__main__':
    '''test1'''
    # # 生成一组随机数据
    # data = np.random.randn(1000)
    #
    # # 绘制直方图
    # plt.hist(data, bins=30, color='skyblue', alpha=0.8)
    #
    # # 设置图表属性
    # plt.title('RUNOOB hist() Test')
    # plt.xlabel('Value')
    # plt.ylabel('Frequency')
    #
    # # 显示图表
    # plt.show()


    '''test2'''
    # data1=np.random.normal(0,1,1000)
    # data2=np.random.normal(2,1,1000)
    # data3=np.random.normal(-2,1,1000)
    #
    # plt.hist(data1,bins=30,alpha=0.5,label='Data 1')
    # plt.hist(data2,bins=30,alpha=0.5,label='Data 2')
    # plt.hist(data3,bins=30,alpha=0.5,label='Data 3')
    #
    # plt.title("test3")
    # plt.xlabel("value")
    # plt.ylabel("Frequency")
    # plt.legend()
    #
    # plt.show()


    '''test3 结合pandas'''
    # random_data=np.random.normal(170,10,250)
    # dataframe=pd.DataFrame(random_data)
    # dataframe.hist()
    #
    # plt.title("test3")
    # plt.xlabel('x-value')
    # plt.ylabel('y-value')
    #
    # plt.show()


    '''test4'''
    data=pd.Series(np.random.normal(size=100))

    plt.hist(data,bins=10)

    plt.title("test4")
    plt.xlabel("x-value")
    plt.ylabel('y-value')
    plt.show()