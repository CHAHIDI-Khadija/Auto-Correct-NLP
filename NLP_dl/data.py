import re 
from collections import Counter
import numpy as np
import pandas as pd


def process_data(file_name):
    words=[]
    with open(file_name) as f:
        file_data = f.read()
    file_data.lower()
    words = re.findall('\w+', file_data)

    return words

word_l = process_data('shakespeare.txt')
vocab = set(word_l)
#print(f"The first ten words in the text are: \n{word_l[0:10]}")


def get_count(word_l):
    
    word_count_dict = {}  
    word_count_dict = Counter(word_l)  

    return word_count_dict
word_count_dict = get_count(word_l)

def get_probs(word_count_dict):
    probs = {}
    m=sum(word_count_dict.values())
    for key in word_count_dict.keys():
        probs[key] = word_count_dict[key] / m

    return probs

probs = get_probs(word_count_dict)
print(probs)