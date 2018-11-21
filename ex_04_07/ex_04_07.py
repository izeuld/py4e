# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(fscore): # fscore is a function parameter
    while True: # this could be an infinite loop if no exit condition is specified!
        score = input('Enter score:')
        if score == 'done':
            print('Goodbye!')
            break # nothing after break is executed, so it has to be the last statement we want
        try:
            fscore = float(score)
            if  0.0 <= fscore <= 1.0: # that's why Python rules!
                if fscore >= 0.9: print('A')
                elif fscore >= 0.8: print('B')
                elif fscore >= 0.7: print('C')
                elif fscore >= 0.6: print('D')
                elif fscore < 0.6: print('F')
            else:
                print('Value must be between 0.0 and 1.0')
        except:
            print('Bad score. Enter numbers only')
        continue

# ? why is it impossible to put "fscore" as argument below?
computegrade(input) # calling a function with an argument
