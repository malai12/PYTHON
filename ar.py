

def rotation(ar,r): #it rotate the array by one
    if len(ar) == 0:
        return ar
    #r = r % len(ar)
    
    return ar[r:]+ar[:r]    

def fun(ar):      #returns the sum that is multiplied by its index
    curVal = 0
    for i in range(n):
        curVal+=i*ar[i]
    return curVal    


 
 #driver code

ar = [8,3,1,2]
n = len(ar)  
cv = fun(ar)
MaxVal = 0
ro = ar
for i in range(n):
    ro = rotation(ro,1)
    MaxVal = fun(ro)
    if MaxVal > cv:
        cv = MaxVal
       
    
print(cv)           
