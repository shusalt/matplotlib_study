import matplotlib.pyplot as plt
import numpy as np

'''绘制线'''
if __name__ == '__main__':
    '''点虚线'''
    # ypoint=np.array([6,2,13,10])
    #
    # plt.plot(ypoint,linestyle=':')
    # plt.show()


    '''点划线'''
    # ypoints=np.array([6,2,13,10])
    # plt.plot(ypoints,ls='-.')
    # plt.show()


    '''线的颜色'''
    # ypoints=np.array([6,2,13,10])
    # plt.plot(ypoints,color='r')
    # plt.show()

    '''绘制绿色的线'''
    # ypoints=np.array([6,2,13,10])
    # plt.plot(ypoints,c='#8FBC8F')
    # plt.show()


    '''线的宽度'''
    # ypoints=np.array([6,2,13,10])
    # plt.plot(ypoints,linewidth='12.5')
    # plt.show()


    '''多线条'''
    y1=np.array([3,7,5,9])
    y2=np.array([6,2,13,10])

    plt.plot(y1)
    plt.plot(y2)
    plt.show()

    x2=np.array([0,1,2,3])
    y2=np.array([3,7,5,9])
    x3=np.array([0,1,2,3,])
    y3=np.array([6,2,13,10])
    plt.plot(x2,y2,x3,y3)
    plt.show()