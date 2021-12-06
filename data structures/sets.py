# Sets : unordered, mutuable, no duplicates


# does not allow duplicates
sets = {'guna', 'guna'}
print(sets)
hello = set("hello aabbcc")  # unordered and removed duplicates in the set
print(hello, "hello")


list_set = set([1, 2, 3, 4, 5, 6, 7])
print(list_set)


# append
sets.add("add this set")
print("append sets", sets)
hello.add(999)
print("append hello", hello)
hello.remove(999)
print("remove hello", hello)



#access method

setu = {'abc','cde','fgh'}
for i in setu:
    print(i)

if 'abc' in setu:
    print("abc is there in the loop")



#union and intersection

odds={1,3,5,7,9}
even={0,2,4,6,8,10}
primes = {2,3,5,7}

u = odds.union(even)  # union method will combine two sets into one
print(u)

i = odds.intersection(primes) # will return the common elements
print(i)

setA= {1,2,3,4,5,6,7,8,9}
setB= {1,2,3,10,11,12}

diff = setA.difference(setB) 
print(diff)

sm_diff = setA.symmetric_difference(setB)
print(sm_diff)


setA.update(setB)
print(setA)