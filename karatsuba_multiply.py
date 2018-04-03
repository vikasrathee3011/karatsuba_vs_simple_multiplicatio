import timeit
import math
#loading math and time module

start_time = timeit.default_timer()
# creating a start time count down initilise to 0

def karatsuba_multiplication(nu1,nu2):          #defining a function
    num1 = str(nu1)                             #converting inteager into string because object of type inteager has no lenght
    num2 = str(nu2)
    x = len(num1)
    y = len(num2)

    if x == 1 or y == 1:
        print('----result----',nu1*nu2)
    else:
        if x >= y:
            n = x
        else:
            n = y
        if n % 2 == 0:
            n  = n
        else:
            n = n + 1
        a = int(num1[0:math.floor(x/2)])        #slicing the numbers for multiplication
        b = int(num1[math.ceil(x/2):x])
        c = int(num2[0:math.floor(y/2)])
        d = int(num2[math.ceil(y/2):y])
        print('----reslut----',int((10**n)*(a*c) + (10**(n/2))*(a*d + b*c) + b*d))  #formula of karatsuba

karatsuba_multiplication(9,1234)
karatsuba_multiplication(7,12345)
karatsuba_multiplication(213,1234)
karatsuba_multiplication(1234,5678)
karatsuba_multiplication(12345,987)
karatsuba_multiplication(3141592653589793238462643383279502884197169399375105820974944592
,2718281828459045235360287471352662497757247093699959574966967627)

stop = timeit.default_timer()                   #countdown ends here
print('program time--',stop)
