from urllib2 import urlopen
from string import punctuation

path = \
'http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt'

works = urlopen(path).read()
lines = works.splitlines()
words = [x.split(' ') for x in lines]
flattened = [
    val.strip().strip(punctuation).lower() \
    for sublist in words for val in sublist \
    if val != '']

text_file = sc.parallelize(flattened)

def word_tuple_mapper(word):
    return (word, 1)

def word_tuple_reducer(x, y):
    return x + y

word_tuples = text_file.map(word_tuple_mapper)
word_counts_rdd = word_tuples.reduceByKey(word_tuple_reducer)
word_counts = word_counts_rdd.collect()

top_words = sorted(word_counts, key=lambda x: x[1], reverse=True)
top_words[:10]
