import math

import copy



a = [[6, 0, 2, 3],

     [0, 4, 2, 1],

     [2, 2, 5, 0],

     [1, 1, 0, 3]]  

b = [24, 18, 21, 15]



def isCorrectArray(a):

    for row in range(0, len(a)):

        if( len(a[row]) != len(b) ):

            print('Розмір не підходить')

            return False

    for row in range(0, len(a)):

        if( a[row][row] == 0 ):

            print('Нульові елементи на головній діагоналі')

            return False

    return True



def isNeedToComplete(x_old, x_new):

    eps = 0.0001

    sum_up = 0

    sum_low = 0

    for k in range(0, len(x_old)):

        sum_up += ( x_new[k] - x_old[k] ) ** 2

        sum_low += ( x_new[k] ) ** 2

    return math.sqrt( sum_up / sum_low ) < eps



def solution(a, b):

    if( not isCorrectArray(a) ):

        print("Помилка у вихідних даних")

    else:

        count = len(b) 

        x = [1 for k in range(0, count) ] 

        numberOfIter = 0  

        MAX_ITER = 100   

        while( numberOfIter < MAX_ITER ):

            x_prev = copy.deepcopy(x)

            for k in range(0, count):

                S = 0

                for j in range(0, count):

                    if( j != k ): S = S + a[k][j] * x[j]

                x[k] = b[k]/a[k][k] - S / a[k][k]

            if isNeedToComplete(x_prev, x) : 

                break

            numberOfIter += 1

        print('Кількість ітерацій на розв\'язок: ', numberOfIter)

        return x    

               

print( 'Розв\'язок: ', solution(a, b) ) 