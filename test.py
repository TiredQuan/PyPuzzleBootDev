from tkinter import Tk,BOTH,Canvas

class Window:
	def __init__(self,width,height):
		self.root = Tk()
		self.root.title('lmalmao')
		self.__canvas = Canvas(self.root, bg='#000000',width=width,height=height)
		self.__canvas.pack()


# root = Tk()
# root.title('lmalmao')
# canvas = Canvas(root, bg='#000000',width=800,height=800)
# canvas.pack()

# root.mainloop()

window = Window(500,500)
window.root.mainloop()

# TODO
# ask
# What's the difference between mainloop() and class update/update_idletasks()