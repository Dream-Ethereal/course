def find_senior(lst): 
    max_age=-1
    list_ans=[]
    for x in lst:
        if x['age'] > max_age:
            max_age=x['age']
    for x in lst:
        if x['age'] == max_age:
            list_ans.append(x)
    return list_ans