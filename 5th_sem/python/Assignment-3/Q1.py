
def greatest(num):
    num_str=str(num)
    digits=[];
    for i in num_str:
        digits.append(int(i))
        digits.sort(reverse=True)
    print("1st largest",digits[0])
    print("2nd largest",digits[1])
    print("3rd largest",digits[2])
   
num=input("Enter a number\n")
greatest(num)

