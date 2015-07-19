__author__ = 'anand'
import datetime
import xml.sax.saxutils
import sys

class HTMLFrame():

    userProfileDict= None
    count = 0


    def __init__(self):
        self.userProfileDict = dict({'u_name':None, "c_year":None, "filename":None, "filetitle":None, "description":None, "keywords":None, "style":None, "body": None})
        self.COPYRIGHT_TEMPLATE = "Copyright (c) {0} {1}. All rights reserved."
        self.STYLESHEET_TEMPLATE = ('<link rel="stylesheet" type="text/css" media="all" href="{0}" />\n')
        self.HTML_TEMPLATE = '''<?xml version="1.0"?>
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
        <head>
        <title>{title}</title>
        <!-- {copyright} -->
        <meta name="Description" content="{description}" />
        <meta name="Keywords" content="{keywords}" />
        <meta equiv="content-type" content="text/html; charset=utf-8" />
        {stylesheet}
        </head>
        <body>{body}</body>
        </html>
        '''
    def readUserInput(self):
        print ("Make HTML Skeleton\n")
        #self.userProfileDict["u_name"] = input("Enter your name (for copyright) " + \
        #            ("" if self.userProfileDict['u_name'] == None else [ self.userProfileDict['u_name'] ]) + \
        #                   " : ")
        try:
            message = 'Enter your name (for copyright)'
            newval = self.getInput(message, self.userProfileDict['u_name'])
            self.userProfileDict['u_name'] = newval if len(newval.strip()) > 0 else self.userProfileDict['u_name']
            message = 'Enter copyright year'
            str1 = datetime.date.today().year if self.userProfileDict['c_year'] == None else self.userProfileDict['c_year']
            newval = self.getInput(message, str1)
            self.userProfileDict['c_year'] = newval if len(newval.strip()) > 0 else self.userProfileDict['c_year']

            #self.userProfileDict["c_year"] = input("Enter copyright year: [" + \
            #  (datetime.date.today().year if self.userProfileDict['c_year'] == None else self.userProfileDict['c_year']) + "] :")

            message = 'Enter filename: '
            newval = None
            self.userProfileDict['filename'] = self.getInput(message)

            message = 'Enter filetitle: '
            newval = None
            self.userProfileDict['filetitle'] = self.getInput(message)

            message = 'Enter description (optional): '
            newval = None
            self.userProfileDict['description'] = self.getInput(message)

            message = 'Enter the text to dipslay(optional): '
            newval = None
            self.userProfileDict['body'] = self.getInput(message)

            message = 'Enter keyword (optional): '
            newval = None
            keywd1 = self.getInput(message)
            keywd2 = self.getInput(message)
            keywd3 = self.getInput(message)
            keywd4 = self.getInput(message)
            self.userProfileDict["keywords"] = (keywd1, keywd2, keywd3, keywd4)

            message = 'Enter the stylesheet filename (optional): '
            newval = None
            self.userProfileDict['style'] = self.getInput(message)

        except IOError:
            print ("Encountered user interrupt. Exiting")
            exit()

    def getInput(self, message, prefilled=None):

        toprintStr = message + (' : ' if prefilled is None else '[{0}] : '.format(prefilled) )
#        print ("The line to print is {0}".format(toprintStr))
        try:
            resmsg = input(str(toprintStr))
        except KeyboardInterrupt:
            print ("Caught KeyboardInterrupt exception")
            raise IOError
#        print (resmsg)
        return str(resmsg)

    def doAction(self):
        self.readUserInput()
        self.makeHTMLFrame()


    def makeHTMLFrame(self):

        html_copyright = (self.COPYRIGHT_TEMPLATE).format(xml.sax.saxutils.escape(self.userProfileDict['u_name']), self.userProfileDict['c_year'])
        html_stylesheet =  self.STYLESHEET_TEMPLATE.format(xml.sax.saxutils.escape(self.userProfileDict['style']))

        html_title = xml.sax.saxutils.escape(self.userProfileDict['filetitle'])
        html_desc = xml.sax.saxutils.escape(self.userProfileDict['description'])
        html_body = xml.sax.saxutils.escape(self.userProfileDict['body'])
#        html_keyword = xml.sax.saxutils.escape(self.userProfileDict['keywords'])
        html_keywords = ",".join(xml.sax.saxutils.escape(i) for i in self.userProfileDict['keywords']) if self.userProfileDict['keywords'] else " "

        final_html = self.HTML_TEMPLATE.format(title=html_title, copyright=html_copyright, description=html_desc, keywords= html_keywords, stylesheet = html_stylesheet, body=html_body)

        try:
            with open("outfile.html", "w") as fobj:
                fobj.write(final_html)
        except FileExistsError:
            print("File already exist")
        except FileNotFoundError:
            print("File does not exist")
        except IOError:
            print ("File write I/O error")


def main():
    p = HTMLFrame()
    while True:
        p.doAction()
        cont_or_not = input ("Do you want to continue? [y/n]")
        print (cont_or_not[:1])
        if cont_or_not[:1] in ('n', 'N'):
            exit()
        else:
            continue


if (__name__ == "__main__"):
    main()



