__author__ = 'anand'

def call_try1():
    print ("Ya see this?")
    hen="this was the story told before"
    print (hen[2:16])
    print (hen[2:16:-1])

    fren = '  64787  '
    fd = int(fren)
    print (fd)

    nd = str(76347)
    n1 = '76347'

    print (n1[3:4])
    print (nd[3:4])

    astr='george was a nice man'
    try:
        mval=int(astr)
    except ValueError:
        print ("invalid conversion")
    except NameError:
        print ("Invalie name of variable")
    else:
        print (mval)
    finally:
        print ("ok all done now")

    grt="fran", 34, 'dav', 99
    print (grt, type(grt))

    alst = ['defge', 43, "53476", 556, 76, 8, 100]
    for i in range(5):
        alst.append(i)
    print ("alst is ", alst)

    blst = [(i,i*i, i*i*i) for i in range(7) if i > 3]
    print ("blst is ", blst)

    dstr= input("Enter a sentence: ")
    gl = []
    tl = []
    try:
        tl = dstr.split(' ')
        print (tl)
    except TypeError as ex:
        print ("You entered wrong data type", ex)
    except ValueError as ex:
        print ("You entered wrong value", ex)
    else:
        for i in tl:
            gl.append(i)
            gl.append('|')
    finally:
        print (dstr)
        df = ''.join(gl)
        print (gl, df)
