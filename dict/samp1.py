__author__ = 'anand'

import random


### JULY changes mde


def callme1(msg):
    str1 = input(msg);
    return str1

def rand1():
    df = random.randint(3, 45)
    ds = random.choice(['ax', 'df', 'ew', 'tr'])
    print (df, ds)

#called like: samp1.strprnt(str1)  Since str1 is string and immutable, so new string msg is created
#string is pass by value and not pass by address reference
def strprnt(msg):
    print ("first inside the strprnt: ", msg)
    msg = "your name"
    print ("last inside the strprnt: ", msg)
    a1 = 'this is string example'
    b1=a1
    if b1 is a1:
        print ('diff strings')
    else:
        print ('same string')

    return msg
