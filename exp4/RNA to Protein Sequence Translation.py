def protein(rna):
    i=0
    ans=''
    for i in range(0,len(rna)-1,3):
        if PROTEIN_DICT[rna[i:i+3]] != 'Stop':
            ans=ans+PROTEIN_DICT[rna[i:i+3]]
        else:
            break
    return ans