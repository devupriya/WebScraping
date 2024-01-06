# Milestone 3
import os
import sys

# Function to create an inverted index from a folder of text files
def create_inverted_index(input_folder, output_file):
  # Dictionary to store the inverted index
  inverted_index = {}

  # Iterate through the files in the input folder
  for file in os.listdir(input_folder):
    # Open the file and read its content
    with open(os.path.join(input_folder, file), "r") as f:
        # Read the content and remove any leading or trailing whitespace
        content = f.read().strip()

        # Split the content by the TAB character to get the title and content
        # Split the content by the TAB character to get the title and content
        if "  " in content:
            list = content.split("  ")
            title = list[0]
            content = list[1]
        else:
            # Set the title to an empty string and the content to the entire file content
            title = file.split(".")[0]
            content = content

         # Split the content into individual terms
        terms = content.split()

        # Iterate through the terms and add them to the inverted index
        for term in terms:
        # If the term is not in the title and not in the inverted index, add it
            if term not in inverted_index:
                inverted_index[term] = {}

        # If the term is not in the title and the title is not in the inverted index for the term, add it
            if title not in inverted_index[term]:
                inverted_index[term][title] = 0

        # Increment the count of the term in the title, if the term is not in the title
            # Increment the count of the term in the title
            inverted_index[term][title] += 1
           

  # Open the output file for writing
  # Open the output file for writing
    with open(output_file+".txt", "w") as f:
  # Iterate through the inverted index and write it to the output file
        for term, titles in inverted_index.items():
            line = term
            for title, count in titles.items():
                line += "\t" + title + "[" + str(count) + "]"
            f.write(line + "\n")
        # Iterate through the inverted index and write it to the output file
        # for term, titles in sorted(inverted_index.items()):
        #      f.write(term + "\t" + "\t".join(titles.keys()) + "\n")


# Main function
def main():
  
  #Get the input folder and output file from the command line arguments
  input_folder = sys.argv[1]
  output_file = sys.argv[2]

  # Create the inverted index
  create_inverted_index(input_folder, output_file)

# Call the main function
if __name__ == "__main__":
  main()
