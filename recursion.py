print("/--------------factorial------------------/")
def factorial(n):
    assert n>=0 and int(n) == n,"it shoud be positive and integer"
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))   

print("/--------------fibanacci series-------------/")
def fibanacci(n):
    assert n>=0 and int(n) == n,"it shoud be positive and integer"
    if n in [0,1]:
        return n
    else:
        return fibanacci(n-1) + fibanacci(n-2)
print(fibanacci(7))  
print("/--------------sumofdigits-------------/")          
def sod(n):
    assert n>=0 and int(n) == n,"it shoud be positive and integer"
    if n==0:
        return 0
    else:
        return (n%10 + sod(int(n/10)))
print(sod(234))     
print("/-------------power of number-------------/") 
def power(base,exp):
    assert exp>=0 and int(exp) == exp,"it shoud be positive and integer"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base*power(base,exp-1)
print(power(2,3))    
print("/-------------gcd program-------------/")             
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(48,18)) 
print("/-------------decimaltobinary-------------/") 
def dtob(n):
    if n==0:
        return 0
    else:
        return n%2 + 10*dtob(int(n/2))
print(dtob(15))  
print("/-------------end-------------/")                      