# BIG O(N)2

# this is an example of big O(n)2 which is much less effecient than the big o(n) interms of time complexity

# this fun iterated to n*n*n times with n*n operations thats an example of big O(n)2

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# this fun iterated to n*n*n times with n*n*n operations thats an example of big O(n)2
def print_items_2(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


print_items(10)
print_items_2(20)
