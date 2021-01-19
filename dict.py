#dictionary --> it is a collection which is unordered,changeable and indexed


print("------------>mehtods")
dic = {"name":"thiru","age":20,"stream":"ECE"}
# clear() --> it clears all data in the dictionary and returns empty dict
# syntax  --> dictname.clear()
# copy()  --> it copies data from one dixt to other dixt
# syntax  --> newdixt = dictname.copy()
# fromkeys() --> it assigns  a value for sequence of keys
# synatx --> newdict = {}.fromkeys(sequemce[],value)

newd = {}.fromkeys([1,2,3,4],9)
print(newd)

# item --> it returns the key value pair in terms of pairs
print(dic.items())

# keys --> it returns all the keys in the dict
print(dic.keys())

# popitem --> it returns last pair of dict and remove from actual dict
print(dic.popitem())

# setdefault() -->it sets the default falue look at exmple
print(dic.setdefault("name1","malai"))
print(dic)

# values --> it returns all the values from the dict
print(dic.values())