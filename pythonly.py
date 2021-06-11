"""
Made by Advaith Sai (@Qubisted)
In depth video on GitHub repos
This program is based on the Tribonacci Sequence
"""

# 1 - First we create a function to store 3 numbers in the sequence
def createRange(n):
    if (n == 0 or n == 1 or n == 2) :
        return 0
    elif (n == 3) :
        return 1
    else :
        return (createRange(n - 1) +
                createRange(n-2)+
                createRange(n-3))

# 2 - Now it's time to make a function to print it in order
def printRange(n) :
    for i in range(1, n):
        print(createRange(i), " ", end = "")

# 3 - Now let's add driver code to choose the sequence length
num = int(input("Input first N number to print in the sequence"))
n = num #assigning num value to N or else it causes problems
printRange(n)
