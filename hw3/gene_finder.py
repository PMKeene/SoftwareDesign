# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Maire Keene
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle

def get_complementary_base(b):
    """Returns the complementary base nucleotide 
    b: the base represented as a length 1 string
    returns: complementary base represented as a length 1 string"""
    if b=='A':
        return 'T'
    elif b=='T':
        return 'A'
    elif b=='C':
        return 'G'
    elif b=='G':
        return 'C'
    else:
        print 'ERROR: Check String Input'

        #Good modularization

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    x=0    
    proteins=''
    while x < len(dna): #Why is this a while? Its fine, but consider using a for loop with a 3rd argument to range (stepsize)
        #chunk the dna
        codon=dna[x:x+3]
        for i in range(len(codons)):
            #then check each chunk as you make it for a match in the list of actual codons
           for j in range(len(codons[i])):
               #and check all the elements of the sub-lists
               if codon==codons[i][j]:
                   #then find the protein that is associated with that codon and stick it in a list of coded amino acids
                  proteins = proteins+ aa[i]
                        #+= works too
        x=x+3
    return proteins

    #Cleanly written, and excellent documentation

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    sequence='AGTCTTGAT'
    print 'input:'+str(sequence)+', expected output: '+'SLD'
    print 'actual output:'+str(coding_strand_to_AA(sequence))
    sequence='ATGCCCGCTTT'
    print 'input:'+str(sequence)+', expected output: '+'MPA'
    print 'actual output:'+str(coding_strand_to_AA(sequence))
    sequence='CCGCGTTCA'
    print 'input:'+str(sequence)+', expected output: '+'PRS'
    print 'actual output:'+str(coding_strand_to_AA(sequence))

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    comp=[]
    rev=''
    #make a list of the sumplementary bases
    for b in dna:   # Beautiful
        comp.append(get_complementary_base(b))
    #turn those back into a string
    for c in comp: # Try ''.join() it does exactly this
        rev=rev+str(c)
    #that is then returned backwards
    return rev[::-1]    # Equally beautiful
   
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    sequence='AGTCTTGAT'
    print 'input:'+str(sequence)+', expected output: '+'ATCAAGACT'
    print 'actual output:'+str(get_reverse_complement(sequence))
    sequence='ATGCCCGCTTT'
    print 'input:'+str(sequence)+', expected output: '+'AAAGCGGGCAT'
    print 'actual output:'+str(get_reverse_complement(sequence))
    sequence='CCGCGTTCA'
    print 'input:'+str(sequence)+', expected output: '+'TGAACGCGG'
    print 'actual output:'+str(get_reverse_complement(sequence)) 

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    x=0    
    ORF=''
    #chunk the dna as before
    while x < len(dna):
        codon=dna[x:x+3]
        #if its a stop codon whatever has been compiled so far will be returned without the stop
        if (codon=='TAG') or (codon=='TAA') or (codon=='TGA'): #This is great. Just FYI, you can save words with "if codon in ['TAG','TAA','TGA']:"
            return ORF
        #and if it's just a normal codon it gets stuck on the end of our ORF
        else:
            ORF = ORF + codon
            #and check the next chunk (we want non-nested)
            x=x+3
    return ORF
    

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    sequence='ATGTGAA'
    print 'input:'+str(sequence)+', expected output: '+'ATG'
    print 'actual output:'+str(rest_of_ORF(sequence))
    sequence='ATGAGATAGG'
    print 'input:'+str(sequence)+', expected output: '+'ATGAGA'
    print 'actual output:'+str(rest_of_ORF(sequence))
    sequence='ATGCCCCCCCCCTAA'
    print 'input:'+str(sequence)+', expected output: '+'ATGCCCCCCCCC'
    print 'actual output:'+str(rest_of_ORF(sequence)) 
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    x=0    
    AllORFs=[]
    while x < len(dna):
        #chunk the dna
        codon=dna[x:x+3]
        #if its the start of something, get me the rest of that
        if (codon=='ATG') :
            ORF=rest_of_ORF(dna[x:]) 
            #then stick it in my list, and begin looking for the next ORF where this one left off
            AllORFs.append(ORF)
            x=x+len(ORF)
        else:
            #...or just keep looking for that ATG
            x=x+3
    return AllORFs 
        
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    sequence='ATGCATGAATGTAGATAGATGTGCCC'
    print 'input:'+str(sequence)+', expected output: '+"['ATGCATGAATGTAGA'"+",'ATGTGCCC']"
    print 'actual output:', rest_of_ORF(sequence)
    sequence='ATGAGATAGG'
    print 'input:'+str(sequence)+', expected output: '+"['ATGAGA']"
    print 'actual output:', rest_of_ORF(sequence)
    

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    CompiledFramesORFs=[]
    for i in range(3): 
        #beginning with how we would normally read it, get me all the ORFs, store
        #then start reading 1 base later and tell me what you find, store
        #and for the complete list, one more shift
         offset=i
         FrameORF=find_all_ORFs_oneframe(dna[offset:]) #You could just use [i:], saves a line
         CompiledFramesORFs += FrameORF
    return CompiledFramesORFs 

    #Hmm, I appreciate that you chose to do this function in a scalable manner

    
def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    sequence='ATGCATGAATGTAG'
    print 'input:'+str(sequence)+', expected output: '+"['ATGCATGAATGTAG'"+",'ATGAATGTAG'"+"'ATG']"
    print 'actual output:', find_all_ORFs(sequence)
    sequence='ATGAGATAGG'
    print 'input:'+str(sequence)+', expected output: '+"['ATGAGA']"
    print 'actual output:', find_all_ORFs(sequence)

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    #the other side of this dna strand
    dna2=get_reverse_complement(dna)
    #now a list added to a list of all the ORFs for each of these strands
    return find_all_ORFs(dna)+find_all_ORFs(dna2) #Good stuff.
    

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    sequence='ATGCGAATGTAGCATCAAA'
    print 'input:'+str(sequence)+', expected output: '+"['ATGCGAATG'"+"'ATGCTACATTCGCAT']"
    print 'actual output:', find_all_ORFs_both_strands(sequence)
    sequence='ATGAGATAGG'
    print 'input:'+str(sequence)+', expected output: '+"['ATGAGA']"
    print 'actual output:', find_all_ORFs_both_strands(sequence)

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    #EVERYTHING we can find, but only tell me the longest one (hence key=len)
    AllTheORFs=find_all_ORFs_both_strands(dna)
    return max(AllTheORFs,key=len) #Great. Also, if max is this short, just nest function calls and 
                                    #turn this function into one line.
    

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """
    
    sequence="ATGCGAATGTAGCATCAAA"
    print 'input:'+str(sequence)+', expected output: '+"ATGCTACATTCGCAT"
    print 'actual output:', longest_ORF(sequence)
    sequence='ATGCATGAATGTAG'
    print 'input:'+str(sequence)+', expected output: '+"ATGCATGAATGTAG"
    print 'actual output:', longest_ORF(sequence)
    

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
#list.shuffle does not seem to be a thing according to what I found on the web
#but there is a shuffle in random, so I'm doing that
#Good decision

    Champions=[]
    #we want to do this num_trials amount of times
    for i in range(num_trials):
        #conversion, shuffle, and re-conversion
        dna=list(dna)
        shuffle(dna)
        dna=collapse(dna)
        #what's the longest random ORF
        winner=longest_ORF(dna)
        #add to hall of fame 
        Champions=Champions + [winner]
        #now tell me who the best of the best are
    return len(max(Champions,key=len))

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    Candidates=find_all_ORFs_both_strands(dna)
    QualifiedProteins=[]
    #checking each ORF
    for i in range(len(Candidates)):
        # only if they're long enough do we care about their AA translation
        if len(Candidates[i]) >threshold:
            AcidString=coding_strand_to_AA(Candidates[i])
            #and so keep track of all the proteins of sufficient length
            QualifiedProteins+=[AcidString]
    return QualifiedProteins

   
if __name__ == "__main__": 
    print "hello friendly NINJA" #Tryna butter up the Ninjas, eh? 