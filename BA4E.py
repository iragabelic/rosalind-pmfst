def TheoreticalSpectrum(peptide):
  #zbroji masu po svakom slovu
  spektar = [0, sum(peptide)]
  dvostruki = peptide + peptide
  p = len(peptide)

  for l in range(1, p):
    for k in range(0, p):
      podpeptid = dvostruki[k:k+l]
      spektar.append(sum(podpeptid))

  return sorted(spektar)

# peptide je niz integera, ima ih isto koliko i slova (isto indeksiranje)
def Expand(peptides):
  novi_peptidi = []
  mase = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

  for peptide in peptides: ##peptidi su prazna lista u listi, u prvom diru
    for masa in mase:     ## uzme svaki po jednom i napravi od njega listu
      novi_peptidi.append(peptide + [masa])

  return novi_peptidi

# peptide je linearan
def IsConsistent(peptide, spectrum):
  rj = []

  linearni_spektar = [0, sum(peptide)]
  for l in range(1, len(peptide)):
    for k in range(0, len(peptide) - l + 1):
      subpeptide = peptide[k:k+l]
      linearni_spektar.append(sum(subpeptide))
  
  for el in linearni_spektar:
    if el in spectrum:
      rj.append(True)
    else:
      rj.append(False)

  return rj


def CyclopeptideSequencing(spec):
  spectrum = []
  peptides = [[]]
  rj = []
  rezultat = []
  res = ""
  temp = 0
  spe = spec.split(" ")
  for s in spe:
    spectrum.append(int(s))

  while len(peptides) > 0:
    peptides = Expand(peptides)
    for peptide in peptides:
      if sum(peptide) == spectrum[-1]: ##suma svake liste u listi
        if TheoreticalSpectrum(peptide) == spectrum:
          rj.append(peptide)
        #peptides = [p for p in peptides if p != peptide] #ovo je isto kao da smo izbacili peptide
      elif(False in IsConsistent(peptide, spectrum)):
        peptides = [p for p in peptides if p != peptide]
        
  for i in range(len(rj)):
    for j in range(len(rj[i])):
      unutra = "-".join(map(str, rj[i]))
    rezultat.append(unutra)

  for i in range(len(rezultat)):
    res += rezultat[i] + " "
  res = res[:-1]

  return res


print(CyclopeptideSequencing('0 113 128 186 241 299 314 427'))
