import const
import math as m

def foo(x):
    return m.pow(x,2)+1

def gen_dots(function):
    x = const._a
    dots = [[],[]]
    while x<const._b:
        y = function(x)
        dots[0].append(x)
        dots[1].append(y)
        x+=const.eps
    return dots

def sympson(arr):
    sum = 0
    for i in range(const.n-2):
        sum += arr[1][i]+4*arr[1][i+1]+arr[1][i+2]
    return sum*const.eps/6


def three_eight(arr):
    sum = 0
    for i in range(const.n-3):
        sum += arr[1][i]+3*arr[1][i+1]+3*arr[1][i+2]+arr[1][i+3]
    return sum*const.eps/8

def five_dots(arr):
    sum = 0
    for i in range(const.n-4):
        sum += arr[1][i]+4*arr[1][i+1]+6*arr[1][i+2]+4*arr[1][i+3]+arr[1][i+4]
    return sum*const.eps/16
