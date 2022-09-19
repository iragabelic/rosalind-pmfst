def ManhattanTourist(n, m, dw, rt):
  down = []
  dw = dw.split("\n")
  for i in range(n): #jer ima n redaka
    sniz = dw[i].split() #splitani niz
    rj = [int(x) for x in sniz]
    down.append(rj)

  right = []
  rt = rt.split("\n")
  for i in range(n + 1): #jer ima n+1 redaka 
    sniz = rt[i].split() #splitani niz
    rj = [int(x) for x in sniz]
    right.append(rj)
  
  #matrica nxm ispunjena s nulama
  s = [] #matrica putova(udaljenosti)
  for i in range(n + 1): #za svaki redak na karti
    s.append([0] * (m+1)) #niz od m+1 nula

  for i in range(1, n+1):
    s[i][0] = s[i-1][0] + down[i-1][0]

  for j in range(1, m+1):
    s[0][j] = s[0][j-1] + right[0][j-1]
    
  for i in range(1, n+1):
    for j in range(1, m+1):
      s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])
      
  return s[n][m] #vracamo zadnji el matrice

print(ManhattanTourist(10, 14, '''2 4 4 1 0 0 2 3 4 3 2 4 0 0 1
0 3 4 1 3 1 4 1 3 3 4 2 2 4 1
1 1 3 3 2 2 1 1 3 0 0 2 3 0 4
2 3 4 4 1 3 1 2 3 0 2 4 4 1 4
2 0 2 3 4 1 4 3 4 2 1 0 1 2 0
3 0 2 1 0 0 1 4 4 1 2 0 0 2 1
0 3 2 2 3 3 3 2 4 4 4 2 3 1 4
1 4 0 2 3 0 0 2 1 0 0 0 0 1 1
3 0 4 2 0 4 4 4 1 0 2 0 2 0 4
4 1 2 1 0 0 2 0 2 2 2 3 0 2 3'''
,
'''1 0 2 1 0 3 0 1 2 1 3 3 3 4
4 2 3 1 4 0 0 1 1 4 1 3 1 1
1 2 3 1 0 2 1 0 3 2 3 0 4 1
4 2 3 3 2 0 1 2 2 2 3 1 3 1
0 2 1 1 3 0 2 2 4 1 2 3 2 4
2 3 1 2 0 1 2 4 1 2 2 1 4 2
1 3 3 1 3 3 0 4 4 2 4 1 3 4
1 3 2 4 3 4 3 2 2 3 4 1 3 4
4 3 2 3 0 4 4 1 0 0 1 4 4 2
3 1 1 4 2 1 2 3 4 4 0 2 2 4
4 3 4 0 2 0 3 3 1 4 3 2 3 3'''))
