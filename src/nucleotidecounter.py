def countLetters(dna) :
    letters={'A':0, 'T':0, 'G':0, 'C':0}
    for c in dna :
        letters[c]+=1
    return letters
    
if __name__ == '__main__':
    print(countLetters("ATGCAATTGGCCA"))
