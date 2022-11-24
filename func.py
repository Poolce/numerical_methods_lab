import const
import math as m
import math_functions as mf

def get_result(a,b,fun):
    res = []
    math_func = None
    if(fun == 'sin(x)'):
        math_func = mf.sin
    if(fun == 'cos^2(x)'):
        math_func = mf.cos_2
    if(fun == '3*(x^4)'):
        math_func = mf.x_4_3
    if(fun == 'x^3'):
        math_func = mf.x_3
    if(fun == 'cos(x)'):
        math_func = mf.cos
    if(fun == 'x^2'):
        math_func = mf.x_2
    
    dots = gen_dots(a,b,math_func)
    res.append(sympson(dots))
    res.append(three_eight(dots))
    res.append(five_dots(dots))
    return res


def foo(x):
    return m.pow(x,2)+1

def gen_dots(a,b,function):
    x = a
    dots = [[],[]]
    while x<b:
        y = function(x)
        dots[0].append(x)
        dots[1].append(y)
        x+=const.eps
    return dots

def sympson(arr):
    sum = 0
    for i in range(len(arr[0])-2):
        sum += arr[1][i]+4*arr[1][i+1]+arr[1][i+2]
    return sum*const.eps/6


def three_eight(arr):
    sum = 0
    for i in range(len(arr[0])-3):
        sum += arr[1][i]+3*arr[1][i+1]+3*arr[1][i+2]+arr[1][i+3]
    return sum*const.eps/8

def five_dots(arr):
    sum = 0
    for i in range(len(arr[0])-4):
        sum += arr[1][i]+4*arr[1][i+1]+6*arr[1][i+2]+4*arr[1][i+3]+arr[1][i+4]
    return sum*const.eps/16
