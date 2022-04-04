##uzimamo zadnji znak stringa, ako je to A vridi 0,
##C 1, G 2 i T 3, to nam je result. Onda to rekurzivno
##ponavljamo za ostatak stringa duljine k-1.
def PatternToNumber(pattern):
  if(len(pattern) == 0):
    return 0
  result = 0
  if(pattern[-1] == 'C'):
    result+=1
  elif(pattern[-1] == 'G'):
    result+=2
  elif(pattern[-1] == 'T'):
    result+=3
  elif(pattern[-1] == 'A'):
    result+=0
  return(result + 4*(PatternToNumber(pattern[:-1])))

print(PatternToNumber("TACTAAGCATAGTGCGTTTCAGTGG"))
    
