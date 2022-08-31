def Clumps(dna, k, L, t):
    lista = []
    for i in range(len(dna)-L+1):
        for j in range(i,i+L-k):
            if(dna[i:i+L].count(dna[j:(j+k)]) == t):
                lista.append(dna[j:(j+k)])
    lista = set(lista)
    for l in lista:
        print(l, end=' ')
    return



Clumps("""GTGTGAAGACATTGTGGGTAGGTTACAATTGAATTGACTCAGGGTCAAGGAGATTTACCGGAAATTGATCCGATTTAGCAGGTGACCGCGGGGAGGGCGACATCCACCCCTCTGCAAGGTTTCTTTGTCGGATATCGGAGCTTAATGGTACATATATCGCTCGGTGTACACGAGAGAGCGGATGGAACTTATCTGGACAACGCGTTCAGACTCGTATAACGTCCATACCCCATCGCTTTGGTAGCACCCGTGATCGAATAGGCAGTGTCTGGGAGGCTGTAGCGGGCAGGCTTGACGACTGAAGTCCGCTATAGGAGGTATATTTAAATATTCCGTTCTTTCTGTCGCCACATACGGCACGACATAATACAAACGTGCCTGTGGCAAGTAAACATAAATACTTACCCGTTTTAGCTCTCGAATTAGGTCGACCTCGACCCCTGAGTCGAATGCGTAGATAGAACACCATCGCGGTATTTAGTCGCAATGAGTTCATCAGCTTTAAGAGTACAACAAGCCCGGTGTAGTAAGGCTCGTCGTGAAGTCTGTCTAAGTACTGCCCGGTTCGATTTTTTCCGGATAGGGTGCCTCCGCACGGAACCCGGGGATCAGCTAGTTGAGAGCAAGACTTACATAGATAGTTTACAGTCGTCCTTTTTGGTTTCTGATGCGCTGTCGGTGTATAACATGCTTGCGAGGTAAATTTGTGACCACCATCATAAGCCAAACAAGTTTACATACCCCGAAGTCCCAGCTCAACGAGTACATCGGCAGAACGCCGTGTTACTACAGTTGCCTTGTTAAGTCCGTCGAACAGAGTACGCGTTTCTATCCATTTCCCTAGAGCCGATCAGACTCTACGAGTTACGGGAACGAAGTCTCATCTCGTAAGTAAAACTTGGTTAGACAGCTGTCCGTTCTGACCTCCACGATTTCACATATCCATTTCACCCTAATCGTCTAGATCGAAAAGCTCTTATCACTCTCTTACAGGTACGGTGCTCGTAGTACGAAGAATGGTTGGAGAGATACGGCTTCTCAGAAAGTCTTCTATCTGGAGCCGTCGTCTCGCCCAATAATCTTGCTCTTAACATTGTACGAGATAGCCCTGTATCATTTGCAAAATACGTACTGTACCTCGCCCGGTTTACCTTGTTGTATCGGCCGTAGTCTCCTAATTAGGTTCGTACTTACATAAGACTGTGCATGTGCCACTGACTATAAATAAACCACAGGTTGTTGTATCAGCGTTCCCGTAATAAGACTCCTAGATCTCAGACCGCTGTTTATGGCTCGCAAGTGTGGCTAATGAAATAGTGCCGTTCACGGTAGTATGCGCAAACAACGCGTGCGCGATAATCGTTACCCCTCCGCTGCAGAAGGCACAATTGATCTATAGGAATCTACATATACAGACAGAGGCTGGGGGTGTGTTGGATCTTGTGGGCTCACGGGCGGCACAAGTCCCGCTCAGGGGTCAGAGTTGCCATGGGTTTTGAATATTCATTAAACCCTTCGCATTGCAGATGAAGGTGGCATCTGGTGTCGGGGGAATTTCGGGGCAGACTATAGTTTTTTCAGTGCCTGGGAAGTCATCTACACGTCGCACCGTCCTCGCGAGCCTAACCGGGCAGAATTTTTATACTTCGCTCATCTCCGGCCTAGTGGGACGTAATTGCCCATGGTCGCCTTGAACCTCCGATATATCAGAATAAAGTATAGCCGCCTGCATAGCCGGTCATCGTTCACCATAGATTAGGGAACGACTCGCCAGGCGCTATTCCAATATATTCTCATGCTTTAGTTGCTTTCGCGTTAGAGGGAAATAACCGAGAACGGCCGGATCCGTGTTTCCACGCTGGCAGGACAGAAGGTGGATCGCCTCGGAGGGAGCAACATAGGGAAGTCCCCGTACAGCTGTCTCTGTGGCAGGAGACTTGGTAGCTATCTAGGGCATCCTAATGGACTGACCGTCTCGGCACATATGGCATTGCACAATTAGCTGCAAGTGAAGCCAACACCTGATGAGATTTGTGGAGTGCCCCTTGACAATTTTAGATCACGAGCTATGTACAATCAAGCCTGATTAAACTTTATGTACGGCCGGCTCTGTAGATATGCTATCTCACCAGAATCATCATTTTAACAAAAGCGTATACTACCCTTAAGTTATAAAGAGTATGGAACGGACCGAGGCACCCACCACACCGGGCTTGTAGCCGGTCAGGGGCTGACCGTCTTTGGCGGAACGATTCTCATTCTAGGCTTGGACTGCCATGCAACCAGGTAAGGGGCCCCCCGTTTTCAAGGTGTACTGAGATACGGGACACTTAAACAAAGGCTGGGACACTGGGCTCGTGAGAGGTATGCAGGGCGGTTTGCCCGGTTTGGGGCGGGGGCGGTTTGCCTAAGGGCGGTTTGCCCCATCAGGGCGGTTTGCCGAACAAACTTTTGCCGGGGCGGTTTGCCATAGAGATATGTGCGTACCGCATACTTACTGGGCGGTTTGCGGGCGGTTTGCCGGCGGTTTGCCAGCCGACCGCTCTCTTCTTAGACAGGGCGGTTTGCCGGGGGTTCTGGGGGGCGGTTTGCCGATAATTTGGGGGCGGTTTGCCCCAGGGCGGTTTGCGGGCGGTTTGCCCTTTGGGGCGGTTTGCCATCTAACACCTCAGCGAAGCAGATTAGGGGGCGGTTTGCCGGGCGGTTTGCCTGTCGAGTTGGGCGGTTTGCCTGGGCGGTTTGCCTCTTATAAAATGTCGTTTTTGTCCAAAGTCATCTAGGGGGCGGTTTGCCTGACAACAAGGGGGCGGTTTGCCTTGCCACTCGGCCTGGGCGGTTTGCCCCACATCTCGCCTTGGGGCGCGGGCGGTTTGCCCATCCTCCCATTACGGTCCAAGATGTACCTCCAAACAGCAAAATACGTTGTCGGGCGGGGGCGGTTTGCCTGTCATACCTAGTCTAATGATTATGCATCCGTTGAAGCGAATATATTCGAGGGGAACAGGGACCATCGGTCGCTGAAGCCTATGAATAGTCGCCCCCGCTCATCACACTGCGGACAGAAATGCTTGTTAAGTACCAGGTAATGTGCGCATATGCCGAACAACAAAAGGTCATTTGAAAATACGCCGCTAACGCGTATGAAGGTCGCTTGACGTCCTTTGTATGTTTAACGGGTTCGAAGAGTTAGTGCATCCATATCACGTTAGAATCCCACGCAAGTGCCGCCGCACAATGACTATCGTGCATATGTTGCTTAATAGCTCACATCTTCACCCGTTCGTTCGAGAGTGGGAGGTAACAGGGCCTCGATAGGGCCCGAAGGCCTGCGATGCGGAAACGTACCATAGGAACGCTGGGCGACTAAGGTCCATCGCCTTGTGTTAGTTCTTAGTCAGAGTATGGGTTCCCAGCTTTCTCTCCGACTGAGTTCCCAGAATCTCATCCCCTGAGGAATTAAGATGGAGTCTGTCAACAAGCTCCTTACCCCTTCTCAACACTTTTAGCCAAGCTTTTACGCCAGTTTACGCGGAAAAAGATGGTTACCCACGAAAGGCTACAAAAACTTCGAGATTCACTCCCAGATCCATAAATATCCCCACCATAAATATCCTCTCCCGCACACCGGGAGGCCATAAATATCCCACCATAAATATCCCGGAGTACCCTCGAGATTCCTGGCTTGCCATCCACACGCGATTGGGAGCGCCCCATCCATAAATATCCGATTACTGCTGCCCATAAATCCATAAATATCCAGACGAACCATAAATATCCTACCTGTTATTGACCATAACCATAAATATCCATATCCCCATAAATATCCTACCACCATAAATATCCTCCGGACTCCGTCCAAACGCAGTGTCCATAAATATCCCCTTAGGGCACCATAAATATCCTAAATATCCTATTGCCTTTATGTAACCCTGTACCATAAATATCCCTGTCGGCCCAGCCAAGCAACAGTACTCGTCCATCTACACTAATGGGTTCGAAATATTTCCACCATAAATATCCCGAACCTGTGATCTGGACGCTCCTTGATACCGCGCGACTACCCATAAATATCCAATATCCATATCCACTCGATCTCCCATAAATATCCTCCGAATTCGGGGTAGAGGGTGGATCATGCCCCATAAATATCCACCATAAATATCCTAAATATCCCGGCGCACGGTCGTGTCTCGCCCGTTGGCTTATACTGGTCGATGGTTGTATTGAGGCGAGTGGATGTGCCTTAAGGACCCTAGAGCCTATCGTAACCCGTACTTTTAAGGTCAACCTCATTACGACCATAGATTTCTTTTCAGAGCCTGCATACACGGGACTTTCCGCCGCGAGACAACACACCGTTCCTCGTGCCGACTAGCCTATACCTCAAGGAATACGAGCTGGAGGTCTCGACTGAAGGAATACGAGGAATGCCAAAAGAAGGAATACGAGATACGAGAAGGATTGATCCTCGTTTAGTAGTAGAATTTGCGTTTCGCATTCAAGGAATACGAGGACATCGCGAGCGTCGTTGTTAGACCATAGATTTAAAAGGAATACGAGAGCTAAGGAATACGAGACGAGGAAACGTGAAGGAATACGAGAGTCTCAAGGAAAGAAGGAATACGAGGATATTGGAGCCTTAGCGTGGAAGGAATACGAGTAGCTTCCTGGTTATATCAGGCCTAAACAGCGCCTACCACAGAAGGAATACGAGGTCTAAGGAAGGAATAAAGGAATACGAGTAAGGAATAAGGAATACGAGTAAGGAATACAAGGAATACGAGCGAGCGAGGACTCAAAGGAATACGAGCACGAGGCAAAGAAGGAATACGAGCGACGACCGGAATAATTGACAAAGCAGTTACAAAAGGAATACGAGGACTTGTTGCGAAGGAAGGAATACGAGGAGAACGAGCCGATATCTACAACTGGAAGACTGAAGGCTCCACCCCAAGGTTGGAGTCCTACTTCTTTCCGGCTTACAGGGGCATGTGTCGTGAGCTCAAGACCTGGTACGGACAGCGGCCAGGACCGTTGTTCCTCGCTAGTCCATCGGTACTATGAACTTGGTCTACTCTAAAACCTGTGTTGGCAACCCTGGTGGGAAGTAATAATGGGGTGAATATATAGTACGTGACCACTTAAAGTGGGAAGTAATAACGTGGACGAAGGTAGCTATGAAAAAATAGCGGATGGGAAGTAATAGAAGTCGACTTGGGAAGTAATATAATAATACCCCGCGCTGGGAAGTAATATGGCCTTGGGAAGTAATATGGGAAGTAATATAATATGGGAAGTAATAGGTGAATGTGTCATTCATGTTGCGGGCGCATAGATTGGGAAGTAATAATTTGAAGGGTGACGCGCCCGTCTCCGCCAAGTTAACCCCGTGGGAATGGGAAGTAATAGTGGGAAGTTGGGAAGTAATAATAGGAACGCGACGCGTGGGAAGTAATAGGAAGTAATAGGAATGGGAAGTAATATGGGAAGTAATAGGATGGGAAGTATGGGAAGTAATTGGGAAGTAATAAAGTAATAACCGCCCCGCCAAGTTAAAATGGACCCTGGGAAGTAATATGGGAAGTAATACTGGGAAGTAATAGAAGTAATAGGATGGGAAGTAATATAGGAAAGTTGGTGGGAAGTAATAAACCGCCAATTATGGGAAGTAATTGGGAAGTAATATACCGCACCGATGCCGCGACATAGGTTACCGCACCGATTGCGACATAGGTACCGCACCGATACCGTACCGCACCGATGCACCGATCGATGTTGTACCGCACCGATCGATCGTGTACCGCACCGATATCCGCCGCGCGACATAGGAAACCATTGTGCGTCTTACAACCGCCGCGAGCGACATAGGAATGCTGCGACATAGGAATCTACAGCGACATAGGTACCGCACCTACCGCACCGATGCGCGACTACCGCACCGATAACCTTTTTTGCGACATAGGAAGACAGGGCGGGCGCGACATAGGAAGAACACATTCCTCAGTTACACGCCCCCGAACACCTTTAAATCCTGGGCCATCTGCGATACCGCACCGATCTTACCGCACCGATTGCGTTTGTACCGCACCGATCCGCACCGATCACCGATCCGTACCGCACCGATGTCATTTAAACGTGGTACCGCACCGATGAGGCCGTGCGCAGCCTATCCGCCAAGCCTTACATCTCGGGTCAACTCTTGTATACTGTATATTATCCTACTGCCCGGCGAGGGCGGCACCCCGTTCATCCTTTAAGACCTCGCAGAGACTGTAGTCCAGCCAGACTTGCGCCCCGCAGTCTGGTCAAGACGTTTTGACCGATGTAGCGCACACGGTAGGAGAAATTAAGTCTCGCACGTAATAGGGGTGTGTAGACCTAGCAGATGCGTGAACTCTCCAGTGAAAGCTGCTAAGCAATGCACTGTCTCACTCTCCTGCCTGCTTTGCCGGTATCAGCCCCGGCCAGTGCGTGTCGCTCCTCCACATGGTTACGTCCTAATGAAAGAGCGGCGGCTCATAGACTAGACAGTAAACTTTCGACGTGGGTTTACCTTACCTCTAAAAATCCACGAATGCTGTGCGCGTGGGTTGCTCCGACACAATAGCTGGTATCCTTATCTCAGGACTTGTTCCAAACTATCAGGGGCTGAGGCGACCCGGCGATCGAATTCATGGGGAGAATGGCCTATTATCACCCCACGTCCCAAGGTTCCGGATAGTAACGAATGAGGCTCAGGTTCAACTCCCCCTGTACTAAACTTGCCCGCCTACCGCACGATTTCATTCGGTTCGTGGGTGAGAAGGAACAGAACACTCGGGTGCAGTGATATTGGCAGCCGACGAACTGAGGTCTTATGTATAGAGAGGAACAGTCGCCACGAGAACACTCGGGTTACGGGGCAGGAACACTCGGGTGGAACACTCGGGTCAATGAACACTCGGGTCACTCGGGTTCATGACTCGCTTTCATTCATGATATACATTTGAACACTCGGGTTCGGGTTCCGCGTAGTTAACCCTTCCTTTCCACGTGAACACTCGGGTCACGAACACTCGGGTGGGTCGTAGCGTTTCGAACACTCGGGTCGGCGTTCCCGGGAGAACACTCGGGTGGAACACTCGGGTGAACACTCGGGTGGGAACACTCGGGTAACACTCGGGTCAATTCCTAACTAGTGCTGTGTCTCCTCAGCTATGAACACTCGGGAACACTCGGGTGAACACTCGGGTTGAAGAACACTCGGGTGAACACTCGAACACTCGGGTATCCGAACACTCGGGTAGTGGAGGTTCTTGCAGGAGTGGAGGTTCGAACACTCGGGTGGGTAGTGAACACTCGGGTCGAAGAACACTCGGGTTAGTTGAGTGAACACTCGGGTGGGTCACCGCTCGGACCCAACGGACTGTGAAGAGTGGAGGTTCTCAAGGAGTGGAGGTTCAGGAGTGGAGGTTCTCTCGGCCGCGATGTGAGTGGAGGTTCTTAAAGAGTGGAGGAGTGGAGGTTCGTTCTACGGTTCAAACAGCTACTAGAGTGGAGAGTGGAGGTGAGTGAGTGGAGGTTCTGGAGGTTCGAGTGGAGGTTCCACCGGGCGAGTGGAGGTTCCCGGAGTGGAGGTTCGTGAGTGGAGTCAGTTCGTGGGCTCTAGAGTTCAGTCAGTTCGTGGGGGAGGTTCAGGTGAGTTCAGTTCGTGGGGTCAGGAGTGTCAGTTCGTTCAGTTCGTGGGGTTCGTGGGCGTTCAGTTCGTGGGGGGTTCTTTAGCAACCAGGCTGGGATTCATCAGTTCGTCAGTTCGTCAGTTCGTGGGGCTTCTCTGGCGTTGATATGTCGTCAGTCAGTTCGTGGGAAAAGCTGTCAGCTTATATCAATGTAGCAGCCTGTAGCCTCTGAGGACCTCGCGGGAATGCAGAATCAGTTCGTGGGGCTACCAACTAGAAGTCAGTTCGTGGGAGGGTATTATCAACTAGCACTTGCGGCCGTAATCTCAATGTCAGTCAGTTCGTGGGTGGGAGTTCTCAGTTCAGTTCGTGGGCTAGATGGGCAACCAGCCGCGTTCTTGTGGTATCGTGCGTGAAGTGCCTTCAGAACTTAACTCAGTTCGTGGGGTGGGGGGGCCACAGATCAGAAAGTGCAGGTGCAGGAGATAGCAGTTGCAGGAGATAGTGCAGGAGATAGCGGTGCAGGAGATAGGTGGGGTGCAGGAGATAGAGCGACCGCTATAGGGATTAATATTGCAGGAGATTGCAGGAGATAGCAGGAGATAGAAGCATGTTGGGCATGCAGGAGATAGGACAGAAGCCGGACAAGGGTGGTTCATGCAGGAGATAGAGTGCATGCAGGAGATAGGAGATAGAGATTGGCTGCAGTAAATTCTGACGTACCATGCCGGTTGATCAAAAGAAAACAACATGCAGGAGATAGGCATGCAGGAGATTGCAGGAGATAGATCGGTGCAGGAGTGCAGGAGATATGCAGGAGATAGATTATGCAGGAGATAGGGCCCAACCGCCTGGACGTTGGGTGCGAAAGCTAGCGAGGACGGCATGCAGGAGATAGCCACCCTCCGCTGCTGCAGGAGATAGTAGCTTAATGCAGGAGATAGATAGGAGATAGGGGTATGTGATCTTACTTAAGCGGCCGTCCTGCTTGAGGCAAAAGTCGGCGGTGCAGGAGATAGGATGCAGGTGCAGGAGATAGAAAAGCAACGTAAACAAGATCAATTCTGTCGGTGATTGGATGCTCGGAGGTGGTTGGTTGTCAGATGTCCTGCGTGGTTGGCAGAGCCGACACGAAATTGTCGGACGCAGAAATGAAAGAATTATTCATAATCTGGAAGGAAACGGGGGGGAGTGAGTACAATTAAGAGCATCGACCCCAAACGAAAGGGACGATTCACCGTTCACGCTAGATTAGGCCTCGTACTACGTTCTTATAGAACATCCGGTCGACATCCAAGGTACGGTACCGCCCGGAGCTCACAATCTGAGGCTAATAAAGGAATACTGCCTTCCTACACAATCCACAATCTGAGGCACAATCTGAGGCACAATCCACAATCTGAGGCCAACCATGGGTTGTCACAATCTGAGGCGGATATCCTTAACGGCACAATCTGAGGCAGTCACAATCTGAGGTTCATGAAGACATTAAGCACAATCTGAGGCGGGGTAACGTAAGCTCGTAACATGGGCACCGTCACAATCTGAGGCGGACGCACAATCTGAGGGAGGCCACAATCTGAGGTTTTATTCATACCTGCCCACAATCTGAGGATTTGAGCCACAATCTGAGGTCACAATCTGAGGCAATCTGAGGCCAATTCTGAAGTCTCACAATCTGAGGCTGAGGCAATCTGAGGGTGGGTATATAAGTATAAGCCTCACAATCTCACTGGGTATATGGGTATATAAGTGCATGGGTATATAAGTATAAGTTGGGTATATAAGAGGAGTGGGTATATAAGGCACAATCTGATGGGTATATAAGGGGTATTGGGTATATAAGTATATATGGGTATATAAGAGTGGGTATATAAGTGGGTATATAAGTGGGTATTGGGTATATAAGATAAGTGGGTATATAAGTGGGTATATAAGTGTGGGTATATAAGTGGGTATATAAGTGGGTATATAATGGGTTGGGTATATAAGATATAAGTGGGTATATAAGTGGGTATATAAGTGGGTATATAAGTGGGTATATAAG
""", 12, 582, 18)
