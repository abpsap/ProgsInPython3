import os

class Fraction:
    def __init__ (self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return  str(self.num) + "/" + str(self.den)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num


afrac = Fraction(2,3)
bfrac = Fraction(100,150)
print(afrac)
print(bfrac)
print (afrac == bfrac)





