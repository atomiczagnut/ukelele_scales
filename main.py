#!/usr/bin/python3

import cairosvg
import io
from tkinter import *
from PIL import Image, ImageTk

main = Tk()

# Draw the fretboard in the background

img_data = cairosvg.svg2png(url = "Fretboard.svg")
img = Image.open(io.BytesIO(img_data))
tk_img = ImageTk.PhotoImage(img)
size = img.size

fretboard = Canvas(main, width = size[0], height = size[1])
fretboard.pack()
fretboard.create_image(0, 0, anchor = 'nw', image = tk_img)

# Select a scale to display
# I used standard MIDI notes (60 = middle C)

# Add functionality for other scales

scaleDict ={ 
	"C Major": [60, 62, 64, 65, 67, 69, 71, 72],
	"C Minor": [60, 62, 63, 65, 67, 68, 70, 72],
	"C Blues": [60, 63, 65, 66, 67, 71, 72],
}

# Default to C Major

scale = scaleDict["C Major"]

# Dictionary that stores x, y values of notes
# The high G string (85) will require its own functionality
# The strings correspond to 85, 153, 220, 287, respectively
# The frets correspond to 115 for open string, then 181, 229, 277, 325, 373, 421, 468


noteDict = {
	60: (153, 115),
	61: (153, 181),
	62: (153, 229),
	63: (153, 277),
	64: (220, 115),
	65: (220, 181),
	66: (220, 229),
	67: (220, 277),
	68: (220, 325),
	69: (287, 115),
	70: (287, 181),
	71: (287, 229),
	72: (287, 277),
	73: (287, 325),
	74: (287, 373),
	75: (287, 421),
	76: (287, 468),
}

# Display circles for the notes

def create_circle(x, y, r, canvas):
	x0 = x - r
	y0 = y - r
	x1 = x + r
	y1 = y + r
	if y == 115:
		return canvas.create_oval(x0, y0, x1, y1) # Open circle indicates open string
	else:
		return canvas.create_oval(x0, y0, x1, y1, fill = "black") # Filled circle indicates finger

for note in scale:
	create_circle(noteDict[note][0], noteDict[note][1], 10, fretboard)

main.mainloop()
