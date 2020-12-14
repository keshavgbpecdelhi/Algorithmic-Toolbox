# python3
#solution of Partitioning_Souvenirs

#NOTE : 
#item_weights = iw
#total_weight = tw
#

import numpy

def Partitioning_Souvenirs(W, n, items):
    count = 0 
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: count += 1

    if count < 3: print('0')
    else: print('1')

if __name__ == '__main__':
    n = int(input())
    iw = [int(i) for i in input().split()]
    tw = sum(iw)
    if n<3: 
        print('0')
    elif tw%3 != 0: 
        print('0')
    else:
        Partitioning_Souvenirs(tw//3, n, iw)
        