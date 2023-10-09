def solution(number):
    sum=0
    if number<0:
        return 0
    for i in range(0,number):
        if i%3==0:
            sum=sum+i
        elif i%5==0:
            sum=sum+i
    return sum
