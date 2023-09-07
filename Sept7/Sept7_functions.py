
def fib(n):
    """
    A function that calculates the first n number of the Fibonacci sequence

    Inputs:
        n: number of Fibonacci numbers to calculate

    """
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a+b
    return a    # return the last number in the sequence

