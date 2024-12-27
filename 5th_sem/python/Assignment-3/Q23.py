def idxvwl(str):
    vow="aeiouAEIOU"
    for idx,val in enumerate(str):
        if(val in vow):
            print(f"{idx}--->{val}")
            


idxvwl("Nabin")