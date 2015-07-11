#!/usr/bin/env python3

import os
import demo2
import try1
import samp1
import strexample
import listExample



def main ():
#    std_dict = (Anand="10", John="50", Mary="35", Tom="70")
    #print (std_dict["Mary"])
    try1.call_try1()
    demo2.demoex2()
    samp1.rand1()

#'String example . String is pass by value, so a implicit new string created when assignment needs to happen

    str1 = "My name is python"
    samp1.strprnt(str1)
    print ("In main: ", str1)
    str1 = samp1.strprnt(str1)
    print ("In main: ", str1)

    strexample.runStrDemo("Tomorrow")
    print ("tomorrow".index("morr"))
    print ("tomorrow".find("rr"))


#List example   LIST is pass by reference, that is object reference is passed
    listExample.listex1()
    ggh = []
    for i in range(3):
        ggh.append(i)
    print ("The list is ",  ggh)
    listExample.listex2(ggh)
    print ("original ggh list is ", ggh)

main()

