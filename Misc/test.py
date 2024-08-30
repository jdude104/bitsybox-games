with open('index.txt') as file_list:
    for line in file_list:
        x = line.split('",')
        #x[2] = x[2][1:-1]
        if x[2][0] == "\"":
            x[2] = x[2][1:];
        x[2] = x[2].replace("\"", "\\\"")
        x[2] = x[2].replace("`", "\\`")
        print("mv -- " + x[0] + ".bitsy.txt\" \"" + x[2] + ".bitsy\"")
