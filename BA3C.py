##odvojimo nizove po retcima, k je duljina
##prvog, odnosno svih nizova jer su svi iste
##duljine. s dvi for petlje usporedujemo svaki
##sa svakim. Usporedujemo sve indekse osim prvog
##u prvom nizu sa pocetkom drugog do k-1
def OverLap(patterns):
  patterns = patterns.split("\n")
  k = len(patterns[0])
  for i in range(len(patterns)):
    first = patterns[i]
    for j in range(len(patterns)):
      second = patterns[j]
      if first[1:] == second[:k-1]:
        print(first + " -> " + second)
OverLap("""GTTATTGACAAAGCGTCACG
GTTAAGCTAGGGCCCCCGCC
TCGGCCTGGGCTTGGACTCT
CGAACGCCCGGGGCCCCTGA
CTAGTGGTCCGGAGTATTGG
GGCCCCAGAGGCGTAAACAG
TGCTAGTAATTACAGGAGCA
CCTGTGAAACGCTCACTCTT
TTTACTACACGTATACTGCG
AAAAACCTTATGCATCGTTG
TACACGTATACTGCGAACCC
AGGAGGTCTTGCACTAACTC
AACCGTGGCCTTGGCCAGTG
GCCCCTGATAGTAACGTAAT
TAGTAATTACAGGAGCAGGC
AGTCACTCGAGACAGCGTTA
AAACAAAACGTTGTATACTG
TCTGTCAGCGCAACCGTGGC
GGGCTAGTGGTCCGGAGTAT
CTGATAGTAACGTAATGAAC
GCACTACTTCCCACGAATAG
GCGCCAAGAGGCCCCAGAGG
GAACCCTCATTTATAGATGT
GTATTGAGGAGATACCAGGA
AAGCTAGGGCCCCCGCCCTG
TGTATACTGTCTACGAACGC
TTCCATATGCTGCGATTGAC
TAGTCACGGACAAACAAAAC
CAGGCAGTACATCGTTGTGC
ACTACACGTATACTGCGAAC
GTAATCCCCGCCCCAATCAA
AAGCCATTGGGTGCGACCGG
CAAATTCCCACTGATTGAAT
TTCCTTCGTAGTCACGGACA
AATAACATCTGCATCTATTA
TCCGGGCTCCTATGTCACCT
TGCTGCGATTGACTCGCAAG
TGATTGAATTAAGTATCATT
CCAAGAGGCCCCAGAGGCGT
GGGACCTTCCTTCGTAGTCA
CGTATACTGCGAACCCTCAT
GGGCTTGGACTCTAGGACGG
TTCCCACGAATAGACCCTCG
CCGATCCGGGCTCCTATGTC
CACTCTCCCAGGGTTTGATG
TACCAGGAAACATATACGGT
TGATGAAGTCATGGTGTAAT
TTACTACACGTATACTGCGA
AAACCCAGTGCAAGCCATTG
GACTCTAGGACGGGTGGTTA
GCCCCCGCCCTGCATAGGGG
AAATTCCCACTGATTGAATT
TTGGCCTGCTACTTGGGGAT
TCACCTGTAGAAGATTATCA
TTATTGACAAAGCGTCACGA
CCAGTGCAAGCCATTGGGTG
CTCTTTCAATCACTCTCCCA
AAAACCTTATGCATCGTTGG
TATGCATCGTTGGGCAGCTC
TGCTACTTGGGGATCCGCTG
TGATAGTAACGTAATGAACA
CATATATATAAACCCAGTGC
ACTCGAGACAGCGTTATTGA
TCCCCGCCCCAATCAAGTCT
TAGACCCTCGAGGGACCTTC
CAATAACATCTGCATCTATT
GCCATCGGGCTAGTGGTCCG
TCGAGACAGCGTTATTGACA
GGGCCCCTGATAGTAACGTA
TCTCAAAAACCTTATGCATC
CGCGCCAAGAGGCCCCAGAG
TTGTATACTGTCTACGAACG
GTCCACAAATTCCCACTGAT
ATCAGGGGGGTTCGCTACCA
TACTTCCCACGAATAGACCC
TTCACCGATCCGGGCTCCTA
CTGCGAACCCTCATTTATAG
CCATATGCTGCGATTGACTC
CTCGCAAGGAGGTCTTGCAC
AGCTCCTCTTCGGCCTGGGC
CCACGAATAGACCCTCGAGG
TCAATCACTCTCCCAGGGTT
TAACACCTGTGATGCGGCAA
AACACCTGTGATGCGGCAAT
CTAACTCAGGCTAAAGTCAC
GGATCCGCTGACACCTCATC
CCGCTGACACCTCATCGCTC
GGCTTATTTCCATATGCTGC
TTGGGTGCGACCGGTTTTAA
GGCAGTACATCGTTGTGCCA
TAACGTAATGAACAACTCTA
GTCATTTCACCTCTGTCAGC
TTTCAATCACTCTCCCAGGG
GTTTCGCGCCAAGAGGCCCC
GGAGGTCTTGCACTAACTCA
TACTGTCTACGAACGCCCGG
AGACAGCGTTATTGACAAAG
TGATGCGGCAATAACATCTG
TATTTCCATATGCTGCGATT
TACTACACGTATACTGCGAA
TGAGGAGATACCAGGAAACA
GAGGTCTTGCACTAACTCAG
ACCTCATATATATAAACCCA
ACAACTCTAGCCCGCTACTC
TTTCGCGCCAAGAGGCCCCA
AGTGACGTGTATACGCAGTG
CAAAAACCTTATGCATCGTT
TGTGCCATCGGGCTAGTGGT
GAATTAAGTATCATTAAAAT
GGAAACATATACGGTTTCGC
CGAGACAGCGTTATTGACAA
CCTATGTCACCTGTAGAAGA
TCTACGAACGCCCGGGGCCC
AACATCTGCATCTATTAGTT
GTTAAGTCAGGCAGTACATC
GTGGTTAAGCTAGGGCCCCC
GCTACTTGGGGATCCGCTGA
CTATGTCACCTGTAGAAGAT
GGGTTTGATGAAGTCATGGT
ACTACTTCCCACGAATAGAC
GCGTAAACAGTTCACCGATC
GCTAGGAGGATGCAATAGCC
GGTCTTGCACTAACTCAGGC
GTTAATCTCTTTCAATCACT
CTTGCGCAGCTCAACCTCAT
TCTAGGACGGGTGGTTAAGC
CCTTCGTAGTCACGGACAAA
TTGTGCCATCGGGCTAGTGG
ACAGGAGCAGGCTTATTTCC
TTTGTCATTTCACCTCTGTC
AACCTTATGCATCGTTGGGC
CACTCGAGACAGCGTTATTG
GATCCGCTGACACCTCATCG
GATAGTAACGTAATGAACAA
ATCGCTAGGAGGATGCAATA
TAGGAGGATGCAATAGCCTT
AACATATACGGTTTCGCGCC
GCAATAGCCTTGCGCAGCTC
GTGCTAGTAATTACAGGAGC
TTAAGTCAGGCAGTACATCG
TCGTTGGGCAGCTCCTCTTC
TACGGTTTCGCGCCAAGAGG
TTACAGGAGCAGGCTTATTT
AACTCTAGCCCGCTACTCCC
GTCACCTGTAGAAGATTATC
GTCCGGAGTATTGGCCTGCT
TGCGACCGGTTTTAACACCT
GAGACAGCGTTATTGACAAA
CACGATATCCGTAGTTGCAC
ATATATAAACCCAGTGCAAG
CGGAGTGATTCCTGTGAAAC
AAACGTTGTATACTGTCTAC
GCTAGTAATTACAGGAGCAG
GAAGATTATCAGGGGGGTTC
CGTGCTAGTAATTACAGGAG
AGTGGTCCGGAGTATTGGCC
ACACCTCATCGCTCGTGCCA
GGGATCCGCTGACACCTCAT
GGTTTCGCGCCAAGAGGCCC
CCAGAGGCGTAAACAGTTCA
CCGCCCCAATCAAGTCTCAA
GCAAGGAGGTCTTGCACTAA
AGACCCTCGAGGGACCTTCC
TATACGCAGTGCCTCTCGCA
TTAAGCTAGGGCCCCCGCCC
AAAGTCACTCGAGACAGCGT
CCCGCCCTGCATAGGGGGTC
TCTCCCAGGGTTTGATGAAG
TGACTCGCAAGGAGGTCTTG
ACCCAGTGCAAGCCATTGGG
CTCCCGCGGAGTGATTCCTG
GGAGTATTGGCCTGCTACTT
GACAGCGTTATTGACAAAGC
GTCGTGCTAGTAATTACAGG
ATAGCCTTGCGCAGCTCAAC
AGAGGCCCCAGAGGCGTAAA
CTCCTCTTCGGCCTGGGCTT
AAACAGTTCACCGATCCGGG
AGGCAGTACATCGTTGTGCC
TCCATATGCTGCGATTGACT
GTGCGACCGGTTTTAACACC
GTCTTGCACTAACTCAGGCT
TGACACCTCATCGCTCGTGC
AAGATTATCAGGGGGGTTCG
GAGGGACCTTCCTTCGTAGT
CGCTACTCCCGCGGAGTGAT
ACAAATTCCCACTGATTGAA
AGGGCCCCCGCCCTGCATAG
CTCTCCCAGGGTTTGATGAA
TACTCCCGCGGAGTGATTCC
CTGATTGAATTAAGTATCAT
TTAGTTCAAATCGGTTAATC
CAGACAATTATCGCTAGGAG
CCGTGGCCTTGGCCAGTGGA
ACAGTTCACCGATCCGGGCT
GCCCTGCATAGGGGGTCCAC
TTTTAACACCTGTGATGCGG
TATCGCTAGGAGGATGCAAT
GGTTTGATGAAGTCATGGTG
ATCTCTTTCAATCACTCTCC
TTGGCCAGTGGAGCTAGAAA
AAGTCATGGTGTAATCCCCG
AATTAAGTATCATTAAAATG
GACCGGTTTTAACACCTGTG
TCACTCGAGACAGCGTTATT
TCACTCTTTGTCATTTCACC
GACAAACAAAACGTTGTATA
CAGTGCCTCTCGCAAATGTA
TGGCCAGTGGAGCTAGAAAC
CTAGGAGGATGCAATAGCCT
TAGGACGGGTGGTTAAGCTA
TCGTGCCAGACAATTATCGC
CTTCGTAGTCACGGACAAAC
GAGTGACGTGTATACGCAGT
CGCCAAGAGGCCCCAGAGGC
ATAAACCCAGTGCAAGCCAT
CACCTGTGATGCGGCAATAA
TAGGGGGTCCACAAATTCCC
AGTTCAAATCGGTTAATCTC
CATCTGCATCTATTAGTTCA
TTGAATTAAGTATCATTAAA
GCAACCGTGGCCTTGGCCAG
TGCCTCTCGCAAATGTATTG
GGCCTGCTACTTGGGGATCC
CAGCGCAACCGTGGCCTTGG
CCCGCGGAGTGATTCCTGTG
GTCACTCGAGACAGCGTTAT
CCCCTGATAGTAACGTAATG
CCCTCATTTATAGATGTTAA
AGGTCTTGCACTAACTCAGG
CGGACAAACAAAACGTTGTA
CTGACACCTCATCGCTCGTG
CTAGGACGGGTGGTTAAGCT
GTTTTAACACCTGTGATGCG
AGAAAGTCGTGCTAGTAATT
TATACTGCGAACCCTCATTT
GTATCATTAAAATGCCGCAA
CTGTGATGCGGCAATAACAT
GGTGTAATCCCCGCCCCAAT
TGCATCTATTAGTTCAAATC
GGGGTCCACAAATTCCCACT
GCTGACACCTCATCGCTCGT
GCCTTGGCCAGTGGAGCTAG
TGTAGAAGATTATCAGGGGG
ATAGACCCTCGAGGGACCTT
CGTTATTGACAAAGCGTCAC
ACCTCATCGCTCGTGCCAGA
CTACTTCCCACGAATAGACC
CAAAGCGTCACGATATCCGT
GATGAAGTCATGGTGTAATC
ATAGATGTTAAGTCAGGCAG
TGTCTACGAACGCCCGGGGC
ATGGTGTAATCCCCGCCCCA
TCATCGCTCGTGCCAGACAA
ATATCCGTAGTTGCACTACT
CTTCGGCCTGGGCTTGGACT
TCCACAAATTCCCACTGATT
TCATGGTGTAATCCCCGCCC
CAAAACGTTGTATACTGTCT
TGAACAACTCTAGCCCGCTA
CCTTGGCCAGTGGAGCTAGA
GGGTCCACAAATTCCCACTG
GCTCCTCTTCGGCCTGGGCT
GGAGATACCAGGAAACATAT
TAAGCTAGGGCCCCCGCCCT
GCAAGCCATTGGGTGCGACC
CCTGATAGTAACGTAATGAA
TTTCCATATGCTGCGATTGA
GCGATTGACTCGCAAGGAGG
AGACAATTATCGCTAGGAGG
ATACTGCGAACCCTCATTTA
TTGACTCGCAAGGAGGTCTT
AAGTCTCAAAAACCTTATGC
GTTTGATGAAGTCATGGTGT
ATTAGTTCAAATCGGTTAAT
ATCGGTTAATCTCTTTCAAT
GCCCCAGAGGCGTAAACAGT
GTGCCATCGGGCTAGTGGTC
CAGCTCAACCTCATATATAT
AGTATTGGCCTGCTACTTGG
ATCCGTAGTTGCACTACTTC
CGCTAGGAGGATGCAATAGC
ATTGGGTGCGACCGGTTTTA
TTGGGCAGCTCCTCTTCGGC
TCAAAAACCTTATGCATCGT
ATATAAACCCAGTGCAAGCC
AGTGCAAGCCATTGGGTGCG
CCCAGGGTTTGATGAAGTCA
GCTCCTATGTCACCTGTAGA
CTTGGACTCTAGGACGGGTG
GTAATTACAGGAGCAGGCTT
CCTGTAGAAGATTATCAGGG
ACTGTCTACGAACGCCCGGG
AAGTCGTGCTAGTAATTACA
GGGGGGTTCGCTACCAAGAA
CACTAACTCAGGCTAAAGTC
CATATGCTGCGATTGACTCG
TCGCAAGGAGGTCTTGCACT
TGCACTACTTCCCACGAATA
TGAAACGCTCACTCTTTGTC
ATACTGTCTACGAACGCCCG
AGTAACGTAATGAACAACTC
GATTATCAGGGGGGTTCGCT
CTGGGCTTGGACTCTAGGAC
ACCTTATGCATCGTTGGGCA
TAGAAGATTATCAGGGGGGT
GATTGAATTAAGTATCATTA
GGTTTTAACACCTGTGATGC
CCTGCATAGGGGGTCCACAA
ACGGGTGGTTAAGCTAGGGC
CAATCACTCTCCCAGGGTTT
CTCTGTCAGCGCAACCGTGG
GATTGACTCGCAAGGAGGTC
CGCGGAGTGATTCCTGTGAA
TGTCATTTCACCTCTGTCAG
ATTTACTACACGTATACTGC
CACGTATACTGCGAACCCTC
AGTCATGGTGTAATCCCCGC
GGGGCCCCTGATAGTAACGT
AGCGTCACGATATCCGTAGT
ACCCTCATTTATAGATGTTA
CTAGCCCGCTACTCCCGCGG
CACCGATCCGGGCTCCTATG
TTCGTAGTCACGGACAAACA
TCCTTCGTAGTCACGGACAA
ATGCAATAGCCTTGCGCAGC
AGTTCACCGATCCGGGCTCC
TGGGCAGCTCCTCTTCGGCC
TGCACTAACTCAGGCTAAAG
GAAAGTCGTGCTAGTAATTA
TGGTTAAGCTAGGGCCCCCG
CTCACTCTTTGTCATTTCAC
GCGCAACCGTGGCCTTGGCC
CATTTCACCTCTGTCAGCGC
TTTAACACCTGTGATGCGGC
ATGCATCGTTGGGCAGCTCC
ATCAAGTCTCAAAAACCTTA
GAACAACTCTAGCCCGCTAC
ACCTTCCTTCGTAGTCACGG
GAAGTCATGGTGTAATCCCC
GGACAAACAAAACGTTGTAT
CCTCATATATATAAACCCAG
TCACCGATCCGGGCTCCTAT
ACCTACGATTTACTACACGT
GTGGTCCGGAGTATTGGCCT
AAAGCGTCACGATATCCGTA
CACGAATAGACCCTCGAGGG
GCATCGTTGGGCAGCTCCTC
GGCTCCTATGTCACCTGTAG
ATTTATAGATGTTAAGTCAG
GGCCCCCGCCCTGCATAGGG
CTAGAAACCTACGATTTACT
GCGGAGTGATTCCTGTGAAA
GAAACATATACGGTTTCGCG
TTCCCACTGATTGAATTAAG
GAAACGCTCACTCTTTGTCA
TTAAGTATCATTAAAATGCC
CGCTCACTCTTTGTCATTTC
CAGGCTAAAGTCACTCGAGA
TATATAAACCCAGTGCAAGC
CGGGGCCCCTGATAGTAACG
GGGCCCCCGCCCTGCATAGG
ACATCTGCATCTATTAGTTC
TAGGGCCCCCGCCCTGCATA
ATCTGCATCTATTAGTTCAA
TGGAGCTAGAAACCTACGAT
CGCTGACACCTCATCGCTCG
GAGGAGATACCAGGAAACAT
AAACCTTATGCATCGTTGGG
CTCTAGGACGGGTGGTTAAG
TACGCAGTGCCTCTCGCAAA
TTCGGCCTGGGCTTGGACTC
AGTGGAGCTAGAAACCTACG
CTTATGCATCGTTGGGCAGC
ACCAAGAAAGTCGTGCTAGT
ATCTATTAGTTCAAATCGGT
CGGCCTGGGCTTGGACTCTA
GGCTAAAGTCACTCGAGACA
GTCACGATATCCGTAGTTGC
CGTGCCAGACAATTATCGCT
AAGCGTCACGATATCCGTAG
CCACAAATTCCCACTGATTG
TGCGCAGCTCAACCTCATAT
GCTCAACCTCATATATATAA
TAGCCTTGCGCAGCTCAACC
CGTGGCCTTGGCCAGTGGAG
GCGTTATTGACAAAGCGTCA
CCACTGATTGAATTAAGTAT
TAGTTGCACTACTTCCCACG
ATACGGTTTCGCGCCAAGAG
GATGCAATAGCCTTGCGCAG
CAGTTCACCGATCCGGGCTC
GTAACGTAATGAACAACTCT
TCCGGAGTATTGGCCTGCTA
ATTGAGGAGATACCAGGAAA
CAAGAGGCCCCAGAGGCGTA
AATGTATTGAGGAGATACCA
CAGGGTTTGATGAAGTCATG
AAATGTATTGAGGAGATACC
ATGTATTGAGGAGATACCAG
AGCTCAACCTCATATATATA
GCAGCTCAACCTCATATATA
GGTCCACAAATTCCCACTGA
CTGCATAGGGGGTCCACAAA
GGAGGATGCAATAGCCTTGC
CGCAACCGTGGCCTTGGCCA
CCGGGCTCCTATGTCACCTG
TCCTGTGAAACGCTCACTCT
CGAGGGACCTTCCTTCGTAG
ACGTATACTGCGAACCCTCA
GTTCAAATCGGTTAATCTCT
CGAACCCTCATTTATAGATG
ACGAATAGACCCTCGAGGGA
ATACCAGGAAACATATACGG
CCGGGGCCCCTGATAGTAAC
TAAGTCAGGCAGTACATCGT
CTACACGTATACTGCGAACC
AGCTAGAAACCTACGATTTA
ATTCCCACTGATTGAATTAA
GTCATGGTGTAATCCCCGCC
AGTGCCTCTCGCAAATGTAT
GTGAAACGCTCACTCTTTGT
TACTTGGGGATCCGCTGACA
CCCTGATAGTAACGTAATGA
CTTTGTCATTTCACCTCTGT
ATGTCACCTGTAGAAGATTA
CGTAGTTGCACTACTTCCCA
GGTTCGCTACCAAGAAAGTC
GCTAAAGTCACTCGAGACAG
AGAAACCTACGATTTACTAC
CGGGTGGTTAAGCTAGGGCC
GTGACGTGTATACGCAGTGC
ACAATTATCGCTAGGAGGAT
CAAGGAGGTCTTGCACTAAC
TCAGGCTAAAGTCACTCGAG
ACGTTGTATACTGTCTACGA
ACGTGTATACGCAGTGCCTC
CGCCCGGGGCCCCTGATAGT
TTATAGATGTTAAGTCAGGC
CTCATCGCTCGTGCCAGACA
TGAATTAAGTATCATTAAAA
TCCTCTTCGGCCTGGGCTTG
CAGTACATCGTTGTGCCATC
GCTTGGACTCTAGGACGGGT
GCCATTGGGTGCGACCGGTT
ATCCCCGCCCCAATCAAGTC
ACTGCGAACCCTCATTTATA
TCTCTTTCAATCACTCTCCC
TAGTAACGTAATGAACAACT
CTACCAAGAAAGTCGTGCTA
CGCAGTGCCTCTCGCAAATG
CCGTAGTTGCACTACTTCCC
TATTGAGGAGATACCAGGAA
TCGTAGTCACGGACAAACAA
CACTACTTCCCACGAATAGA
TCATTTATAGATGTTAAGTC
GAGCTAGAAACCTACGATTT
TGATTCCTGTGAAACGCTCA
AATCAAGTCTCAAAAACCTT
CGGTTTCGCGCCAAGAGGCC
CGCAAATGTATTGAGGAGAT
TGGGTGCGACCGGTTTTAAC
CGCTCGTGCCAGACAATTAT
GTAGTCACGGACAAACAAAA
CGTTGTGCCATCGGGCTAGT
TCTTTGTCATTTCACCTCTG
TGCAAGCCATTGGGTGCGAC
TGTCACCTGTAGAAGATTAT
CAAACAAAACGTTGTATACT
TGGGCTTGGACTCTAGGACG
ACACGTATACTGCGAACCCT
CATGGTGTAATCCCCGCCCC
GTGCCTCTCGCAAATGTATT
GTAAACAGTTCACCGATCCG
GTACATCGTTGTGCCATCGG
CGCAAGGAGGTCTTGCACTA
ACGCCCGGGGCCCCTGATAG
CCATCGGGCTAGTGGTCCGG
GCTTATTTCCATATGCTGCG
CCCACGAATAGACCCTCGAG
TGTATACGCAGTGCCTCTCG
GGGGTTCGCTACCAAGAAAG
CACAAATTCCCACTGATTGA
ACTCTAGGACGGGTGGTTAA
TAGAAACCTACGATTTACTA
TCCCAGGGTTTGATGAAGTC
TAGTGGTCCGGAGTATTGGC
AGATACCAGGAAACATATAC
TCTGCATCTATTAGTTCAAA
AACGCTCACTCTTTGTCATT
AAGGAGGTCTTGCACTAACT
GATTCCTGTGAAACGCTCAC
AATGAACAACTCTAGCCCGC
ATCGTTGGGCAGCTCCTCTT
GCCTGGGCTTGGACTCTAGG
TCACTCTCCCAGGGTTTGAT
CTACTTGGGGATCCGCTGAC
ACAGCGTTATTGACAAAGCG
ATCGGGCTAGTGGTCCGGAG
AAGTATCATTAAAATGCCGC
TTGACAAAGCGTCACGATAT
TATTGACAAAGCGTCACGAT
CAAGCCATTGGGTGCGACCG
CAACCTCATATATATAAACC
AAAGTCGTGCTAGTAATTAC
CTCAACCTCATATATATAAA
GCAGTACATCGTTGTGCCAT
CTCTTCGGCCTGGGCTTGGA
GCACTAACTCAGGCTAAAGT
GTCTCAAAAACCTTATGCAT
AATCTCTTTCAATCACTCTC
GTCAGGCAGTACATCGTTGT
CCAGGAAACATATACGGTTT
GACACCTCATCGCTCGTGCC
CTCTAGCCCGCTACTCCCGC
TCGCTAGGAGGATGCAATAG
AGCCCGCTACTCCCGCGGAG
CCAGACAATTATCGCTAGGA
AGTCACGGACAAACAAAACG
TACATCGTTGTGCCATCGGG
CTCCTATGTCACCTGTAGAA
CGGTTTTAACACCTGTGATG
CTCATTTATAGATGTTAAGT
CCGGTTTTAACACCTGTGAT
TCTCGCAAATGTATTGAGGA
CTCTTTGTCATTTCACCTCT
GGCCCCTGATAGTAACGTAA
GACGTGTATACGCAGTGCCT
CAGGCTTATTTCCATATGCT
TAATCTCTTTCAATCACTCT
TGTGAAACGCTCACTCTTTG
AACGTTGTATACTGTCTACG
TGGACTCTAGGACGGGTGGT
GCTAGTGGTCCGGAGTATTG
GACAAAGCGTCACGATATCC
AATAGCCTTGCGCAGCTCAA
TCAGGCAGTACATCGTTGTG
AACAACTCTAGCCCGCTACT
GCTACTCCCGCGGAGTGATT
GAGGCGTAAACAGTTCACCG
CTGTGAAACGCTCACTCTTT
CTGCTACTTGGGGATCCGCT
AGGATGCAATAGCCTTGCGC
TATACTGTCTACGAACGCCC
CGAATAGACCCTCGAGGGAC
TGGGGATCCGCTGACACCTC
CCAAGAAAGTCGTGCTAGTA
CAAATCGGTTAATCTCTTTC
CATTTATAGATGTTAAGTCA
ATTTCACCTCTGTCAGCGCA
CACCTCTGTCAGCGCAACCG
ACTAACTCAGGCTAAAGTCA
TAGCCCGCTACTCCCGCGGA
CACCTCATCGCTCGTGCCAG
CATCGGGCTAGTGGTCCGGA
AGGCTTATTTCCATATGCTG
GGCGTAAACAGTTCACCGAT
TCGGTTAATCTCTTTCAATC
CTACGATTTACTACACGTAT
TGGCCTTGGCCAGTGGAGCT
CCTTGCGCAGCTCAACCTCA
ACTCTCCCAGGGTTTGATGA
ATTGACTCGCAAGGAGGTCT
CTCGTGCCAGACAATTATCG
CACGGACAAACAAAACGTTG
TACAGGAGCAGGCTTATTTC
GGTGGTTAAGCTAGGGCCCC
CAAGAAAGTCGTGCTAGTAA
TCTTTCAATCACTCTCCCAG
CATCGTTGTGCCATCGGGCT
AGTTGCACTACTTCCCACGA
GACCCTCGAGGGACCTTCCT
CTACGAACGCCCGGGGCCCC
GATACCAGGAAACATATACG
AGAAGATTATCAGGGGGGTT
CCTCTTCGGCCTGGGCTTGG
TGACAAAGCGTCACGATATC
CCCTCGAGGGACCTTCCTTC
ACGGACAAACAAAACGTTGT
CAATCAAGTCTCAAAAACCT
CCGGAGTATTGGCCTGCTAC
GGCCTTGGCCAGTGGAGCTA
ATCGTTGTGCCATCGGGCTA
TATGCTGCGATTGACTCGCA
ATACGCAGTGCCTCTCGCAA
CGGTTAATCTCTTTCAATCA
TGGTGTAATCCCCGCCCCAA
ACTTCCCACGAATAGACCCT
GGTTAATCTCTTTCAATCAC
GTGGCCTTGGCCAGTGGAGC
TAGTTCAAATCGGTTAATCT
TCGTTGTGCCATCGGGCTAG
GCCCGCTACTCCCGCGGAGT
GGGTGGTTAAGCTAGGGCCC
CCGCCCTGCATAGGGGGTCC
TGCGAACCCTCATTTATAGA
TAAGTATCATTAAAATGCCG
CCCAATCAAGTCTCAAAAAC
GAGGCCCCAGAGGCGTAAAC
CCTCTGTCAGCGCAACCGTG
ATTGACAAAGCGTCACGATA
GAAACCTACGATTTACTACA
CGGGCTAGTGGTCCGGAGTA
GTGCCAGACAATTATCGCTA
GATGCGGCAATAACATCTGC
GGGCTCCTATGTCACCTGTA
TAGATGTTAAGTCAGGCAGT
GGCCTGGGCTTGGACTCTAG
AACGCCCGGGGCCCCTGATA
ACTCGCAAGGAGGTCTTGCA
TTCCTGTGAAACGCTCACTC
GCTAGAAACCTACGATTTAC
CCCTGCATAGGGGGTCCACA
AACAAAACGTTGTATACTGT
TCCGCTGACACCTCATCGCT
CCAGTGGAGCTAGAAACCTA
CGCTACCAAGAAAGTCGTGC
CACTGATTGAATTAAGTATC
TGTCAGCGCAACCGTGGCCT
TACGATTTACTACACGTATA
CATCGTTGGGCAGCTCCTCT
AATTCCCACTGATTGAATTA
CCATTGGGTGCGACCGGTTT
TAATTACAGGAGCAGGCTTA
GAGATACCAGGAAACATATA
AACAGTTCACCGATCCGGGC
TCTTCGGCCTGGGCTTGGAC
TCGAGGGACCTTCCTTCGTA
CACTCTTTGTCATTTCACCT
AAGAGGCCCCAGAGGCGTAA
GACGGGTGGTTAAGCTAGGG
CAATAGCCTTGCGCAGCTCA
TGCATAGGGGGTCCACAAAT
AGGGTTTGATGAAGTCATGG
TTCAAATCGGTTAATCTCTT
ATATGCTGCGATTGACTCGC
TATCAGGGGGGTTCGCTACC
TGCAATAGCCTTGCGCAGCT
TCCTATGTCACCTGTAGAAG
GACAATTATCGCTAGGAGGA
AGTGATTCCTGTGAAACGCT
TCGGGCTAGTGGTCCGGAGT
GGACTCTAGGACGGGTGGTT
TGCCAGACAATTATCGCTAG
TAATCCCCGCCCCAATCAAG
CAACTCTAGCCCGCTACTCC
CAGTGGAGCTAGAAACCTAC
CCCGCCCCAATCAAGTCTCA
GGCCAGTGGAGCTAGAAACC
GGAGTGATTCCTGTGAAACG
AACCCTCATTTATAGATGTT
CTCGAGGGACCTTCCTTCGT
TATCCGTAGTTGCACTACTT
TTGCACTACTTCCCACGAAT
CTCTCGCAAATGTATTGAGG
TTAACACCTGTGATGCGGCA
GGTGCGACCGGTTTTAACAC
GGGGGTCCACAAATTCCCAC
GTGATTCCTGTGAAACGCTC
TCTTGCACTAACTCAGGCTA
ACGAACGCCCGGGGCCCCTG
AAGTCACTCGAGACAGCGTT
GCGAACCCTCATTTATAGAT
CTGTCAGCGCAACCGTGGCC
AGCCATTGGGTGCGACCGGT
CCTCTCGCAAATGTATTGAG
ATGTTAAGTCAGGCAGTACA
TGCATCGTTGGGCAGCTCCT
CTAGTAATTACAGGAGCAGG
ACCGATCCGGGCTCCTATGT
GACCTTCCTTCGTAGTCACG
AGCAGGCTTATTTCCATATG
GCCTCTCGCAAATGTATTGA
GGGGGTTCGCTACCAAGAAA
CTTCCTTCGTAGTCACGGAC
CCCAGAGGCGTAAACAGTTC
GCCAGACAATTATCGCTAGG
TTTCACCTCTGTCAGCGCAA
TCGCGCCAAGAGGCCCCAGA
AGGAAACATATACGGTTTCG
ACCAGGAAACATATACGGTT
AGTCGTGCTAGTAATTACAG
ATGAAGTCATGGTGTAATCC
TATATATAAACCCAGTGCAA
AAGTCAGGCAGTACATCGTT
GTTGGGCAGCTCCTCTTCGG
CCCCGCCCTGCATAGGGGGT
CTTGCACTAACTCAGGCTAA
TTCACCTCTGTCAGCGCAAC
AGATTATCAGGGGGGTTCGC
CTCAGGCTAAAGTCACTCGA
CAACCGTGGCCTTGGCCAGT
CCCCGCCCCAATCAAGTCTC
GCTCACTCTTTGTCATTTCA
TCCCGCGGAGTGATTCCTGT
CCTGCTACTTGGGGATCCGC
GGGCAGCTCCTCTTCGGCCT
GTATACGCAGTGCCTCTCGC
CGTGTATACGCAGTGCCTCT
AATTATCGCTAGGAGGATGC
TTATCGCTAGGAGGATGCAA
TATCATTAAAATGCCGCAAC
ATAACATCTGCATCTATTAG
GCCTGCTACTTGGGGATCCG
CTAGGGCCCCCGCCCTGCAT
CTGTAGAAGATTATCAGGGG
GCGCAGCTCAACCTCATATA
CGATTTACTACACGTATACT
GCGGCAATAACATCTGCATC
TCAGCGCAACCGTGGCCTTG
CAAATGTATTGAGGAGATAC
CCTGGGCTTGGACTCTAGGA
ATAGTAACGTAATGAACAAC
GTATTGGCCTGCTACTTGGG
TGGTCCGGAGTATTGGCCTG
TATGTCACCTGTAGAAGATT
TCATTAAAATGCCGCAACGA
GGACCTTCCTTCGTAGTCAC
AGGGGGGTTCGCTACCAAGA
GATGTTAAGTCAGGCAGTAC
ACACCTGTGATGCGGCAATA
CAGCTCCTCTTCGGCCTGGG
ATTATCAGGGGGGTTCGCTA
TTATCAGGGGGGTTCGCTAC
CCTTCCTTCGTAGTCACGGA
GAGGATGCAATAGCCTTGCG
GCCAGTGGAGCTAGAAACCT
CCTACGATTTACTACACGTA
GTCAGCGCAACCGTGGCCTT
TAATGAACAACTCTAGCCCG
GCAGGCTTATTTCCATATGC
ACTCTAGCCCGCTACTCCCG
CTTGGCCAGTGGAGCTAGAA
GTGGAGCTAGAAACCTACGA
TATAAACCCAGTGCAAGCCA
TCATTTCACCTCTGTCAGCG
AGCCTTGCGCAGCTCAACCT
CCGCTACTCCCGCGGAGTGA
AAATCGGTTAATCTCTTTCA
ATTTCCATATGCTGCGATTG
ACAAAACGTTGTATACTGTC
TGAAGTCATGGTGTAATCCC
CTACTCCCGCGGAGTGATTC
ATGAACAACTCTAGCCCGCT
ATAGGGGGTCCACAAATTCC
ACCGGTTTTAACACCTGTGA
ACCTGTAGAAGATTATCAGG
CTCAAAAACCTTATGCATCG
TCGCTCGTGCCAGACAATTA
GGGGATCCGCTGACACCTCA
TTATTTCCATATGCTGCGAT
AACCTACGATTTACTACACG
GGCTTGGACTCTAGGACGGG
TGCGGCAATAACATCTGCAT
CTGCGATTGACTCGCAAGGA
GGTTAAGCTAGGGCCCCCGC
CGCAGCTCAACCTCATATAT
ATCGCTCGTGCCAGACAATT
AGGAGCAGGCTTATTTCCAT
AACCCAGTGCAAGCCATTGG
CGATCCGGGCTCCTATGTCA
CCCGCTACTCCCGCGGAGTG
TGCGATTGACTCGCAAGGAG
AGTCAGGCAGTACATCGTTG
CCAATCAAGTCTCAAAAACC
CGTAAACAGTTCACCGATCC
ATTCCTGTGAAACGCTCACT
ACGTAATGAACAACTCTAGC
AATAGACCCTCGAGGGACCT
GGCTAGTGGTCCGGAGTATT
ATTAAGTATCATTAAAATGC
CTTATTTCCATATGCTGCGA
AACGTAATGAACAACTCTAG
TAACTCAGGCTAAAGTCACT
AGGACGGGTGGTTAAGCTAG
AATCACTCTCCCAGGGTTTG
TCACGGACAAACAAAACGTT
ACGATTTACTACACGTATAC
AAACATATACGGTTTCGCGC
CCCCAATCAAGTCTCAAAAA
ATCCGCTGACACCTCATCGC
CATTGGGTGCGACCGGTTTT
ACTCAGGCTAAAGTCACTCG
CTCGCAAATGTATTGAGGAG
AGCGCAACCGTGGCCTTGGC
AGCTAGGGCCCCCGCCCTGC
CAGGGGGGTTCGCTACCAAG
AGTCTCAAAAACCTTATGCA
GTTCGCTACCAAGAAAGTCG
GTTCACCGATCCGGGCTCCT
CGATATCCGTAGTTGCACTA
CCTCATTTATAGATGTTAAG
ATTGGCCTGCTACTTGGGGA
CCTCGAGGGACCTTCCTTCG
GACTCGCAAGGAGGTCTTGC
CTTGGGGATCCGCTGACACC
ATCACTCTCCCAGGGTTTGA
CTGCATCTATTAGTTCAAAT
GCTGCGATTGACTCGCAAGG
GCGTCACGATATCCGTAGTT
CGTAGTCACGGACAAACAAA
TCGTGCTAGTAATTACAGGA
GTGTAATCCCCGCCCCAATC
CACCTGTAGAAGATTATCAG
CGTAATGAACAACTCTAGCC
TATACGGTTTCGCGCCAAGA
GTGATGCGGCAATAACATCT
GTCACGGACAAACAAAACGT
AATTACAGGAGCAGGCTTAT
ATATACGGTTTCGCGCCAAG
AGGCGTAAACAGTTCACCGA
TAAACCCAGTGCAAGCCATT
ACGCTCACTCTTTGTCATTT
GTAATGAACAACTCTAGCCC
AACTCAGGCTAAAGTCACTC
AATCCCCGCCCCAATCAAGT
GGAGCAGGCTTATTTCCATA
TGTGATGCGGCAATAACATC
AAACCTACGATTTACTACAC
CGCCCTGCATAGGGGGTCCA
ACCGTGGCCTTGGCCAGTGG
AACCTCATATATATAAACCC
GGCAGCTCCTCTTCGGCCTG
GTTGTATACTGTCTACGAAC
ACCTCTGTCAGCGCAACCGT
AGTACATCGTTGTGCCATCG
GTAGAAGATTATCAGGGGGG
GCCCCAATCAAGTCTCAAAA
GTGTATACGCAGTGCCTCTC
TTGCACTAACTCAGGCTAAA
TTCGCGCCAAGAGGCCCCAG
AGTATCATTAAAATGCCGCA
CATATACGGTTTCGCGCCAA
GCTACCAAGAAAGTCGTGCT
AGGGACCTTCCTTCGTAGTC
AATCGGTTAATCTCTTTCAA
ATGCGGCAATAACATCTGCA
GCTAGGGCCCCCGCCCTGCA
CAGAGGCGTAAACAGTTCAC
TCTATTAGTTCAAATCGGTT
CCGCGGAGTGATTCCTGTGA
TACTGCGAACCCTCATTTAT
CGGAGTATTGGCCTGCTACT
CTTCCCACGAATAGACCCTC
GCCCGGGGCCCCTGATAGTA
CAGGAGCAGGCTTATTTCCA
CTCCCAGGGTTTGATGAAGT
ACCTGTGATGCGGCAATAAC
CCCCAGAGGCGTAAACAGTT
CGTCACGATATCCGTAGTTG
GCAATAACATCTGCATCTAT
TAACATCTGCATCTATTAGT
GCTCGTGCCAGACAATTATC
TTGTCATTTCACCTCTGTCA
TGTAATCCCCGCCCCAATCA
GGACGGGTGGTTAAGCTAGG
CGGCAATAACATCTGCATCT
TACGAACGCCCGGGGCCCCT
TTCGCTACCAAGAAAGTCGT
GAGCAGGCTTATTTCCATAT
CAATTATCGCTAGGAGGATG
TAAAGTCACTCGAGACAGCG
CAAGTCTCAAAAACCTTATG
GTATACTGCGAACCCTCATT
CCCAGTGCAAGCCATTGGGT
GCCTTGCGCAGCTCAACCTC
ACATATACGGTTTCGCGCCA
CATCGCTCGTGCCAGACAAT
CGCCCCAATCAAGTCTCAAA
TATTAGTTCAAATCGGTTAA
CATCTATTAGTTCAAATCGG
TTAATCTCTTTCAATCACTC
TTGGACTCTAGGACGGGTGG
ATTATCGCTAGGAGGATGCA
GTTGCACTACTTCCCACGAA
GATTTACTACACGTATACTG
AGGCTAAAGTCACTCGAGAC
GCATAGGGGGTCCACAAATT
GGTCCGGAGTATTGGCCTGC
CGGGCTCCTATGTCACCTGT
CCTTATGCATCGTTGGGCAG
TCAGGGGGGTTCGCTACCAA
ACCCTCGAGGGACCTTCCTT
ATCCGGGCTCCTATGTCACC
TTGGGGATCCGCTGACACCT
GGGTGCGACCGGTTTTAACA
GTGCAAGCCATTGGGTGCGA
GATATCCGTAGTTGCACTAC
AGGGGGTCCACAAATTCCCA
CCCACTGATTGAATTAAGTA
TGGCCTGCTACTTGGGGATC
TCAACCTCATATATATAAAC
TTTATAGATGTTAAGTCAGG
ATCATTAAAATGCCGCAACG
CTGTCTACGAACGCCCGGGG
GGGTTCGCTACCAAGAAAGT
CTAAAGTCACTCGAGACAGC
AGGCCCCAGAGGCGTAAACA
ATATATATAAACCCAGTGCA
TATTGGCCTGCTACTTGGGG
ATTGAATTAAGTATCATTAA
TCACGATATCCGTAGTTGCA
GAACGCCCGGGGCCCCTGAT
ACTCTTTGTCATTTCACCTC
CTCGAGACAGCGTTATTGAC
ATGCTGCGATTGACTCGCAA
TGACGTGTATACGCAGTGCC
ACATCGTTGTGCCATCGGGC
GCCAAGAGGCCCCAGAGGCG
ACGGTTTCGCGCCAAGAGGC
CGTTGGGCAGCTCCTCTTCG
ACTCCCGCGGAGTGATTCCT
TCACCTCTGTCAGCGCAACC
GCAGCTCCTCTTCGGCCTGG
CGATTGACTCGCAAGGAGGT
CTCATATATATAAACCCAGT
GCGACCGGTTTTAACACCTG
TCCGTAGTTGCACTACTTCC
TCCCACTGATTGAATTAAGT
CCTGTGATGCGGCAATAACA
GTATACTGTCTACGAACGCC
TGTATTGAGGAGATACCAGG
ACAAAGCGTCACGATATCCG
TTCAATCACTCTCCCAGGGT
TACCAAGAAAGTCGTGCTAG
CATAGGGGGTCCACAAATTC
TATAGATGTTAAGTCAGGCA
GGATGCAATAGCCTTGCGCA
TTGCGCAGCTCAACCTCATA
CCAGGGTTTGATGAAGTCAT
TTATGCATCGTTGGGCAGCT
CCTCATCGCTCGTGCCAGAC
AGAGGCGTAAACAGTTCACC
ACTTGGGGATCCGCTGACAC
TCGCAAATGTATTGAGGAGA
CAGTGCAAGCCATTGGGTGC
AGGAGATACCAGGAAACATA
CGACCGGTTTTAACACCTGT
CTATTAGTTCAAATCGGTTA
TCAAGTCTCAAAAACCTTAT
ACTGATTGAATTAAGTATCA
AAACGCTCACTCTTTGTCAT
GCAAATGTATTGAGGAGATA
TCTAGCCCGCTACTCCCGCG
ACAAACAAAACGTTGTATAC
GAATAGACCCTCGAGGGACC
AGGAGGATGCAATAGCCTTG
TGCCATCGGGCTAGTGGTCC
GAGTGATTCCTGTGAAACGC
AGCGTTATTGACAAAGCGTC
TCATATATATAAACCCAGTG
TGTTAAGTCAGGCAGTACAT
TAAACAGTTCACCGATCCGG
TTGAGGAGATACCAGGAAAC
CAGGAAACATATACGGTTTC
CAGCGTTATTGACAAAGCGT
TCGCTACCAAGAAAGTCGTG
CCCGGGGCCCCTGATAGTAA
GAGTATTGGCCTGCTACTTG
TCAAATCGGTTAATCTCTTT
TTTGATGAAGTCATGGTGTA
GCAGTGCCTCTCGCAAATGT
AAAACGTTGTATACTGTCTA
AGTAATTACAGGAGCAGGCT
ACGCAGTGCCTCTCGCAAAT
AAGAAAGTCGTGCTAGTAAT
GGCAATAACATCTGCATCTA
GCATCTATTAGTTCAAATCG
ATTACAGGAGCAGGCTTATT
TTGATGAAGTCATGGTGTAA
TCCCACGAATAGACCCTCGA
GTTGTGCCATCGGGCTAGTG
AGATGTTAAGTCAGGCAGTA
GTCTACGAACGCCCGGGGCC
GTAGTTGCACTACTTCCCAC
GATCCGGGCTCCTATGTCAC
CGTTGTATACTGTCTACGAA
CTTTCAATCACTCTCCCAGG
ACGATATCCGTAGTTGCACT
CCCCCGCCCTGCATAGGGGG
GGAGCTAGAAACCTACGATT
""")
