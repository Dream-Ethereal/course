def is_pangram(s):
    s=s.lower()
    dic={}
    flag=0
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for x in range(0,26):
        if chr(x+97) not in dic:
            return False
    return True