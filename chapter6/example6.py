import matplotlib.pyplot as plt
import numpy as np

'''matplotlib 绘制多图'''
if __name__ == '__main__':
    '''subplot实例'''
    # xpoints=np.array([0,6])
    # ypoints=np.array([0,100])
    #
    # plt.subplot(1,2,1)
    # plt.plot(xpoints,ypoints)
    # plt.title("plot 1")
    #
    # x=np.array([1,2,3,4])
    # y=np.array([1,4,9,16])
    #
    # plt.subplot(1,2,2)
    # plt.plot(x,y)
    # plt.title("plot 2")
    # plt.suptitle("test")
    # plt.show()

    '''实例2'''
    # plot1
    x=np.array([0,6])
    y=np.array([0,100])

    plt.subplot(2,2,1)
    plt.plot(x,y)
    plt.title("plot 1")

    # plot2
    x=np.array([1,2,3,4])
    y=np.array([1,4,9,16])

    plt.subplot(2,2,2)
    plt.plot(x,y)
    plt.title("plot 2")

    # plot2
    x=np.array([1,2,3,4])
    y=np.array([3,5,7,9])

    plt.subplot(2,2,3)
    plt.plot(x,y)
    plt.title("plot3")

    # plot3
    x=np.array([1,2,3,4])
    y=np.array([4,5,6,7])

    plt.subplot(2,2,3)
    plt.plot(x,y)
    plt.title("plot 3")

    # plot4
    x=np.array([1,2,3,4])
    y=np.array([4,5,6,7])

    plt.subplot(2,2,4)
    plt.plot(x,y)
    plt.title("plot 4")

    plt.suptitle("test2")
    plt.show()