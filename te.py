# Driver program
arr = [50, 40, 70, 60, 90]
index = [3, 0, 4, 1, 2]
n = len(arr)
temp = [0] * n
print(temp)#heolllo
 
# arr[i] should be
    # present at index[i] index
for i in range(0,n):
    temp[index[i]] = arr[i]
    print(index[i],end=" ")
print(temp)
# Copy temp[] to arr[]
for i in range(0,n):
    arr[i] = temp[i]
    print(temp[i],end=" ")
    index[i] = i
    
    
