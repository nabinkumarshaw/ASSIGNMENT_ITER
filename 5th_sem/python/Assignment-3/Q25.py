def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def co_prime(a,b):
    return gcd(a,b)==1

print(co_prime(8,15))