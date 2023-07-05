import matplotlib.pyplot as plt
import numpy as np

'''matplotlib 网格线'''
if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    '''添加简单的网格线'''
    # x=np.array([1,2,3,4])
    # y=np.array([1,4,9,16])
    #
    # plt.title('测试')
    # plt.xlabel('x-label')
    # plt.ylabel('y-label')
    # plt.plot(x,y)
    # plt.grid()
    # plt.show()


    '''简单的网格线，axis参数为x'''
    # x=np.array([1,2,3,4])
    # y=np.array([1,4,9,16])
    #
    # plt.title('测试')
    # plt.xlabel('x-label')
    # plt.ylabel('y-label')
    #
    # plt.plot(x,y)
    # plt.grid(axis='x')
    # plt.show()

    '''设置一些参数'''
    x=np.array([1,2,3,4])
    y=np.array([1,4,9,16])

    plt.title('测试')
    plt.xlabel('x-label')
    plt.ylabel('y-label')

    plt.plot(x,y)
    plt.grid(color='r',linestyle='--',linewidth=0.5)
    plt.show()