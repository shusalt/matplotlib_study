import matplotlib.pyplot as plt
import numpy as np

'''imsave()'''
if __name__ == '__main__':
    # 创建一幅灰度图像
    img_gray = np.random.random((100, 100))

    # 创建一幅彩色图像
    img_color = np.zeros((100, 100, 3))
    img_color[:, :, 0] = np.random.random((100, 100))
    img_color[:, :, 1] = np.random.random((100, 100))
    img_color[:, :, 2] = np.random.random((100, 100))

    plt.imshow(img_gray,cmap='gray')
    plt.imsave('../graph/img_gray.png',img_gray,cmap='gray')

    plt.imsave('../graph/img_gray.jpg',img_color)