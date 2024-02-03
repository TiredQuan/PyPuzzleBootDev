from graphic import Window,Cell


def main():
	window = Window(800,600)

	cell = Cell(50,100, window)
	cell.left_wall = None
	cell.draw()
	
	cell = Cell(125,200, window)
	cell.right_wall = None
	cell.draw()
	
	cell = Cell(225,250, window)
	cell.bottom_wall = None
	cell.draw()
	
	cell = Cell(300,500, window)
	cell.top_wall = None
	cell.draw()
	
	window.root.mainloop()

main()
