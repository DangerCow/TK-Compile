
#------------<FOR ANYONE PEEKING IN THIS FILE>------------#

#--------<this was just a test to make the standered of my program so i knew what to do>---------#

from tkinter import *

root = Tk()

canvas = Canvas(root, width=500, height=600)
canvas.pack()

line = canvas.create_line(0,0,500,600)
line2 = canvas.create_line(500,0,0,600)
box = canvas.create_rectangle(25,25,130,60)

root.mainloop()
