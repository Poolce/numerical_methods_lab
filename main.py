import math as m
import func
import const


def main():
    x = const._a
    dots = func.gen_dots(func.foo)

    sympson_result = func.sympson(dots)
    sthree_eight_result = func.three_eight(dots)
    five_dots_result = func.five_dots(dots)

    print(sympson_result)
    print(sthree_eight_result)
    print(five_dots_result)
    print(int("5+2"))




        

if __name__ == '__main__':
    main()