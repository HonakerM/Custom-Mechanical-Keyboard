
x_movement = 17.63 - 0.63
y_movement = -13.21+26.21
output_file=""
for line in open("da912032c8a4bccd065ccc609f62979f.board.scr"):
    words = line.strip().split(" ")

    if(len(words)==0):
        continue

    if(words[0]=="ROTATE"):
        if(words[2][0]=="D"):
            words[1]="R270"
        else:
            words = []
    elif(words[0]=="MOVE"):
        if(words[1][0]=="D"):
            location_x = round(float(words[2].replace("(","")),2)
            location_y = round(float(words[3].replace(");","")),2)
            words[2] = "("+str(location_x+x_movement)
            words[3] = str(location_y+y_movement)+");"
        else:
            words = []

    output_line = " ".join(words)
    output_file=output_file+output_line+"\n"

with open('board.scr', 'w') as the_file:
    the_file.write(output_file)
