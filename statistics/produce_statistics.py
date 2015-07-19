from functools import reduce

__author__ = 'anand'

import collections
import sys
import string
from operator import add

class mystatistics():

    stat_rec = None
    stat_file_lst = []
    MEAN, MODE, MEDIAN = range(0,3)

    def __init__(self):
        self.stat_rec_template = collections.namedtuple("stat_rec", "mean mode median stddev")

    def readFiles(self, files):

        for file in files:
            with open(file, "r") as fobj:
                for ln in fobj:
                    stat_file_ln = ln.strip(string.whitespace)
                    file_lst = stat_file_ln.split(' ')
                    # At this point tje file_lst is a list of str.
                    # But we need a list of int
                    # so do a map of each list element from str to int
                    file_lst = map(float, file_lst)

                    #The above conversion of list with str items conversion to int items could
                    # also be done using generator as follows:

                    #int_file_lst = ( float(w) for w in file_lst )

                    #In above generator function the (..) is the a generator function. The generator function returns a
                    # sequence rather than a single value. This new sequence generated out of a original sequence then can be used

                    self.stat_file_lst.extend(file_lst)

        amean = self.find_mean(self.stat_file_lst[:])
        amode = self.find_mode(self.stat_file_lst[:])
        amedian = self.find_median(self.stat_file_lst[:])
        stat_rec = self.stat_rec_template(amean, amode, amedian, 0)

        print ("The mean [{0}], mode {1}, median [{2}]".format(stat_rec[self.MEAN], stat_rec[self.MODE], stat_rec[self.MEDIAN]))

    def find_mean(self, lst):
        asum=0
#        listsum = [sum + num for num in self.stat_file_lst]  Dont use list comprehension to reduce the result to a single value
        # if you need to reduce list to a single value, use reduce function or lambda, or a sequence operator such as sum()

        # Using sum operator of sequence.
        # This will work
        #asum = sum(lst)

        #Using lambda below
        #This will work
        #asum = reduce (lambda x, y: x + y, lst)

        # Using reduce below. For this you need to have in import section:
        # import from operator import add
        # from functools import reduce
        print (lst)
        asum = reduce(add, lst)
        amean = asum / len(lst)
        print ("mean {0}".format(amean))
        print ("The sum is {0}, the count of numbers is {1}, the mean is {2}".format(sum, len(lst), amean))
        return float(amean)

    def find_mode(self, lst):

        stat_dict = collections.defaultdict(int)
        for num in lst:
            stat_dict[num] += 1

        highval = max(stat_dict.values())
        modeval = [highkey for highkey, val in stat_dict.items() if val == highval]
        print ("mode {0}".format(modeval))
        return modeval

    def find_median(self, lst):

        sorted(lst)
        if (len(lst) % 2 == 0):
            ind = int((len(lst) + 1 ) /  2) - 1
            amedian = float((lst[ind] + lst[ind +1]) / 2)
            print ("median {0}".format(amedian))
            return amedian
        else:
            ind = len(lst) / 2
            amedian = float(float(lst[ind]))
            print ("median {0}".format(amedian))
            return amedian


def main():
    if len(sys.argv) < 3:
        print ("Failed running {0}, insufficient arguments. Need 3 provided {1}".format(sys.argv[0]), len(sys.argv))
    else:
        astat = mystatistics()
        astat.readFiles(sys.argv[1:])

if __name__ == "__main__":
    main()











