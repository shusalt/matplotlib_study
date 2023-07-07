import matplotlib.pyplot as plt
import numpy as np
'''imshow()'''

if __name__ == '__main__':
    '''test1'''
    # img=np.random.rand(10,10)
    # plt.imshow(img,cmap='gray')
    # plt.show()

    '''test2'''
    # img=np.random.rand(10,10,3)
    # plt.imshow(img)
    # plt.show()


    '''热力图'''
    # data=np.random.rand(10,10)
    # plt.imshow(data,cmap='hot')
    # plt.colorbar()
    # plt.show()


    '''地图'''
    # import matplotlib.pyplot as plt
    # import numpy as np
    # from PIL import Image
    #
    # # 加载地图图像, 下载地址：https://static.runoob.com/images/demo/map.jpeg
    # img = Image.open('map.jpg')
    #
    # # 转换为数组
    # data = np.array(img)
    #
    # # 绘制地图
    # plt.imshow(data)
    #
    # # 隐藏坐标轴
    # plt.axis('off')
    #
    # # 显示图像
    # plt.show()



    '''显示矩阵'''
    # data=np.random.rand(10,10)
    # plt.imshow(data)
    # plt.colorbar()
    # plt.show()


    '''更多实例'''
    n=4

    # 创建一个 n x n 的二维numpy数组
    a = np.reshape(np.linspace(0, 1, n ** 2), (n, n))

    plt.figure(figsize=(12, 4.5))

    # 第一张图展示灰度的色彩映射方式，并且没有进行颜色的混合
    plt.subplot(131)
    plt.imshow(a, cmap='gray', interpolation='nearest')
    plt.xticks(range(n))
    plt.yticks(range(n))
    # 灰度映射，无混合
    plt.title('Gray color map, no blending', y=1.02, fontsize=12)

    # 第二张图展示使用viridis颜色映射的图像，同样没有进行颜色的混合
    plt.subplot(132)
    plt.imshow(a, cmap='viridis', interpolation='nearest')
    plt.yticks([])
    plt.xticks(range(n))
    # Viridis映射，无混合
    plt.title('Viridis color map, no blending', y=1.02, fontsize=12)

    # 第三张图展示使用viridis颜色映射的图像，并且使用了双立方插值方法进行颜色混合
    plt.subplot(133)
    plt.imshow(a, cmap='viridis', interpolation='bicubic')
    plt.yticks([])
    plt.xticks(range(n))
    # Viridis 映射，双立方混合
    plt.title('Viridis color map, bicubic blending', y=1.02, fontsize=12)

    plt.show()