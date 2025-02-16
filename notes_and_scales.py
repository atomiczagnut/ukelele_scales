
# The collections which define the notes and scales

# Dictionary that defines the scales
# I used standard MIDI notes (60 = middle C)

# TODO: Add functionality for other scales

scaleDict ={ 
	"C Major": [60, 62, 64, 65, 67, 69, 71, 72],
	"C Minor": [60, 62, 63, 65, 67, 68, 70, 72],
	"C Blues": [60, 63, 65, 66, 67, 71, 72],
	"C Spanish": [60, 61, 64, 65, 67, 68, 70, 72],
}

# Dictionary that stores x, y values of notes
# TODO: The high G string will require its own functionality

noteDict = {
	60: (100, 25),
	61: (100, 100),
	62: (100, 150),
	63: (100, 200),
	64: (150, 25),
	65: (150, 100),
	66: (150, 250),
	67: (150, 200),
	68: (150, 250),
	69: (200, 25),
	70: (200, 100),
	71: (200, 150),
	72: (200, 200),
	73: (200, 250),
	74: (200, 300),
	75: (200, 350),
	76: (200, 400),
}

