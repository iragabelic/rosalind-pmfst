def comp(a, b):
  kmers = []
  for i in range(len(a) - (b - 1)):
    kmers.append(a[i:i+b])
  for k in kmers:
    print(k)

comp("AGGCTGGTGACCACCTTCTCACCAAGTTCCGGGTCCGTAGAGTTTGAGTGATGTACCACAAATTTGTTATAGGCAATTCGCAAACACCAACGGCTCCCGTAGATATTCACCCTGAAGTAGTGGCGGCGGGTTAGGCAAAAATGTTCTACTATCACAGTGATCTGCAACTTATGAGTATCTCGTAAAGACGGAACAGCGGACGTCGTTAGAGCTGACACAGGTTAATGAGGACTTACCTGTGAGTAATCGGTATATCAATTCTAGTGCACATCGGACGGTGATCCCTCAACTTTTTATAGAGTATGGATCAGCGACTTGCTTATTTTTGAGTCTGAGTGGAGCGTCAAAGGGCTTCCTTTTCCTGGTGCCTTAAAACACAAATCTTCAGAGGCTATGGCGGCGCGGTTGACTGACCAGGCCCCACTGCCATGATTCCCGGGTATTTGAATAGATCACGGTGAAAGACGGTCTGCGAATGTTAGTGCACTCGATTTCTTGAGACCCCGAGCGCGTCAGGCTCCCGAATTTTCGAAGAGATAAGTTTAAAGTCACTTACCGCACGGCTCTGTGCCTATTATGCGTGGTGAAATCAACAGTGGGGGGTTCGACCTTTTGACGCTACTGTTGAACTAGGGTGGGACTCCCGAGCTTTCTCAAAGCGAAACAGCCTGAGGCCATAGCAGCAAGCATCAATACCAACAAATGACCAGTTAGAACGATGGAGACGCCCAGCATGATCCCTTTCATGCTTATCACTCTATGCCCTTGGACGCGTAGACATACTGTGGCGGATTATGTCAACATCTCAGGTGGCTCTCACTGTGCTGGCGATGATTTAGCAGGTTAGCGCTAACGAGCCTTCCGTTGGACGAGGCCGCACAACGGAAACGATAACCTCACTGCTCATGCACAGGGAGAAAGCGCTTTATTGTCCTCGAAGATACAGGTTTTAAATATCCCATGATTTTGATGTTGACCAAGGCTTCGATGTGTTGAATGA", 50)
