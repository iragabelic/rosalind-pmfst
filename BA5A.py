##gledamo koliko je kovanica bilo na poziciji - coin
##jer onda samo dodamo taj coin 

def Change(money, coins):
    minnumcoins = (money + 1) * [0]
    for m in range(1, money + 1):
        minnumcoins[m] = m + 1 #za slučaj da su sve po 1
        for coin in coins: # za svaki element prolazimo svim coinima koji su manji
            if m >= coin:
                if minnumcoins[m - coin] + 1 < minnumcoins[m]:
                    minnumcoins[m] = minnumcoins[m - coin] + 1
    return minnumcoins[money]
print(Change(19536, [1,3,5]))
