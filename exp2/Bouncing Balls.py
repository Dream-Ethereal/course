def bouncing_ball(h, bounce, window):
    if h<=0 or bounce <=0 or bounce >=1 or window >=h: 
        return -1
    ans=1
    while True:
        h=h*bounce
        if h<=window:
            break
        else:
            ans+=2
    return ans