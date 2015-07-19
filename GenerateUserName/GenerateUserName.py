import collections
from os import sys
import string


__author__ = 'anand'

class genUsernm():
    inpfile = ""
    outfile = ""
    rec_layout = None
    usrDict = collections.defaultdict(int)

    def __init__(self, *file):

        self.inpfile, self.outfile = file
#        ID, FIRSTNAME, MIDNAME, LASTNAME, DEPT = range(1,6)
        self.rec_layout = collections.namedtuple ("rec_layout", "ID FIRSTNAME MIDNAME LASTNAME DEPT")
#        recData = self.rec_layout()

    def readFile(self):
        with open(self.inpfile, "r") as inpf:
            wordlst = []
            for ln in inpf:
                ln = ln.rstrip(string.whitespace)
                wordlst = ln.split(':')
#                recData = self.rec_layout(wordlst)      Gives error:
                print (wordlst)
                recData = self.rec_layout(*wordlst)
                print ('The record Data is {0}'.format(recData))
                if (len(recData.MIDNAME) < 1):
                    usrnm = (recData.FIRSTNAME[0] + recData.LASTNAME).lower()
                else:
                    usrnm = (recData.FIRSTNAME[0] + recData.MIDNAME[0] + recData.LASTNAME).lower()
                usrnm = usrnm[:8]
                self.usrDict[usrnm] += 1
                if (self.usrDict[usrnm] > 1):
                    usrnm += str(self.usrDict[usrnm] - 1)

                print (usrnm)
                print (self.usrDict)


def main():
    inpfile = sys.argv[1]
    outfile = ''
    ghy = genUsernm(inpfile, outfile)
    ghy.readFile()

if __name__ == "__main__":
    main()





