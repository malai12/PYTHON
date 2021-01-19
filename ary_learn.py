print("-------------------- array insertion -------------------------")

from array import *            #importing array module

a1 = array('i',[1,2,3,4,5,6])  #creating array
a2 = array('i',[1,2,3,4,5,6])

# print(a1)                                 #space complexity O(n)

a1.insert(6,7)                 #array insertion syntax will be a1.insert(index,value)
a1.insert(0,1)
print(a1)

#if we insert at the end of the array its time complexity will be "O(1)" or if we insert in the 
#beginning/in the middle the time complexity is "O(n)" 

print("-------------------- array traversal -------------------------")

def traverse(array):                      #time complexity O(n)
    for i in array:                       # space complexity O(1) -> no extra space needed
        print(i,end=" ")
    print()    

traverse(a1)
#traversal mean visiting all the element in the array

print("-------------------- access array element --------------------")

def accesselement(array,index):
    assert index < len(array),"There is no element in that array"
    print(array[index])                                
                                                     # space complexity O(1) -> no extra space needed
accesselement(a1,1)                                 # time complexity O(1)
    
print("------------------ search element in array -------------------")

def search(array,value):
    for i in array:
        if i==value:
            return a1.index(value)
    return "There is no element in this array"

print(search(a1,6))    

print("-------------------- delete an element -----------------------")

a1.remove(4)                                    #time complexity O(n)/O(1)
print(a1)                                       # space complexity O(1)

print("-------------------- use of extend method --------------------")
a1.extend(a2)
print(a1)

print("------------------ use of fromlist method --------------------")
l = [12,32,42,1,12]
a1.fromlist(l)       #this is for add a list to array
print(a1)

print("-------------------- use of reverse method -------------------")
a1.reverse()
print(a1)

print("-------------------- use of extend method --------------------")
print(a1.buffer_info())     # it shows number of element in array and memory address

#                  TWO DIMENSION ARRAY           

print("-------------------- TWO DIMENSION ARRAY ---------------------")
import numpy as np
todary = np.array([[1,23,4,5],[12,32,42,4],[123,34,5,4]])
print(todary)

print("-------------------- insertion in 2d array ---------------------")
newtodary = np.insert(todary,0, [[12,3,45]], axis=1)
print(newtodary)

print("------------------ access element in 2d array ------------------")
def access(array,ri,ci):
    if ri>=len(array) and ci>=len(array[0]):
        print("Incorrect index")
    else:                                             #time complexity O(1)
        print(array[ri][ci])                            # space complexity O(1)
access(newtodary,2,2)      

print("-------------------- traversal in 2d array ---------------------")
def traverse2d(array):
    for i in range(len(array)):
        for j in range(len(array[0])):              #time complexity O(mn)
            print(array[i][j],end=" ")              #space complecity O(1)
        print()  
traverse2d(newtodary)   

print("-------------------- search in 2d array ------------------------")          
def search2d(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):                      #time complexity O(mn)
            if array[i][j] == value:                        # space complexity O(1)
                return "the element is in "+str(i) +" "+ str(j)+" the position"
    return "The element not found"
print(search2d(newtodary,32))                

print("-------------------- deletion in 2d array ---------------------")

newtodary = np.delete(newtodary,0,axis=1)                    #time complexity O(mn)
print(newtodary)                                              # space complexity O(1)gig