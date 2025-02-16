#!/usr/bin/python3

from tkinter import *
from GUI import *
from notes_and_scales import *

main = Tk()
main.title("Ukelele Scales")

canvas = Canvas(main, width = 500, height = 600)
canvas.pack()

draw_fretboard(canvas)

scale = scaleDict["C Major"]

for note in scale:
    draw_note(noteDict[note][0], noteDict[note][1], canvas)

main.mainloop()
