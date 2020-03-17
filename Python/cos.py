from math import sqrt

def pearson(rating1, rating2):
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0
    for key in rating1:
        if key in rating2:
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    denominator = sqrt(sum_x2) * sqrt(sum_y2);
    if denominator == 0:
        return 0
    else:
        return sum_xy / denominator