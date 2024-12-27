def pro_of_digit(num):
    pro=1
    while(num!=0):
        rem=num%10
        pro=pro*rem
        num=num//10
    return pro

num=int(input("Enter a number\n"))
print("Product of digits of the number is",pro_of_digit(num))
