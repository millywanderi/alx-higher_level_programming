#!/usr/bin/python3
def multiple_returns(sentence):
    len_sent = len(sentence)
    if len_sent == 0:
        tuple_new = (len_sent, None)
    tuple_new = (len_sent, sentence[0])
    return tuple_new
