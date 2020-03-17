from math import sqrt

def euclidean(rating1, rating2):
    distance = 0
    commonRatings = False 
    for key in rating1:
        if key in rating2:
            distance += (rating1[key] - rating2[key]) ** 2
            commonRatings = True
    if commonRatings:
        return sqrt(distance)
    else:
        return -1 