#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0 and sentence != "":
        return len(sentence), sentence[0]
    elif sentence == "":
        return len(sentence), None
    else:
        return None
