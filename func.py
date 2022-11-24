import const
import math as m
import math_functions as mf
import numpy as np

def get_result(a,b,fun):
    res = [[],[]]
    current = None
    math_func = None
    if(fun == 'sin(x)'):
        math_func = mf.sin
        current = -m.cos(b)+m.cos(a)
    if(fun == 'cos^2(x)'):
        math_func = mf.cos_2
        current = (b/2)+(m.sin(2*b)/4)-(a/2)-(m.sin(2*a)/4)
    if(fun == '5*(x^4)'):
        math_func = mf.x_4_5
        current = m.pow(b,5)-m.pow(a,5)
    if(fun == 'x^3'):
        math_func = mf.x_3
        current = (m.pow(b,4)/4)-(m.pow(a,4)/4)
    if(fun == 'cos(x)'):
        math_func = mf.cos
        current = m.sin(b)-m.sin(a)
    if(fun == 'x^2'):
        math_func = mf.x_2
        current = (m.pow(b,3)-m.pow(a,3))/3
    
    dots = gen_dots(a,b,math_func)
    symps = sympson(dots)
    t_e = three_eight(dots)
    f_d = five_dots(dots)
    res[0].append(symps)
    res[0].append(t_e)
    res[0].append(f_d)
    res[0].append(current)
    res[1].append(np.abs(current - symps)/current*100)
    res[1].append(np.abs(current - t_e)/current*100)
    res[1].append(np.abs(current - f_d)/current*100)
    res[1].append(np.abs(current - current)/current*100)
    return res


def foo(x):
    return m.pow(x,2)+1

def gen_dots(a,b,function):
    x = a
    dots = [[],[]]
    while x<b+const.eps:
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
