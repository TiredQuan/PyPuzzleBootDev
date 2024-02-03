from tkinter import Tk,BOTH,Canvas

class Window:
	def __init__(self,width,height):
		self.root = Tk()
		self.root.title('Mazy Puzzle')
		self.__canvas = Canvas(self.root, bg='white',width=width,height=height)
		self.__canvas.pack()
	
	def draw_line(self, line, fill="black"):
		line.draw(self.__canvas, fill)

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Line:
	def __init__(self, point1, point2):
		self.__p1 = point1
		self.__p2 = point2
	def draw(self, canvas, fill="black"):
		canvas.create_line(
			self.__p1.x,self.__p1.y,self.__p2.x,self.__p2.y, fill = fill, width = 2
		)
		canvas.pack(fill=BOTH, expand=1)

class Cell():
	def __init__(self,edge_s, edge_e, win): # edge_start edge _end, imagine the opposite end points of a square, edge start < edge end, edge start -> edge end
		self.top_wall = Line(Point(edge_s,edge_s),Point(edge_e,edge_s))
		self.right_wall = Line(Point(edge_e,edge_s),Point(edge_e,edge_e))
		self.bottom_wall = Line(Point(edge_s,edge_e),Point(edge_e,edge_e))
		self.left_wall = Line(Point(edge_s,edge_s),Point(edge_s,edge_e))
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

