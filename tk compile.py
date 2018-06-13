#------------<END GOALS>------------#

#-----<make json structure>------#  GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! 

#-----<read json>------# GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! 

#-----<add function vars>------# GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! 

#-----<create python file>------# GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! 

#-----<add tk to python file>------# GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! 

#-----<if ui elment in json file add it to the python file>------# GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! 

#-----<add end tk to python file>------# GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! 

#-----<make user freindly>------# GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD! GOOD!

#-----<add more content>------#

#-----<add boutons>------#

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#-----<read json>------#

print("reading json data")

import json

import os

x = __file__
print(x)
file = os.path.abspath(os.path.join(x, os.path.pardir))

with open(file + "\\data.json") as af:
    data = json.load(af)
#end

wind_hight = 0
wind_width = 0
wind_name = "made with tk compile"

wind_content = {}

for key, val in dict(data).items():

    for val_key, val_val in dict(val).items():

        if val_key == "hight":
            wind_hight = int(val_val)
        #end
        if val_key == "width":
            wind_width = int(val_val)
        #end
        if val_key == "name":
            wind_name = val_val
        #end

        if val_key == "content":
            for vval_key, vval_val in  dict(val_val).items():
                wind_content[vval_key] = vval_val
            #end
        #end
    #end
#end

#-----<create python file>------#

print("createing the python file")

try:
    os.remove("tk.py")
except OSError as e:
    print(e)
#end

f = open(file + "\\tk.py", "w")

f.close

#-----<add tk to python file>------#

print("importing tk to python file")

f = open(file + "\\tk.py","a")

f.write("from tkinter import *\n")
f.write("\nroot = Tk()\n\n")
f.write("canvas = Canvas(root, height=" + str(wind_hight) + ", " +  "width=" + str(wind_width) + ")\n")
f.write("root.title('" + wind_name + "')\n")
f.write("canvas.pack()\n\n")

#-----<add function vars>------#

f_top_l = (0,0) #---<top left>---#
f_top_r = (wind_width,0) #---<top right>---#

f_bot_l = (0,wind_hight) #---<botem left>---#
f_bot_r = (wind_width,wind_hight) #---<botem right>---#

f_cent = (wind_width / 2, wind_hight / 2)

#-----<if ui elment in json file add it to the python file>------#

def shape_v4(creation,shape):
    if shape in  key: #---<rect gen>---#

        f.write(key + " " + "= " + creation + "(")

        a = 0

        for ex in list(val):

            #if a != len(list(val)) - 2: f.write(",")
            a += 1

            i = 0

            for x in list(ex):

                #--------<types>---------#
                if "f_c" in str(x):
                    f.write(", fill = '" + str(x)[4:len(str(x))] + "'")
                #end
                if "f_o" in str(x):
                    f.write(", outline = '" + str(x)[4:len(str(x))] + "'")
                #end

                if "f_w" in str(x):
                    f.write(", width = " + str(x)[4:len(str(x))] + "")
                #end

                #--------<functions>---------#
                if "f_top_l" in  x:
                    f.write("0,0")
                elif "f_bot_r" in x:
                    f.write(str(wind_width)+","+str(wind_hight))
                elif "f_bot_l" in  x:
                    f.write("0," + str(wind_hight))
                elif "f_top_r" in x:
                    f.write(str(wind_width) + ",0")
                else:
                    if "f_c" not in x and "f_o" not in x and "f_w" not in x:
                        if i != len(list(ex)) - 2: f.write(",")
                    #end
                    i += 1

                    if "f_c" not in x and "f_o" not in x and "f_w" not in x: f.write(x)
                #end
            #end
        #end

        f.write(")\n")
    #end
#end

print("compileing tk code")

for key,val in wind_content.items():

    shape_v4("canvas.create_line","line")

    shape_v4("canvas.create_rectangle","box")
#end

#-----<add end tk to python file>------#

print("finishing up")

f.write("\nroot.mainloop()")

f.close

print("DONE!")

print("compiled at " + file + "\\tk.py")
print("make shure to hit enter or your file will not be writen")

inp = input("")