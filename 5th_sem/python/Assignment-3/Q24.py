import string
def rmvpun(str):
   return "".join([i for i in str if i not in string.punctuation])

print(rmvpun("Hello! how,you are now?"))