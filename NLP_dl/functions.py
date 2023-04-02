## string manipulation

switch_l = []
delete_l = []
replace_l = []
exiinsert_l = []

n_best = []
letters = 'abcdefghijklmnopqrstuvwxyz'
from data_process import vocab,probs

def delete_letter(word,verbose=True):
    split_l=[]
    for c in range(len(word)):
        split_l.append((word[:c],word[c:]))
    for a,b in split_l:
        delete_l.append(a+b[1:])
        #if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")

    return delete_l


def switch_letter(word, verbose=False):
    split_l=[]
    len_word=len(word)
    for c in range(len_word):
        split_l.append((word[:c],word[c:]))
    switch_l = [a + b[1] + b[0] + b[2:] for a,b in split_l if len(b) >= 2]
    
    #if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}") 

    return switch_l


def replace_letter(word,verbose=False): 
    split_l=[]
    split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]

    replace_l = [l+i+r[1:] for l,r in split_l for i in letters if r and (l+i+r[1:] != word)]
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")   
    
    return replace_l

def insert_letter(word, verbose=False):
    split_l=[]
    for c in range(len(word)+1):
        split_l.append((word[0:c],word[c:]))
    insert_l = [ a + l + b for a,b in split_l for l in letters]

    #if verbose: print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")
    
    return insert_l

def edit_one_letter(word, allow_switches = True):
    
    edit_one_set = set()
    
    edit_one_set.update(delete_letter(word))
    if allow_switches:
        edit_one_set.update(switch_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(insert_letter(word))

    return edit_one_set


def edit_two_letters(word, allow_switches = True):
    
    edit_two_set = set()
    
    edit_one = edit_one_letter(word,allow_switches=allow_switches)
    for w in edit_one:
        if w:
            edit_two = edit_one_letter(w,allow_switches=allow_switches)
            edit_two_set.update(edit_two)

    
    return edit_two_set


def get_corrections(word, probs, vocab):
    suggestions = []
    if ( word in vocab and word):
        suggestions.append(word)
    suggestions = list(edit_one_letter(word).intersection(vocab) or edit_two_letters(word).intersection(vocab))
    n_best = [[s,probs[s]] for s in list(reversed(suggestions))]
    #n_best = [s for s in list(reversed(suggestions))]
    #if verbose: print("suggestions = ", suggestions)

    return n_best


# my_word = 'dys' 
# tmp_corrections = get_corrections(my_word, probs, vocab)
# #for i, word_prob in enumerate(tmp_corrections):
# #    print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")
# print(tmp_corrections)
# # w = "eat"
# # x=replace_letter(w,verbose=False)
# # print(x)