def Translation(a):
  novi = a.replace("T", "U")
  kmers = []
  kod = ""
  for i in range(0,len(novi), 3):
      kmers.append(novi[i:i+3])
  for j in range(len(kmers)):
    if(kmers[j][0] == 'A' and kmers[j][1] == 'A'):
      if(kmers[j][2] == 'A' or kmers[j][2] == 'G'):
        kod += 'K'
      else:
        kod += 'N'
        
    if(kmers[j][0] == 'A' and kmers[j][1] == 'C'):
      kod += 'T'
    if(kmers[j][0] == 'C' and kmers[j][1] == 'C'):
      kod += 'P'
    if(kmers[j][0] == 'C' and kmers[j][1] == 'G' or kmers[j] == 'AGA' or kmers[j] == 'AGG'):
      kod += 'R'
    if(kmers[j][0] == 'C' and kmers[j][1] == 'U' or kmers[j] == 'UUA' or kmers[j] == 'UUG'):
      kod += 'L'
    if(kmers[j][0] == 'G' and kmers[j][1] == 'C'):
      kod += 'A'
    if(kmers[j][0] == 'G' and kmers[j][1] == 'G'):
      kod += 'G'
    if(kmers[j][0] == 'G' and kmers[j][1] == 'U'):
      kod += 'V'
    if(kmers[j][0] == 'U' and kmers[j][1] == 'C' or kmers[j] == 'AGC' or kmers[j] == 'AGU'):
      kod += 'S'
    if(kmers[j] == 'UUC' or kmers[j] == 'UUU'):
      kod += 'F'
    if(kmers[j][0] == 'U' and kmers[j][1] == 'G'):
      if(kmers[j][2] == 'U' or kmers[j][2] == 'C'):
          kod += 'C'
      if(kmers[j][2] == 'G'):
        kod += 'W'
      if(kmers[j][2] == 'A'):
          break

    if(kmers[j][0] == 'U' and kmers[j][1] == 'A'):
      if(kmers[j][2] == 'U' or kmers[j][2] == 'C'):
          kod += 'Y'
      if(kmers[j][2] == 'A' or kmers[j][2] == 'G'):
          break
        
    if(kmers[j][0] == 'A' and kmers[j][1] == 'U'):
      if(kmers[j][2] == 'A' or kmers[j][2] == 'C' or kmers[j][2] == 'U'):
        kod += 'I'
      else:
        kod += 'M'

    if(kmers[j][0] == 'C' and kmers[j][1] == 'A'):
      if(kmers[j][2] == 'A' or kmers[j][2] == 'G'):
        kod += 'Q'
      else:
        kod += 'H'

    if(kmers[j][0] == 'G' and kmers[j][1] == 'A'):
      if(kmers[j][2] == 'A' or kmers[j][2] == 'G'):
        kod += 'E'
      else:
        kod += 'D'
      
  return kod
      
print(Translation("""AUGAGUUGCACGGGCAGACUGGCUCGUUCUGAUCGGACCUCAAAUGGGACACCGCCGGUCCCAGGCACCGAGACCAUUUCCCUAUCGGUGAGGGAUGCUAAUUGUCGAAUUACAGCCCGACACAAAGUGUUGGGCUUUCGUGCAUCAUAUCAACCGAACUCUAGGCCUACAGAUCUAAUGAAAAUCGGAUCUAGCGUGUCGCGAAAUGUCUUCCUGGGUAAGGCUUUUAGAGUGACAGAGGACCUAGUUGGUGCGGCUGCGUCCAAAGAAAAUUUCAGCGCGUGCAAGGUGUUUAUUGGGAUCGUUCAUGGAAAGAAAGAUGGUGGGUAUAACGGUUCGGGUUUGCAGAAAGCUAUUCAUCGCCACGACACAAGCGUUGCACAUACUGGCCGCACGCGGCGUUGGGGACCUAUUGGUUCACGAGUCCGGCCCUUGAGACUAAACUUAGCUCAGGAUGGCUUCUGCACUGUCAGGUCAAUUCGUGCCCCCGAGACUAAUGAUCCAUUCCGCCGCCCUGGUUGGGAGGAUUUUGGUUCACAUUUGAAGCAUCAAGGUCAGUAUCUUUCCAGGCCCGCGAAAUCUCAAGAGGCAGACCAGCGGUUGCGGCUCGCAAUAAGUUGGGUACCUACCCGGUGGAAUCGAUGGCAUGGAAGCAUCCAGGACUUGCCCACCGCUAGAUCCCUUCCUAUGGCAAUUUUUCCUAUCACGUCGUUAGGAAUUUCCGUGCCCAGGCAGCAUAGAGGCCGAGUAAAUUGUCGCCAUGUCCGAUCUCUGACACGGCGGUGUCGACACAUUUCCUACACCAUUUGCAACUCCCAAGUAAAAGGCCAAGAAAAGCAAAAUGUACCCAGGGAGGUUGAAUCUAGAAUGAACCCCAAGAAUCUCGCAAUGCGAAAAAACUGUUGCGUGGCGCACAGCAGCUCGCGCCCGACCGCACCGAUACUGGUGAACGGGUACCCCUUAGGCCGAGAGUUGGAGUCUUUUCCGGCUCAUCCGUUUAUGAUUUAUACAGCUAACCUUAUGAACUCACGCGCAGGUGACAGCGACCCUCCGUUCGUACAACAUAUCGAGUGUCUCCACCGGCUAGUCUUCUCCAUACUGAGACUUCUGCGAAUAUCCACGCUUUGUCGGUACGAUCCAGCCUGGCCUGUGCGGUGCCUACGGCGAACGGCGAAGAUUACUAUAAAUGUGCACUCCAUGUACAAGAUGACUUAUGGCAUACAUCGUCUCACAGAGAAAUGCGGUAAGCCGAUGUGUUUGGUCUUAUUAAGCGGGGUUUGGAGAAUAUUAUCUGCAUACUUAAUGACAUCUGAAGCAGUCACAUUCCGCGUCAUGAGGAGCUACCUAAGAAUUCCAGGUACCGGGGAUACAGUUCCUUCAGAUGGGAUCUUCUGUUCCGUACUUCCAAUGCUCGUAAAGGGUUUCACGGUCGAGUUAAUGGUGUUCGAACGAGUCAGUACGUGGUUUAACCCAAGUAAACGAAGGACAUGGCAUUGUCAAAGACCUGGGCGUUUUGCGGAUGAGUGGAGGGGAAGCCCAAACGUGAAAGACGUCCGCAGUGACGAAUUUGACAUAGAGGGGGUCCCGGUCGUUCGACUAACAUGGGUUAUGGUGACAGUCGAUGGCACUGCACAGCAAACGUCAUUACACCAGCCCAUGGUUGUAGCUCACCCCCUGAUGAGUUCGUUUAAGUUAGUACGGCGCAACAACAACCAAGCGGGCGCUUUCCAAAAACAUCCCUAUAUAUUGCUGGUCGGCUCCGGGGCCCGCAUCGGUUAUUGCCGCUAUGGGAAGUCACUCAACCGCGUUCCAUGGAGUUCCAGUCCGAUCGUAAAGCGUUCGUCAAAUUGCUAUAAUCGACCGUUACCGCGAGGUUGCGCAGUUCAGGCCGUCACUUCUUCUGAUACGUUGCUUACAAUGUUCAUAGAAGGCCCCUUAGGGAUGGCCUCGACGCAAAAGCAUUUUUACUUGAUAUGUACUUUCUCACCGAGCCUCUGCGUGCAAAAUAAUCUUAUCGAUCUUGCGAUAAUGGCAAGGAGUCCCGAUCCCUACCUUCUAUCGGAUUUGACCGCACUAAGCAUAGUCAUUCAAGGACGGAUAGGGGCACUACGCUGGUCUGUAAGAGCCAGUGGCGUACCGAGUACAGUAUUUUGCCAUUUGCAAAGUGGAUACUCAGAGCGUACUGUCACUCCACCCCAACACCUGCCGGACCUAUGCCUAAGCUUAGUCGUGAUAGAGACUCGCGUGAACCCGAUCACCCAAUCUCAGGCGCGCGCUUUACCGUUUUGUAUUCGUAGGAAAAAGCCGAUGCGACAGACUACGAGUGCGUCAAACGGCUUCAUCUGGGCUGUUUACAGUGUGUAUGGACUUUCCAGGGGAAAGCCCCAGGUACGUGGGGAAAACCCUGGUGCUACUACACUGCGGCGGCAUAUCUUCGAAAACAUAUAUCCUAUCGGCUCCUCAGCCGUGCUUAGCGAGGAUUUACAACUGAAGUCCGAGAGGCUUCUCAGUAGUGGUAGGCGCGGUACGUUCAUCGGAGUGACAGGCGGCUAUAGUUUAGCGGCGUUGGGUCGGAACCCAAAGAGUAUAGCUAGGGCUCAGACGCGUGGGGUGUCGUCACGUGAUGAUAUACAUGGAUCUUGGAUGGAUGCUGGAUGUUCGGCAAUUCGGUUAACCUAUAAGAAUCCUCAAAGUCACUAUUACCGUCUUCCUGCGCUAACUGGUCCCUCCGUGACCUGGGAAUGGGAUGCCGCCGGAACAGAAAUUAAUUGCGUUAGCACUAUCUUGCUAAACACGAUAAGACUUGCUUCGUGUUUGGGCCUUAGACCAGCCGAAUCUAAAAGAGGAAGACUUUACUACCGGGGGCUAAUGCGGCGGUUAGCUAGAGUUCUAUUGCCCUGUGUCAACACCUCAAAUAGAAGUAAGUCCUGUUCCCUCCAGGAAAAAUUCACGAUGGUUCGGCGUGUGCUCAUUACUUGUAGGUAUGCGCCUACCACGAUUAUCCAGUGCUGGCCCCUAGGCGAGUUCUCCUCGCAUGGAAGCCUUGUACUCCUCAGUCAGGUUGACCAAAAAAUCUCUCUCUGGCGCGACCCUCACUGCCGGUGGUCCACCGGAACAGUGGGUGAGCUCGACCUCGAACGAGGACUCGGAGGCAGGACGUCGCUCCUAAAACAGGAAGAGCGCCCCAUACGCCGCAACGCCUUUCGUGAGCACACUUCCCUGAAGGCUUACCGCCACCGUAACGUCCACUUCCGCAUCGGACCGCAGUCUACCUCAAUCUUGUACUGUCUUAAUAGUCGCACGCCGGGAGGUGAGAUAGUCCCUGUCUCUGACUGCAUUGGGCGUUUUGCCUGUGCCAUACAAUCAGUGGACGCGAGCUUCUUUAUCUUAUCCCAGCAGGGCAAUUCUAAGGUGCCCUUACAGUUCGCCGCAACGCAUUCUGAACCAAGGAUGACGUGUACUCGUAAUCUUGAUUUUGGAACUGACUUGUCCAGCACAUCAUUGCGUAGUUGGAUUUGUCAGAAAUUCGUCUGUCCACAGUCCGCGGGAGGGGACGUAAGUGGGCUCGUUCCCUACAGGUUCAUUAAGCACCUACUGACCACUCCUCGGAGCGGACCGUUCUGUCUCGGGCUAAUAUCACCUAGUGAAUGCUCUGCCUGCCAUCGACCACCGUUUGAUCUCGAAAUAGAAGUUCAGCACACACUCAAGGCAACAAAUAACCCAAGGGCAGGCGUCGAAGUAAUUCAUCACAUGCAUCUCCUCAGAUCUAGUAUUAUCGCGACGUUUUGCUGGGCGAUACACAGCGAUGAAGCGGAAUUUUUUCUAUUGUGCCGUCGUAUUGAGAAAGAAGCGAGUCUGGGUUCUUGCCUUAGCAUGGUUUUAAUAAAAACCGCGUCGGUCAUAGUCAUGAAGCGAUUUGACCGGGGAGCGACCACUGCAACGGACGUUGUGGCGCCUGUAGGGUUAAUUGAGCUCGAACAUGGACCACCCAAGGGGGUCACGUCACUGCCCUGCCUCCAAAACGACGGGGCUGACGCGGUCCUUAUACGAACGCACCUUGUGUCUACAGAUAGCGCGAUAACGUUGGCUACCUACACUUAUCGUUGCUGGGCGAGAAGCUCAAGCAGGGUUGCGCCGGCACUUGGCACGUUCGAAUUAAGGCGUUCUUUCCCGGCCUUCCCGACCCCCCAACGUCAUCGUUCAGUACUAGUACGCAUGUUGGAUCAGACCUCCACUCACAUCUCUAAAGGUAGCACGAAAUGCAACAGGGAUGCUGUUUCAUCAGGUGAGCAAUGGGGCGGAAGAUCUCUUUGUCACGUAGCGACUACACCCUUAGCAAAAACUAUUAACGGUGAUUACAUUGGGCAGCUUCCAACUAGUUUUGUCGCGGGUAAUAUGUACUGUAUUAGAUGUGGACUGUCUCCACUAAUUAAUUUUUGCCUGCCGUCCCUCUCGCCCAGCUCGUCGGCAGAGAUUUACCUAGUAGUUCGUUGCCCGGGGCGUAGCGGUCAGUCAGGACGGCAGAUAACGUGUUGCCCGGGCCAUGAAUGUAUAUCGAUGUCAGGUCAGGCCCAGGUUGGUAAGAGUAGGUUGUUUGUGUCUGGUCCCGUACCCCGUGCUCAUCGCCACGAGGCUCCCAUUCAACCAUUCCCUAUAAUGGUUCCCAUCAAGCUCUUGGUUCCGACUGCUGGUCAACGUCGCGGAGGUUUUUACGGGUUAAUCAGUAGUCAAAACGUAGAAAUUCCAAUGUACAGCCUUGGGUACCAUUUUGGCACUGUAACUCGAGUGCUGACAAAUAAGAAGUCCCGACCACUUCCUAACAACGGCGCACUCGCGAGAACGGAACGUCAAAGUACAACCACUGAUCCCAACUGCUUGGGGAAGUGGACAUUGACUGAGGCUGUCGUUUAUUCCAGAUCUAAAAAGCGCUUCAUUGUGAGGUGCCUAUACCAGGUAUUAACAUCACUUGUUAAGACAGAACCCCGCGGCUUAGCGGCUGGCCUACCCGUCGACAAACCUGAAAUACGGUGCGCGAAAUUGUUGUUGACGUUGACUUCCUGGUACGAGCACACGGUUUAUACGGUCAUACGCGGACAAGUAGCCAAGUUUCCCUUUAAGAUGAGAGCAAUCUCUCCGCAAAAGAUCGCCACGGCUCCGCUCAUUCUUUCUUUGACACGUAAAAAGAUUACCACCAUGGGGAUGAGAUCGAUUUCGAAUCCGUCCGACACCCACGCAGAGAUAGUCUUUUCACGCUCAAUAAUGCACGAGUUCAUGGUGAAAUGGGUGAAACUUGGGGAGUGGACUAACUCAUGGCUCCGUGAUCGACCCCGCGACGCUAGUGCUAUGGCAACUCGUAGGAUAGGGAAGCGGAUCUUCUCGGGGAAACGCUGCCAGCUGUCCAAUAACGGAACAGUACCGAAGACGCUCAUCGAUUCAAAUUCCCUCAGAGUUUGUGUUAUUUUCUAUGCUCACCACCGCGAUAUCAUCUGCCAUGACGGUGCGGCUGUAAUAGUUUCUUGGCAUAAGAAAGACCCACCGUCCAAUCCACUCGAGGAGAAUGCACCUAAUUCUGCAGUUAAGCUCGACCCGUCCUCAGGACCUUCUCGUGCCAGGGUAAGAUGGAGGCGGAGCACGACCUCCGCGCCACAAAUGAGAGGUCCCGUCAAUGAGUCAGUCGUCCGCGAAGGCGGUAGAUAUUGUGGGGCUGCACGGCUGCGGUACAGCUGUUUUGGGUUGAAGCUAACACGGUCACCUUCGAGUCAGCCGACGGGUCUCAGCAGGUUUCUAACUCCCCAGCGGGGAAUUGAUACGCCCGGAGCCUGGCAACCACGGCGAUUUUUCACAUGCUUAGCGAGACAGAGUUCACCCUCGUGCGCUAAAGGGGACUUUAUAGGGAAAGUUGCGCUCCGCGCCUCGGUUACUGGUAUAGGCGUGAACGGGACUAUGCCAAAGACAAGGACUCGAAGAGAAGCUCAACCCCGUAGGCUGACGGUGGUAAGGAGCUGGCUAUACCGACACCUCUGGUUUAUAUAUUAUACACUAACUAGAUGUUUGUUGGCGCGGCACGGACUGGCCAUAACAGGGUCGCCCGGCUGCCAUUGCCAAGCGUUACAAGAUGCGUCCACUUUUAGGCCUCUUGGAGGCGUCAGGCUGGACAUCUUAAUUGACCAGACGGAACAGUACACCUCAGUCCCCGUGGAAUGGCGUAACCCAAUCUUGCCUCGUCAGAUUAUUGACAUAUCUAAAUUCCGCGCUAGACAACUAGUUGGCCAAAGUCGAUCAUCUGCGUCGAGCUCUCGGAAGACCAGUGUUCACACCUCGUAUAGGAUCGGUUACAUUGUUUUAACCCCUGAGUCUCCGACCCGACGUGCUUGGGAGGAGUUGCGCGCAAUUUUCGAUUCGCACAGACCUGCUCCACAAUCGUUGAGUUUACUGGUGUUCACCCUCGUACUAUUCUGGGAGGUCGUAUCCCCAGCGAUGCAGCGAAGUAUAAGACGCAUAAUGAGAAGGAUACCGAGACUGCGAAACAAGGUUGCUAUAUUGGUGCCUCGAUCCAAUCCACUACGCCAGAGCCAAAAAUCUGAAAUACACAUGCGUCGUAUGCUCAUGACUUUCGUUUACUCGUUUAAGAGACACAUCCAACGGAUUCCUGUGUUAACCCUAGGGUCCCGGCCUUAUCUCGGCGAAUGGAAUCCGUGCCGGGGAAUGUCUACAAUUUACUGCAGUUUUGUUUGCAUUGGUAGCAAAACUGGAGAGAAUGACCAUCUUCGACGUAGUUAUCGGGGACUCGAGCCAAAACCAGCAGCGUGUUGGGCCAAACAAUCGAUUGAUGGUCCUACUUCGCCCCAGAGAUCAAUAAGCGGCAUGGGUGAAGGUCCGGGUAUGGGCUCGCACCUCCCGUCGCAAUUACAAGUGGUGUCAAGCCCCUUUCUUUGGUAUUUGUUCGCGUGGGGAACAGUAAUGCCCGUUCAAGUUACUGUGGAGGAAAGGCAAUUGAGCCCCGUCCCCCUCAUGGUCCUAUACUAUUUAACUCGUGUGCGAACAGCGGCAUCAGACGAUUGGGGGGGGAUCGCACUUAACAUGGUACAUCCUUCAGAUCGCCCUUCGGGUCCCCUAUAUCGUUCGCAGAUUGAAAUCAGAUUUUCAAGAAGCCGUCCAGAAAUAUUCGGUCCUACUGACGCUCAAUUAAAUCAAAUGCACUCCCUAAUAAUGCCGUACUGCAACUGGUAUACCUCGGGGCGAAUCCAUAGUUUUGACAAAAGAAUCUUAUGCUUAGGGUAUGAAAGAAUUCCGUGCUUCGAGGUGCGUCAAGUCGACCGGUCACAGCUAUCUCCAAAGGCUGUAAACGUCCACCGCCGCGAUCGCCGUGGGUACCUCUGGAGACCUGUCAGGAGGACGACGUACGGCUACCCGAGCCUCAAUGACCGAUUGCGAGUCCUAAGAGUACCACUACCAUCCAAUCCUAAGUGCGGGCACUACACGCCUCGGACGCACUCCAUCUGGAUUUUGACACAGCCUGCGGGUGAAAACUACCCGCCCGGUUCUCCGGCAGGGAUGCAGCCCGUUCCUAGUUCAGUGCCGGGACUACAUGUUUAUACACAUUCCGGAAAUCUCCUGACGCUAAGCCCACGGAGAGUAGCUUCUUUUCGGAGGAUACUUACGGCAGCCCUAAAUAAUCGCUGCCUUUCAACCGCGUUGCACAAAAGUCGACAUGCGUUCGAUACGAACGAACACGCCUUGCCGGUUCCGUUGACAAUCUUUACUUGGUCACUGCACACGCCAGGGAAAAGAUCCUGCCGGUGUCGUAUUAUGUAUCCCUCUUCGAUACACACUGGGUUACCAGAUUCACCGGCGAGUAUCUCUUGGAAGGCCUGCCGAGUGCGUGACAAACGUCGGCAUGAGAGCCCGUCGGUCACCCGGUUCCCUGUAACAUCGGUAAACAAGUGGUGGUGCGCUGAUUACCGUCACUUAGUACUGCAUUCAAUUCUAUACGUGUCGGGAUGGGUAGGAAGCGAAAUCAAUAAAUUUCGGCAAUGCGCUCAGGAGCGAGCCUUCUCCGAGAUGCAGAGAACUAAUCAAUCCACUCCGUCACACGGGUCACAUAAUAAAAGUCACCUCUUUAGGGCCAAGGGUAACCUCAGACUGUUAAGUAAGGCCGGCAGGCUAAUUUCUAAUGCGCUGCCGAUAUGUCCCGAGUCUCGCCCUGACACUACAUUGGGGGGGAUGGAGUGCUUUGCGAACUCCAAAAUAAGGCGAUGUUGCCACCGAGGUAGAGUGAGCGAAAGUUAUAACCUCGUAUUGUUUCCAAGGACGAAGGCGAAGACCUAUAAGCAUCCCGCAACGACCUUAAGCGAGCUGAACUCGGGCCUCACGUUUAUAAAGGCUGCCCGUUUUCCAGGCGGCUCGCGUUUGCAAGUUCGUGAGGAUGGUGGUGUAUAUCGAUGCGCCAACGGCAUGCUUCCUUUACUUGUAUUAUUGAGGCCUGGGUGUUGGUGGACGGAAAUCGCAGUCAUACCCAUUAUACUGGGUGAUGACUCUAAAAAAUGCGGUGGGUUACAGCACACCGAGGACUUUGAUGCCAACAAUACACCCUUUGAUGCGAAGUUUACGGAAAUUAGACUGCAUUGCCGUCGAUAUUACACCAUGGUAGGCGUUCGUCCGGCCACCUUGCUACCGGCCAGAACGACCCCUCCGCUGUGCGUUACCGAACACUGCAAGUUCCUAUUUCGUAGCGGAAUCGGUGUUGUUAAAUCCCAUGAGAUUAUUGUCUCUUUAACCGAUGCAUUCCCACCUUGCGUGUCGCAUAAUCUAGGGCGCACGUUGUUUUGCUUGGGAGUAUCAACAACCGUGCUCGGCAUACCACAAACGCAUAGCAGACAUAAUGGGUGGUUGCUAGGGCGACACGUCGCCGCGCAGGCGGUAAUGGCAUCAUGUUCUCCUAACAGAAGAGUGCUGAAAAGAGUAAUUGGCUUAGGUCCCACUCGUUCGAGAAACUUGACUUUUCGUGAAACACGCCAGUUCAAGUGGCCUGUCCAUAUCCUAUCCCCUCGCAUCCAAGUUAUAGGGAAGCGUCUGCUUCAAGAUCCCUGGAUACAUCGGACAAAGGCACUGGAAUUCACCAAAAUCAAUUGA

"""))

##provjera di je greska

##def mismatch(a, b):
##    indices = []
##    for i in range(len(a)):
##        if(a[i] != b[i]):
##            indices.append(a[i])
##    return indices
##
##print(mismatch("""MPMGLVWHKQGPLERISIRGVIGVRSGYNETIRRNWVMLVSKSALFVSTCCQCNPPYLTCYKQLKSPDVTRFARAQDMDQFRDHTQMAGRTNLEQTFCAQPVQLTMDLEYYQDPPVAYVLQYMVPRRMPALSVITNPPNQELQSLWSYLQLSVSQISRGRLTCVTLLLVIWDNQLLRYSYLCQAFEMVMSSNIRSLGAETLKVLTDPNRECASVTIPQLTQQSALSIRAPPRYLHTELRRCRTSLARTTLRFVSSCTSRFGASIPSFQELYCSLYTGLSFVQISRSIKNAVDQTCGKPIDNTQIVISFQSSRLQRCSLIARLQADRTFFLYKRGWCRGVCSIVIYLTGICYVKLCCYATGISTVSDSYKPRGYVQLQVFLFRHVTVYVIRTYENSVTGASRYQADYIMGRDLPTLVDSLPVVSYSWNQYLLLVCGPRRGDLLWPLLGRDPTVKFKPRTYRQRRSFTAFMTRKCVSLWAQLTARRRTSRKLIRALTHGWKMRMSRHAVVYTGIEGILGSKTELTVPTQPLYILLPCSGPSCVLMTGVRPFWSSSQDSRWSTTIRPEGGVLSVSCRQIANSTFSVLESLGLFIEVRHGHGKIPLYRSSTCSNCSQVCQSNEWTAWFLNSPAAGPNQCQIVYNTKYCIAGYAPSPLLSTARAASYRYKCSWYFLLLFLTCSLISGQFLEPGIMKCALGMLKVGSECNLDEPHVSSTAGYHGHVNTLCCIIAVSPPLSLRVKRPAGRVVFEIGPACDQDGGQLASNIVITRNPTGWHPWTSRVSALTIRSLQCPQCVNEGWHWSHPEPGQMGRYLHPNSIPYEACVSTYTIAEKFSVQFSTRSIDWECPVRILATYTRQLELRCLTGTCFSYWNTPKIPTVTPQVARKSKETDRNASIQPPMAATVPATGLSKQWIVIQSSRDLRTDDEMDTTFQTQRYGFGISTTECYTLPSLYSAPKSRNTHTCHASPSNDSWSCFKLCGVSIRDRKRRVWTASRCNDLASEKGGRQGTPPTRIPPSLPRKTTQTGAANLAYWSQFINGDKSPDGYTKQVGTDAIYAARVQAHSLTCSRLSRIVCSGSAVGWDGDDFRESDVDRECEVTSGPRPQRFCIYIMSSVSTDGGVCRKIWIFHLLSNSCRSLFSPSSDREQKLGIMAQAEVFCHALSKFLFRLCSISSLRALSSYPRSGRVLSIVTNIPQWDSRPRLRIDYQQFTPIFQNPPGKLLQPNDTCLGCSNCLQSSPLLFTRAGLLGLFRTMAPITYGCMTRSAWSSLQRGGPLDVILSTSRATLFKRCVRSRFRNPCGINVLTNFHEPRALLFSAPRGNPSYTVMFASTAATCERLALARQRTYSRFLFERTRKQALKGRTSDQDGLSAGVTWKGVNSGRYLYSTCRQGLRRLIRTMMKQIGRLFYRTRCTLLVHRDPGAEHYLSTPIVKQGRGYHRRTRLPFLLFYDQCPARGVPLLVRLVTNALSPYITMSYACQTCNRAQESVSLLPSTCAYPYRSINSDPVGAWKVGSLNTHYICKLPKVSPPRWASSQQIASTVVRSDTQSRDESINGQGRLKVAIIVCRVTARSVAEVGGYWKKRHRSPRSIFDMKNRDTWHDGGRGPTSSSDQYYPITGIPVLSTPSRRPQARLTIKSSSIWAYRDQPMLTQPCITYPVLLLQWAVASRMSAISGIRLAGLWGAANAPVQLFLYLSQCAHLGTYCVYHEMGPMYMVLPNQRRLRRFSLGGQILCYPFRTTYSRAVVRPYPDTPQGYSGNGVNTGFLRRWPGPVPCLWVKGVAHHASKLRWKTLACTALSLPALPSHPGLLKSLLKRGEVKKLEAARTVLRALQPHRTNGGYTKELGQEEEHWFRYSFGGTIGALYDRKVAVWYRSSQVIYNGPIYRLVQEPSCASPITLFSRVLLNVVSYLEITVKRQLFTPNTIPGRGLSQRKGALFFLIPPYPSSFELIRKPYRRTQPAFPGSLGDDPLLPCICRSKLRLRRITVYGSSRPVEDVGTTESRCPKTFYSLPLALCWCRSTGVGIYGYLEPDYPYYTRRAPAIPIWRHPVYRAFVQLTLAQATVPGPKPFLLLPVGTGPFIKIFGRHGFAVLAAVRYCTLCSDPIRGPDSRLSLVTESARQVLTPVEYTDLQLCSLGSIQKSKRLSRLSLTKFDELAARTNARFVRPVGYQQVKPRVIETETPYRTYRPNPPTDVDEEHKQRLLAVKRYIGFRGTLSDRPQAALIKGECKASRSGQLLEIQRGSERLDCRITLTLLKDPLGYFYGVDSQPPAVQLSYDAFSQLIKNRCFRNYKSRAFQGTNVARKSIWDRSSDPGLREPLCWTLDKRWAKYTQQPQPCQPVPTSNVFECRRGQTEVRQNALVYSPTFANFRVSADSTVLLPATGSLIVPSGRSERNPDYHAPCSLCPNLNSGLPGRIVGTPRTDKRRAVTQLRVSEASCPQRNRSPDSCALGKCPLPLDNSTSRFCGPCAQYSDLTTFLRLLFSQTSPDGRFFQQIIAVLKVGKCIRATAALNPASYLASRAAQSGNIVEGQRGPILSRSMLVKRNWRCHGSLPCNRTTGETLTILGIMYGSVGGSRILQAVVQSVARRAPQATDGFGQLLTKPFVRARTSEEDKGWVVTSIFPRRNAYDPLGKVGPTWRTPGYRMIPQADKWGIGPTNGDTANCVGGCLRVICPSRASKQHAAICLSGTSFARVGKGREEKVRQTESQAWTRFNLGNARRGGVDQILRKLTIDRGGLRGHARISTKYRPRLQRNATMAGKDTRQYLSAFKFELATRAYRSALILWELIQRSTRTLAYSTGRIELPTTVPHSSPGVVLLGVVNLRGEATQQALFSYLDSTTPYECLDIAPNSWFTSESSWPRSDAILSYRLVNDPAELLSAGPSTLSHPLCGSIGRSLTRGDRLTKDYYVVHNLSSSLTRLDRQSSATRSLRPCLWVTTENTIYLQRTCFYSDWDCMRCLSDKGGYDGNYSRVTAYHYCRPKVHDEATVLYKLKGTPIRFGPAHNHRGALALRPVETTPLRTSPEYVEHPYDEESNTGRGAARQEGLEVQLIAGQYDAWQCMDNWTVHISRLCTGVQSPPLARRVSYLGISPDIWGQSFSFRYTWPFKSSTGAIDWRHGLYSFLSTLIIGCCSRALTERSRRGPAR""", """MPMGLVWHKQGPLERISIRGVIGVRSGYNETIRRNWVMLVSKSALFVSTCCQCNPPYLTCYKQLKSPDVTRFARAHDMDHFRDHTHMAGRTNLEQTFCAQPVHLTMDLEYYQDPPVAYVLQYMVPRRMPALSVITNPPNQELHSLWSYLHLSVSQISRGRLTCVTLLLVIWDNHLLRYSYLCQAFEMVMSSNIRSLGAETLKVLTDPNRECASVTIPHLTQQSALSIRAPPRYLHTELRRCRTSLARTTLRFVSSCTSRFGASIPSFHELYCSLYTGLSFVHISRSIKNAVDQTCGKPIDNTQIVISFQSSRLHRCSLIARLQADRTFFLYKRGWCRGVCSIVIYLTGICYVKLCCYATGISTVSDSYKPRGYVHLQVFLFRHVTVYVIRTYENSVTGASRYQADYIMGRDLPTLVDSLPVVSYSWNQYLLLVCGPRRGDLLWPLLGRDPTVKFKPRTYRQRRSFTAFMTRKCVSLWAQLTARRRTSRKLIRALTHGWKMRMSRHAVVYTGIEGILGSKTELTVPTHPLYILLPCSGPSCVLMTGVRPFWSSSQDSRWSTTIRPEGGVLSVSCRQIANSTFSVLESLGLFIEVRHGHGKIPLYRSSTCSNCSHVCQSNEWTAWFLNSPAAGPNQCQIVYNTKYCIAGYAPSPLLSTARAASYRYKCSWYFLLLFLTCSLISGQFLEPGIMKCALGMLKVGSECNLDEPHVSSTAGYHGHVNTLCCIIAVSPPLSLRVKRPAGRVVFEIGPACDQDGGQLASNIVITRNPTGWHPWTSRVSALTIRSLQCPQCVNEGWHWSHPEPGHMGRYLHPNSIPYEACVSTYTIAEKFSVHFSTRSIDWECPVRILATYTRQLELRCLTGTCFSYWNTPKIPTVTPHVARKSKETDRNASIQPPMAATVPATGLSKQWIVIQSSRDLRTDDEMDTTFQTHRYGFGISTTECYTLPSLYSAPKSRNTHTCHASPSNDSWSCFKLCGVSIRDRKRRVWTASRCNDLASEKGGRHGTPPTRIPPSLPRKTTQTGAANLAYWSQFINGDKSPDGYTKHVGTDAIYAARVQAHSLTCSRLSRIVCSGSAVGWDGDDFRESDVDRECEVTSGPRPQRFCIYIMSSVSTDGGVCRKIWIFHLLSNSCRSLFSPSSDREQKLGIMAQAEVFCHALSKFLFRLCSISSLRALSSYPRSGRVLSIVTNIPQWDSRPRLRIDYHQFTPIFHNPPGKLLQPNDTCLGCSNCLQSSPLLFTRAGLLGLFRTMAPITYGCMTRSAWSSLQRGGPLDVILSTSRATLFKRCVRSRFRNPCGINVLTNFHEPRALLFSAPRGNPSYTVMFASTAATCERLALARHRTYSRFLFERTRKHALKGRTSDQDGLSAGVTWKGVNSGRYLYSTCRHGLRRLIRTMMKQIGRLFYRTRCTLLVHRDPGAEHYLSTPIVKQGRGYHRRTRLPFLLFYDQCPARGVPLLVRLVTNALSPYITMSYACQTCNRAQESVSLLPSTCAYPYRSINSDPVGAWKVGSLNTHYICKLPKVSPPRWASSQHIASTVVRSDTHSRDESINGHGRLKVAIIVCRVTARSVAEVGGYWKKRHRSPRSIFDMKNRDTWHDGGRGPTSSSDHYYPITGIPVLSTPSRRPQARLTIKSSSIWAYRDQPMLTQPCITYPVLLLQWAVASRMSAISGIRLAGLWGAANAPVQLFLYLSQCAHLGTYCVYHEMGPMYMVLPNQRRLRRFSLGGQILCYPFRTTYSRAVVRPYPDTPHGYSGNGVNTGFLRRWPGPVPCLWVKGVAHHASKLRWKTLACTALSLPALPSHPGLLKSLLKRGEVKKLEAARTVLRALQPHRTNGGYTKELGQEEEHWFRYSFGGTIGALYDRKVAVWYRSSQVIYNGPIYRLVQEPSCASPITLFSRVLLNVVSYLEITVKRHLFTPNTIPGRGLSHRKGALFFLIPPYPSSFELIRKPYRRTQPAFPGSLGDDPLLPCICRSKLRLRRITVYGSSRPVEDVGTTESRCPKTFYSLPLALCWCRSTGVGIYGYLEPDYPYYTRRAPAIPIWRHPVYRAFVQLTLAQATVPGPKPFLLLPVGTGPFIKIFGRHGFAVLAAVRYCTLCSDPIRGPDSRLSLVTESARQVLTPVEYTDLQLCSLGSIQKSKRLSRLSLTKFDELAARTNARFVRPVGYQQVKPRVIETETPYRTYRPNPPTDVDEEHKHRLLAVKRYIGFRGTLSDRPQAALIKGECKASRSGHLLEIHRGSERLDCRITLTLLKDPLGYFYGVDSQPPAVHLSYDAFSQLIKNRCFRNYKSRAFQGTNVARKSIWDRSSDPGLREPLCWTLDKRWAKYTHQPQPCQPVPTSNVFECRRGQTEVRHNALVYSPTFANFRVSADSTVLLPATGSLIVPSGRSERNPDYHAPCSLCPNLNSGLPGRIVGTPRTDKRRAVTQLRVSEASCPQRNRSPDSCALGKCPLPLDNSTSRFCGPCAHYSDLTTFLRLLFSQTSPDGRFFHQIIAVLKVGKCIRATAALNPASYLASRAAQSGNIVEGHRGPILSRSMLVKRNWRCHGSLPCNRTTGETLTILGIMYGSVGGSRILQAVVHSVARRAPQATDGFGHLLTKPFVRARTSEEDKGWVVTSIFPRRNAYDPLGKVGPTWRTPGYRMIPQADKWGIGPTNGDTANCVGGCLRVICPSRASKHHAAICLSGTSFARVGKGREEKVRHTESQAWTRFNLGNARRGGVDQILRKLTIDRGGLRGHARISTKYRPRLQRNATMAGKDTRHYLSAFKFELATRAYRSALILWELIQRSTRTLAYSTGRIELPTTVPHSSPGVVLLGVVNLRGEATQHALFSYLDSTTPYECLDIAPNSWFTSESSWPRSDAILSYRLVNDPAELLSAGPSTLSHPLCGSIGRSLTRGDRLTKDYYVVHNLSSSLTRLDRHSSATRSLRPCLWVTTENTIYLQRTCFYSDWDCMRCLSDKGGYDGNYSRVTAYHYCRPKVHDEATVLYKLKGTPIRFGPAHNHRGALALRPVETTPLRTSPEYVEHPYDEESNTGRGAARQEGLEVQLIAGQYDAWQCMDNWTVHISRLCTGVQSPPLARRVSYLGISPDIWGHSFSFRYTWPFKSSTGAIDWRHGLYSFLSTLIIGCCSRALTERSRRGPAR"""))

##[75, 79, 85, 102, 142, 149, 173, 217, 267, 281, 313, 374, 526, 612, 805, 833, 879, 932, 1004, 1046,
#1205, 1212, 1341, 1355, 1388, 1534, 1545, 1554, 1610, 1751, 1915, 1929, 2198, 2233, 2238, 2271, 2330,
#2355, 2468, 2491, 2529, 2581, 2596, 2678, 2702, 2762, 2828, 2921, 3094]










