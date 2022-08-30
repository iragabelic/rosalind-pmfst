from itertools import product
def freq(dna, k):
    kmers = []
    svi = [''.join(i) for i in product('ACGT', repeat = k)]
    rez = [0] * len(svi)
    for i in range(len(dna) - (k - 1)):
        kmers.append(dna[i:i+ k])      
      
    for j in range(len(kmers)):
      ind = svi.index(kmers[j])
      rez[ind] += 1
    for r in rez:
        print(r, end=' ')

freq("""GTTATAATATCTGGCCCTCAGTAGAGATGTCTTAAAACGCGAGCATGCGGCTGTCTTCTCTCGTTCTACAAGAGAAAACGTCGTTAGACGCTTGGGCTCCGCTGCGATAGGCTTGTTTTTACTCCCTCGCCCAGCGCTTAGCAGACTAACCTCTGGAAACTGAGACGGGGAGCCCTACTGCTCGCCGATCGGAAAAATGTATTCAGAACGCTACGATTCCCTTATGCACATACTCGGTTAATAACCCGATTGACGGCGGAATAGAAGAGACTTTAACTAGCATGGGGGGACCCAGGAGAATCAAACCCGCGCGTCCAGCTACCGCCAAGTCGGCACTAACATTGCGACAATCGACGACTCGAAAGACTACCAAGGTTCCTCTAGTCCGTCGGTCAACCTTGGGTATCTGTACTGCCGGAACGTATAACGCCTATACGAGAATTTACTACATACTCATAAAATGCCGTATGGCTTTTACTTAACACCAGCAAACCTTCGGCAAGCTCTGCGGCCAATGATTTTACGTATAGAATCTAGTCGCCTAGCAAATTTGTACCCAGCTTGGGCGGGCAGGTTAAAACAGTCGTTTCCAGTTAGTTGGGGCATGCCATAGAAATATCACCAGGATGCAAACTGCACCACAAAAGGTGGTGGAAATTACAAGTGACACCTGAGAAGAGTCGATGTG""", 5)
