# BIG O(N)^2

# WE ARE A PASSING A NUMBER N AND WE RAN N^2 OPERATIONS SO THATS O(N)^2 -OPERATIONS OF N * N SQUARE TIMES

def print_items(n):
    for i in range(n):  #LOOP THROUGH THE LIST OF N NUMBERS
        for j in range(n):
            print(i,j) 


# N CUBE TIMES
def print_items(n):
    for i in range(n):  #LOOP THROUGH THE LIST OF N NUMBERS
        for j in range(n):
            for k in range(n):
                print(i,j,k) 

print_items(10) # O(N)^2 - OPERATIONS OF N + N TIMESs