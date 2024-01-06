#task Milestone 4
import math
import sys

infile_name = sys.argv[1]
outfile_name = sys.argv[2]


def milestone4(infile_name,outfile_name):
# Read inverted index from file
    inverted_index = {}
    with open(infile_name, 'r') as infile:
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
    # print(f"max_freq = {max_freq}")

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
    # print(f"tf = {tf}")


    # Calculate IDF Coefficient
    def get_IDF_Coeff(inverted_index, max_freq):
        Ni = {}
        for word, docs in inverted_index.items():
            Ni[word] = len(docs)

        idf_coeff = {}
        for word, ni in Ni.items():
            N = len(max_freq)
            idf_coeff[word] = round((math.log10(N/ni) + 1), 3)
            
        return idf_coeff


    idf = get_IDF_Coeff(inverted_index, max_freq)

    # print(f"idf = {idf}")

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
    with open(outfile_name+".txt", 'w') as f:
        # Write the header row
        f.write(f"{' ':<10}")  
        for key in inner_keys:
            f.write(f"{key:<10}")  
        f.write('\n')  

        # Write the data rows
        for key in keys:
            f.write(f"{key:<10}") 
            for inner_key in inner_keys:
                value = data[key][inner_key] + 1
                f.write(f"{value:<10.3f}") 
            f.write('\n')  

milestone4(infile_name,outfile_name)