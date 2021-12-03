# tuples are ordered and unchangeable


tuples = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


new_tuple = tuple(["guna", "sudha", "amma"])  # using built in function
print(type(new_tuple), new_tuple)


# indexing
print("index", tuples[0])
print("index -2", new_tuple[-2])
print("index", new_tuple.index("amma"))

# loop
for n in new_tuple:
    print(n)

if "guna" in new_tuple:
    print("guna is there")
else:
    print("guna is not there")


# slicing
print(new_tuple[1: 3])
print("rev", new_tuple[::-1])

# length
count_tuple = (1, 2, 3, 4, 2, 1, 3, 4, 2)
print("length", len(new_tuple))
print("count", count_tuple.count(1))


# variable assignment
ass_tuple = "guna", 23, "Developer"

name, age, job = ass_tuple  # no of elements should be same
print(f"hi iam {name} age {age} and iam a {job}")
