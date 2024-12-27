def rem_vow(str):
    vowels="aeiouAEIOU"
    ans=" "
    for i in str:
        if(i not in vowels):
            ans=ans+i
    return ans

print(rem_vow("Hello World"))