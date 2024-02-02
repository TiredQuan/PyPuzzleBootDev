from tkinter import Tk, BOTH, Canvas
class Window:
	def __init__(self, width, height):
		self.__root = Tk()
		self.__root.title("Maze copier")
		self.__canvas = Canvas(self.__root, bg = "white", height = height, width = width)
		self.__canvas.pack()