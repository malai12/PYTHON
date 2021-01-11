from itertools import permutations
from tqdm import tqdm
def largest(l):
    lst = []
    for i in tqdm(permutations(l, len(l))):
        # provides all permutations of the list values,
        # store them in list to find max
        print(i,end=" ")
        lst.append("".join(map(str,i))) 
    #print(lst)    
    return max(lst)
 
print(largest([54, 546, 548, 60]))