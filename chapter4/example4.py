import matplotlib.pyplot as plt
import numpy as np

'''matplotlib 轴标签和标题'''
if __name__ == '__main__':
    '''设置显示中文'''
    plt.rcParams['font.sans-serif']='SimHei'
    plt.rcParams['axes.unicode_minus']=False

    '''轴标签'''
    # x=np.array([1,2,3,4])
    # y=np.array([1,4,9,16])
    # plt.plot(x,y)

    # plt.xlabel("x-label")
    # plt.ylabel("y-label")
    # plt.show()

    '''标题'''
    # x=np.array([1,2,3,4])
    # y=np.array([1,4,9,16])
    # plt.plot(x,y)
    #
    # plt.title("hello word")
    # plt.xlabel('x-label')
    # plt.ylabel('y-label')
    # plt.show()


    '''设置显示中文字体'''
    # plt.rcParams['font.sans-serif']='SimHei'
    # plt.rcParams['axes.unicode_minus']=False
    #
    # x=np.arange(1,11)
    # y=2*x+5
    # plt.title('测试')
    # plt.xlabel('x轴')
    # plt.ylabel('y轴')
    # plt.plot(x,y)
    # plt.show()


    '''标签与标签的定位'''
    x=np.arange(1,11)
    y=2*x+5
    plt.title('测试')
    plt.xlabel("x轴",loc='left')
    plt.ylabel("y轴",loc='top')
    plt.plot(x,y)
    plt.show()