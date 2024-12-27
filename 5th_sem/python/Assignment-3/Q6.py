def palindrom(str):
    return (str[::-1] == str)

str="abahfg"

if(palindrom(str)):
    print("It is a palindromic string")
else:
    print("It is not a palindrom string")