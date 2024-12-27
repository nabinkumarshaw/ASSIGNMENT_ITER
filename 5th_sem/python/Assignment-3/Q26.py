import string
def rmvvow(str):
    vow="aeiouAEIOU"
    return "".join([i if i not in vow else 'k' for i in str])

print(rmvvow("Hello how,you are now"))