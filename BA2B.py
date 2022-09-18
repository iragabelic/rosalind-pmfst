from itertools import product

def HammingDistance(first, second):
  cnt = 0
  for i in range(len(first)):
    if first[i] != second[i]:
      cnt += 1
  return cnt

def Patterns(text, k):
  patterns = []
  for i in range(len(text) - k + 1):
    pattern = text[i:k+i]
    patterns.append(pattern)
  return patterns

def MinPattern(text, pattern, k):
  mini = k
  for pat in Patterns(text, k):
    if(HammingDistance(pattern, pat) < mini):
      mini = HammingDistance(pattern, pat)
  return mini

def DnaSum(dna, pattern, k):
  suma = 0
  for i in range(len(dna)):
    suma += MinPattern(dna[i], pattern, k)
  return suma

def MedianString(k, dnaList):
  dna = dnaList.split("\n")
  d = float('inf')
  median = ""

  all_k_mers = [''.join(i) for i in product('ACGT', repeat = k)]

  for kmer in all_k_mers:
    distance = DnaSum(dna, kmer, k)
    if(distance < d):
      d = distance
      median = kmer
  
  return median
print(MedianString(3,"""AAATTGACGCAT
GACGACCACGTT
CGTCAGCGCCTG
GCTGAGCACCGG
AGTACGGGACAG"""))




















