__author__ = 'anand'

import samp1

def demoex2():
    counter = age = 0;
    while True:
        ln = samp1.callme1("Enter an integer: ")
        try:
            boy = int(ln)
        except ValueError as err:
            print ("You entered a non-integer ");
            print (err);
            continue
        except EOFError:
            break
        counter += 1
        age  += boy
        if counter > 2:
            break

    print ("The final value of the counter is " + str(counter) + " Age is " + str(age));
    return


