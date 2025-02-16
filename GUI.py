# The functions which control the GUI

def draw_fretboard(canvas) -> None:
	"""
	Draws the fretboard to the Tkinter canvas.
	
	Args: 
		canvas: Tkinter canvas object.
		
	Returns:
		None.
	"""
	canvas.create_line(50, 50, 50, 450)
	canvas.create_line(100, 50, 100, 450)
	canvas.create_line(150, 50, 150, 450)
	canvas.create_line(200, 50, 200, 450)
	canvas.create_line(50, 50, 200, 50, width = 5)
	canvas.create_line(50, 100, 200, 100)
	canvas.create_line(50, 150, 200, 150)
	canvas.create_line(50, 200, 200, 200)
	canvas.create_line(50, 250, 200, 250)
	canvas.create_line(50, 300, 200, 300)
	canvas.create_line(50, 350, 200, 350)
	canvas.create_line(50, 400, 200, 400)
	canvas.create_line(50, 450, 200, 450)

def draw_note(x: int, y: int, canvas) -> None:
	"""
	Draws a circle on the fretboard where the note should be.

	Args:
		x (int): Which string to draw the note on
		y (int): How far down on the string to draw the note
		canvas: Tkinter canvas object

	Returns:
		None.   
	"""
	x0 = x - 10
	y0 = y - 10
	x1 = x + 10
	y1 = y + 10
	if y < 50:
		canvas.create_oval(x0, y0, x1, y1) # Open circle indicates open string
	else:
		canvas.create_oval(x0, y0, x1, y1, fill = "black") # Filled circle indicates finger

def create_scale_menu(canvas):
	pass
