from urllib2 import urlopen
from string import punctuation
from copy import copy
# for Python 3 users
# from functools import reduce

## Adding nested lists ##

N = [[1,2,3], [4,5,6]]

def sum_numbers_in_list(list_of_ints):
    '''
    Takes a list of ints and returns their sum
    '''
    return sum(list_of_ints)

def sum_pairs_of_numbers(running_total, next_int):
    '''
    Adds the next number to the running total
    '''
    return running_total + next_int

M = map(sum_numbers_in_list, N)
R = reduce(sum_pairs_of_numbers, M)

print('Input: {}'.format(N)
print('Output of Mapper: {}', M)
print('Output of Reducer: {}', R)

## Shakespeare word counts ##

def word_dict_mapper(word):
    return {word: 1}

def word_dict_reducer(running_dict, word_dict):
    running_dict_copy = copy(running_dict)
    for key in word_dict.keys():
        if key not in running_dict_copy:
            running_dict_copy[key] = 0
        running_dict_copy[key] += 1
    return running_dict_copy

path = \
'http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt'

works = urlopen(path).read()
lines = works.splitlines()
words = [x.split(' ') for x in lines]
flattened = [
    val.strip().strip(punctuation).lower() \
    for sublist in words for val in sublist \
    if val != '']

word_count_dict = map(word_dict_mapper, flattened)
first_hundred = word_count_dict[:100]
word_counts = reduce(word_dict_reducer, first_hundred)
