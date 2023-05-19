#!/usr/bin/python3
def weight_average(my_list=[]):
    t_weig = 0
    t_score = []
    if my_list:
        for m in my_list:
            t_weig += m[1]
            t_score.append(m[0] * m[1])
        return (sum(t_score) / t_weig)
    return 0
