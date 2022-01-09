# BIG O(2N) - DROP CONSTANT

# WE ARE A PASSING A NUMBER N AND WE RAN N^2 OPERATIONS SO THATS O(N)^2 -OPERATIONS OF N + N TIMES

def print_items(n):
    for i in range(n):  #LOOP THROUGH THE LIST OF N NUMBERS
        print(i)
    for j in range(n):
        print(j) 


print_items(10) # O(N)^2 - OPERATIONS OF N + N TIMESs