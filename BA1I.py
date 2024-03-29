from itertools import product

def Mismatch(a, b):
  counter = 0
  for i in range(len(a)):
    if(a[i] != b[i]):
      counter += 1
  return counter
  
def freq(genom, length, mismatch):
  svi = [''.join(i) for i in product('ACGT', repeat = length)]
  lista = []
  kmers = []
  dic = {}
  for i in range(len(genom) - length + 1):
    kmers.append(genom[i:i+length])


  for j in range(len(kmers)):
    for k in range(len(svi)):
      if(Mismatch(kmers[j], svi[k]) <= mismatch):
        lista.append(svi[k])
  for el in lista:
    if el in dic:
      dic[el] = dic[el] + 1
    else:
      dic[el] = 1
  for val in dic:
    max_key = max(dic, key=dic.get)
    if(dic[val] == dic[max_key]):
        print(val, end=' ')
       
  return 

freq("""AAAGTCCACGGGTCAGAAAGTCCACGGGTCAGAAAGTCCAGCTATACAAAGTCCAATATCGCCGGGTCAGATATCGCAAAGTCCACTAGCTGACCTAGCTGACATATCGCGCTATACATATCGCAAAGTCCAGCTATACCTAGCTGACATATCGCCGGGTCAGGCTATACGCTATACCTAGCTGACATATCGCCTAGCTGACGCTATACCTAGCTGACGCTATACATATCGCATATCGCATATCGCATATCGCGCTATACCTAGCTGACATATCGCGCTATACAAAGTCCAATATCGCATATCGCGCTATACAAAGTCCAAAAGTCCAAAAGTCCAAAAGTCCACTAGCTGACCTAGCTGACAAAGTCCAGCTATACATATCGCAAAGTCCAGCTATACAAAGTCCAGCTATACATATCGCCTAGCTGACCTAGCTGACCGGGTCAGCTAGCTGACGCTATACCGGGTCAGCGGGTCAGCGGGTCAGATATCGCCGGGTCAGCTAGCTGACAAAGTCCAGCTATACGCTATACCTAGCTGACATATCGCATATCGCAAAGTCCAATATCGCATATCGCCGGGTCAGAAAGTCCAGCTATACCGGGTCAGCGGGTCAGCTAGCTGACGCTATACCGGGTCAGCGGGTCAGAAAGTCCACGGGTCAGATATCGCGCTATACCGGGTCAGATATCGCAAAGTCCAAAAGTCCACTAGCTGACCTAGCTGACCGGGTCAGAAAGTCCACTAGCTGACAAAGTCCAATATCGCGCTATACATATCGCATATCGCAAAGTCCACGGGTCAGAAAGTCCAGCTATACCGGGTCAGAAAGTCCAGCTATACGCTATACCGGGTCAG""", 7, 2)
