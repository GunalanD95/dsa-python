# template strings functions

from string import Template
from unicodedata import name

def main():

    #Usual string formating with format()
    str1 = "Hi iam {0} i work in {1}".format("Gunalan","IT")
    print("str1",str1)

    #CREATE A TEMPLATE STRINGS
    temp1 = Template("Iam a ${club} Fan")
    str2 = temp1.substitute(club="Barcelona")
    print("str2",str2)

if __name__ == '__main__':
    main()