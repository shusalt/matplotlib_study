import matplotlib.pyplot as plt
import numpy as np
'''拼图'''

if __name__ == '__main__':
    '''test1'''
    # y=np.array([35,25,25,15])
    # plt.pie(y)
    # plt.show()

    '''test2'''
    # y = np.array([35, 25, 25, 15])
    # plt.pie(y,labels=['A','B','C','D'],
    #         colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"])
    # plt.title('test1')
    # plt.show()

    '''test3'''
    # sizes=[15,30,45,10]
    #
    # labels=['A','B','C','D']
    #
    # colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    #
    # explode=(0,0.1,0,0)
    #
    # plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
    #
    # plt.title('test')
    #
    # plt.show()


    '''test4'''
    y=np.array([35,25,25,15])
    plt.pie(y,labels=['A','B','C','D'],
            colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],
            explode=(0, 0.2, 0, 0),
            autopct='%.2f%%')
    plt.title("test")
    plt.show()