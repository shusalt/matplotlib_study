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
    # x=np.array([0,6])
    # y=np.array([0,100])
    #
    # plt.subplot(2,2,1)
    # plt.plot(x,y)
    # plt.title("plot 1")
    #
    # # plot2
    # x=np.array([1,2,3,4])
    # y=np.array([1,4,9,16])
    #
    # plt.subplot(2,2,2)
    # plt.plot(x,y)
    # plt.title("plot 2")
    #
    # # plot2
    # x=np.array([1,2,3,4])
    # y=np.array([3,5,7,9])
    #
    # plt.subplot(2,2,3)
    # plt.plot(x,y)
    # plt.title("plot3")
    #
    # # plot3
    # x=np.array([1,2,3,4])
    # y=np.array([4,5,6,7])
    #
    # plt.subplot(2,2,3)
    # plt.plot(x,y)
    # plt.title("plot 3")
    #
    # # plot4
    # x=np.array([1,2,3,4])
    # y=np.array([4,5,6,7])
    #
    # plt.subplot(2,2,4)
    # plt.plot(x,y)
    # plt.title("plot 4")
    #
    # plt.suptitle("test2")
    # plt.show()

    '''subplots()'''
    # 图一
    x=np.linspace(0,2*np.pi,400)
    y=np.sin(x**2)
    #
    # fig,ax=plt.subplots()
    # ax.plot(x,y)
    # ax.set_title('simple plot')
    # plt.show()


    # 图二
    # f,(ax1,ax2)=plt.subplots(1,2,sharey=True)
    # ax1.plot(x,y)
    # ax1.set_title('sharing y axis')
    # ax2.scatter(x,y)
    # plt.show()


    # 图三
    # fig,axs=plt.subplots(2,2,subplot_kw=dict(projection="polar"))
    # axs[0,0].plot(x,y)
    # axs[1,1].scatter(x,y)
    # plt.show()
