def bin_to_dec(num):
    return int(str(num), 2)

def dec_to_bin(num):
    return bin(num)[2:]

print(bin_to_dec(1111))
print(dec_to_bin(15))