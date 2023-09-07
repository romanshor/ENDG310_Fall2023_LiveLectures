
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



def plot_ballistic_trajectory(v_0):
    """
    A function that plots the ballistic trajectory of a projectile

    Inputs:
        v_0: initial velocity of the projectile

    """
    import numpy as np
    import matplotlib.pyplot as plt

    g = 9.81
    t = np.linspace(0, 2*v_0/g, 100)
    y = v_0*t - 0.5*g*t**2

    plt.plot(t, y)
    plt.xlabel('time (s)')
    plt.ylabel('height (m)')
    plt.show()