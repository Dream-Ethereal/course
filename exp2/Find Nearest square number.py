def nearest_sq(n):
    temp=n**0.5
    if abs((temp//1)**2-n)>abs((temp//1+1)**2-n):
        return (temp//1+1)**2
    elif abs((temp//1)**2-n)<abs((temp//1+1)**2-n):
        return (temp//1)**2
    else:
        return n;