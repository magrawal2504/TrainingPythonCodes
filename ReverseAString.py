import timeit

# WAP to print a string in reverse order
# Method 1- reverse string using Slicing is faster because its execution
# time is faster among all methods


# Method 1- reverse string using Slicing --- execution time- 0.002 seconds
def reverse_slicing(string):
    return string[::-1]


input_string = "Hello"
print("Reverse String is ", reverse_slicing(input_string))


# Method 2-Reverse String using For Loop -- execution time 0.009 seconds
def reverse_for_loop(string):
    revstr = ''
    for i in string:
        revstr = i + revstr
    return revstr


input_string = "Hello"
print("Reverse String is ", reverse_for_loop(input_string))


# Method 3-Reverse a String using While Loop -- execution time 0.012 seconds
def reverse_while_loop(string):
    revstr = ''
    length = len(string) - 1
    while length >= 0:
        revstr = revstr + string[length]
        length = length - 1
    return revstr


input_string = "Hello"
print("Reverse String is ", reverse_while_loop(input_string))


# Method 4-Reverse a String using join() and reversed()
# -- execution time 0.017 seconds
def reverse_using_join_reversed(string):
    revstr = ''.join(reversed(string))
    return revstr


input_string = "Hello"
print("Reverse String is ", reverse_using_join_reversed(input_string))


# Method 5-Reverse String using List reverse() -- execution time 0.011 seconds
def reverse_using_reverse(string):
    temp_list = list(string)
    temp_list.reverse()
    return ''.join(temp_list)


input_string = "Hello"
print("Reverse String is ", reverse_using_reverse(input_string))


# Method 6-Reverse String using Recursion -- execution time 0.029 seconds
def reverse_using_recursion(string):
    if len(string) == 0:
        return string
    else:
        return reverse_using_recursion(string[1:]) + string[0]


input_string = "Hello"
print("Reverse String is ", reverse_using_recursion(input_string))


# Code to check the execution time in seconds
def execution_time():
    SETUP_CODE = '''
from __main__ import reverse_using_recursion'''

    TEST_CODE = '''
string = "Hello"
reverse_using_recursion(string)'''

# timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

# priniting minimum exec. time
    print('execution time: {}'.format(min(times)))


execution_time()
