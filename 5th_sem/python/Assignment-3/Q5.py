def ndig(num):
    count=0
    while(num!=0):
        rem=num%10
        count+=1
        num//=10
    return count

print(ndig(125355))