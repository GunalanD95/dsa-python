# unordered , mutuable , key value pair


# create a dictionary

dic = {'name': 'sachin', 'age': 30, 'city': 'mumbai'}

print("dic", dic)

new_dic = dict(name='messi', age=35, city='barcelona')
print("new_dic", new_dic)


# accessing

name = dic['name']
print(f"the player name is {name}")


# addin new key value pair
dic["country"] = "india"
new_dic["country"] = "spain"
print("dic", dic)
print("append new_dic", new_dic)


# update a key value pair
new_dic["country"] = "france"
print("update new_dic", new_dic)


# delete a key value pair
del new_dic["country"]
print("delete", new_dic)

dic.pop("age")
print("delete dic age", dic)

dic.popitem()  # delete last key value pair


# check if key is present

if "name" in dic:
    print(f"name is {dic['name']}")
else:
    print("country is not present")


try:
    print(f"name is {dic['country']}")
except KeyError:
    print("country is not present")


#looping in dic

# key loop
for key in new_dic:
    print("key", key)

for key in new_dic.keys():
    print("keys as list", key)

# value loop
for value in new_dic.values():
    print("value", value)

# key value pair loop
for key, value in new_dic.items():
    print("key value pair", key, value)


# copy/ duplicate

copy_dic = new_dic.copy()
copy_dic_new = dict(new_dic)
copy_dic["name"] = "leo messi"
print("copy_dic", copy_dic)
print("copy_dic orginal", new_dic)


# assignment

ditto_dic = dic
ditto_dic["name"] = "ditto"
print("ditto_dic", ditto_dic)
print("name will change in original dic too if we use like this", dic)


# update
dic_1 = {'name': 'neymar', 'age': 30, 'country': 'brazil', 'city': 'rio'}
dic_2 = {'name': 'suarez', 'age': 35, 'country': 'urugay'}
print("dic_1", dic_1)
print("dic_2", dic_2)

dic_1.update(dic_2)  # will update the value of dic_1 if the key is same
# dic1 value got overriden by dic2 values
print(dic_1, "dic_1 after update method")
