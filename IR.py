
import sys
import re
import os
import math
from porterstem import PorterStemmer


# Read the input folder , query ,stopwords from the command line
documents = sys.argv[1]
query = sys.argv[2]
stopfile_name = sys.argv[3]

parent_dir = os.getcwd()
input_dir = os.path.join(parent_dir, documents)

#this will add the query to a file inside documents folder
with open(os.path.join(os.path.join(parent_dir, documents), "query.txt"), "a") as f:
    # Write the text to the file using the write() method
        f.write(query)
        
outfile_name = "outputfolder"

#this function will preprocess the documents and query by converting to lowercase,removing punctuation,tokenize text,
#remove hyperlinks,Remove <a> tags but keep their content,remove stop words and stemming using porterstemmer library
# after preprocessing join words back into a single string and  Write the pre-processed text to the output file

def do_preprocess(input_dir,stopfile_name, parent_dir, outfile_name):
# # Loop through all the files in the input directory
    for filename in os.listdir(input_dir):
        # Read the contents of the file
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
        
        with open(os.path.join(output_dir, filename), 'w') as f:
            f.write(modified_text)

do_preprocess(input_dir,stopfile_name, parent_dir, outfile_name)

output_file = "InvertedIndexTable"

# This Function  create an inverted index from a folder of text files,first create Dictionary to store the inverted index
# Split the content by the TAB character to get the title and content,Set the title to an empty string and the content to the entire file content
# Increment the count of the term in the title, if the term is not in the title and Increment the count of the term in the title         
def create_inverted_index(output_folder, output_file):
  inverted_index = {}

  # Iterate through the files in the input folder
  for file in os.listdir(output_folder):
    with open(os.path.join(output_folder, file), "r") as f:
       
        content = f.read().strip()
        if "  " in content:
            list = content.split("  ")
            title = list[0]
            content = list[1]
        else:
            title = file
            content = content
        terms = content.split()
        for term in terms:
                if term not in inverted_index:
                    inverted_index[term] = {}
                if title not in inverted_index[term]:
                    inverted_index[term][title] = 0       
                inverted_index[term][title] += 1
           
    with open(output_file, "w") as f:
        for term, titles in inverted_index.items():
            line = term
            for title, count in titles.items():
                line += "\t" + title + "[" + str(count) + "]"
            f.write(line + "\n")


create_inverted_index("outputfolder", "InvertedIndexTable")

outfile_name = "TFIDF_Matrix.txt"
#function to create TFIDF Matrix
def milestone4(output_file,outfile_name):
# Read inverted index from file
    inverted_index = {}
    with open(output_file, 'r') as infile:
        for line in infile:
            term, *doc_ids = line.strip().split('\t')
            inverted_index[term] = doc_ids
    new_inverted_index = {}
    for keys, values in inverted_index.items():
        temp = {}
        for s in values:
            key, value = s.split('[')
            temp[key] = int(value[:-1])
        new_inverted_index[keys] = temp
    inverted_index = new_inverted_index
        

    # Calculate the Maximum Frequency of each Document
    def get_max_freq(inverted_index):
        max_freq = {}
        for d in inverted_index.values():
            for key, value in d.items():
                if key not in max_freq.keys():
                    max_freq[key] = value
                else:
                    if max_freq[key] < value:
                        max_freq[key] = value
        return(max_freq)




    max_freq = get_max_freq(inverted_index)

  

    # Calculate the Term Frequency
    def get_tf(inverted_index, max_freq):
        tf = {}
        for k , v in inverted_index.items():
            temp = {}
            for key, value in v.items():
                temp[key] = value/max_freq[key]
            for key, value in max_freq.items():
                if key not in temp.keys():
                    temp[key] = 0
            tf[k] = temp        
        return tf


    tf = get_tf(inverted_index, max_freq)
  


    # Calculate IDF Coefficient
    def get_IDF_Coeff(inverted_index, max_freq):
        Ni = {}
        for word, docs in inverted_index.items():
            Ni[word] = len(docs)

        idf_coeff = {}
        for word, ni in Ni.items():
            N = len(max_freq)
            idf_coeff[word] = round((math.log10(N/ni)), 3)
            
        return idf_coeff


    idf = get_IDF_Coeff(inverted_index, max_freq)



    # Calcutate TFxIDF matrix
    def get_tf_idf(tf, idf):
        tf_idf = {}
        for word, docs in tf.items():
            temp = {}
            for doc, value in docs.items():
                temp[doc] = value * idf[word]
            tf_idf[word] = temp


        return tf_idf 

    tf_idf = get_tf_idf(tf, idf)
    # print(f"TFxIDF = {tf_idf}")




    # Writing to a file
    data = tf_idf

    # Get the keys for the outer dictionary (i.e. 'sample', 'document', 'second')
    keys = list(data.keys())

    # Get the keys for the inner dictionaries (i.e. 'D1', 'D2')
    inner_keys = data[keys[0]].keys()

    # Open a file for writing
    with open(outfile_name, 'w') as f:
        # Write the header row
        f.write(f"{' ':<10}")  
        for key in inner_keys:
            f.write(f"{key:<10}")  
        f.write('\n')  

        # Write the data rows
        for key in keys:
            f.write(f"{key:<10}") 
            for inner_key in inner_keys:
                value = data[key][inner_key]  
                f.write(f"{value:<10.3f}") 
            f.write('\n')  
    return max_freq.keys()



total_docs = milestone4(output_file,outfile_name)


input = "TFIDF_Matrix.txt"
d2 = "D.txt"
def cosinecalc(input,d1,d2):
    with open(input, 'r') as f:
        data = {}
        lines = f.readlines()
        headers = lines[0].split()

        for line in lines[1:]:
            words = line.split()

            key = words[0]
            values = (words[1:])
            values = [float(value) for value in values]
            value_dict = dict(zip(headers, values))
            data[key] = value_dict
            

    # Calculate |D|
    def get_mod(d):
        mod = 0
        for i in d:
            mod += i**2
        return  math.sqrt(mod)
    
    # Seperate the D1 and D2 values
    def get_d(doc, data):
        d = []
        for _, docs in data.items():
            for key, value in docs.items():
                if key == doc:
                    d.append(value)
        return d


    d1 = get_d(d1, data)
    d2 = get_d(d2, data)


    # Calculate the dot product
    def d1_dot_d2(d1, d2):
        result = 0
        for i in range(len(d1)):
            result += d1[i] * d2[i]
        return result



    # Calculate the cosine simularity
    def cosine_simularity(d1, d2):
        mod_d1 = get_mod(d1)
        mode_d2 = get_mod(d2)   
        dot_d1_d2 = d1_dot_d2(d1, d2)
        return dot_d1_d2/(mod_d1*mode_d2)

    return cosine_simularity(d1, d2)

cosine_sim = {}
for key in total_docs:
    value = cosinecalc(input,key,d2)
    cosine_sim[key] = value
    
max_value = max(cosine_sim.values())
max_key = max(cosine_sim, key = cosine_sim.get)
# sorted_d = dict( sorted(cosine_sim.items(), key=operator.itemgetter(1),reverse=True))
sorted_dict = {k: v for k, v in sorted(cosine_sim.items(), key=lambda item: item[1], reverse=True)}
for k, v in sorted_dict.items():
    print(f'{k}  : {v}')
