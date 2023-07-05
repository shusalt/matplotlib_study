import matplotlib.markers
import matplotlib.pyplot as plt
import numpy as np


'''绘图标记'''
if __name__ == '__main__':
    '''marker标记'''
    # ypoints=np.array([1,3,4,5,8,9,6,1,3,4,5,2,6])
    # plt.plot(ypoints,marker='o')
    # plt.show()

    '''定义箭头标记'''
    # plt.plot([1,2,3],marker=matplotlib.markers.CARETDOWNBASE)
    # plt.show()

    '''定义星星标记'''
    # plt.plot([1,3,4,5,8,9,1,3,4,5,2,4],marker='*')
    # plt.show()

    '''fmt参数定义基本格式，例如标记、线条样式和颜色'''
    # ypoints=np.array([6,2,13,10])
    #
    # plt.plot(ypoints,'o:r')
    # plt.show()


    '''标记大小与颜色，markersize:标记大小,markerfacecolor：标记内部颜色,markeredgecolor：标记外部颜色'''
    # ypoints=np.array([6,2,13,10])
    # plt.plot(ypoints,marker='o',ms=20)
    # plt.show()

    '''标记内部与边框的颜色'''
    ypoints=np.array([6,2,13,10])
    plt.plot(ypoints,marker='o',ms=20,mec='#4CAF50',mfc='#4CAF50')
    plt.show()
