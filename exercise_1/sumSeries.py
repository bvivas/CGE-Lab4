"""
File: sumSeries.py

Author:
    Miguel Garcia Gonzalez
    Belen Vivas Garcia

Computacion a Gran Escala - Practica 4
"""


import math
import matplotlib.pyplot as plt


"""
Sum n first terms in ascending order
"""
def sumSeriesA(n):

    sum = 0
    for i in range(1, n+1):
        sum += 1 / (i ** 4)

    return sum


"""
Sum n first terms in descending order
"""
def sumSeriesD(n):

    sum = 0
    for i in range(n, 0, -1):
        sum += 1 / (i ** 4)

    return sum


"""
Private method to compute the real result of the series
"""
def __real_result():

    return ((math.pi) ** 4) / 90


"""
Private method to plot the difference between the ascending and descending values
"""
def __plot_diff_asc_desc(n):

    # Plot the difference between the ascending and descending values
    x_values = []
    y_values = []

    for i in range(1, n+1):
        y_values.append(abs(sumSeriesA(i) - sumSeriesD(i)))
        x_values.append(i)

    plt.plot(x_values, y_values)
    plt.title("DIFFERENCE BETWEEN ASCENDING AND DESCENDING VALUES")
    plt.xlabel("n")
    plt.ylabel("Difference")
    plt.savefig('plot/diff_asc_desc_{}.png'.format(n))
    plt.clf()


"""
Private method to plot the difference between each value and the real one
"""
def __plot_diff_real(n):

    res_real = __real_result()

    # Plot the difference between the ascending value and the real one
    x_values = []
    y_values = []

    for i in range(1, n+1):
        y_values.append(abs(sumSeriesA(i) - res_real))
        x_values.append(i)

    plt.plot(x_values, y_values)
    plt.title("DIFFERENCE BETWEEN ASCENDING AND REAL VALUE")
    plt.xlabel("n")
    plt.ylabel("Difference")
    plt.savefig('plot/diff_asc_real_{}.png'.format(n))
    plt.clf()

    # Plot the difference between the descending value and the real one
    x_values = []
    y_values = []

    for i in range(1, n+1):
        y_values.append(abs(sumSeriesD(i) - res_real))
        x_values.append(i)

    plt.plot(x_values, y_values)
    plt.title("DIFFERENCE BETWEEN DESCENDING AND REAL VALUE")
    plt.xlabel("n")
    plt.ylabel("Difference")
    plt.savefig('plot/diff_desc_real_{}.png'.format(n))
    plt.clf()


if __name__ == '__main__':

    n = 1000000

    # Result obtained in ascending order
    res_asc = sumSeriesA(n)
    print("{} first terms in ascending order: {:.20f}".format(n, res_asc))

    # Result obtained in descending order
    res_desc = sumSeriesD(n)
    print("{} first terms in descending order: {:.20f}".format(n, res_desc))

    # Real result
    res_real = __real_result()
    print("Real result: {:.20f}\n".format(res_real))

    # See which result is closer to the real one
    if(abs(res_real - res_asc) < abs(res_real - res_desc)):
        print("The ascending order result is closer to the real one\n")
    else:
        print("The descending order result is closer to the real one\n")

    # Find out the n value from which different results are obtained
    n_diff = 0
    for i in range(1, n):
        if(sumSeriesA(i) != sumSeriesD(i)):
            n_diff = i
            break

    print("n value from which different values are obtained: {}".format(n_diff))


    # Plot the difference between the two values with n=1000
    # __plot_diff_asc_desc(1000)

    # Plot the difference between the two values with n=10000
    # __plot_diff_asc_desc(10000)

    # Plot the difference between the two values with n=100000
    # __plot_diff_asc_desc(100000)

    # Plot the difference between the ascending value and the real one with n=100
    # __plot_diff_real(100)

    # Plot the difference between the ascending value and the real one with n=100
    # __plot_diff_real(20)
