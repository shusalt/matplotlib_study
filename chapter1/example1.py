import matplotlib.pyplot as plt
import numpy as np
'''matplotlab pyplot'''
if __name__ == '__main__':
    # xpoints=np.array([0,6])
    # ypoints=np.array([0,100])
    #
    # '''绘制出的线图'''
    # plt.plot(xpoints,ypoints)
    # plt.show()


    '''绘制(1,3)到(8,10)的线'''
    # xpoints=np.array([1,8])
    # ypoints=np.array([3,10])
    #
    # plt.plot(xpoints,ypoints)
    # plt.show()


    '''绘制(1,3)到(8,10)的两个点'''
    # xpoints=np.array([1,8])
    # ypoints=np.array([3,18])
    #
    # plt.plot(xpoints,ypoints,'o')
    # plt.show()


    '''绘制一条不规则线'''
    # xpoints=np.array([1,2,6,8])
    # ypoint=np.array([3,8,1,10])
    #
    # plt.plot(xpoints,ypoint)
    # plt.show()


    '''如果我们不指定x轴上的点，则x会根据y的值来设置0,1,2，3...N-1'''
    # ypoints=np.array([3,10])
    # plt.plot(ypoints)
    # plt.show()


    '''更多值的实例'''
    # ypoints=np.array([3,8,1,10,5,7])
    # plt.plot(ypoints)
    # plt.show()


    '''绘制正弦与余弦图'''
    x=np.arange(0,4*np.pi,0.1)
    y=np.sin(x)
    z=np.cos(x)
    plt.plot(x,y,x,z)
    plt.show()