def disemvowel(string_):
    str='aeiouAEIOU'
    ans=''
    for x in string_:
        if str.count(x) != 1:
            ans+=x
    return ans