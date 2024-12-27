def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum

num=60
if(num==perfect(num)):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")