import math

def cal_rectangle_perimeter(a, b):
    return 2*(a + b)

def cal_circle_area(r):
    return math.pi * pow(r, 2)

if __name__ == '__main__':
    f = int(input("choose function: \n\
        0. cal_rectangle_perimeter \n\
        1. cal_circle_area \n\
        Please enter an integer: "))

    mult = int(input("Add multiplier: "))

    if f == 0:
        a = int(input("Input value a: "))
        b = int(input("Input value b: "))
        result = cal_rectangle_perimeter(a, b)

    elif f == 1:
        r = int(input("Input value r: "))
        result = cal_circle_area(r)

    else:
        result = "Wrong input"
    print(f"\nResult: {result * mult}")