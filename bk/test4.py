from sympy import Symbol, sympify, simplify, pprint, expand, Poly, solve
from control import *
import matplotlib.pyplot as plt
from functools import reduce

if __name__ == '__main__':
    s = Symbol('s')
    u = Symbol('u')
    # expr1 = input("please input the zero part of the function:")
    expr1 = 80
    # expr1 = s**2 + 2 * s + 3
    expr1 = sympify(expr1)
    # expr2 = input("please input the pole part of the function:")
    expr2 = (1 + 10 * s) * (1 + s) * (1 + 5 * s)*s
    # expr2 = (1 + s) ** 2
    expr2 = sympify(expr2)
    a = solve(6 / (1 + u * 3 - 9) - 0.1, u)
    u = int(a[0] + 3)
    print("u:", u)
    expr = expr1 / expr2
    print("the initial transfer function:")
    pprint(expr)

    sy1 = Poly(expr1, s).all_coeffs()
    sy2 = Poly(expr2, s).all_coeffs()

    # condition_phs = input("please input the phase limitation: ")
    # condition_w = input("please input the frequency limitation:")

    condition_phs = 60
    condition_w = 0.3

    a = list(map(int, sy1))
    b = list(map(int, sy2))
    sys_tf = tf(a, b)

    sys = ss(sys_tf)
    print("sys:", sys_tf)
    gm, pm, wg, wp = margin(sys)

    print("gm: ", gm)
    print("pm: ", pm)
    print("wg: ", wg)
    print("wp: ", wp)

    poles = pole(sys)
    print(poles)

    plt.figure(1)
    bode(sys)

    mag, phase, omega = freqresp(sys, [condition_w])
    if phase[0][0][0] > 0:
        print("phase margin at condition_w: ", phase[0][0][0] / 3.1415926 * 180 - 360 + 180, mag, phase, omega)
    else:
        print("phase margin at condition_w: ", phase[0][0][0] / 3.1415926 * 180 + 180, mag, phase, omega)

    1-1/poles[-1]*s

    # if



    # # TODO:比较得到的与条件
    # if wp < condition_w or pm < condition_phs:
    #     wl = -poles[0]
    #     # print(abs(1/reduce(lambda x, y: x * y, poles)))
    #     wh = (-30*poles[-1])
    #     print("wh: ", wh)
    #     expr3 = (1 + s / wl) * pow((1 + s / wh), len(poles) - 1)
    #     print("expr3: ", expr3)
    #     expr4 = expr1/expr3
    #     sy3 = Poly(expr3, s).all_coeffs()
    #     c = list(map(int, sy3))
    #     sys_tf = tf(a, c)
    #     sys = ss(sys_tf)
    #     gm, pm, wg, wp = margin(sys)
    #
    #     print("pm: ", pm)
    #     print("wp: ", wp)
    #     plt.figure(2)
    #     bode(sys)
    plt.show()