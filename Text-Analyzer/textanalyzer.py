import os
import string

filename="text.txt"
words=[]
word_counts={}
cleaned_words=[]

if os.path.exists(filename):
    with open(filename,"r", encoding="utf-8") as file: 
        text=file.read()   
    words = text.split()
else:
    print(f"'{filename}' not found. Please create it and add some text.")


for word in words:
    word=word.lower().strip(string.punctuation) 
    if word !="":
        cleaned_words.append(word)

"""
for word in cleaned_words:
    if word in word_counts:
        word_counts[word]+=1
    else:
        word_counts[word]=1

    most_common = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10] """

#or

from collections import Counter

word_counts=Counter(cleaned_words)
most_common=word_counts.most_common(10)  


total = len(cleaned_words)
for word, count in most_common:
    percentage = (count / total) * 100
    print(f"{word}: {count} ({percentage:.2f}%)")

print(f"Total words: {len(cleaned_words)}")
print(f"Unique words: {len(word_counts)}")
print("Most common words: ")
for word,count in most_common:
    print(f"{word}: {count}")
