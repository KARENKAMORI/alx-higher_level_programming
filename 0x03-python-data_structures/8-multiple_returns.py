#!/usr/bin/python3
def multiple_returns(sentence):
    t = len(sentence)
    c = sentence[0] if t > 0 else "None"
    sentence_new = t, c
    return (sentence_new)
