def shift_one(str):
    result=[]
    for i in str:
        if i == 'z':
            result.append('a')
        else:
           result.append(chr(ord(i)+1))
            
    return "".join(result)

print(shift_one("nabin"))