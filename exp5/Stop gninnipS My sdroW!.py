def spin_words(sentence):
    ans=''
    flag=0
    sentence=sentence.split()
    for x in sentence:
        if(flag==1):
                ans+=' '
        if len(x)>=5:
            ans=ans+x[::-1]
            flag=1
        else:
            ans+=x
            flag=1
    return ans
