import sys
import csv
import random
import numpy as np

if len(sys.argv)==1:
    print('Try to add "start" as an argument.')

if len(sys.argv) == 2 :
    if sys.argv[1] == 'start':
        a=np.random.randint(1,10,2000)
        matrix=a.reshape(200,10)
        with open('ints.csv' , 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(matrix)
        print('Done! ')
        print('Try the same thing but this time with "end" to get all the even numbers in the CSV file.')

    if sys.argv[1] == 'end':
        with open('ints.csv', 'r') as file:
            reader=csv.reader(file)
            for row in reader:
                for i in row:
                    if int(i)%2==0:
                        print(int(i) , end=' ')
            print()
        print(" Good job ,isn't it?")