def Expand(leaderboard):
  mase=[57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
  novipeptidi=[]
  for peptid in leaderboard:
    for masa in mase:
      novi=peptid+[masa]
      novipeptidi.append(novi)
  return novipeptidi


def Cyclospectrum(peptide):
  p=len(peptide)
  dvostruki=peptide+peptide
  spektar=[0, sum(peptide)]

  for l in range(1, p):
    for k in range(0, p):
      subp=dvostruki[k:k+l]
      spektar.append(sum(subp))
  
  spektar.sort()
  return spektar


def Score(peptide, Spectrum):
  cyclospectrum=Cyclospectrum(peptide)
  score=0

  svi=set(cyclospectrum+Spectrum)
  for el in svi:
    score+=min(cyclospectrum.count(el), Spectrum.count(el))
  return score


def Trim(leaderboard, Spectrum, N):
  if len(leaderboard)<N:
    return leaderboard

  scores=dict()
  for j in range(len(leaderboard)):
    scores[j]=Score(leaderboard[j], Spectrum)
  scores_sort=sorted(scores.values(), reverse=True) #valuesi iz dict scores poredani silazno

  granica=scores_sort[N-1]
  return [leaderboard[idx] for idx, el in scores.items() if el>=granica]


#BA4G
def LeaderboardCyclopeptideSequencing(Spectrum, N):
  leaderboard=[[]]
  leaderpeptide=[]
  sp = Spectrum.split(" ")
  spectrum = []
  for s in sp:
    spectrum.append(int(s))
    

  while len(leaderboard)>0:
    leaderboard=Expand(leaderboard)
    for peptid in leaderboard:
      if sum(peptid)==spectrum[-1]:
        if Score(peptid, spectrum)>Score(leaderpeptide, spectrum):
          leaderpeptide=peptid
      elif sum(peptid)>spectrum[-1]:
        leaderboard=[p for p in leaderboard if p!=peptid]
    leaderboard=Trim(leaderboard, spectrum, N)
  for l in leaderpeptide:
    print(l, end='-')

  return

LeaderboardCyclopeptideSequencing("""0 71 113 129 147 200 218 260 313 331 347 389 460""", 10)
