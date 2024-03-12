

import math


print('Lets solve a quadratic equation\n')

#Getting values of a,b, and c
a = input('for ax^2+bx+c, specify the value of a:')
b = input('for ax^2+bx+c, specify the value of b:')
c = input('for ax^2+bx+c, specify the value of c:')



#Describing Variables

negative_b = int(-1)*int(b)
print("Value of -1*b: " + str(negative_b))

b_square = int(b)*int(b)
print("Value of b squared: " + str(b_square))


four_ac = int(-4)*int(a)*int(c)
print("Value of -4*a*c: " + str(four_ac))


two_a = int(2)*float(a)
print("Value of 2*a: " + str(two_a))


bsq_4ac = int(b_square+four_ac)
print("Value of b^2-4ac: " + str(bsq_4ac))

if(bsq_4ac<0):
    print('There is no solution to this quadratic equation')
    exit(-1)


square_root = math.sqrt(int(b_square+four_ac))
print("Value of b squared minus 4*a*c: "+str(square_root))

#Describing the roots
root_one= (negative_b - square_root)/two_a
print("Your first x intercept is: "+ str(root_one))

root_two= (negative_b + square_root)/two_a
print("Your second x intercept is: " + str(root_two))