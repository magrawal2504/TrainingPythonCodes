# Program to check whether the entered
# number is positive, negative or zero
def check_number(num):
    if num > 0:
        print("Positive Number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative Number")


num = float(input("Enter a number(for positive, negative and zero):"))
check_number(num)


# Program to check whether the entered year is leap year or not
def check_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{} is a leap year".format(year))
            else:
                print("{} is not a leap year".format(year))
        else:
            print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))


year = int(input("Enter a year(for leap year):"))
check_leap_year(year)

# Program to check whether the number is prime or not.


def Check_Prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("{} is not prime number".format(num))
                break
        else:
            print("{} is prime number".format(num))
    else:
        print("{} is not prime number".format(num))


num = int(input("Enter a number(checking prime no.):"))
Check_Prime(num)

# Program to print the prime number in an interval


def prime_no_in_range(lower_no, upper_no):
    for number in range(lower_no, upper_no+1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)


lower_no, upper_no = input("Enter two number(lower and upper range):").split()
prime_no_in_range(int(lower_no), int(upper_no))


# Program to find factorial of a number
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    elif x <= 0:
        print("Enter A Valid number")
    else:
        return (x * factorial(x-1))


num = int(input("Enter A Number(for factorial):"))
print("The factorial of", num, "is", factorial(num))


# Program to print the fibonacci sequence using while loop
def fibonacci_series(no_of_terms):
    num1, num2 = 0, 1
    count = 0
    if no_of_terms <= 0:
        print("please enter positive number")
    elif no_of_terms == 1:
        print("fibonacci series upto ", no_of_terms, "is: ")
        print(num1)
    else:
        print("fibonacci series upto ", no_of_terms, "is: ")
        while count < no_of_terms:
            print(num1)
            num = num1 + num2
            num1 = num2
            num2 = num
            count += 1


no_of_terms = int(input("Enter no. of terms(for fibonacci series): "))
fibonacci_series(no_of_terms)


# Program to print fibonacci series using for loop
def fibonacci_series_for_loop(noOfTerms):
    fibonacciSeries = [0, 1]

    if noOfTerms <= 0:
        print("please enter positive number")
    elif noOfTerms == 1:
        print(fibonacciSeries[0])
    elif noOfTerms == 2:
        print(fibonacciSeries)
    else:
        for i in range(2, noOfTerms):
            nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
            fibonacciSeries.append(nextElement)
        print(fibonacciSeries)


noOfTerms = int(input("Enter no. of terms(for fibonacci series): "))
fibonacci_series_for_loop(noOfTerms)


# Program to find the sum of natural number using while loop by
# decrementing the update condition
def Sum_natural_no(no_of_terms):
    sum = 0
    if no_of_terms <= 0:
        print("Enter the whole positive number")
    else:
        while no_of_terms > 0:
            sum = sum + no_of_terms
            no_of_terms = no_of_terms - 1
        print("Sum of natural number is : ", sum)


no_of_terms = int(input("Enter number of terms for sum of natural no: "))
Sum_natural_no(no_of_terms)


# Program to find the sum of natural number by using
# while loop and update condition in incrementing way
def Sum_natural_no1(no_of_terms):
    sum = 0
    count = 1

    if no_of_terms <= 0:
        print("Enter the whole positive no.")
    else:
        while count <= no_of_terms:
            sum = sum + count
            count = count + 1
        print("Sum of natural no. is: ", sum)


no_of_terms = int(input("Enter number of terms for sum of natural no: "))
Sum_natural_no1(no_of_terms)


# Program to find the sum of natural no. using the formula
def Sum_natural_no_by_formula(n):
    if (n % 2) == 0:
        # for even no.
        return (n / 2) * (n + 1)
    else:
        # for odd no.
        return ((n + 1) / 2) * n


n = int(input("Enter the no. of terms for sum of natural no.: "))
print(Sum_natural_no_by_formula(n))
