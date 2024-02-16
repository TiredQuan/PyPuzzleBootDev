from graphic import Window,Cell


def main():
	window = Window(800,600)

	# cell_1 = Cell(50,50,100,100, window)
	# cell_1.right_wall = None
	# cell_1.draw()
	
	# cell_2 = Cell(100,50,150,100, window)
	# cell_2.left_wall = None
	# cell_2.right_wall = None
	# cell_2.bottom_wall = None
	# cell_2.draw()
	
	cell_0 = Cell(150,100,200,150, window)
	cell_0.top_wall = None
	cell_0.draw()

	cell_3 = Cell(150,50,200,100, window)
	cell_3.right_wall = None
	cell_3.bottom_wall = None
	cell_3.draw()
	
	cell_4 = Cell(200,50,250,100, window)
	cell_4.left_wall = None
	cell_4.draw()
	

	cell_3.draw_move(cell_4)
	cell_3.draw_move(cell_0, True)

	window.root.mainloop()

main()

# I FUCKING HATE SHAPES