temp = { '1': '124', '2':'1235', '3':'236', '4':'1457', '5':'24568','6': '3569', '7':'478', '8':'57890', '9':'689', '0':'08'}
def get_pins(observed):
 if observed == []:
    return []
 if len(observed)>1:
    ans = []
    t = temp[observed[0]]
    for x in t:
        for i in get_pins(observed[1:]):
            ans.append(x+i)
    return ans 
 else: 
    return  temp[observed[0]]