import matplotlib.pyplot as plt
import numpy as np

'''柱状图'''
if __name__ == '__main__':
    '''test1'''
    # x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
    # y = np.array([12, 22, 6, 18])
    #
    # plt.bar(x, y)
    # plt.show()

    '''test2'''
    # x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
    # y = np.array([12, 22, 6, 18])
    #
    # plt.barh(x,y,color="#4CAF50")
    # plt.show()

    '''test3'''
    # x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
    # y = np.array([12, 22, 6, 18])
    # plt.bar(x, y, color=["#4CAF50", "red", "hotpink", "#556B2F"])
    # plt.show()

    '''test4'''
    # x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
    # y = np.array([12, 22, 6, 18])
    # plt.bar(x,y,width=0.1)
    # plt.show()

    '''test5'''
    x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
    y = np.array([12, 22, 6, 18])

    plt.barh(x, y, height=0.1)
    plt.show()




