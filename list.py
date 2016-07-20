# 1. Difference among list, tuple, dict and set
#list, ordered, use index to get element
mylist = [1, 2, 3, 4, 'Oh']  

#tuple, ordered, immutable, use index to get element
mytuple = (1, 1, 2, 'Hello', (4, 5))

#dict, non-ordered, key-value pairs, use key to get element, fast
mydict = {'Wang' : 1, 'Hu' : 1, 'Liu' : 4}

#set, non-ordered, value must be unique
myset = set(['Wang', 'Wang', 'Hu', 'Liu', 4])  

print(mylist)  
print(mytuple)  
print(mydict)  
print(myset) 

# 2. Add and remove elements from a list
fruits = ["orange", "apple", "banana"]
print fruits

fruits.append("peach")
print fruits

fruits.remove("apple")
print fruits

del fruits[0]
print fruits

for index in range(len(fruits)):
    print fruits[index]

for fruit in fruits:
    print fruit


# 3. Generator
l1 = [1,2,3,4,5,6,7,8,9,10]    
l2 = [i for i in l1 if i<6]
l3 = [i*i for i in l2]
print l1
print l2
print l3


def foo(n):
    for x in range(n):
        yield x**3
for x in foo(5):
    print x


# 4. Iterator

print range(1,10)
print range(2,4,2)
print range(0,-10,-2)