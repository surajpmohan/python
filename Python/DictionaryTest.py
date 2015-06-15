with open("birds.txt",'r') as b_file:
    lines = b_file.readlines()
print lines[0]
b_dictionary = {}
for line in lines:
    line = line.rstrip()
    if b_dictionary.get(line) == None:
        b_dictionary[line] = 0
    b_dictionary[line]=b_dictionary.get(line) + 1
for key in b_dictionary.keys():
    print key , ": " , b_dictionary[key]
    
    