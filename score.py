import math

def rad(d):
   return d * math.pi / 180.0

def getDistance(LngA, LatA, LngB, LatB):
    R = 6371.004
    C = math.sin(rad(LatA)) * math.sin(rad(LatB)) + math.cos(rad(LatA)) * math.cos(rad(LatB)) * math.cos(rad(LngA - LngB))
    return (R * math.acos(C))

def score(LngA, LatA, LngB, LatB):
    D = getDistance(LngA, LatA, LngB, LatB)
    #大於100不顯示 小於100的計分，距離越近分數越高
    if (D > 50):
        return -1
    else:
        return 100 - D

