def get_count(sentence):
    ans=0
    for value in sentence:
        if value=='a' or value=='e' or value=='i' or value=='o' or value=='u':
            ans+=1
    return ans