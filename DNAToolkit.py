#DNA toolkit.file
nucleotides = ['A','T','C','G']
def validateseq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq
    
    
def countnucfrequency(seq):
    tmpFreqDict = {"A": 0, "T" : 0, "C" : 0, "G" : 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1 
    return tmpFreqDict
    
    
def dnasecondstring(dnaseq):
    DNAstr = str()
    for nuc in dnaseq:
        if nuc == 'A':
            DNAstr += 'T'
        if nuc == 'T':
            DNAstr += 'A'
        if nuc == 'C':
            DNAstr += 'G'
        if nuc == 'G':
            DNAstr += 'C'
    return DNAstr
    
    
def dnatranscription(dnaseq):
    RNAstr = str()
    for nuc in dnaseq:
        if nuc == 'A':
            RNAstr += 'U'
        if nuc == 'T':
            RNAstr += 'A'
        if nuc == 'C':
            RNAstr += 'G'
        if nuc == 'G':
            RNAstr += 'C'
    return RNAstr
    
    
#def proteinsynthesis(rnaseq):
    

    
            

