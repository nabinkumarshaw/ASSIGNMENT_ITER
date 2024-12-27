def numbers():
    li=[]
    for i in range(100,500):
        if i % 3 == 0 and i % 5 == 0:
            li.append(i)
    print(li)
    
numbers()