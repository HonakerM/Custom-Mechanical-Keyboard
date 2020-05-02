
line_doc = []
previous_keyboard = (0,0)
current_key = 0
old_location = -1.50
output_file=""
previous_diode = {1:(0,0),2:(0,0)}
current_diode = 1
name_list = set()
for line in open("da912032c8a4bccd065ccc609f62979f.schematic.scr"):
    words = line.strip().split(" ")
    if(len(words)>1 and "KEYSWITCH" in words[1]):
        #if(words[2] in name_list):
        #    words[2]=words[2]+"_1"
        new_location_x = round(float(words[3].replace("(","")),2)
        #words[3] = "("+str(round(new_location_x,2))
        new_location_y = round(float(words[4].replace(");","")),2)
        #if(new_location_y != old_location):
        #    current_key = 0
        #    old_location = new_location_y
        #else:
        #    current_key = current_key+1
#
        previous_keyboard = (new_location_x,new_location_y)

    if(len(words)>1 and "DIODE" in words[1]):
        if(words[2] in name_list):
            words[2]=words[2]+"_1"
        new_location_x = round(previous_keyboard[0]+0.1,2)
        words[4] = "("+str(new_location_x)
        new_location_y = round(previous_keyboard[1]+0.6,2)
        words[5] = str(new_location_y)+");"
        if(current_diode == 3):
            current_diode=1

        previous_diode[current_diode]= (new_location_x,new_location_y)
        current_diode= current_diode+1

    if(len(words)>1 and "NET" in words[0]):
        words[2] = str("(")+str(round(previous_diode[1][0],2))
        words[3] = str(round(previous_diode[1][1],2)+0.2)+str(")")
        words[4] = str("(")+str(round(previous_diode[2][0],2))
        words[5] = str(round(previous_diode[2][1],2)+0.2)+str(");")

    output_line = " ".join(words)
    output_file=output_file+output_line+"\n"

with open('schematic.scr', 'w') as the_file:
    the_file.write(output_file)
