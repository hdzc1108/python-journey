#一元二次方程计算器
import math
a = float(input ('enter number a:'))
b = float(input ('enter number b:'))
c = float(input ('enter number c:'))
if a == 0:
    if b == 0:
        print ('此方程错误')
    else:
        x = - c / b
        print ('x=',x)
else:
    delta = b ** 2 - 4 * a * c
    if delta >= 0:
        x_one = (-b + math.sqrt(delta)) / (2 * a)
        x_two = (-b - math.sqrt(delta)) / (2 * a)
        print('x1=', x_one)
        print('x2=', x_two)
    else:
        print('该方程在实数范围内无解')