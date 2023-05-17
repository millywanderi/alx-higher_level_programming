#!/usr/bin/python3
def weight_average(my_list=[]):
    t_weig = 0
    t_score = 0
    if not my_list:
        return 0
        for score, weig in my_list:
            t_score = t_score + (score * weig)
            t_weig = t_weig + weig
        if t_weig == 0:
            return 0
        tt = t_score / t_weig
    return tt
