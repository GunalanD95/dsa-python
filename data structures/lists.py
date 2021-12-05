# Lists are ordered , mutable , allows duplicated elements


my_list =["messi","neymar","fati"]

print(my_list[-1]) # getting the n-th element

for n in my_list: #iterating throught the list
    print(n)

if "messi" in my_list: # checking "string" is in there the list
    print("messi is there")


print("length of the list" ,len(my_list)) #length of the list


my_list.append("guna")# adding a new element using append keyword
my_list.insert(2,"sudhan") # inserting a new element in index/pos 2

del my_list[0] # deleting the item with index as 0
print(my_list)
my_list.remove("fati") # deleting the item fati from the list using remove method
print(my_list)

my_list.sort() #sorting a list
print(my_list,"sorted")


rv_lst = my_list.reverse() # reversing the list
print(rv_lst)
my_list.clear() # will remove all the elements from the list


dum_list = [1,2] * 5 # creating a list with given list * 5
print(dum_list)

nx_list = [3,4] * 5
b_next_lst = dum_list + nx_list #adding two lists as one
print(b_next_lst)


a = b_next_lst[1:4] #slicing using index
print(a)

a = b_next_lst[::2] #using step (here its taking only the 2nd item)
print(a)




#Assignment operator

lis = [2,6,4,7,8,9,12,3]

nes = lis 

nes.append("guna") #changes will affect in both lists since both are same
print("lis",lis)


#copy method

liss = [2,6,4,7,8,9,12,3]

ness = lis 

ness.append("guna") #changes will affect in both lists since both are same
print("lis",liss)




# list comprenhension

list_cmp = [1,2,3,4,5,6,7,8,9,10]

sqrd_list = [i*i for i in list_cmp]
print("sqrd list",sqrd_list)


