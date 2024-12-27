def count(num):
    c=0
    while num!=0:
        rem=num%10
        c+=1
        num=num//10
    return c

def armstrong(num):
    tot=0
    c=count(num)
    while(num!=0):
        rem=num%10
        tot+=rem**c
        num//=10
        
    return tot

num=1634
if(num==armstrong(num)):
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")