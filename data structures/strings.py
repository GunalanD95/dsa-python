# strings are ordered , immutable , text representation

string = 'Gunalan'
print("string", string)

string_with_qts = 'I\'m a string'  # we can use \ to have ' inside a strings
print("string_with_qts", string_with_qts)

one_line_string = """Hello\
iam a string with \
multiple lines"""  # we can use \ to convert mutiple lines into one line string

print("one_line_string", one_line_string)

multiple_line_string = """Hello 
iam a string with
multiple lines"""
print("multiple_line_string", multiple_line_string)


multiple_line_strings_with = """Hello \n iam a string with \n multiple lines"""
print("multiple_line_string usig \n ",
      multiple_line_strings_with)  # we can use \n inside a string to create a new line


# access a string

my_string = "MESSI"
print("access the index 0 of the my_string", my_string[0])

# strings can be changed [0] = 'A' immutable
string_meth = "LeoMessi"
# string_meth[0] = 'A'
print("string_meth", string_meth)


# slicing a string

slice_string = "GUNALAN"
print("slice_string", slice_string[0:4])  # 0:3 means from 0 to 3
print("slice_string", slice_string[0:])  # 0: means from 0 to the end
print("slice_string", slice_string[:])  # : means from the start to the end
print("slice_string", slice_string[::2])  # ::2 means every 2nd element
# ::-1 means every element in reverse order
print("slice_string", slice_string[::-1])


# reverse a string with for loop

def emp(string_1):
    rv = ""
    for i in string_1:
        rv = i + rv
    return rv


string_1 = "Gunalan"
print(emp(string_1))


# concatenate strings
name = "Gunalan"
surname = "Deivaganapathy"
age = 23
job = "Software Engineer"
print(f"My name is {name} {surname} and I am {age} years old and I am a {job}")

# check confiton
if "Software" in job:
    print("Keyword Software is there")
else:
    print("Keyword Software is not there")


# remove white space in strings
white_string = "    Gunalan    "
print("white_string", white_string)
print("white_string", white_string.strip())  # strip() removes white space

# captiliaze() capitalizes the first letter
cap = "gunalan"
print("captiliaze", cap.capitalize())

# uppercase() will convert the string to uppercase
print("uppercase", cap.upper())

# lowercase() will convert the string to lowercase
print("lowercase", cap.lower())

# check the word starts with a particular letter or word
print(cap.startswith("g"))
print(cap.startswith("guna"))

# check the word end with a particular letter or word
print(cap.endswith("lan"))


# check the index of a particular letter
k = "guna"
print("find the index of letter g", k.find('g'))

# count the number of substring in a string
new = "gunalan"
print("find the count of letter a", new.count('a'))

# replace a substring with another substring
re = "Spain"
print(re.replace('Spain', 'France'))
print(re)  # since strings are immutables we are not changing the original string, we can print it again


# list with strings
new_word = "Are you Okay?"
new_list = list(new_word)
print(new_list)


# remove elements from a string

dev = "www.gunalan.com"
ksi = dev.strip('wcomg') # it will remove the wcomg letters from the string not as whole word but as a substring
print(ksi,"ksi")


# remove elements from a string from right side
whitnoise = "       KING ALDO       "
print(whitnoise.rstrip(),"rstrip")

# remove elements from a string from left side
blacknoise = "       KING ALDO       "
print(whitnoise.lstrip(),"lstrip")


# remove prefix from the string
pre_string = "Gunalan Deivaganapathy"
print(pre_string.removeprefix("Gunalan"),"pre_string")

# remove suffix from the string
suffix_string = "Gunalan Deivaganapathy"
print(suffix_string.removesuffix("Deivaganapathy"),"pre_string")


# replace a substring with another substring
replace_string = "Gunalan Deivaganapathy"
print(replace_string.replace("a", "@"),"replace_string")


import re

string_1 = "i love my job  but i want    to travel to    travel    tho"
print(string_1.replace(" ", "-"),"replace_string_1") # replace every single spaces with -

string_2 = re.sub("\s+", "-", string_1) # replace the all the spaces with -
print(string_2,"replace_string_2")

string_3 = re.sub("\s+", "-", string_1) # replace the all the spaces with -
print(string_2,"replace_string_2")


#maxsplit in string
# split function will basically return a list of substrings

max_split = "www.toniandguy.com"
print(max_split.split(".", maxsplit=1)) # split the string with . and maxsplit is 1
print(max_split.split(".", maxsplit=2)) # split the string with . and maxsplit is 2



# .join method in strings

list_1 = ["Gunalan", "Deivaganapathy"]
print(" ".join(list_1),"join method") # join the list of elements into a single string with space

# partition method in strings

part_string = "Gunalan Deivaganapathy"
print(part_string.partition(" ")) # just like split method but it will return a tuple of 3 elements


# ljust , rjust and center method in strings
just_string = "Gunalan Deivaganapathy"
print(just_string.ljust(50, "*")) # ljust will add the len(50) * to the right side of the string

print(just_string.rjust(50, "*")) # rjust will add the len(50) * to the left side of the string

print(just_string.center(50, "*")) # center will add the len(50) * to the both left and right of the string


# zfill method in strings

num_z = "123"
print(num_z.zfill(10)) # zfill will add the 0 to the left side of the string until the len(10)