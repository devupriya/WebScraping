import os
input_folder_name = input("Enter the input folder name");
query = input("Enter the queries:");
stop_file_name = input("Stop words file name.. ");

path = "C:\\Users\\Rajan\\Desktop\\joy projects\\undone\\ID_568_3500\\" + input_folder_name;
os.chdir(path)
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
listl = list(a.split(" "))
f.write(a);

    
