import re 
import pandas as pd
import numpy as np
from collections import Counter
words=[]
word_count_dict = {} 
with open('shakespeare.txt') as f:
        data = f.read()
data = data.lower()
words = re.findall('\w+', data)
vocab = set(words)
 
word_count_dict = Counter(words) 
#print(f"The first ten words in the text are: \n{words[0:10]}")
def get_probs(word_count_dict): 
       probs = {}
       m=sum(word_count_dict.values())
       for key in word_count_dict.keys():
            probs[key] = word_count_dict[key] /m

       return probs
probs = get_probs(word_count_dict)
