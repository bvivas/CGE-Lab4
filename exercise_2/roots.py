"""
File: roots.py

Author:
    Miguel Garcia Gonzalez
    Belen Vivas Garcia

Computacion a Gran Escala - Practica 4
"""


import math


"""
Use quadratic expression:
    x = (-b +- sqrt(b²-4ac)) / 2a
"""
def quadratic1(a, b, c):
    
    x1 = (-b - math.sqrt((b**2) - (4*a*c))) / (2*a)
    x2 = (-b + math.sqrt((b**2) - (4*a*c))) / (2*a)

    return x1, x2


"""
Use quadratic expression:
    x = 2c / (-b +- sqrt(b²-4ac))
"""
def quadratic2(a, b, c):
    
    x1 = (2*c) / (-b + math.sqrt((b**2) - (4*a*c)))
    x2 = (2*c) / (-b - math.sqrt((b**2) - (4*a*c)))

    return x1, x2


"""
Use quadratic expression:
    q = (-1/2)(b+sign(b)sqrt(b²-4ac))
with roots:
    x1 = q/a
    x2 = c/q
"""
def quadratic3(a, b, c):
    
    # Sign of b
    sign = 0
    if(b > 0): sign = 1
    elif(b < 0): sign = -1
    else: sign = 0

    q = (-1/2)*(b + sign*math.sqrt((b**2) - (4*a*c)))

    x1 = q / a
    x2 = c / q

    return x1, x2


if __name__ == '__main__':

    a = -20
    b = 40300
    c = 10

    # Result of quadratic expression 1
    q1_x1, q1_x2 = quadratic1(a, b, c)
    print("Quadratic expression 1:\nx1 = {:.20f}\nx2 = {:.20f}".format(q1_x1, q1_x2))


    # Result of quadratic expression 2
    q2_x1, q2_x2 = quadratic2(a, b, c)
    print("Quadratic expression 2:\nx1 = {:.20f}\nx2 = {:.20f}".format(q2_x1, q2_x2))


    # Result of quadratic expression 3
    q3_x1, q3_x2 = quadratic3(a, b, c)
    print("Quadratic expression 3:\nx1 = {:.20f}\nx2 = {:.20f}".format(q3_x1, q3_x2))
