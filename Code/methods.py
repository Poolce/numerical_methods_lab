def sympson(a,b,function):
    dots = gen_dots(a,b,2,function)
    res = dots[0]+4*dots[1]+dots[2]
    res*=(b-a)/6
    return res
    
def three_eight(a,b,function):
    dots = gen_dots(a,b,3,function)
    res = dots[0]+3*dots[1]+3*dots[2]+dots[3]
    res*=(b-a)/8
    return res

def five_dots(a,b,function):
    
    dots = gen_dots(a,b,4,function)
    res = 7*dots[0]+32*dots[1]+12*dots[2]+32*dots[3]+7*dots[4]
    res*=(b-a)/90
    return res

def gen_dots(a,b,n,function):
    eps = (b-a)/n
    dots = []
    for i in range(n+1):
        dots.append(function(a+eps*i))
    return dots