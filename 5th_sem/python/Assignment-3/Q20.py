def prime(num):
    flag=0
    for i in range(2,num):
        if(num % i==0):
            flag=1
            break
    
    if(flag==0):
        return 1
    else:
        return 0
    
num=100
for i in range(2,num+1):
    if(prime(i)):
        print(i,end=" ")