a = [12,12,13,4,3,2,"thiru"]
print("thiru" in a)            #in operator it returns true or flase

#mising a number between 1 to 40
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40] 
sum1 = 40*41//2               # sum of 1,2,3,..n => n(n+1)/2
sum2 = sum(a)
print(sum1-sum2)

#program to find all pairs of integers whose sum is equal to given num

p = [2,6,3,9,11]
s = 9
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i]+p[j] == s:
            print(p[i],p[j])

# maximun product of two integers in an given array

import numpy as np
ar = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
def maxpro(array):
    current_max = 1
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j]>current_max:
                current_max = array[i]*array[j]
    print(current_max)
maxpro(ar)    

# program -> is unique array
ar = [1,2,3,4,5,6,7,8,9,10,11,12,3,14,15,1,17,18,19,2]

def isunique(list):
    e = []
    for i in range(len(list)):
        if list[i] not in e:
            e.append(list[i])
    print(e)
isunique(ar)         

#program for rotate matrix by 90 degree

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
def rotate90(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n-layer-1
        for i in range(first,last):
            top = matrix[layer][i]  #save top element
            matrix[layer][i] = matrix[-i-1][layer]  #move left element to top
            matrix[-i-1][layer] = matrix[-layer-1][-i-1] # move bottom element to left
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]  # move right element to bottom
            matrix[i][-layer-1] = top                   # move first element to right
        print(matrix)
rotate90(m)        
