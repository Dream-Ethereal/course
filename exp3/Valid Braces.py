def valid_braces(string):  
    flag = 0  
    temp = ''  
    for x in string:  
        if x == '(':  
            temp += '('  
        elif x == '{':  
            temp += '{'  
        elif x == '[':  
            temp += '['  
        elif x == ')':  
            if temp=='' or temp[-1] != '(':  
                flag = 1  
            else:  
                temp = temp[:-1]  
        elif x == '}':  
            if temp=='' or temp[-1] != '{':  
                flag = 1  
            else:  
                temp = temp[:-1]  
        elif x == ']':
            if temp=='' or temp[-1] != '[':  
                flag = 1  
            else:  
                temp = temp[:-1]  
    if flag == 1:  
        return False  
    elif temp == '':
        return True  
    else:  
        return False