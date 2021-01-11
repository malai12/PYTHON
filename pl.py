s = input()
n = len(s)
d = []
a = []

for i in range(0,n,2):
    d.append(s[i])
    
for j in range(1,n,2):
    a.append(s[j])
    
for k in range(len(d)):
    for l in range(int(d[k])):
        print(a[l],end="")    
