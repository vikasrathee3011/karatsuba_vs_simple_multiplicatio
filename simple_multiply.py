import timeit
start_time = timeit.default_timer()
def multiplication(A,B):
    nu1 = A
    nu2 = B
    num1 = str(nu1)
    num2 = str(nu2)
    print('----result----',int(num1)*int(num2))
multiplication(9,1234)
multiplication(7,12345)
multiplication(213,1234)
multiplication(1234,5678)
multiplication(12345,987)
multiplication(3141592653589793238462643383279502884197169399375105820974944592
,2718281828459045235360287471352662497757247093699959574966967627)
stop = timeit.default_timer()
print('program time--',stop)
