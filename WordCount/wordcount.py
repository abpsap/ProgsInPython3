__author__ = 'anand'

import os
import sys
import string

class makeUniqueWordDict:

    lnlst = []
    strlst = []
    worddict = {}


    def __init__(self, fname):
        try:
            open(fname, "r")
        except:
            print ("error opening{0}".format(fname))
            exit()

    def populateDict(self, fname):
        with open(fname, "r") as fobj:    #This is a start of inplicit file open and start of while loop
                                          # until end of file is reached
            rdlinelst = []
            strip_chars = string.digits + string.whitespace + string.punctuation
            for ln in fobj:
                try:
                    rdlinelst = [ rd.strip(strip_chars) for rd in ln.split(" ") if len(ln.strip('\n')) != 0]
#                    print (rdlinelst)
                except:
                    print ("cannot open {0} for reading".format(fobj))
                    exit()
                if len(rdlinelst) > 0:
                    print (rdlinelst)
                for wd in rdlinelst:
                    if wd not in self.worddict.keys():
                        self.worddict[wd] = 1
                    else:
                        self.worddict[wd] += 1
        print ( self.worddict )
        return None

def main(story):
    p = makeUniqueWordDict(story)
    p.populateDict(story)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print ('invalid number of arguments for {0}'.format(sys.argv[0]))
    else:
        main(os.sys.argv[1])







