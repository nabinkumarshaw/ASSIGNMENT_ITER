def add():
    sum=0
    for i in range(1,51):
        if(i%2==0):
            sum+=i*i
    return sum

print(add())