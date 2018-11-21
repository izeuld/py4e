# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

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
