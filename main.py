#DNA toolset/code testing file
from DNAToolkit import *
import random
#nuccount = int(input('Insert the number of nucleotides of the DNA string: '))
rndstr = ''.join([random.choice(nucleotides)
    for nuc in range(200)])
print('-'*10,'Sequência de DNA','-'*10)
print(validateseq(rndstr))
print('-'*10,'Contagem de Nucleotídeos','-'*10)
print(countnucfrequency(rndstr))
print('-'*10,'Sequência de DNA secundária','-'*10)
print(dnasecondstring(rndstr))
print('-'*10,'Sequência de RNA Mensageiro','-'*10)
print(dnatranscription(rndstr))
rnastr = dnatranscription(rndstr)
print('-'*10,'Sequência de Aminoácidos','-'*10)
n = 3
rnastrdiv = [rnastr[i:i+n] for i in range(0, len(rnastr), n)]
aminoseq = list()
for k,v in enumerate(rnastrdiv):
    if v == 'AUG':
        del rnastrdiv[0:k]
        break
else:
    print("Sequência de RNA não possui códon de iniciação")
    exit()
for codon in rnastrdiv:
    if codon == 'AUG':
        aminoseq.append('Met')
    elif codon in ('GCU', 'GCG' , 'GCA', 'GCC'):
        aminoseq.append('Ala')
    elif codon in ('ACA', 'ACU', 'ACG', 'ACC'):
        aminoseq.append('Tre')
    elif codon in ('CCU', 'CCA', 'CCG', 'CCC'):
        aminoseq.append('Pro')
    elif codon in ('UCU' , 'UCA' , 'UCG' , 'UCC' , 'AGU' , 'AGC'):
        aminoseq.append('Ser')
    elif codon in ('GGU' , 'GGA' , 'GGC' , 'GGG'):
        aminoseq.append('Gli')
    elif codon in ('AUU' , 'AUC' , 'AUA'):
        aminoseq.append('Iso')
    elif codon in ('GUU' , 'GUA' , 'GUC' , 'GUG'):
        aminoseq.append('Val')
    elif codon in ('CUU' , 'CUA' , 'CUC' , 'CUG' , 'UUA' , 'UUG'):
        aminoseq.append('Leu')
    elif codon in ('GUU' , 'GUA' , 'GUC' , 'GUG'):
        aminoseq.append('Val')
    elif codon in ('GAU' , 'GAC'):
        aminoseq.append('Asp')
    elif codon in ('GAA' , 'GAG'):
        aminoseq.append('Glu')
    elif codon in ('AAU' , 'AAC'):
        aminoseq.append('Asn')
    elif codon in ('AAA' , 'AAG'):
        aminoseq.append('Lis')
    elif codon in ('CAU' , 'CAC'):
        aminoseq.append('His')
    elif codon in ('UAU' , 'UAC'):
        aminoseq.append('Tyr')
    elif codon in ('UUU' , 'UUC'):
        aminoseq.append('Phe')
    elif codon in ('UGU' , 'UGC'):
        aminoseq.append('Cys')
    elif codon in 'UGG':
        aminoseq.append('Trp')
    elif codon in ('CGU' , 'CGC' , 'CGA' , 'CGG' , 'AGA' , 'AGG'):
        aminoseq.append('Arg')
    elif codon in ('UAA' , 'UAG' , 'UGA'):
        break
for amino in aminoseq:
    print(amino,end='-')
        
    
    
    