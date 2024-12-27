def nthfib(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a,b=0,1
        for i in range(n-2):
            a,b=b,a+b
        return b
    
print(nthfib(5))
            