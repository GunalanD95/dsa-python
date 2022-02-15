import stack_class


def reverse_string(my_string):
    """
    Reverse a string
    """
    reversed_string = ""
    reversed_string1 = ""
    s = stack_class.Stack()
    reversed_string = s.reverse(my_string)
    print(reversed_string)

    # appending the string elements to the stack 
    for i in my_string:
        s.push(i)

    # popping the elements from the stack and appending to the reversed string
    while not s.is_empty():
        reversed_string1 += s.pop()
    print(reversed_string1)


if __name__ == "__main__":
    reverse_string("krowemarf bew a si ognajD")