from tkinter import Tk,BOTH,Canvas

class Window:
	# The Window class is used to....make a window, with it's parameters being
	# the width and height of the window, in pixels
	def __init__(self,width,height):
		self.root = Tk()
		self.root.title('Mazy Puzzle')
		self.__canvas = Canvas(self.root, bg='white',width=width,height=height)
		self.__canvas.pack()
	
	def draw_line(self, line, fill="black"):
		line.draw(self.__canvas, fill)

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

class Cell():
	# Cell uses both Lines and Points to make a square, simply by drawing lines using
	# using the designated xy cords, takes in 2 xy cords, and draw each side using
	# those cords
	def __init__(self, x1, y1, x2, y2, win):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.top_wall = Line(Point( x1, y1 ),Point( x1, y2 ))
		self.right_wall = Line(Point( x1, y1 ),Point( x2, y1 ))
		self.bottom_wall = Line(Point( x2, y1 ),Point( x2, y2 ))
		self.left_wall = Line(Point( x1, y2 ),Point( x2, y2 ))
		self.__win = win
	def draw(self):
		if self.top_wall:
			self.__win.draw_line(self.top_wall)
		if self.right_wall:
			self.__win.draw_line(self.right_wall)
		if self.bottom_wall:
			self.__win.draw_line(self.bottom_wall)
		if self.left_wall:
			self.__win.draw_line(self.left_wall)
	def draw_move (self,to_cell, undo=False):
		# Draw move should take in 2 cells, and then see if there ISN'T an overlap
		# If there isn't, then draw a line inbetween them
		mid_x1 = (self.x1 + to_cell.x1)/2
		mid_x2 = (self.x2 + to_cell.x2)/2
		mid_y1 = (self.y1 + to_cell.y1)/2
		mid_y2 = (self.y2 + to_cell.y2)/2
		move_line = Line(Point(mid_x1, mid_y1),Point(mid_y1, mid_y2), lambda x: "gray" if undo else "red")