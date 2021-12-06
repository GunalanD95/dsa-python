# BIG O((N)2 + n)


# this fun iterated to n*n*n times with n*n operations thats an example of big O(n)2


def print_items_2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    for k in range(n):
        print(k)


# print_items_2 is an example of big O(n)2+n

# first for loop ran throught o(n2) times and then the second for loop ran throught o(n) times = o(n2+n)

print_items_2(10)
