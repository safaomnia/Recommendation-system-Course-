import codecs 
from math import sqrt

def adjustCos(band1, band2, userRatings):
   averages = {}
   for (key, ratings) in userRatings.items():
      averages[key] = (float(sum(ratings.values())) / len(ratings.values()))
   num = 0  # numerator
   dem1 = 0 # first half of denominator
   dem2 = 0
   for (user, ratings) in userRatings.items():
      if band1 in ratings and band2 in ratings:
         avg = averages[user]
         num += (ratings[band1] - avg) * (ratings[band2] - avg)
         dem1 += (ratings[band1] - avg)**2
         dem2 += (ratings[band2] - avg)**2
   return num / (sqrt(dem1) * sqrt(dem2))