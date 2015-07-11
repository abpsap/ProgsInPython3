__author__ = 'anand'

#from format_op import format_inp
#from format_op import make_html

# line1 = "An, simple, sentence, Example, Here"
# tag1 = "h1"
#
# mylst = line1.split(",")
# print (mylst)
#
# builtline1 = format_inp(mylst, tag1)
#
# bstr = make_html(" ".join(builtline1))

class makeHTML():

    filelist = []
    linelist = []
    count = 0
    ab_str = ""

    def __init__(self, lst):
        filelist = lst

    def beginHTML(self):
        astr = ''
        astr = '<HTML>' + '<table border=\'1\'>'
        self.filelist.insert(0, astr)
#        print (astr)
        return None

    def beginTableRow(self):
        astr = ''
        if self.count % 2 == 0:
            if self.count == 0:
                astr = '<tr bgcolor = \'lightpink\'>'
            else:
                astr = '<tr bgcolor = \'lightgreen\'>'
        else:
            astr = '<tr bgcolor = \'lightyellow\'>'

        self.count += 1

        self.filelist.append(astr)
#        print (astr)
        return None

    def endHTML(self):
        astr = '</HTML>' + '</table>'
        self.filelist.append(astr)
#        print (astr)
        return None

    def endTableRow(self):
        astr = '</tr>'
        self.filelist.append(astr)
#        print (astr)
        return None

    def addRow(self, item):
        item = '<td>' + str(item) + '</td>'
        return item


    def parseFile(self):
        outlst = []
        try:
            with open("cvs_input.txt", "r") as fobj:
                for ln in fobj.readlines():
#                    print (ln)
                    outlst = ln.split(",")      #instead of doing unpacking below on ln which is str, we convert ln to a list where each word is s element.
                                        # This way unpacking iteration is on words instead of on letters
#                begining_word, *lin, end_word = lnlst
                    newoutlst = outlst[:-1]
                    self.beginTableRow()
                    [self.filelist.append(self.addRow(i)) for i in newoutlst]
                    self.endTableRow()
        except:
            print ("file read error")
#        print (self.filelist)

#print ( "The line generated is {op:s}".format(op=bstr) )

#class main():

def main():
    mainlist = []
    h = makeHTML(mainlist)
    h.beginHTML()
    h.parseFile()
    h.endHTML()
    print (h.filelist)
    htm = " ".join(h.filelist)
    print (htm)
    with open("cvs2html.html", "w") as foutobj:
        foutobj.write(htm)



main()






