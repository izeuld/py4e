score = input("Enter score:")
fscore = float(score)
if  0.0 <= fscore <= 1.0: # that's why Python rules!
    if fscore >= 0.9: print("A")
    elif fscore >= 0.8: print("B")
    elif fscore >= 0.7: print("C")
    elif fscore >= 0.6: print("D")
    elif fscore < 0.6: print("F")
else:
    print("Value must be between 0.0 and 1.0")
