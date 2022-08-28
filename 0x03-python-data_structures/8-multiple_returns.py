#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        char = None
    else:
        for char in sentence:
            return leng, char
    return leng, char 
