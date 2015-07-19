def readfl():
    lst=[]
    with open("names" , "r") as fobj:
        [lst.append(ln.split(':')) for ln in fobj ]
    print lst

readfl()        
