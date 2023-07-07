import matplotlib.pyplot as plt
import numpy as np
'''散点图'''

if __name__ == '__main__':
    '''test1'''
    # x=np.array([1,2,3,4,5,6,7,8])
    # y=np.array([1,4,9,16,7,11,23,18])
    #
    # plt.scatter(x,y)
    # plt.show()


    '''test2'''
    # x=np.array([1,2,3,4,5,6,7,8])
    # y=np.array([1,4,9,16,7,11,23,18])
    # size=np.array([20,50,100,200,500,1000,60,90])
    # plt.scatter(x,y,s=size)
    # plt.show()


    '''test3'''
    # x=np.array([1,2,3,4,5,6,7,8])
    # y=np.array([1,4,9,16,7,11,23,18])
    # colors=np.array(['red','green','black','orange','purple','beige','cyan','magenta'])
    #
    # plt.scatter(x,y,c=colors)
    # plt.show()


    '''test4'''
    # x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    # y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    # plt.scatter(x,y,color='hotpink')
    #
    # x1=np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
    # y1=np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
    # plt.scatter(x1,y1,color='#88c999')
    # plt.show()

    '''test5'''
    # np.random.seed(19680801)
    #
    # N=50
    # x=np.random.rand(N)
    # y=np.random.rand(N)
    # colors=np.random.rand(N)
    # area=(30*np.random.rand(N))**2
    #
    # plt.scatter(x,y,s=area,c=colors,alpha=0.5)
    # plt.title("scatter test")
    # plt.show()

    '''test6 颜色条'''
    # x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    # y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    # colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    #
    # plt.scatter(x,y,c=colors,cmap='viridis')
    # plt.colorbar()
    # plt.show()

    '''test7 换另一种颜色'''
    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

    plt.scatter(x,y,c=colors,cmap='afmhot_r')
    plt.colorbar()
    plt.show()