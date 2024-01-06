# Open the file create a dict
import math
import sys

#Read the input file
input = sys.argv[1]

# Read the document identifiers
d1 = sys.argv[2]
d2 = sys.argv[3]

#this function calculates the cosine similarity by Calculating  the dot product of vectors divided by their length
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
            

    # print(data)

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
        
    
    print(f"Cosine Simularity = {cosine_simularity(d1, d2)}")
    return cosine_simularity(d1, d2)

cosinecalc(input,d1,d2)