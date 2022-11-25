import const
import math as m
import math_functions as mf
import numpy as np
import methods as meth


def gen_x_dots(a,b,n):
    eps = (b-a)/n
    res = []
    for i in range(n+1):
        res.append(a+eps*i)
    return res

def get_method_result(a,b,n,function,method):
    res = 0
    dots = gen_x_dots(a,b,n)
    for i in range(n):
        res+=method(dots[i],dots[i+1],function)
    return res

def get_result(a,b,fun,n):
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
    
    symps = get_method_result(a,b,n,math_func,meth.sympson)
    t_e = get_method_result(a,b,n,math_func,meth.three_eight)
    f_d = get_method_result(a,b,n,math_func,meth.five_dots)

    res[0].append(symps)
    res[0].append(t_e)
    res[0].append(f_d)
    res[0].append(current)
    res[1].append(np.abs(current - symps)/current*100)
    res[1].append(np.abs(current - t_e)/current*100)
    res[1].append(np.abs(current - f_d)/current*100)
    res[1].append(np.abs(current - current)/current*100)
    return res