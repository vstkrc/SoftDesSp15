class DNASequence(object):
    """ Represents a sequence of DNA """
    def __init__(self, nucleotides):
        """ constructs a DNASequence with the specified nucleotides.
             nucleotides: the nucleotides represented as a string of
                          capital letters consisting of A's, C's, G's, and T's """
        self.nucleotides = nucleotides
 
    def __str__(self):
        """ Returns a string containing the nucleotides in the DNASequence
        >>> seq = DNASequence("TTTGCC")
        >>> print seq
        TTTGCC
        """
        return self.nucleotides

    def get_reverse_complement(self):
        """ Returns the reverse complement DNA sequence represented
            as an object of type DNASequence

            >>> seq = DNASequence("ATGC")
            >>> rev = seq.get_reverse_complement()
            >>> print rev
            GCAT
            >>> print type(rev)
            <class '__main__.DNASequence'>
        """
        res = ""
        for nuc in self.nucleotides:
            if nuc == "A":
                res += "T"
            elif nuc == "T":
                res += "A"
            elif nuc == "C":
                res += "G"
            elif nuc == "G":
                res += "C"
        return DNASequence(res[::-1])

    def get_proportion_ACGT(self):
        """ Computes the proportion of nucleotides in the DNA sequence
            that are 'A', 'C', 'G', and 'T'
            returns: a dictionary where each key is a nucleotide and the
                corresponding value is the proportion of nucleotides in the
            DNA sequence that are that nucleotide.
            (NOTE: this doctest will not necessarily always pass due to key
                    re-ordering don't worry about matching the order)
        >>> seq = DNASequence("AAGAGCGCTA")
        >>> d = seq.get_proportion_ACGT()
        >>> print (d['A'], d['C'], d['G'], d['T'])
        (0.4, 0.2, 0.3, 0.1)
        """
        cnt_A = 0.0
        cnt_C = 0.0
        cnt_G = 0.0
        cnt_T = 0.0
        total = len(self.nucleotides)

        for nuc in self.nucleotides:
            if nuc == "A":
                cnt_A += 1
            elif nuc == "C":
                cnt_C += 1
            elif nuc == "G":
                cnt_G += 1
            elif nuc == "T":
                cnt_T += 1

        return {"A": cnt_A/total, "C": cnt_C/total, "G": cnt_G/total, "T": cnt_T/total}
if __name__ == '__main__':
    import doctest
    doctest.testmod()
