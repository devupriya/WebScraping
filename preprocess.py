
import os
import string
import re
from porterstem import PorterStemmer
import sys


infilename = sys.argv[1]
outfilename = sys.argv[2]
stopfilename = sys.argv[3]

## Set the input directories
parent_dir = os.getcwd()
path = os.path.join(parent_dir, infilename)
if not os.path.exists(path):
   os.makedirs(path)
input_dir = path

# Specify the directory containing the input text files
directory = path

#this function will preprocess the documents and query by converting to lowercase,removing punctuation,tokenize text,
#remove hyperlinks,Remove <a> tags but keep their content,remove stop words and stemming using porterstemmer library
# after preprocessing join words back into a single string and  Write the pre-processed text to the output file

def do_preprocess(input_dir,stopfile_name, parent_dir, outfile_name):
    for filename in os.listdir(input_dir):
        with open(os.path.join(input_dir, filename), 'r') as f:
            text = f.read()
        text_low = text.lower()
        text_punct = re.sub(r'[^a-z0-9]', ' ', text_low) 
        text_num = re.sub(r"\b[0-9]+\b\s*", "", text_punct)
        tokens = text_num.split()
        clean_tokens = [t for t in tokens if len(t) > 1]
        clean_text = " ".join(clean_tokens) 
        clean_text = re.sub(r"https?://\S+", "", clean_text)
        clean_text = re.sub(r"<a[^>]*>(.*?)</a>", r"\1", clean_text)
        words = clean_text.split()
        stopword_dir = os.getcwd()
        with open(os.path.join(parent_dir, stopfile_name), 'r') as f:
            stop_words = f.read().split()
            words = [word for word in words if word not in stop_words]
        t=PorterStemmer()
        words = [t.stem(word,0,len(word)-1) for word in words]
        modified_text = ' '.join(words)
    
        output_dir = os.path.join(parent_dir, outfile_name)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)


        # Write the pre-processed text to the output file
        with open(os.path.join(output_dir, filename), 'w') as f:
            f.write(modified_text)



do_preprocess(input_dir,stopfilename, parent_dir , outfilename)
