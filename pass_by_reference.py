# Pass by object reference exercise 1
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 

f(2)
f(3,[3,2,1])
f(3)


# Pass by object reference exercise 2
l_mem = []
l = l_mem           # the first call
for i in range(2):
    l.append(i*i)

print(l)            # [0, 1]
print(l_mem)


# Pass by object reference exercise 3
def reassign(list):
    list = [0,1]
list =[0]
reassign(list)
print(list)

def append(a):
    a.append(1)
a =[0]
append(a)
print(a)


# Pass by object reference exercise 4
listA = [0]
listB = listA
listB.append(1)
print listA

listA = [0]
listB = listA
listA.append(1)
print listB