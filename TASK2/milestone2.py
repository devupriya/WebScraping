import os
input_folder_name = input("Enter the input folder name");
output_folder_name = input("Enter the output folder name");
stop_words = []
stop_word = input("Enter the stop word one per line and enter y to stop entering");
while stop_word != "Y":
    stop_word = input();
    stop_words.append(stop_word)
path = "C:\\Users\\Rajan\\Desktop\\joy projects\\undone\\ID_568_3500\\" + input_folder_name;
os.chdir(path)
i =0
a = ""

for file in os.listdir():
    file = f"{path}\{file}"
    with open(file, 'r') as f:
        a = a + str(f.read())
        
parent_dir = "C:\\Users\\Rajan\\Desktop\\joy projects\\undone\\ID_568_3500\\"
path = os.path.join(parent_dir, output_folder_name)
os.mkdir(path)
name = path + "\\D1" + ".txt"
f = open(name, "a")
print(f)
print("elfsdjf")
listl = list(a.split(" "))
for w in listl:
    if w not in stop_words:
        f.write(w);
        f.write(" ");

    
