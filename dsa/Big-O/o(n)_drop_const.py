# BIG O(N) DROP CONSTANTS


# this fun iterated to n+n times with n operations , but as to simplify we need to drop constants thats an example of drop constants in big O(n)

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items(10)
