def duplicate_encode(word):
    ans=''
    word=word.lower()
    for i in word:
        if word.count(i) > 1:
            ans+=')'
        else:
            ans+='('
    return ans