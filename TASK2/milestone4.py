import os
input_folder_name = input("Enter the input folder name");
output_folder_name = input("Enter the output folder name");
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
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
# iterate through rows
for i in range(len(result)):  
# iterate through columns
    for j in range(len(result[0])):
        result[i][j] = result[i][j] + result[i][j]
for r in result:
listl = list(a.split(" "))
f.write(a);
print("Operation done and the file is created. ");

    
