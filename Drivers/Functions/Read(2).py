# Write mode

filev = open('tiku.txt','w')
filev.write('This is tiku\n')
filev.write('Here we are getting data\n')
filev.write('our main focus is vrushti.jigar67@gmail.com dfvddjagd\n')
filev.write('we have a so many doubts here what we can do for it\n')
filev.close()

#

def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)


file_read_from_head('tiku.txt', 1)