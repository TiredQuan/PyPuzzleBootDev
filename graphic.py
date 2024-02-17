from tkinter import Tk,BOTH,Canvas

class Window:
	# The Window class is used to....make a window, with it's parameters being
	# the width and height of the window, in pixels
	def __init__(self,width,height):
		self.__root = Tk()
		self.__root.title('Mazy Puzzle')
		self.__canvas = Canvas(self.__root, bg='white',width=width,height=height)
		self.__canvas.pack()
	
	def draw_line(self, line, fill="black"):
		line.draw(self.__canvas, fill)
	
	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()

	def run(self):
		self.__root.mainloop()
		

class Point:
	# Point is a class that makes a landmark, with its parameters pinpointing the
	# location of the landmark
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Line:
	# Line takes in two points, and draws a Line in-between them, hense the name
	def __init__(self, point1, point2):	
		self.__p1 = point1
		self.__p2 = point2
	def draw(self, canvas, fill="black"):
		canvas.create_line(
			self.__p1.x,self.__p1.y,self.__p2.x,self.__p2.y, fill = fill, width = 2
		)
		canvas.pack(fill=BOTH, expand=1)

