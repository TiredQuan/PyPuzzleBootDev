from tkinter import Tk,BOTH,Canvas

class Window:
	def __init__(self,width,height):
		self.__root = Tk()
		self.__root.title('lmalmao')
		self.__canvas = Canvas(root, bg='#000000',width=width,height=height)
		self.__canvas.pack()


root = Tk()
root.title('lmalmao')
canvas = Canvas(root, bg='#000000',width=800,height=800)
canvas.pack()

root.mainloop()