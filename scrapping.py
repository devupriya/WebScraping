import urllib.request
import re, os
import sys

# Read command line arguments
outfile_name = sys.argv[1]

directory = outfile_name
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)

if not os.path.exists(path):
   os.makedirs(path)

def getLinks():

    allLinks = []

    # Specify the website to crawl
    url = "http://www.griffith.ie"

    # Create a request object with a User-Agent header
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    # Make a request to the website and retrieve the HTML
    response = urllib.request.urlopen(request)
    html = response.read().decode()

    # Find all the links in the HTML using a regular expression
    links = re.findall(r'<a\s+href=[\'"]?([^\'" >]+)', html)

    # Print the links
    for i in range(1, 21):
        link = f"{url}{links[i]}"
        allLinks.append(link)
    return allLinks


def get_text(url):
    # Create a request object with a User-Agent header
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    # Make a request to the website and retrieve the HTML
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')


    # Extract the text from the HTML using a regular expression
    text = re.sub(r"<[^>]*>|<style[^>]*>[^<]*</style>|<script[^>]*>[^<]*</script>", '', html).replace("\n", "")

    return text

# Write the document identifiers as the header of each column
#outfile.write('\t' + '\t'.join(weights.keys()) + '\n')

# Close the output file
#outfile.close()

links = getLinks()
with open(os.path.join(parent_dir, f"all_links.txt"), "w") as all_links:
    for link in links:
        name = f"D{links.index(link)}"
        line = f"{name}        = {link}\n"
        all_links.write(line)

for link in links:
    text = get_text(link)
    name = f"D{links.index(link)}"
    print(f"{name}      = {link}")
    filename = os.path.join(path, f"{name}.txt")
    with open(filename, 'w') as f:
            for line in text:
                f.write(line)
    f.close()

print("TASK COMPLETED")