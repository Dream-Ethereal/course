def find_outlier(integers):
    flag=0
    if((integers[-1]+integers[-2])%2==1 and (integers[-3]+integers[-2])%2==0):
        return (integers[-1]) 
    if((integers[0]+integers[1])%2==1 and (integers[1]+integers[2])%2==0):
        return (integers[0]) 
    for i in range(0,len(integers)-1):
        if((integers[i]+integers[i+1])%2==1):
            if(flag==1):
                return (integers[i]) 
            flag=1