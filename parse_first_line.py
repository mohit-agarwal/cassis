# Author: Mohit Aggarwal

import urllib2
from pyparsing import *

# Group together the tokens belonging to a column header.
def group_tokens(tokens):
    return reduce(lambda x, y : x + " " + y, tokens)

# Parse firse line of the dataset.
def parse(data):
    real_number = Word(nums+'.')
    natural_number = Word(nums)
    alpha_word = Word(alphas)
    alphanum_word = Word(alphas+nums+'-')

    mid_header = (natural_number + OneOrMore(alpha_word)).setParseAction(lambda s,l,t : group_tokens(t))
    last_header = (natural_number + OneOrMore(alphanum_word)).setParseAction(lambda s,l,t : group_tokens(t))
    grammar = real_number + mid_header + mid_header + mid_header + mid_header + last_header
    print grammar.parseString(data)

# Get first line of the dataset.
def getFirstLine():
    target_url = 'http://kurucz.harvard.edu/atoms/1401/gf1401.gam'
    fp = urllib2.urlopen(target_url) 
    return fp.readline()

def main():
    first_line = getFirstLine()
    parse(first_line)

if __name__ == '__main__':
    main()
