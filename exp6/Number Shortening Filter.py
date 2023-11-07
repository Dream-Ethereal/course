def shorten_number(suffixes, base):
    def process(Str):
        if type(Str) != str or Str.isdigit() == False:
            return str(Str)
        count=0
        temp=int(Str)
        while temp//base >0 and count+1<len(suffixes):
            temp=temp//base
            count+=1
        return str(temp)+suffixes[count]
    return process