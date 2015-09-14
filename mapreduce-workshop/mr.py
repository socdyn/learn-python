from urllib2 import urlopen
# for Python 3 users
# from functools import reduce

## Adding nested lists ##



## Shakespeare word counts ##

shakespeare_path = \
'http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt'

shakespeare_works = urlopen(shakespeare_path).read()
print(shakespeare_works)
