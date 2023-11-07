def count_developers(lst):
    res=0
    for x in lst:
        if x['continent']=='Europe' and x['language']=='JavaScript':
            res+=1
    return res