##ako je duljina 1, samo pozivamo NumberToSymbol jer to znači da je samo jedno slovo
##zadatak riješen po pseudokodu iz knjige

def NumberToSymbol(num):
  result = ""
  if(num == 0):
    result="A"
  elif(num == 1):
    result="C"
  elif(num == 2):
    result="G"
  elif(num == 3):
    result="T"
  return result
    
def NumberToPattern(ind, k):
  if(k == 1):
    return NumberToSymbol(ind)
  prefixIndex = ind // 4
  r = ind % 4
  symbol = NumberToSymbol(r)
  prefixPattern = NumberToPattern(prefixIndex, k-1)
  return(str(prefixPattern) + str(symbol))

print(NumberToPattern(8925, 10))
