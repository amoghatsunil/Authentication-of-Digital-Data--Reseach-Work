# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 23:14:26 2020

@author: amogha
"""



from newspaper import Article
article = Article('https://www.dqindia.com/whatsapp-message-coronavirus-vaccine-fake-truth')
article.download()
article.parse()

print(article.authors)
print(article.publish_date)

import math 
import string 
import sys 
 
def read_file(filename): 
    try: 
        with open(filename, 'r',encoding="utf8") as f: 
            data = f.read() 
        return data 

    except IOError: 
        print("Error opening or reading input file: ", filename) 
        sys.exit() 


translation_table = str.maketrans(string.punctuation+string.ascii_uppercase," "*len(string.punctuation)+string.ascii_lowercase) 


def get_words(text): 

    text = text.translate(translation_table) 
    word_list = text.split() 

    return word_list 


def count_frequency(word_list): 

    D = {} 

    for new_word in word_list: 

        if new_word in D: 
            D[new_word] = D[new_word] + 1
        else: 
            D[new_word] = 1

    return D 

 
def word_frequencies(filename): 
    line=read_file(filename) 
    word=get_words(line) 
    freq_mapping=count_frequency(word) 

    print("File", filename, ":", ) 
    print(len(line), "lines, ", ) 
    print(len(word), "words, ", ) 
    print(len(freq_mapping), "distinct words") 

    return freq_mapping 



def dotProduct(D1, D2): 
    Sum = 0.0
    for key in D1: 
        if key in D2: 
            Sum+=(D1[key] * D2[key]) 
    return Sum

 
def vector_angle(D1, D2): 
    numerator=dotProduct(D1, D2) 
    denominator=math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2)) 
    return math.acos(numerator / denominator) 


def documentSimilarity(filename_1, filename_2): 
    sortedlist_1=word_frequencies(filename_1) 
    sortedlist_2=word_frequencies(filename_2) 
    distance = vector_angle(sortedlist_1, sortedlist_2) 
    print("The distance between the documents is: % 0.6f (radians)"% distance) 

documentSimilarity('authentic.txt', 'newsinput.txt') 
