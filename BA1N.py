from itertools import product

def hamming(a, b):
  counter = 0
  for i in range(len(a)):
    if(a[i] != b[i]):
      counter += 1
  return counter

def neighbor(dna, d):
  rez = []
  svi = [''.join(i) for i in product('ACGT', repeat = len(dna))]

  for i in range(len(svi)):
    if(hamming(svi[i], dna) <= d):
      rez.append(svi[i])
  for s in rez:
    print(s)

  return
neighbor("GTAGAAATAAG", 3)
  
